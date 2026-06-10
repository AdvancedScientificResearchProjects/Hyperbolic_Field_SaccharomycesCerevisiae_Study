"""Extract structured JSON from free-text LLM responses.

Modeled on the BloodPlasma study's parsing layer, adapted to the yeast density
fields: density, cell_estimate, budding, distribution.
"""

import json
import logging
import re

logger = logging.getLogger(__name__)

_JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*\n?(.*?)\n?\s*```", re.DOTALL)

DENSITY_NORMALIZE = {
    "low": "low",
    "sparse": "low",
    "medium": "medium",
    "moderate": "medium",
    "mid": "medium",
    "high": "high",
    "dense": "high",
    "very_high": "high",
}

BUDDING_NORMALIZE = {
    "none": "none",
    "no": "none",
    "absent": "none",
    "0": "none",
    "few": "few",
    "rare": "few",
    "occasional": "few",
    "some": "some",
    "moderate": "some",
    "many": "many",
    "frequent": "many",
    "abundant": "many",
}

DISTRIBUTION_NORMALIZE = {
    "even": "even",
    "uniform": "even",
    "homogeneous": "even",
    "clustered": "clustered",
    "clumped": "clustered",
    "aggregated": "clustered",
    "sparse": "sparse",
    "scattered": "sparse",
    "mixed": "mixed",
    "heterogeneous": "mixed",
}


def extract_json(text: str) -> dict | None:
    """Extract and parse the first JSON object from LLM response text."""
    raw = _find_json_string(text)
    if raw is None:
        return None
    try:
        data = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return None
    if not isinstance(data, dict):
        return None
    return data


def extract_single_structured(text: str) -> dict | None:
    """Extract a single-field yeast density assessment from response text."""
    data = extract_json(text)
    if data is None:
        return None
    return _normalize_single(data)


def _find_json_string(text: str) -> str | None:
    match = _JSON_BLOCK_RE.search(text)
    if match:
        return match.group(1).strip()

    brace_start = text.find("{")
    if brace_start == -1:
        return None

    depth = 0
    for i in range(brace_start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[brace_start : i + 1]
    return None


def _normalize_enum(val, table: dict) -> str | None:
    if not isinstance(val, str):
        return None
    raw = val.strip().lower().replace(" ", "_").replace("-", "_")
    if not raw or raw == "null":
        return None
    return table.get(raw, raw)


def _normalize_cell_estimate(val) -> int | None:
    if isinstance(val, bool):
        return None
    if isinstance(val, int):
        return val
    if isinstance(val, float):
        return int(val)
    if isinstance(val, str):
        digits = re.sub(r"[,\s]", "", val.strip())
        m = re.search(r"\d+", digits)
        if m:
            return int(m.group(0))
    return None


def _normalize_single(data: dict) -> dict | None:
    result = {}

    density = _normalize_enum(data.get("density"), DENSITY_NORMALIZE)
    if density is not None:
        result["density"] = density

    cell_estimate = _normalize_cell_estimate(data.get("cell_estimate"))
    if cell_estimate is not None:
        result["cell_estimate"] = cell_estimate

    budding = _normalize_enum(data.get("budding"), BUDDING_NORMALIZE)
    if budding is not None:
        result["budding"] = budding

    distribution = _normalize_enum(data.get("distribution"), DISTRIBUTION_NORMALIZE)
    if distribution is not None:
        result["distribution"] = distribution

    notes = data.get("notes")
    if isinstance(notes, str) and notes.strip() and notes.strip().lower() != "null":
        result["notes"] = notes.strip()

    return result if result else None
