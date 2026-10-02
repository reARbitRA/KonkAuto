import math
from pathlib import Path
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = Path(__file__).resolve().parents[2] / "assets" / "fonts"

# Page geometry: 16:9 widescreen (1920 x 1080 pt)
W = 1920
H = 1080
MARGIN_X = 94
MARGIN_TOP = 72
MARGIN_BOTTOM = 76
COLS = 12
GUTTER = 20
COL_W = (W - 2 * MARGIN_X - (COLS - 1) * GUTTER) / COLS  # 126.0 pt

# Strict Palette from Master Prompt
COAL_HEX = "#101214"
BONE_HEX = "#F2F0E8"
ORANGE_HEX = "#F05A28"
YELLOW_HEX = "#FFD447"
STEEL_HEX = "#748088"
GREEN_HEX = "#72D48C"

COAL = HexColor(COAL_HEX)
BONE = HexColor(BONE_HEX)
ORANGE = HexColor(ORANGE_HEX)
YELLOW = HexColor(YELLOW_HEX)
STEEL = HexColor(STEEL_HEX)
GREEN = HexColor(GREEN_HEX)

# Tonal structural greys derived strictly within the coal/steel/bone axis for ink depth
COAL_LIGHT = HexColor("#1B1F23")
COAL_MID = HexColor("#262B30")
STEEL_DARK = HexColor("#4A5359")
STEEL_LIGHT = HexColor("#A7B0B6")
BONE_DARK = HexColor("#DEDAD0")
BONE_MID = HexColor("#E6E3D8")


