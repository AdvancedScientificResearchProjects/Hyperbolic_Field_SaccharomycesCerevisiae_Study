"""Prompt templates for blind Saccharomyces cerevisiae microscopy density scoring.

Single-image, blinded vision assessment. The experimental condition (control vs.
channel 17/19/21 field exposure) is NEVER disclosed to the model; images are passed
under neutral filenames so the score cannot be biased by the assignment.

Output fields match the records actually stored in results/llm_full/llm_full.json:
density, cell_estimate, budding, distribution.
"""

STRUCTURED_OUTPUT_SUFFIX = (
    "\n\nAfter your analysis, output a JSON code block with structured data:\n"
    "```json\n"
    "{\n"
    '  "density": "low | medium | high",\n'
    '  "cell_estimate": 600,\n'
    '  "budding": "none | few | some | many",\n'
    '  "distribution": "even | clustered | sparse | mixed",\n'
    '  "notes": "brief observations about morphology, packing, and texture"\n'
    "}\n"
    "```\n"
    "Rules:\n"
    "- density: overall yeast cell density across the visible field.\n"
    "- cell_estimate: a single integer, your best estimate of the number of\n"
    "  yeast cells visible in the field.\n"
    "- budding: how prominent budding / dividing cells are across the field.\n"
    "- distribution: how the cells are spatially arranged in the field.\n"
    "Fill only the fields you can determine from the image. Use null for uncertain fields."
)

# Single-image blind density assessment (no experiment context, neutral filename).
SINGLE_PROMPT = (
    "You are an expert microscopy image analyst specializing in yeast "
    "(Saccharomyces cerevisiae) cultures.\n\n"
    "You are shown ONE brightfield microscopy field of a yeast sample, imaged at "
    "100x or 10x magnification. The experimental condition that produced this "
    "sample is NOT disclosed to you, and the filename is neutral — assess the "
    "image purely on what is visible. Do not guess the condition.\n\n"
    "Assess this single field:\n\n"
    "1. **Density**: Overall yeast cell density across the visible field "
    "(low / medium / high).\n"
    "2. **Cell estimate**: Approximate number of yeast cells visible in the field "
    "(a single integer).\n"
    "3. **Budding**: How prominent are budding / dividing cells "
    "(none / few / some / many)?\n"
    "4. **Distribution**: How are the cells spatially arranged "
    "(even / clustered / sparse / mixed)?\n"
    "5. **Morphology notes**: Any notable features — cell size, packing, debris, "
    "out-of-focus regions, or artifacts.\n\n"
    "Be precise, objective, and use consistent terminology. Describe only what you see."
    + STRUCTURED_OUTPUT_SUFFIX
)
