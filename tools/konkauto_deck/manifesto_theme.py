"""Monochrome industrial visual system for the 19-slide KONKAUTO manifesto deck."""
from __future__ import annotations

import math
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

from theme import W, H, register_fonts as register_base_fonts, draw_wrapped

BLACK = HexColor("#000000")
WHITE = HexColor("#FFFFFF")
CYAN = HexColor("#7C9BFF")

LEFT = 92
RIGHT = 1828
TOP = 1008
BOTTOM = 76
CONTENT_W = RIGHT - LEFT

ACTS = {
    1: "FOUNDATION",
    2: "CONTRACT",
    3: "EXECUTION",
    4: "GOVERNANCE",
    5: "ADOPTION",
}


def register_fonts():
    register_base_fonts()


def frame(c: canvas.Canvas, number: int, act: str, *, dark: bool, kicker: str = "KONKAUTO // SDAD TECHNICAL DOCTRINE"):
    """Alternating black/white master frame with a strict monochrome + cyan system."""
    bg = BLACK if dark else WHITE
    fg = WHITE if dark else BLACK
    c.setFillColor(bg)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Upper registration rule and a single cyan intervention mark.
    c.setStrokeColor(fg)
    c.setLineWidth(2)
    c.line(LEFT, TOP, RIGHT, TOP)
    c.setFillColor(CYAN)
    c.rect(LEFT, TOP - 3, 44, 6, fill=1, stroke=0)

    c.setFillColor(fg)
    c.setFont("PlexMonoBold", 13)
    c.drawString(LEFT, TOP + 16, kicker)
    c.drawRightString(RIGHT, TOP + 16, f"SDAD / 16:9       {number:02d} / 19")

    # Footer stays typographic and quiet; no extra color except the cyan registration block.
    c.setStrokeColor(fg)
    c.setLineWidth(3)
    c.line(LEFT, BOTTOM, RIGHT, BOTTOM)
    c.setFillColor(fg)
    c.setFont("PlexMonoBold", 13)
    c.drawString(LEFT, BOTTOM - 26, f"KONKAUTO / {act} / SPECIFICATION-DRIVEN AGENTIC DEVELOPMENT")
    c.drawRightString(RIGHT, BOTTOM - 26, f"{number:02d} / 19")
    c.setFillColor(CYAN)
    c.rect(LEFT, BOTTOM - 3, 26, 6, fill=1, stroke=0)


def headline(c, text, *, x=LEFT, y=918, size=58, color=WHITE, font="ArchivoBlack"):
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawString(x, y, text)


def text(c, x, y, value, *, size=22, color=WHITE, font="PlexSans", align="left"):
    c.setFillColor(color)
    c.setFont(font, size)
    if align == "center":
        c.drawCentredString(x, y, value)
    elif align == "right":
        c.drawRightString(x, y, value)
    else:
        c.drawString(x, y, value)


def paragraph(c, x, y_top, value, *, width, size=21, leading=28, color=WHITE, font="PlexSans", align="left"):
    return draw_wrapped(c, x, y_top, value, font, size, leading, width, color=color, align=align)


def plate(c, x, y, w, h, *, fill=BLACK, stroke=WHITE, lw=3, accent=None, accent_width=10, rivets=True):
    c.saveState()
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(lw)
    c.rect(x, y, w, h, fill=1, stroke=1)
    if accent is not None:
        c.setFillColor(accent)
        c.rect(x, y, accent_width, h, fill=1, stroke=0)
    if rivets:
        c.setFillColor(stroke)
        r = 3
        for rx, ry in ((x + 10, y + 10), (x + w - 10, y + 10), (x + 10, y + h - 10), (x + w - 10, y + h - 10)):
            c.circle(rx, ry, r, fill=1, stroke=0)
    c.restoreState()


def arrow(c, x1, y1, x2, y2, *, color=WHITE, lw=4, head=16, double=False, dash=None):
    c.saveState()
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(lw)
    if dash:
        c.setDash(*dash)
    theta = math.atan2(y2 - y1, x2 - x1)
    pad = head * 0.7
    sx1, sy1 = x1, y1
    if double:
        sx1 = x1 + pad * math.cos(theta)
        sy1 = y1 + pad * math.sin(theta)
    ex2 = x2 - pad * math.cos(theta)
    ey2 = y2 - pad * math.sin(theta)
    c.line(sx1, sy1, ex2, ey2)
    c.setDash()

    def draw_head(x, y, angle):
        p = c.beginPath()
        p.moveTo(x, y)
        p.lineTo(x - head * math.cos(angle) + head * 0.62 * math.sin(angle),
                 y - head * math.sin(angle) - head * 0.62 * math.cos(angle))
        p.lineTo(x - head * math.cos(angle) - head * 0.62 * math.sin(angle),
                 y - head * math.sin(angle) + head * 0.62 * math.cos(angle))
        p.close()
        c.drawPath(p, fill=1, stroke=0)

    draw_head(x2, y2, theta)
    if double:
        draw_head(x1, y1, theta + math.pi)
    c.restoreState()