def register_fonts():
    """Register the locally bundled, OFL-licensed display, sans, and mono fonts."""
    pdfmetrics.registerFont(TTFont("ArchivoBlack", str(FONT_DIR / "ArchivoBlack-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("PlexSans", str(FONT_DIR / "IBMPlexSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("PlexSansMedium", str(FONT_DIR / "IBMPlexSans-Medium.ttf")))
    pdfmetrics.registerFont(TTFont("PlexSansSemiBold", str(FONT_DIR / "IBMPlexSans-SemiBold.ttf")))
    pdfmetrics.registerFont(TTFont("PlexSansBold", str(FONT_DIR / "IBMPlexSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("PlexMono", str(FONT_DIR / "IBMPlexMono-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("PlexMonoMedium", str(FONT_DIR / "IBMPlexMono-Medium.ttf")))
    pdfmetrics.registerFont(TTFont("PlexMonoSemiBold", str(FONT_DIR / "IBMPlexMono-SemiBold.ttf")))
    pdfmetrics.registerFont(TTFont("PlexMonoBold", str(FONT_DIR / "IBMPlexMono-Bold.ttf")))


def col_x(col_idx):
    """0-indexed column left X coordinate (0..11)."""
    return MARGIN_X + col_idx * (COL_W + GUTTER)


def col_span_w(num_cols):
    """Width of `num_cols` columns including internal gutters."""
    return num_cols * COL_W + (num_cols - 1) * GUTTER


def draw_slide_frame(c, slide_num, act_name, bg_mode="coal", kicker=None):
    """
    Draws the background (Coal or Bone), subtle exposed 12-column engineering grid,
    corner registration crosshairs, top structural bar, and the required running footer:
    'KONKAUTO / [ACT NAME]                                      NN / 20'
    """
    is_coal = (bg_mode == "coal")
    bg_color = COAL if is_coal else BONE
    fg_color = BONE if is_coal else COAL
    grid_color = COAL_LIGHT if is_coal else BONE_DARK
    rule_color = STEEL_DARK if is_coal else COAL

    # Background fill
    c.saveState()
    c.setFillColor(bg_color)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Exposed 12-column grid (subtle vertical guide lines & top/bottom ticks)
    c.setStrokeColor(grid_color)
    c.setLineWidth(0.75)
    for i in range(COLS):
        xL = col_x(i)
        xR = xL + COL_W
        c.line(xL, MARGIN_BOTTOM, xL, H - MARGIN_TOP)
        c.line(xR, MARGIN_BOTTOM, xR, H - MARGIN_TOP)

    # Horizontal grid hairlines
    for y in range(int(MARGIN_BOTTOM + 120), int(H - MARGIN_TOP), 120):
        c.line(MARGIN_X, y, W - MARGIN_X, y)

    # Registration marks at the 4 corners of the content frame
    c.setStrokeColor(STEEL)
    c.setLineWidth(1.5)
    corners = [
        (MARGIN_X, MARGIN_BOTTOM),
        (W - MARGIN_X, MARGIN_BOTTOM),
        (MARGIN_X, H - MARGIN_TOP),
        (W - MARGIN_X, H - MARGIN_TOP),
    ]
    for cx, cy in corners:
        c.line(cx - 10, cy, cx + 10, cy)
        c.line(cx, cy - 10, cx, cy + 10)

    # Top structural rule
    top_y = H - MARGIN_TOP
    c.setStrokeColor(fg_color if not is_coal else STEEL)
    c.setLineWidth(2.5)
    c.line(MARGIN_X, top_y, W - MARGIN_X, top_y)

    # Optional top kicker / classification bar above top rule
    c.setFont("PlexMonoBold", 13)
    c.setFillColor(STEEL if is_coal else STEEL_DARK)
    top_label = kicker if kicker else f"SYS.BLUEPRINT // {act_name}"
    c.drawString(MARGIN_X, top_y + 14, top_label)
    c.drawRightString(W - MARGIN_X, top_y + 14, f"SLIDE {slide_num:02d} // 16:9 VECTOR SPEC")

    # Small orange accent block on top rule left
    c.setFillColor(ORANGE)
    c.rect(MARGIN_X, top_y - 3, 48, 6, fill=1, stroke=0)

    # Bottom heavy baseline and running footer
    bot_y = MARGIN_BOTTOM
    c.setStrokeColor(fg_color)
    c.setLineWidth(3.5)
    c.line(MARGIN_X, bot_y, W - MARGIN_X, bot_y)

    # Footer text: "KONKAUTO / [ACT NAME]                                      NN / 20"
    c.setFont("PlexMonoBold", 14)
    c.setFillColor(fg_color)
    c.drawString(MARGIN_X, bot_y - 28, f"KONKAUTO / {act_name}")
    c.drawRightString(W - MARGIN_X, bot_y - 28, f"{slide_num:02d} / 20")

    # Decorative micro-notches along bottom baseline
    c.setFillColor(ORANGE)
    c.rect(MARGIN_X, bot_y - 3.5, 28, 7, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.rect(W - MARGIN_X - 90, bot_y - 3.5, 18, 7, fill=1, stroke=0)

    c.restoreState()


def draw_halftone_rect(c, x, y, w, h, dot_color, spacing=14, radius=2.2):
    """Draws a restrained graphic-novel vector halftone dot field inside (x, y, w, h)."""
    c.saveState()
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.setFillColor(dot_color)
    row = 0
    cy = y + spacing / 2.0
    while cy < y + h:
        offset = (spacing / 2.0) if (row % 2 == 1) else 0
        cx = x + spacing / 2.0 + offset
        while cx < x + w:
            c.circle(cx, cy, radius, stroke=0, fill=1)
            cx += spacing
        cy += spacing * 0.866
        row += 1
    c.restoreState()


def draw_hatch_rect(c, x, y, w, h, line_color, spacing=12, lw=1.5, angle=45):
    """Draws crisp diagonal architectural hatching clipped to a rectangle."""
    c.saveState()
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.setStrokeColor(line_color)
    c.setLineWidth(lw)
    diag = w + h + 40
    step = spacing
    pos = -h - 20
    while pos < w + 20:
        if angle >= 0:
            c.line(x + pos, y, x + pos + h, y + h)
        else:
            c.line(x + pos, y + h, x + pos + h, y)
        pos += step
    c.restoreState()


def draw_hazard_band(c, x, y, w, h, stripe_w=18, bg_col=YELLOW, fg_col=COAL, border_w=2.5):
    """Draws a classic brutalist industrial hazard stripe bar (yellow & coal)."""
    c.saveState()
    c.setFillColor(bg_col)
    c.rect(x, y, w, h, fill=1, stroke=0)
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.setFillColor(fg_col)
    pos = -h - stripe_w
    while pos < w + h:
        poly = c.beginPath()
        poly.moveTo(x + pos, y)
        poly.lineTo(x + pos + stripe_w, y)
        poly.lineTo(x + pos + stripe_w + h, y + h)
        poly.lineTo(x + pos + h, y + h)
        poly.close()
        c.drawPath(poly, fill=1, stroke=0)
        pos += stripe_w * 2
    c.restoreState()
    if border_w > 0:
        c.saveState()
        c.setStrokeColor(COAL)
        c.setLineWidth(border_w)
        c.rect(x, y, w, h, fill=0, stroke=1)
        c.restoreState()


def draw_brutalist_plate(
    c, x, y, w, h, fill_col=COAL_LIGHT, stroke_col=BONE, lw=3.0,
    shadow_offset=6, shadow_col=COAL, rivets=True, rivet_col=STEEL
):
    """Draws a square-edged industrial plate with hard graphic-novel shadow and corner rivets."""
    c.saveState()
    if shadow_offset and shadow_col is not None:
        c.setFillColor(shadow_col)
        c.rect(x + shadow_offset, y - shadow_offset, w, h, fill=1, stroke=0)
    c.setFillColor(fill_col)
    c.setStrokeColor(stroke_col)
    c.setLineWidth(lw)
    c.rect(x, y, w, h, fill=1, stroke=1)
    if rivets:
        c.setFillColor(rivet_col)
        inset = 9
        for rx, ry in [(x + inset, y + inset), (x + w - inset, y + inset),
                       (x + inset, y + h - inset), (x + w - inset, y + h - inset)]:
            c.circle(rx, ry, 2.8, fill=1, stroke=0)
    c.restoreState()


def draw_arrow(c, x1, y1, x2, y2, color=BONE, lw=3.5, head_len=14, head_w=9, bidirectional=False, dashed=False):
    """Draws a crisp vector arrow (single or double-headed)."""
    c.saveState()
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(lw)
    if dashed:
        c.setDash(8, 5)
    angle = math.atan2(y2 - y1, x2 - x1)
    sx1, sy1 = x1, y1
    sx2, sy2 = x2 - head_len * 0.7 * math.cos(angle), y2 - head_len * 0.7 * math.sin(angle)
    if bidirectional:
        sx1, sy1 = x1 + head_len * 0.7 * math.cos(angle), y1 + head_len * 0.7 * math.sin(angle)
    c.line(sx1, sy1, sx2, sy2)
    c.setDash()

    # Forward head at (x2, y2)
    p = c.beginPath()
    p.moveTo(x2, y2)
    p.lineTo(x2 - head_len * math.cos(angle) + head_w * math.sin(angle),
             y2 - head_len * math.sin(angle) - head_w * math.cos(angle))
    p.lineTo(x2 - head_len * math.cos(angle) - head_w * math.sin(angle),
             y2 - head_len * math.sin(angle) + head_w * math.cos(angle))
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    if bidirectional:
        p2 = c.beginPath()
        p2.moveTo(x1, y1)
        p2.lineTo(x1 + head_len * math.cos(angle) + head_w * math.sin(angle),
                  y1 + head_len * math.sin(angle) - head_w * math.cos(angle))
        p2.lineTo(x1 + head_len * math.cos(angle) - head_w * math.sin(angle),
                  y1 + head_len * math.sin(angle) + head_w * math.cos(angle))
        p2.close()
        c.drawPath(p2, fill=1, stroke=0)
    c.restoreState()


def draw_gear(c, cx, cy, r_outer, r_inner, r_hole, num_teeth, fill_col=STEEL, stroke_col=COAL, lw=2.5, phase=0.0):
    """Draws a precision mechanical gear."""
    c.saveState()
    c.setFillColor(fill_col)
    c.setStrokeColor(stroke_col)
    c.setLineWidth(lw)
    p = c.beginPath()
    step = 2 * math.pi / num_teeth
    for i in range(num_teeth):
        a0 = phase + i * step
        a1 = a0 + step * 0.18
        a2 = a0 + step * 0.32
        a3 = a0 + step * 0.68
        a4 = a0 + step * 0.82
        pts = [
            (cx + r_inner * math.cos(a0), cy + r_inner * math.sin(a0)),
            (cx + r_inner * math.cos(a1), cy + r_inner * math.sin(a1)),
            (cx + r_outer * math.cos(a2), cy + r_outer * math.sin(a2)),
            (cx + r_outer * math.cos(a3), cy + r_outer * math.sin(a3)),
            (cx + r_inner * math.cos(a4), cy + r_inner * math.sin(a4)),
        ]
        if i == 0:
            p.moveTo(*pts[0])
        else:
            p.lineTo(*pts[0])
        for pt in pts[1:]:
            p.lineTo(*pt)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    if r_hole > 0:
        c.setFillColor(COAL)
        c.circle(cx, cy, r_hole, fill=1, stroke=1)
    c.restoreState()


def draw_padlock(c, cx, cy, w=46, h=38, body_col=YELLOW, stroke_col=COAL, lw=3.0, label="G"):
    """Draws a heavy industrial human-gate padlock in Hazard Yellow with dark Coal contour & text."""
    c.saveState()
    # Shackle
    shackle_r = w * 0.30
    shackle_cy = cy + h * 0.5
    c.setStrokeColor(stroke_col)
    c.setLineWidth(lw * 1.8)
    p = c.beginPath()
    p.moveTo(cx - shackle_r, shackle_cy - 2)
    p.lineTo(cx - shackle_r, shackle_cy + shackle_r * 0.6)
    p.arc(cx - shackle_r, shackle_cy - shackle_r * 0.4, cx + shackle_r, shackle_cy + shackle_r * 1.6, 0, 180)
    p.lineTo(cx + shackle_r, shackle_cy - 2)
    c.drawPath(p, fill=0, stroke=1)

    # Lock body
    bx = cx - w / 2.0
    by = cy - h / 2.0
    c.setFillColor(body_col)
    c.setStrokeColor(stroke_col)
    c.setLineWidth(lw)
    c.rect(bx, by, w, h, fill=1, stroke=1)

    # Top hazard stripe on lock
    draw_hazard_band(c, bx + 2, by + h - 9, w - 4, 7, stripe_w=6, bg_col=YELLOW, fg_col=COAL, border_w=0)

    # Keyhole or label (ALWAYS dark COAL on YELLOW!)
    c.setFillColor(COAL)
    if label:
        c.setFont("ArchivoBlack", 14)
        c.drawCentredString(cx, by + 9, label)
    else:
        c.circle(cx, by + h * 0.42, 4.5, fill=1, stroke=0)
        c.rect(cx - 2, by + 6, 4, h * 0.3, fill=1, stroke=0)
    c.restoreState()


def draw_badge(c, x, y, text, bg_col=YELLOW, fg_col=COAL, border_col=COAL, font="PlexMonoBold", size=13, pad_x=10, h=26):
    """Draws a sharp square-edged status/ID badge and returns its width."""
    c.saveState()
    tw = pdfmetrics.stringWidth(text, font, size)
    w = tw + 2 * pad_x
    c.setFillColor(bg_col)
    c.setStrokeColor(border_col)
    c.setLineWidth(2.0)
    c.rect(x, y, w, h, fill=1, stroke=1)
    c.setFillColor(fg_col)
    c.setFont(font, size)
    c.drawString(x + pad_x, y + (h - size) / 2.0 + 2, text)
    c.restoreState()
    return w


def wrap_lines(text, font, size, max_w):
    """Splits text into lines that fit within max_w."""
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_w or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(c, x, y_top, text, font, size, leading, max_w, color=BONE, align="left"):
    """Draws multi-line wrapped text starting at y_top and returns the next y position."""
    c.saveState()
    c.setFont(font, size)
    c.setFillColor(color)
    lines = wrap_lines(text, font, size, max_w)
    cy = y_top
    for ln in lines:
        if align == "left":
            c.drawString(x, cy, ln)
        elif align == "center":
            c.drawCentredString(x + max_w / 2.0, cy, ln)
        elif align == "right":
            c.drawRightString(x + max_w, cy, ln)
        cy -= leading
    c.restoreState()
    return cy
