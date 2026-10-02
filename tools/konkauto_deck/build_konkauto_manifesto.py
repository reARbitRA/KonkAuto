#!/usr/bin/env python3
"""Build the 19-slide monochrome KONKAUTO technical manifesto PDF."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from manifesto_theme import W, H, register_fonts  # noqa: E402
from manifesto_slides import (  # noqa: E402
    draw_01, draw_02, draw_03, draw_04, draw_05,
    draw_06, draw_07, draw_08, draw_09, draw_10,
    draw_11, draw_12, draw_13, draw_14, draw_15,
    draw_16, draw_17, draw_18, draw_19,
)

SLIDES = [
    draw_01, draw_02, draw_03, draw_04, draw_05,
    draw_06, draw_07, draw_08, draw_09, draw_10,
    draw_11, draw_12, draw_13, draw_14, draw_15,
    draw_16, draw_17, draw_18, draw_19,
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "KONKAUTO_SDAD_Manifesto_19slides.pdf",
        help="output PDF path (default: repository root / KONKAUTO_SDAD_Manifesto_19slides.pdf)",
    )
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    register_fonts()
    pdf = canvas.Canvas(str(args.output), pagesize=(W, H), pageCompression=1, invariant=1)
    pdf.setTitle("KONKAUTO — A Technical Doctrine for Specification-Driven Agentic Development")
    pdf.setAuthor("KONKAUTO")
    pdf.setSubject("Specification-Driven Agentic Development — 19-slide manifesto")
    pdf.setKeywords("KONKAUTO, SDAD, agents, specification, governance, traceability")
    pdf.setCreator("KONKAUTO monochrome vector manifesto generator")
    for slide in SLIDES:
        slide(pdf)
        pdf.showPage()
    pdf.save()
    print(f"Wrote {args.output} ({len(SLIDES)} slides)")


if __name__ == "__main__":
    main()
