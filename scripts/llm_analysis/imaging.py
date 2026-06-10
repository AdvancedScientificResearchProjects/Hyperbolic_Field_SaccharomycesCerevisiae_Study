"""Image loading and base64 encoding for LLM vision APIs."""

import base64
from pathlib import Path


def load_photo_b64(jpg_path: Path) -> str:
    """Load a JPEG microscopy field at original resolution, return base64 string."""
    return base64.b64encode(Path(jpg_path).read_bytes()).decode("ascii")


def build_image_content(b64: str) -> dict:
    """Build a LangChain-compatible image content block."""
    return {
        "type": "image_url",
        "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
    }
