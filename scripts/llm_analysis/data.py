"""Load yeast microscopy fields and attach journal metadata.

Modeled on the BloodPlasma study's data layer. Each microscopy field (one JPG)
is a "photo". Channel / set / zone come from the lab journal mapping in
data/photos/journal-mapping.csv, which maps contiguous image-number ranges to
experimental groups. Blinding is enforced by passing neutral filenames to the
model (the channel/set/zone metadata is recorded only after scoring).
"""

import csv
import logging
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PHOTOS_DIR = DATA_DIR / "photos"
JPG_DIR = PHOTOS_DIR / "jpg"
JOURNAL_MAPPING_CSV = PHOTOS_DIR / "journal-mapping.csv"

# Real experimental channels. 0 = control (no field exposure), 17/19/21 = field
# channels. These names are used only for reporting AFTER blind scoring.
CHANNEL_NAMES = {
    "0": "control",
    "17": "ch17",
    "19": "ch19",
    "21": "ch21",
}


@dataclass
class PhotoInfo:
    filename: str          # neutral stem, e.g. "IMG_4801"
    num: int               # image number, e.g. 4801
    jpg_path: Path
    channel: str = "unknown"   # "0" | "17" | "19" | "21" | "unknown"
    set: str = "unknown"       # "1" | "2" | "3" | "unknown"
    zone: str = "—"            # journal zone label
    group_id: str | None = None


def _parse_int(value: str) -> int | None:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def _load_journal_ranges() -> list[dict]:
    """Load the journal mapping as a list of group range records."""
    if not JOURNAL_MAPPING_CSV.exists():
        raise FileNotFoundError(f"Journal mapping not found: {JOURNAL_MAPPING_CSV}")

    ranges: list[dict] = []
    with open(JOURNAL_MAPPING_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            start = _parse_int(row.get("img_start"))
            end = _parse_int(row.get("img_end"))
            if start is None or end is None:
                continue
            ranges.append({
                "group_id": row.get("group_id"),
                "set": str(row.get("set", "")).strip(),
                "channel": str(row.get("channel", "")).strip(),
                "zone": (row.get("zone") or "—").strip() or "—",
                "img_start": start,
                "img_end": end,
            })
    return ranges


def _lookup_group(num: int, ranges: list[dict]) -> dict | None:
    """Return the journal group whose inclusive range contains ``num``."""
    for r in ranges:
        if r["img_start"] <= num <= r["img_end"]:
            return r
    return None


def _num_from_stem(stem: str) -> int | None:
    """Extract the trailing image number from a filename stem like IMG_4801."""
    digits = "".join(ch for ch in stem if ch.isdigit())
    return int(digits) if digits else None


def load_photos(channel_filter: list[str] | None = None) -> list[PhotoInfo]:
    """Load every microscopy field JPG and attach journal metadata.

    Args:
        channel_filter: Optional list of channel codes ("0","17","19","21") to keep.
    """
    if not JPG_DIR.exists():
        raise FileNotFoundError(f"JPG dir not found: {JPG_DIR}")

    ranges = _load_journal_ranges()

    photos: list[PhotoInfo] = []
    for jpg_path in sorted(JPG_DIR.glob("*.jpg")):
        stem = jpg_path.stem
        num = _num_from_stem(stem)
        if num is None:
            logger.warning("Could not parse image number from %s — skipping", stem)
            continue

        group = _lookup_group(num, ranges)
        if group is None:
            channel = "unknown"
            set_id = "unknown"
            zone = "—"
            group_id = None
        else:
            channel = group["channel"] or "unknown"
            set_id = group["set"] or "unknown"
            zone = group["zone"]
            group_id = group["group_id"]

        if channel_filter and channel not in channel_filter:
            continue

        photos.append(PhotoInfo(
            filename=stem,
            num=num,
            jpg_path=jpg_path,
            channel=channel,
            set=set_id,
            zone=zone,
            group_id=group_id,
        ))

    logger.info(
        "Loaded %d microscopy fields (%d mapped to a journal group)",
        len(photos),
        sum(1 for p in photos if p.group_id is not None),
    )
    return photos


def group_by_channel(photos: list[PhotoInfo]) -> dict[str, list[PhotoInfo]]:
    """Group fields by experimental channel."""
    groups: dict[str, list[PhotoInfo]] = {}
    for photo in photos:
        groups.setdefault(photo.channel, []).append(photo)
    return groups
