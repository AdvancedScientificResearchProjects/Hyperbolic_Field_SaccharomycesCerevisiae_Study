#!/usr/bin/env python3
"""Single-image blind density scoring of yeast microscopy fields via Claude Opus 4.8.

Each microscopy JPG is sent to the Anthropic API in ONE independent vision call at
temperature 0, under a neutral filename, with the experimental condition blinded.
The structured density / cell_estimate / budding / distribution score is extracted
and written into results/llm_full/llm_full.json in the BloodPlasma metadata+records
shape. Progress is checkpointed so the run can be resumed.

Usage:
    python -m scripts.llm_analysis.run_single --provider anthropic --model claude-opus-4-8
    python -m scripts.llm_analysis.run_single --provider anthropic --channels 0,19 --max-photos 5
    python -m scripts.llm_analysis.run_single --provider anthropic --dry-run
    python -m scripts.llm_analysis.run_single --provider anthropic --resume
"""

import argparse
import asyncio
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

from langchain_core.messages import HumanMessage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def _load_env():
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    project_root = Path(__file__).resolve().parent.parent.parent
    if (project_root / ".env").exists():
        load_dotenv(project_root / ".env", override=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Blind single-image yeast density scoring")
    parser.add_argument("--provider", default="anthropic",
                        help="Provider name (default: anthropic)")
    parser.add_argument("--model",
                        help="Informational model id label, e.g. claude-opus-4-8. "
                             "The active model is set in providers.PROVIDER_CONFIGS.")
    parser.add_argument("--channels",
                        help="Comma-separated channel filter (e.g. 0,17,19,21)")
    parser.add_argument("--output-dir", default="results/llm_full",
                        help="Output directory (default: results/llm_full)")
    parser.add_argument("--output-name", default="llm_full.json",
                        help="Output filename (default: llm_full.json)")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Delay between images in seconds (default: 1.0)")
    parser.add_argument("--timeout", type=int, help="Per-call timeout override (seconds)")
    parser.add_argument("--resume", action="store_true",
                        help="Skip already-scored images and append to existing output")
    parser.add_argument("--dry-run", action="store_true",
                        help="List images without calling the API")
    parser.add_argument("--max-photos", type=int, help="Max images to process (for testing)")
    return parser.parse_args()


def _load_progress(progress_path: Path) -> set[str]:
    if progress_path.exists():
        return set(json.loads(progress_path.read_text()))
    return set()


def _save_progress(progress_path: Path, done: set[str]):
    progress_path.write_text(json.dumps(sorted(done), indent=2))


async def score_photo(photo, name, model, prompt, timeout):
    from scripts.llm_analysis.imaging import load_photo_b64, build_image_content
    from scripts.llm_analysis.providers import call_provider

    b64 = load_photo_b64(photo.jpg_path)
    # Neutral filename only — no channel / set / zone leaked into the prompt.
    message = HumanMessage(content=[
        {"type": "text", "text": prompt},
        build_image_content(b64),
    ])
    return await call_provider(name, model, message, timeout)


def _build_record(photo, structured: dict | None) -> dict:
    """Assemble one output record: blind score + recovered journal provenance."""
    record = {
        "file": f"{photo.filename}.jpg",
        "num": photo.num,
        "channel": photo.channel,
        "set": photo.set,
        "zone": photo.zone,
    }
    if structured:
        for key in ("density", "cell_estimate", "budding", "distribution"):
            if key in structured:
                record[key] = structured[key]
        if "notes" in structured:
            record["description"] = structured["notes"]
    return record


def main():
    _load_env()
    args = parse_args()

    from scripts.llm_analysis.data import load_photos, group_by_channel, CHANNEL_NAMES
    from scripts.llm_analysis.providers import init_providers, PROVIDER_CONFIGS
    from scripts.llm_analysis.prompts import SINGLE_PROMPT
    from scripts.llm_analysis.parsing import extract_single_structured

    provider_name = args.provider
    if provider_name not in PROVIDER_CONFIGS:
        logger.error("Unknown provider '%s'. Known: %s",
                     provider_name, list(PROVIDER_CONFIGS))
        sys.exit(1)

    model_id = PROVIDER_CONFIGS[provider_name]["model"]

    models = init_providers([provider_name])
    if provider_name not in models:
        logger.error("Provider '%s' not available — check %s.",
                     provider_name, PROVIDER_CONFIGS[provider_name]["api_key_env"])
        sys.exit(1)
    model = models[provider_name]
    logger.info("Active provider: %s (%s)", provider_name, model_id)

    channel_filter = args.channels.split(",") if args.channels else None
    photos = load_photos(channel_filter)
    if not photos:
        logger.error("No microscopy fields found.")
        sys.exit(1)

    groups = group_by_channel(photos)
    for ch, items in sorted(groups.items()):
        logger.info("  %s (%s): %d fields", ch, CHANNEL_NAMES.get(ch, ch), len(items))

    if args.dry_run:
        for photo in photos:
            ch_name = CHANNEL_NAMES.get(photo.channel, photo.channel)
            print(f"  {photo.filename}.jpg [ch={photo.channel}/{ch_name} "
                  f"set={photo.set} zone={photo.zone}]")
        print(f"\nTotal: {len(photos)} fields, model {model_id}")
        return

    project_root = Path(__file__).resolve().parent.parent.parent
    output_dir = project_root / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    results_path = output_dir / args.output_name
    progress_path = output_dir / ".progress.json"

    records: list[dict] = []
    done_keys: set[str] = set()
    if args.resume:
        done_keys = _load_progress(progress_path)
        if results_path.exists():
            existing = json.loads(results_path.read_text())
            records = existing.get("records", [])
        if done_keys:
            logger.info("Resuming: %d fields already scored", len(done_keys))

    todo = [p for p in photos if f"{p.filename}.jpg" not in done_keys]
    if args.max_photos:
        todo = todo[: args.max_photos]
    logger.info("Scoring %d fields", len(todo))

    def _write_output():
        output = {
            "metadata": {
                "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "mode": "single_image_blind",
                "provider": provider_name,
                "model": (args.model or model_id.split(":")[-1]),
                "total_fields": len(records),
                "blinded": True,
                "scoring": "one independent blind vision pass per field, "
                           "neutral filenames",
            },
            "records": records,
            "n": len(records),
        }
        results_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))

    async def run():
        for i, photo in enumerate(todo):
            ch_name = CHANNEL_NAMES.get(photo.channel, photo.channel)
            logger.info("[%d/%d] %s.jpg (ch=%s/%s)",
                        i + 1, len(todo), photo.filename, photo.channel, ch_name)

            result = await score_photo(photo, provider_name, model,
                                       SINGLE_PROMPT, args.timeout)

            if result.get("analysis"):
                structured = extract_single_structured(result["analysis"])
                status = "OK" if structured else "PARSE_FAIL"
            else:
                structured = None
                status = result.get("error", "NO_OUTPUT")

            records.append(_build_record(photo, structured))
            logger.info("  %s (%dms)", status, result.get("latency_ms", 0))

            done_keys.add(f"{photo.filename}.jpg")
            _save_progress(progress_path, done_keys)
            _write_output()

            if i < len(todo) - 1 and args.delay > 0:
                await asyncio.sleep(args.delay)

    asyncio.run(run())

    scored = sum(1 for r in records if "density" in r)
    logger.info("Done: %d/%d fields scored", scored, len(records))
    logger.info("Results: %s", results_path)


if __name__ == "__main__":
    main()
