"""Vision LLM provider initialization and async call wrapper.

Canonical reproducible scorer for the Saccharomyces cerevisiae density study.
Modeled on the BloodPlasma study's provider layer. A multi-provider scaffold is
kept for portability, but only the Anthropic / Claude Opus 4.8 entry is active in
this study: every blind density score in results/llm_full/llm_full.json comes from
a single independent vision pass through that model at temperature 0.
"""

import asyncio
import logging
import os
import time

from langchain_core.messages import HumanMessage

logger = logging.getLogger(__name__)


def _extract_prompt_text(message: HumanMessage) -> str:
    """Extract the text portion of a message (skipping base64 image data)."""
    if isinstance(message.content, str):
        return message.content
    parts = []
    img_count = 0
    for block in message.content:
        if isinstance(block, dict):
            if block.get("type") == "text":
                parts.append(block["text"])
            elif block.get("type") == "image_url":
                img_count += 1
                parts.append(f"[image_{img_count}]")
    return "\n".join(parts)


PROVIDER_CONFIGS = {
    # Active provider for this study. Claude Opus 4.8 via LangChain's
    # init_chat_model("anthropic:...") path, deterministic (temperature 0).
    "anthropic": {
        "model": "anthropic:claude-opus-4-8",
        "timeout": 300,
        "api_key_env": "ANTHROPIC_API_KEY",
        "key_param": "api_key",
        "temperature": 0,
    },
    # --- Inactive scaffold (kept for portability; not used to produce results) ---
    "openai": {
        "model": "openai:gpt-5",
        "timeout": 300,
        "api_key_env": "OPENAI_API_KEY",
        "key_param": "api_key",
        "temperature": 0,
    },
    "google": {
        "model": "google_genai:gemini-2.5-flash",
        "timeout": 90,
        "api_key_env": "GOOGLE_API_KEY",
        "key_param": "google_api_key",
        "temperature": 0,
    },
}


def _has_key(config: dict) -> bool:
    return bool(os.getenv(config["api_key_env"]))


def init_providers(
    filter_names: list[str] | None = None,
) -> dict[str, object]:
    """Initialize and return available provider model instances.

    Args:
        filter_names: Optional list of provider names to include. If None, every
                      provider with an API key present in the environment is used.
                      For this study pass ["anthropic"].
    """
    from langchain.chat_models import init_chat_model

    models: dict[str, object] = {}

    for name, config in PROVIDER_CONFIGS.items():
        if filter_names and name not in filter_names:
            continue
        if not _has_key(config):
            logger.info("Skipping %s — no API key (%s)", name, config["api_key_env"])
            continue

        try:
            api_key = os.getenv(config["api_key_env"])
            models[name] = init_chat_model(
                model=config["model"],
                temperature=config.get("temperature", 0),
                **{config["key_param"]: api_key},
            )
            logger.info("Initialized %s (%s)", name, config["model"])
        except Exception as e:
            logger.error("Failed to init %s: %s", name, e)

    return models


async def call_provider(
    name: str,
    model: object,
    message: HumanMessage,
    timeout: int | None = None,
) -> dict:
    """Call a single provider with a timeout. Returns a result dict.

    On success: {"provider", "analysis", "latency_ms"}.
    On failure: {"provider", "error", "latency_ms"}.
    """
    cfg_timeout = timeout or PROVIDER_CONFIGS.get(name, {}).get("timeout", 60)

    start = time.monotonic()
    try:
        response = await asyncio.wait_for(
            model.ainvoke([message]),
            timeout=cfg_timeout,
        )
        elapsed = int((time.monotonic() - start) * 1000)

        content = response.content
        if isinstance(content, list):
            content = " ".join(
                block.get("text", "") if isinstance(block, dict) else str(block)
                for block in content
            )

        return {"provider": name, "analysis": content, "latency_ms": elapsed}

    except asyncio.TimeoutError:
        elapsed = int((time.monotonic() - start) * 1000)
        return {
            "provider": name,
            "error": f"Timeout after {cfg_timeout}s",
            "latency_ms": elapsed,
        }

    except Exception as e:
        elapsed = int((time.monotonic() - start) * 1000)
        logger.error("Provider %s failed: %s", name, e)
        return {
            "provider": name,
            "error": f"{type(e).__name__}: {e}",
            "latency_ms": elapsed,
        }