def gear(c, cx, cy, outer, inner=None, teeth=12, *, fill=WHITE, stroke=BLACK, hole=0, phase=0.0, lw=3):
    """Hard-edged vector gear; all fills remain within black, white, and cyan."""
    if inner is None:
        inner = outer * 0.76
    c.saveState()
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(lw)
    path = c.beginPath()
    step = 2 * math.pi / teeth
    points = []
    for i in range(teeth):
        a = phase + i * step
        points.extend([
            (cx + inner * math.cos(a), cy + inner * math.sin(a)),
            (cx + inner * math.cos(a + step * 0.16), cy + inner * math.sin(a + step * 0.16)),
            (cx + outer * math.cos(a + step * 0.31), cy + outer * math.sin(a + step * 0.31)),
            (cx + outer * math.cos(a + step * 0.69), cy + outer * math.sin(a + step * 0.69)),
            (cx + inner * math.cos(a + step * 0.84), cy + inner * math.sin(a + step * 0.84)),
        ])
    path.moveTo(*points[0])
    for p in points[1:]:
        path.lineTo(*p)
    path.close()
    c.drawPath(path, fill=1, stroke=1)
    if hole:
        c.setFillColor(BLACK if fill != BLACK else WHITE)
        c.circle(cx, cy, hole, fill=1, stroke=1)
    c.restoreState()


def beam(c, x1, y1, x2, y2, *, color=WHITE, width=12):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.setLineCap(0)
    c.line(x1, y1, x2, y2)
    c.restoreState()


def rivets(c, coords, color=WHITE, radius=4):
    c.saveState()
    c.setFillColor(color)
    for x, y in coords:
        c.circle(x, y, radius, fill=1, stroke=0)
    c.restoreState()


def hatch(c, x, y, w, h, *, color=WHITE, spacing=14, lw=2, reverse=False):
    """Restrained 45-degree monochrome hatching, clipped to a rectangular bay."""
    c.saveState()
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    pos = -h - 10
    while pos <= w + h:
        if reverse:
            c.line(x + pos, y + h, x + pos + h, y)
        else:
            c.line(x + pos, y, x + pos + h, y + h)
        pos += spacing
    c.restoreState()


def bolt(c, cx, cy, r=16, color=CYAN, stroke=BLACK):
    c.saveState()
    c.setFillColor(color)
    c.setStrokeColor(stroke)
    c.setLineWidth(2)
    c.circle(cx, cy, r, fill=1, stroke=1)
    c.setStrokeColor(stroke)
    c.setLineWidth(2)
    c.line(cx - r * 0.45, cy, cx + r * 0.45, cy)
    c.restoreState()


def person(c, x, y, scale=1.0, *, color=WHITE, stroke=BLACK, mechanical=False):
    """Anonymous angular human/operator silhouette (never a cute robot)."""
    c.saveState()
    c.setFillColor(color)
    c.setStrokeColor(stroke)
    c.setLineWidth(3 * scale)
    c.circle(x + 38 * scale, y + 190 * scale, 24 * scale, fill=1, stroke=1)
    p = c.beginPath()
    p.moveTo(x + 4 * scale, y + 72 * scale)
    p.lineTo(x + 15 * scale, y + 150 * scale)
    p.lineTo(x + 28 * scale, y + 166 * scale)
    p.lineTo(x + 51 * scale, y + 166 * scale)
    p.lineTo(x + 65 * scale, y + 150 * scale)
    p.lineTo(x + 76 * scale, y + 72 * scale)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.setLineWidth(13 * scale)
    c.line(x + 21 * scale, y + 72 * scale, x + 14 * scale, y + 4 * scale)
    c.line(x + 58 * scale, y + 72 * scale, x + 66 * scale, y + 4 * scale)
    c.setLineWidth(11 * scale)
    c.line(x + 12 * scale, y + 145 * scale, x - 15 * scale, y + 110 * scale)
    c.line(x + 65 * scale, y + 145 * scale, x + 94 * scale, y + 112 * scale)
    if mechanical:
        # Mechanical seams and exposed pivots are white/black/cyan only.
        c.setStrokeColor(CYAN)
        c.setLineWidth(3 * scale)
        c.line(x + 38 * scale, y + 155 * scale, x + 38 * scale, y + 87 * scale)
        c.setFillColor(CYAN)
        c.circle(x + 38 * scale, y + 126 * scale, 5 * scale, fill=1, stroke=0)
        c.circle(x + 38 * scale, y + 91 * scale, 5 * scale, fill=1, stroke=0)
    c.restoreState()


def gate(c, cx, cy, width=84, height=70, *, label="G", dark=True):
    """Human-only cyan lock gate with black lettering on cyan."""
    c.saveState()
    fg = WHITE if dark else BLACK
    c.setStrokeColor(CYAN)
    c.setLineWidth(8)
    c.arc(cx - width * 0.28, cy + height * 0.08, cx + width * 0.28, cy + height * 0.88, 0, 180)
    c.line(cx - width * 0.28, cy + height * 0.42, cx - width * 0.28, cy + height * 0.04)
    c.line(cx + width * 0.28, cy + height * 0.42, cx + width * 0.28, cy + height * 0.04)
    c.setFillColor(CYAN)
    c.setStrokeColor(fg)
    c.setLineWidth(3)
    c.rect(cx - width / 2, cy - height / 2, width, height * 0.64, fill=1, stroke=1)
    c.setFillColor(BLACK)
    c.setFont("ArchivoBlack", 18)
    c.drawCentredString(cx, cy - 11, label)
    c.restoreState()


def center_label(c, cx, y, value, *, size=18, color=WHITE, font="PlexMonoBold"):
    text(c, cx, y, value, size=size, color=color, font=font, align="center")
