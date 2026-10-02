#!/usr/bin/env python3
"""Build the 20-slide KONKAUTO specification-driven development deck as a vector PDF.

All slide lettering is selectable PDF text; diagrams are vector shapes. Run from any
working directory with `python3 tools/konkauto_deck/build_konkauto_deck.py`.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from theme import W, H, register_fonts  # noqa: E402
from slides_act1 import draw_slide_01, draw_slide_02, draw_slide_03  # noqa: E402
from slides_act2 import draw_slide_04, draw_slide_05, draw_slide_06, draw_slide_07  # noqa: E402
from slides_act3 import draw_slide_08, draw_slide_09, draw_slide_10  # noqa: E402
from slides_act4 import draw_slide_11, draw_slide_12  # noqa: E402
from slides_act5 import (  # noqa: E402
    draw_slide_13, draw_slide_14, draw_slide_15,
    draw_slide_16, draw_slide_17, draw_slide_18,
)
from slides_act6 import draw_slide_19, draw_slide_20  # noqa: E402

SLIDES = [
    draw_slide_01, draw_slide_02, draw_slide_03,
    draw_slide_04, draw_slide_05, draw_slide_06, draw_slide_07,
    draw_slide_08, draw_slide_09, draw_slide_10,
    draw_slide_11, draw_slide_12,
    draw_slide_13, draw_slide_14, draw_slide_15,
    draw_slide_16, draw_slide_17, draw_slide_18,
    draw_slide_19, draw_slide_20,
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "KONKAUTO_SDAD_Workflow.pdf",
        help="output PDF path (default: repository root / KONKAUTO_SDAD_Workflow.pdf)",
    )
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    register_fonts()
    pdf = canvas.Canvas(str(args.output), pagesize=(W, H), pageCompression=1, invariant=1)
    pdf.setTitle("KONKAUTO — Specification-Driven Agentic Development")
    pdf.setAuthor("KONKAUTO")
    pdf.setSubject("Specification-driven agentic development workflow")
    pdf.setKeywords("KONKAUTO, SDAD, agents, specifications, traceability, governance")
    pdf.setCreator("KONKAUTO vector deck generator")

    for slide in SLIDES:
        slide(pdf)
        pdf.showPage()
    pdf.save()
    print(f"Wrote {args.output} ({len(SLIDES)} slides)")


if __name__ == "__main__":
    main()
