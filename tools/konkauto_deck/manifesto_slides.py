"""Nineteen-slide monochrome/cyan KONKAUTO industrial manifesto."""
from __future__ import annotations

import math
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

from manifesto_theme import (
    BLACK, WHITE, CYAN, LEFT, RIGHT, CONTENT_W,
    frame, headline, text, paragraph, plate, arrow, gear, beam, rivets,
    hatch, bolt, person, gate, center_label,
)

ACT_I = "FOUNDATION"
ACT_II = "CONTRACT"
ACT_III = "EXECUTION"
ACT_IV = "GOVERNANCE"
ACT_V = "ADOPTION"


def _color(dark):
    return (WHITE, BLACK) if dark else (BLACK, WHITE)


def _heading(c, title, *, dark, size=54, y=918):
    fg, _ = _color(dark)
    headline(c, title, y=y, size=size, color=fg)


def _line(c, x1, y1, x2, y2, color=WHITE, width=2):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1, y1, x2, y2)
    c.restoreState()


def _poly(c, points, *, fill=BLACK, stroke=WHITE, lw=3):
    c.saveState()
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(lw)
    p = c.beginPath()
    p.moveTo(*points[0])
    for pt in points[1:]:
        p.lineTo(*pt)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.restoreState()


def _pillar(c, x, y, w, h, *, dark=True, accent=True):
    fg, bg = _color(dark)
    c.saveState()
    c.setFillColor(bg)
    c.setStrokeColor(fg)
    c.setLineWidth(4)
    c.rect(x, y, w, h, fill=1, stroke=1)
    c.rect(x - 14, y + h - 22, w + 28, 22, fill=1, stroke=1)
    c.rect(x - 20, y - 16, w + 40, 16, fill=1, stroke=1)
    if accent:
        c.setFillColor(CYAN)
        c.rect(x + 12, y + 14, 8, h - 52, fill=1, stroke=0)
    c.restoreState()


def draw_01(c):
    """Title sheet — the specification is the source."""
    frame(c, 1, ACT_I, dark=True, kicker="KONKAUTO // ENGINEERING DOCTRINE 01")
    text(c, 100, 820, "KONKAUTO", size=104, color=WHITE, font="ArchivoBlack")
    text(c, 104, 730, "A MAXIMUM-TIER METHODOLOGY FOR", size=25, color=CYAN, font="PlexMonoBold")
    text(c, 104, 690, "SPECIFICATION-DRIVEN AGENTIC DEVELOPMENT", size=30, color=WHITE, font="ArchivoBlack")
    text(c, 104, 651, "(SDAD)", size=27, color=WHITE, font="PlexMonoBold")

    # Three-line doctrine block.
    text(c, 104, 525, "THE REPOSITORY IS THE BRAIN.", size=30, color=WHITE, font="ArchivoBlack")
    text(c, 104, 478, "THE AGENT IS THE HANDS.", size=30, color=WHITE, font="ArchivoBlack")
    text(c, 104, 431, "MARKDOWN IS THE CONTRACT.", size=30, color=WHITE, font="ArchivoBlack")
    _line(c, 104, 406, 560, 406, CYAN, 7)
    text(c, 104, 346, "THE SPECIFICATION IS THE SOURCE.", size=22, color=WHITE, font="PlexMonoBold")
    text(c, 104, 310, "A technical doctrine for systems that outlive every session.", size=19, color=WHITE, font="PlexSans")

    # Monumental steel frame structure, partially revealed in high-contrast cutaway.
    fx, fy, fw, fh = 1132, 172, 652, 738
    c.setStrokeColor(WHITE)
    c.setLineWidth(5)
    c.rect(fx, fy, fw, fh, fill=0, stroke=1)
    # Main load-bearing columns and 5 horizontal I-beam levels.
    for x in (fx + 54, fx + 300, fx + fw - 54):
        beam(c, x, fy + 30, x, fy + fh - 30, color=WHITE, width=20)
        _line(c, x - 13, fy + 30, x + 13, fy + 30, BLACK, 4)
    for i in range(1, 6):
        y = fy + i * fh / 6
        beam(c, fx + 32, y, fx + fw - 32, y, color=WHITE, width=15)
        _line(c, fx + 40, y, fx + fw - 40, y, BLACK, 3)
    # Cross bracing, truss bays and a single cyan load-bearing seam.
    for i in range(5):
        y0 = fy + 30 + i * (fh - 60) / 5
        y1 = y0 + (fh - 60) / 5
        _line(c, fx + 74, y0, fx + 282, y1, WHITE, 5)
        _line(c, fx + 318, y0, fx + fw - 74, y1, WHITE, 5)
        _line(c, fx + fw - 74, y0, fx + 318, y1, WHITE, 5)
    beam(c, fx + fw - 52, fy + 40, fx + fw - 52, fy + fh - 40, color=CYAN, width=10)
    rivets(c, [(fx + 54, fy + 32 + i * 126) for i in range(6)], WHITE, 5)
    rivets(c, [(fx + fw - 54, fy + 32 + i * 126) for i in range(6)], WHITE, 5)
    text(c, fx + 28, fy + fh + 18, "LOAD-BEARING SPECIFICATION FRAME", size=14, color=CYAN, font="PlexMonoBold")


def draw_02(c):
    """Core thesis — code is a derivative."""
    frame(c, 2, ACT_I, dark=False, kicker="THESIS / CODE IS A DERIVATIVE")
    _heading(c, "CODE IS NOT THE SOURCE OF TRUTH.", dark=False, size=54)

    keypoints = [
        ("CODE IS DERIVED", "A specification is the source; implementation is its output."),
        ("COMPLETE + VERSIONED", "Machine-legible contracts can be regenerated, extended, repaired or rebuilt."),
        ("NOT THE CODE", "The source of truth is never the product code."),
        ("THE DOCUMENTATION", "It is the documentation the code was compiled from."),
    ]
    y = 775
    for i, (label, desc) in enumerate(keypoints):
        c.setFillColor(CYAN)
        c.rect(102, y - 12, 9, 64, fill=1, stroke=0)
        text(c, 132, y + 24, label, size=19, color=BLACK, font="PlexMonoBold")
        paragraph(c, 132, y - 4, desc, width=610, size=18, leading=23, color=BLACK, font="PlexSans")
        y -= 148

    # A hard-edged printing press: specification plates feed gears; code exits as product.
    mx, my = 1000, 250
    plate(c, mx, my, 780, 590, fill=BLACK, stroke=BLACK, lw=3, accent=CYAN, rivets=False)
    # Input document rollers and steel sheets.
    for i, label in enumerate(("SPEC", "ADR", "AC")):
        x = mx + 58 + i * 150
        c.setFillColor(WHITE)
        c.setStrokeColor(BLACK)
        c.setLineWidth(3)
        c.rect(x, my + 368, 112, 118, fill=1, stroke=1)
        c.setStrokeColor(CYAN if i == 0 else BLACK)
        c.setLineWidth(3)
        for j in range(3):
            c.line(x + 17, my + 455 - j * 22, x + 91, my + 455 - j * 22)
        text(c, x + 56, my + 386, label, size=16, color=BLACK, font="PlexMonoBold", align="center")
    arrow(c, mx + 80, my + 330, mx + 286, my + 330, color=CYAN, lw=6, head=19)
    # Press housing and opposed gears.
    c.setStrokeColor(WHITE)
    c.setLineWidth(7)
    c.rect(mx + 268, my + 118, 310, 246, fill=0, stroke=1)
    gear(c, mx + 360, my + 254, 79, 62, 12, fill=WHITE, stroke=BLACK, hole=22, lw=3)
    gear(c, mx + 489, my + 254, 79, 62, 12, fill=CYAN, stroke=BLACK, hole=22, lw=3, phase=0.1)
    beam(c, mx + 384, my + 161, mx + 384, my + 120, color=WHITE, width=20)
    beam(c, mx + 465, my + 161, mx + 465, my + 120, color=WHITE, width=20)
    # Output code plates leave the press.
    arrow(c, mx + 578, my + 245, mx + 718, my + 245, color=CYAN, lw=6, head=20)
    for i in range(3):
        x = mx + 592 + i * 46
        c.setFillColor(WHITE)
        c.setStrokeColor(BLACK)
        c.setLineWidth(2)
        c.rect(x, my + 141 - i * 18, 38, 97, fill=1, stroke=1)
        c.setStrokeColor(BLACK)
        for j in range(3):
            c.line(x + 6, my + 215 - i * 18 - j * 18, x + 30, my + 215 - i * 18 - j * 18)
    text(c, mx + 388, my + 67, "DOCUMENTS IN  →  CODE OUT", size=16, color=WHITE, font="PlexMonoBold", align="center")
    text(c, 100, 142, "The specification is not a comment beside the source. It is the mold that gives the source its shape.", size=20, color=BLACK, font="PlexSansBold")


def draw_03(c):
    """Three laws — pillars that carry the system."""
    frame(c, 3, ACT_I, dark=True, kicker="STRUCTURAL LAWS / NON-NEGOTIABLE")
    _heading(c, "THE THREE LAWS OF KONKAUTO", dark=True, size=54)
    laws = [
        ("LAW 01", "POINTERS OVER IDEAS", "You never prompt the agent with ideas. You prompt it with pointers."),
        ("LAW 02", "STATELESS AGENTS BY DESIGN", "Every session is stateless. Continuity must come from the repository, not the chat."),
        ("LAW 03", "THE REPO MUST BOOTSTRAP ITSELF", "A brand-new agent with zero context must read one file and know how to proceed."),
    ]
    xs = [116, 704, 1292]
    for i, (law, title, desc) in enumerate(laws):
        x = xs[i]
        _pillar(c, x + 46, 287, 390, 470, dark=True, accent=(i == 1))
        text(c, x + 241, 799, law, size=17, color=CYAN, font="PlexMonoBold", align="center")
        text(c, x + 241, 680, title, size=21, color=WHITE, font="ArchivoBlack", align="center")
        paragraph(c, x + 63, 622, desc, width=356, size=20, leading=28, color=WHITE, font="PlexSans", align="center")
        # Load-transfer brackets.
        beam(c, x + 241, 265, x + 241, 208, color=WHITE, width=9)
        c.setStrokeColor(CYAN if i == 1 else WHITE)
        c.setLineWidth(4)
        c.line(x + 30, 205, x + 452, 205)
        c.circle(x + 30, 205, 7, fill=1, stroke=1)
        c.circle(x + 452, 205, 7, fill=1, stroke=1)
    text(c, LEFT + 8, 137, "PILLARS, NOT ADVICE: REMOVE ANY ONE AND THE OPERATING MODEL LOSES ITS LOAD PATH.", size=16, color=CYAN, font="PlexMonoBold")


def draw_04(c):
    """Repository as a cognitive architecture."""
    frame(c, 4, ACT_I, dark=False, kicker="REPOSITORY / EXTERNALIZED COGNITION")
    _heading(c, "THE REPOSITORY IS A COGNITIVE ARCHITECTURE", dark=False, size=48)
    paragraph(c, 100, 846, "KONKAUTO treats a software repository as more than storage: it is an externalized mind for humans and agents.", width=590, size=22, leading=31, color=BLACK, font="PlexSans")
    # Architectural head silhouette, left-facing profile, opened to expose mechanical memory.
    _poly(c, [(790, 250), (760, 385), (777, 604), (850, 781), (1035, 847), (1224, 801), (1320, 670), (1377, 647), (1331, 600), (1330, 478), (1258, 338), (1110, 265)], fill=BLACK, stroke=BLACK, lw=4)
    # Jaw/neck is a structural beam, not a body illustration.
    _poly(c, [(867, 270), (1018, 197), (1252, 237), (1325, 337), (1210, 373), (1070, 320)], fill=BLACK, stroke=BLACK, lw=3)
    # Cutaway brain rooms inside the cranium.
    for i, (x, y, label) in enumerate([(884, 601, "STATE"), (1074, 624, "LEDGER"), (963, 426, "SPECS"), (1154, 427, "TRACE")]):
        c.setFillColor(WHITE)
        c.setStrokeColor(WHITE)
        c.setLineWidth(3)
        c.rect(x, y, 154, 130, fill=1, stroke=1)
        for j in range(3):
            _line(c, x + 18, y + 90 - j * 25, x + 132, y + 90 - j * 25, BLACK, 3)
        gear(c, x + 128, y + 112, 22, 15, 8, fill=CYAN if i == 2 else BLACK, stroke=WHITE, hole=5, lw=2)
        text(c, x + 77, y + 17, label, size=12, color=BLACK, font="PlexMonoBold", align="center")
    # Rails and ducts join every memory room.
    c.setStrokeColor(CYAN)
    c.setLineWidth(7)
    c.line(1038, 666, 1070, 666)
    c.line(1040, 485, 1153, 485)
    c.line(1038, 472, 1038, 602)
    c.line(1230, 557, 1268, 557)
    # Articulated agent hands at lower right, built from engineered plates.
    beam(c, 1370, 465, 1500, 412, color=BLACK, width=44)
    beam(c, 1500, 412, 1602, 454, color=BLACK, width=34)
    for i in range(4):
        beam(c, 1600 + i * 27, 454, 1688 + i * 15, 520 - i * 40, color=BLACK, width=13)
        bolt(c, 1601 + i * 27, 454, 10, CYAN, BLACK)
    beam(c, 1376, 464, 1434, 322, color=BLACK, width=25)
    text(c, 1440, 264, "AGENT / EXECUTION HAND", size=14, color=CYAN, font="PlexMonoBold")
    # Thesis rail.
    plate(c, 100, 137, 1705, 83, fill=BLACK, stroke=BLACK, accent=CYAN, rivets=False)
    text(c, 136, 169, "THE REPOSITORY IS THE BRAIN  |  THE AGENT IS THE HANDS  |  MARKDOWN IS THE CONTRACT", size=19, color=WHITE, font="PlexMonoBold")


def draw_05(c):
    """Operating principles — nine engraved control-panel plates."""
    frame(c, 5, ACT_I, dark=True, kicker="CONTROL STANDARD / P1–P9")
    _heading(c, "THE OPERATING PRINCIPLES OF SDAD", dark=True, size=50)
    principles = [
        ("P1", "DOCS BEFORE CODE", "No src/ file without a spec link."),
        ("P2", "ONE ENTRY POINT", "AGENTS.md is always read first."),
        ("P3", "STATUS IS EXPLICIT", "Lifecycle state is visible in the record."),
        ("P4", "DECISIONS ARE IMMUTABLE", "A new ADR supersedes; it does not erase."),
        ("P5", "HANDOFFS ARE WRITTEN", "Snapshot current state; append the session history."),
        ("P6", "BIDIRECTIONAL TRACEABILITY", "Walk from spec to test and back."),
        ("P7", "AGENT PROPOSES", "Humans approve; the repository records."),
        ("P8", "VERIFY, DO NOT ASSERT", "A command exits 0; its output is recorded."),
        ("P9", "LEAST PRIVILEGE, ROTATED", "Scope write access; rotate the key."),
    ]
    # Hardwired logic bus behind the plates.
    for x in (646, 1241):
        beam(c, x, 230, x, 827, color=WHITE, width=5)
    for y in (423, 626):
        beam(c, 108, y, 1810, y, color=WHITE, width=5)
    panel_w, panel_h = 548, 178
    xs = [104, 690, 1276]
    ys = [636, 430, 224]
    for i, (pid, title, desc) in enumerate(principles):
        x, y = xs[i % 3], ys[i // 3]
        plate(c, x, y, panel_w, panel_h, fill=BLACK, stroke=WHITE, lw=2.4, accent=CYAN, accent_width=8, rivets=True)
        text(c, x + 26, y + 139, pid, size=17, color=CYAN, font="PlexMonoBold")
        text(c, x + 94, y + 137, title, size=17, color=WHITE, font="ArchivoBlack")
        paragraph(c, x + 26, y + 91, desc, width=panel_w - 52, size=18, leading=24, color=WHITE, font="PlexSans")


def draw_06(c):
    """Repository anatomy — a multi-level specification foundry."""
    frame(c, 6, ACT_II, dark=False, kicker="REPOSITORY / MACHINE-ROOM PLAN")
    _heading(c, "THE KONKAUTO REPOSITORY ANATOMY", dark=False, size=49)
    text(c, 102, 852, "Every directory has a purpose. No directory exists by accident.", size=21, color=CYAN, font="PlexSansBold")

    # AGENTS.md is the only front door.
    door_x, door_y = 100, 401
    plate(c, door_x, door_y, 280, 340, fill=BLACK, stroke=BLACK, lw=4, accent=CYAN, accent_width=12)
    # Gate arch and vault wheel
    c.setStrokeColor(WHITE)
    c.setLineWidth(6)
    c.rect(door_x + 34, door_y + 28, 212, 248, fill=0, stroke=1)
    c.arc(door_x + 70, door_y + 169, door_x + 210, door_y + 309, 0, 180)
    gear(c, door_x + 140, door_y + 150, 51, 39, 10, fill=CYAN, stroke=WHITE, hole=14, lw=3)
    text(c, door_x + 140, door_y + 298, "AGENTS.md", size=22, color=WHITE, font="PlexMonoBold", align="center")
    text(c, door_x + 140, door_y + 55, "SINGLE ENTRY", size=13, color=CYAN, font="PlexMonoBold", align="center")
    arrow(c, door_x + 280, door_y + 168, 442, door_y + 168, color=CYAN, lw=6, head=19)

    # Six steel floors represented by heavy chambers.
    floors = [
        ("MEMORY", ".forge/", "STATE.md · LEDGER.md · TRACE.md"),
        ("INTENT", "vision/ · brainstorm/ · knowledge/", "WHY · RAW IDEAS · REFERENCE"),
        ("CONTRACT", "specs/ · decisions/", "WHAT IS ALLOWED TO BE BUILT"),
        ("EXECUTION", "plans/ · tasks/", "ORDERED WORK / ATOMIC UNITS"),
        ("CONTROLS", "quality/ · ops/ · .github/", "QUALITY · SECURITY · CI"),
        ("PRODUCT", "src/ · tests/", "DERIVED CODE / VERIFIABLE BEHAVIOR"),
    ]
    bx, bw = 480, 1320
    by0, bh, gap = 177, 104, 12
    for i, (name, dirs, desc) in enumerate(floors):
        y = by0 + i * (bh + gap)
        plate(c, bx, y, bw, bh, fill=BLACK, stroke=BLACK, lw=2.4, accent=CYAN if i in (0, 2, 5) else None, accent_width=8, rivets=False)
        text(c, bx + 24, y + 73, f"FLOOR {6-i:02d} / {name}", size=13, color=CYAN, font="PlexMonoBold")
        text(c, bx + 265, y + 68, dirs, size=19, color=WHITE, font="PlexMonoBold")
        text(c, bx + 265, y + 31, desc, size=15, color=WHITE, font="PlexMono")
        arrow(c, door_x + 280, y + bh / 2, bx, y + bh / 2, color=BLACK, lw=2, head=11)
    text(c, 480, 145, "CODE IS OUTPUT, NOT AUTHORITY.", size=16, color=BLACK, font="PlexMonoBold")


def draw_07(c):
    """Knowledge flow — ideas become verified implementation."""
    frame(c, 7, ACT_II, dark=True, kicker="PROMOTION / RAW THOUGHT TO VERIFIABLE IMPLEMENTATION")
    _heading(c, "FROM RAW THOUGHT TO VERIFIABLE IMPLEMENTATION", dark=True, size=45)
    text(c, LEFT, 850, "Promotion is deliberate. Nothing becomes a contract by accident.", size=21, color=CYAN, font="PlexSansBold")

    labels = ["BRAINSTORM", "VISION", "SPEC", "ADR", "PLAN", "TASK", "BRANCH", "COMMIT", "TEST", "VERIFIED CODE"]
    x0, step_w = 105, 170
    y0 = 434
    # Conveyor rails and repeated rollers.
    beam(c, 105, y0, 1812, y0, color=WHITE, width=11)
    beam(c, 105, y0 - 38, 1812, y0 - 38, color=WHITE, width=11)
    for i in range(18):
        x = 126 + i * 96
        c.setFillColor(BLACK)
        c.setStrokeColor(WHITE)
        c.setLineWidth(3)
        c.circle(x, y0 - 18, 15, fill=1, stroke=1)
    for i, label in enumerate(labels):
        x = x0 + i * step_w
        h = 128 + (i % 3) * 28
        color = CYAN if i in (0, 2, 9) else WHITE
        # Each stage is a machine station, not a card.
        c.setFillColor(BLACK)
        c.setStrokeColor(color)
        c.setLineWidth(3)
        c.rect(x + 12, y0 + 10, 128, h, fill=1, stroke=1)
        beam(c, x + 28, y0 + 10, x + 28, y0 + h + 10, color=color, width=8)
        c.setFillColor(color)
        c.rect(x + 45, y0 + h - 8, 78, 8, fill=1, stroke=0)
        text(c, x + 76, y0 + h - 42, f"{i+1:02d}", size=17, color=CYAN, font="PlexMonoBold", align="center")
        # Station name is compact but readable, split if needed.
        if label == "VERIFIED CODE":
            text(c, x + 76, y0 + h - 76, "VERIFIED", size=13, color=WHITE, font="PlexMonoBold", align="center")
            text(c, x + 76, y0 + h - 99, "CODE", size=13, color=WHITE, font="PlexMonoBold", align="center")
        else:
            size = 12 if len(label) > 7 else 15
            text(c, x + 76, y0 + h - 78, label, size=size, color=WHITE, font="PlexMonoBold", align="center")
        if i < 9:
            arrow(c, x + 143, y0 + 82, x + step_w + 6, y0 + 82, color=CYAN if i == 1 else WHITE, lw=3, head=12)
    # Ore at entry, calibrated part at exit.
    for i in range(3):
        _poly(c, [(122 + i*22, 348), (136 + i*22, 371), (155 + i*22, 359), (146 + i*22, 337)], fill=CYAN if i == 1 else WHITE, stroke=BLACK, lw=2)
    c.setFillColor(WHITE)
    c.setStrokeColor(WHITE)
    c.setLineWidth(3)
    c.rect(1675, 324, 120, 72, fill=0, stroke=1)
    _line(c, 1690, 375, 1778, 375, CYAN, 4)
    _line(c, 1690, 355, 1758, 355, WHITE, 3)
    text(c, 105, 275, "ORE IN", size=14, color=CYAN, font="PlexMonoBold")
    text(c, 1678, 275, "CALIBRATED PART OUT", size=14, color=CYAN, font="PlexMonoBold")


def draw_08(c):
    """Governed document lifecycles as interlocked routing rails."""
    frame(c, 8, ACT_II, dark=False, kicker="LIFECYCLES / HUMAN-CONTROLLED TRANSITIONS")
    _heading(c, "STATUS IS THE CONTROL PLANE", dark=False, size=57)
    text(c, 100, 856, "Documents do not age. They transition by governance.", size=21, color=CYAN, font="PlexSansBold")
    tracks = [
        ("BRAINSTORM", ["SEED", "GROWING", "PROMOTED", "ABANDONED"]),
        ("SPEC", ["DRAFT", "REVIEW", "APPROVED", "IMPLEMENTING", "IMPLEMENTED", "VERIFIED", "DEPRECATED"]),
        ("ADR", ["PROPOSED", "ACCEPTED", "SUPERSEDED"]),
        ("PLAN", ["DRAFT", "ACTIVE", "COMPLETE", "ARCHIVED"]),
        ("TASK", ["OPEN", "DOING", "REVIEW", "DONE", "BLOCKED"]),
    ]
    label_x = 104
    track_x, track_w = 355, 1448
    row_y = [746, 616, 486, 356, 226]
    for (name, states), y in zip(tracks, row_y):
        text(c, label_x, y + 22, name, size=16, color=CYAN if name == "SPEC" else BLACK, font="PlexMonoBold")
        n = len(states)
        node_w = min(172, (track_w - 26*(n-1)) / n)
        gap = (track_w - n*node_w) / (n-1) if n > 1 else 0
        for j, state in enumerate(states):
            x = track_x + j * (node_w + gap)
            c.setFillColor(BLACK)
            c.setStrokeColor(BLACK)
            c.setLineWidth(2)
            c.rect(x, y, node_w, 68, fill=1, stroke=1)
            c.setFillColor(CYAN if state in ("APPROVED", "VERIFIED") else WHITE)
            c.rect(x, y + 58, node_w, 10, fill=1, stroke=0)
            font_size = 13 if len(state) > 10 else 14
            text(c, x + node_w/2, y + 27, state, size=font_size, color=BLACK if state in ("APPROVED", "VERIFIED") else WHITE, font="PlexMonoBold", align="center")
            if j < n - 1:
                col = CYAN if (name == "SPEC" and j in (1, 4)) else BLACK
                arrow(c, x + node_w, y + 34, x + node_w + gap, y + 34, color=col, lw=3, head=11)
        if name == "SPEC":
            # Human-only locks on REVIEW → APPROVED and IMPLEMENTED → VERIFIED.
            for j in (1, 4):
                gx = track_x + (j + 1) * node_w + (j + 0.5) * gap
                gate(c, gx, y + 35, width=38, height=34, label="H", dark=False)
            text(c, track_x + 380, y - 20, "HUMAN GATES / REVIEW → APPROVED  ·  IMPLEMENTED → VERIFIED", size=11, color=CYAN, font="PlexMonoBold")
    text(c, 100, 151, "BRAINSTORM  ·  SPEC  ·  ADR  ·  PLAN  ·  TASK — EACH TYPE HAS ITS OWN TRANSITIONS.", size=15, color=BLACK, font="PlexMonoBold")


def draw_09(c):
    """AGENTS.md — single point of bootstrap and authority."""
    frame(c, 9, ACT_II, dark=True, kicker="AGENTS.MD / THE CONSTITUTION")
    _heading(c, "AGENTS.MD — THE CONSTITUTION OF THE SYSTEM", dark=True, size=43)
    # Blast door / charter gateway.
    dx, dy, dw, dh = 670, 300, 600, 510
    _poly(c, [(dx, dy), (dx, dy+dh-90), (dx+85, dy+dh), (dx+dw-85, dy+dh), (dx+dw, dy+dh-90), (dx+dw, dy)], fill=BLACK, stroke=WHITE, lw=7)
    c.setStrokeColor(CYAN)
    c.setLineWidth(5)
    c.rect(dx+55, dy+40, dw-110, dh-125, fill=0, stroke=1)
    c.setFillColor(BLACK)
    c.setStrokeColor(WHITE)
    c.setLineWidth(4)
    c.rect(dx+120, dy+70, dw-240, dh-180, fill=1, stroke=1)
    text(c, dx+dw/2, dy+dh-72, "AGENTS.md", size=33, color=CYAN, font="PlexMonoBold", align="center")
    gear(c, dx+dw/2, dy+240, 102, 78, 12, fill=WHITE, stroke=BLACK, hole=27, lw=4)
    for a in range(0,360,45):
        rad=math.radians(a)
        bolt(c, dx+dw/2+200*math.cos(rad), dy+dh/2+140*math.sin(rad), 10, CYAN, BLACK)
    person(c, 278, 370, 1.35, color=WHITE, stroke=BLACK, mechanical=True)
    text(c, 180, 330, "NEW SESSION / ZERO CONTEXT", size=13, color=CYAN, font="PlexMonoBold")
    arrow(c, 435, 575, dx-22, 575, color=CYAN, lw=6, head=22)
    # Structured knowledge lines beyond the gate.
    for i in range(5):
        y=dy+140+i*58
        _line(c, dx+dw+46, y, dx+dw+345, y, WHITE, 4)
        c.setFillColor(CYAN)
        c.rect(dx+dw+46, y-5, 18, 10, fill=1, stroke=0)
    paragraph(c, 1320, 744, "Identity · authority · constraints · responsibilities · escalation · conduct", width=440, size=19, leading=27, color=WHITE, font="PlexSans")
    text(c, 100, 223, "“The only thing you should ever tell a new agent to read first, is AGENTS.md.”", size=23, color=WHITE, font="PlexSansBold")
    text(c, 100, 182, "It turns a general-purpose agent into a project-specific engineer.", size=18, color=CYAN, font="PlexSans")


def draw_10(c):
    """Seven-step ignition sequence for a zero-context agent."""
    frame(c, 10, ACT_III, dark=False, kicker="BOOT SEQUENCE / REPOSITORY FIRST")
    _heading(c, "HOW ANY AGENT BOOTS WITH ZERO CONTEXT", dark=False, size=47)
    # Master switch / turbine casing.
    bx, by, bw, bh = 100, 266, 335, 570
    plate(c, bx, by, bw, bh, fill=BLACK, stroke=BLACK, accent=CYAN, accent_width=12)
    gear(c, bx+bw/2, by+310, 121, 93, 16, fill=WHITE, stroke=BLACK, hole=31, lw=4)
    text(c, bx+bw/2, by+472, "AGENTS.md", size=20, color=WHITE, font="PlexMonoBold", align="center")
    text(c, bx+bw/2, by+107, "IGNITION / MASTER SWITCH", size=12, color=CYAN, font="PlexMonoBold", align="center")
    # Seven rungs, a conduit drops from master switch into each step.
    steps = [
        ("01", ".forge/STATE.md", "Where are we?"),
        ("02", "Last 3 .forge/LEDGER.md entries", "What just happened?"),
        ("03", ".forge/CONVENTIONS.md + GLOSSARY.md", "How do we think and speak?"),
        ("04", "specs/INDEX.md + IMPLEMENTING specs", "What is the contract?"),
        ("05", "tasks/DOING/ → tasks/OPEN/", "Resume work, then select next."),
        ("06", "make bootstrap && make test", "Verify a green baseline; report red before build."),
        ("07", "Print a 5-LINE SESSION PLAN", "Commit to intent before work."),
    ]
    x, w, h, top = 505, 1295, 70, 795
    for i, (num, main, note) in enumerate(steps):
        y=top-i*82
        # conduit branch
        c.setStrokeColor(CYAN if i in (0,5,6) else BLACK)
        c.setLineWidth(3)
        c.line(bx+bw, by+110+i*44, x-24, by+110+i*44)
        c.line(x-24, by+110+i*44, x-24, y+h/2)
        arrow(c, x-24, y+h/2, x, y+h/2, color=CYAN if i in (0,5,6) else BLACK, lw=3, head=12)
        plate(c, x, y, w, h, fill=BLACK, stroke=BLACK, accent=CYAN if i in (0,5,6) else None, accent_width=8, rivets=False)
        text(c, x+28, y+25, num, size=23, color=CYAN, font="ArchivoBlack")
        text(c, x+115, y+39, main, size=18 if len(main)<33 else 15, color=WHITE, font="PlexMonoBold")
        text(c, x+115, y+13, note, size=14, color=WHITE, font="PlexSans")
    text(c, 102, 152, "START WITH REPO STATE, NOT CHAT MEMORY.", size=16, color=BLACK, font="PlexMonoBold")


def draw_11(c):
    """Specification as an engineering RFC rather than a wish."""
    frame(c, 11, ACT_II, dark=True, kicker="SPECIFICATION / AN ENGINEERING CONTRACT")
    _heading(c, "SPECS ARE ENGINEERING RFCs, NOT PROMPTS", dark=True, size=46)
    # Philosophy left, dossier right.
    paragraph(c, 104, 795, "If two competent agents can implement the same specification in materially different ways, the specification is underspecified.", width=610, size=28, leading=39, color=WHITE, font="PlexSansBold")
    text(c, 104, 455, "A SPEC MUST CLOSE THE CHOICE SPACE.", size=18, color=CYAN, font="PlexMonoBold")
    _line(c, 104, 430, 644, 430, WHITE, 3)
    text(c, 104, 380, "The goal is not more prose. It is less room for unrecorded interpretation.", size=20, color=WHITE, font="PlexSans")

    # Open dossier sheet, carefully aligned as a technical artifact.
    px, py, pw, ph = 820, 220, 930, 628
    plate(c, px, py, pw, ph, fill=WHITE, stroke=WHITE, lw=3, accent=CYAN, accent_width=13)
    text(c, px+44, py+ph-56, "SPEC / ENGINEERING RFC", size=17, color=BLACK, font="PlexMonoBold")
    text(c, px+44, py+ph-101, "BEHAVIORAL CONTRACT", size=28, color=BLACK, font="ArchivoBlack")
    sections = [
        "01  SUMMARY", "02  MOTIVATION", "03  SCOPE", "04  BEHAVIORAL CONTRACT",
        "05  RULES", "06  DATA MODEL", "07  ACCEPTANCE CRITERIA",
        "08  NFRs / SECURITY", "09  OPEN QUESTIONS", "10  VERIFICATION PLAN / TRACEABILITY",
    ]
    for i, s in enumerate(sections):
        yy = py+ph-153-i*44
        c.setStrokeColor(BLACK)
        c.setLineWidth(1.6)
        c.line(px+44, yy-13, px+pw-48, yy-13)
        text(c, px+48, yy, s, size=15 if len(s)<28 else 13, color=CYAN if i in (3,6) else BLACK, font="PlexMonoBold")
        # Clause markers and margin ticks.
        c.setFillColor(BLACK)
        c.rect(px+pw-88, yy-5, 34, 7, fill=1, stroke=0)
        c.setFillColor(CYAN if i in (3,6) else BLACK)
        c.circle(px+22, yy+5, 4, fill=1, stroke=0)
    text(c, px+44, py+35, "COMPLETE · VERSIONED · MACHINE-LEGIBLE", size=13, color=BLACK, font="PlexMonoBold")


def draw_12(c):
    """Acceptance criteria transferred from specification to executable test."""
    frame(c, 12, ACT_II, dark=False, kicker="ACCEPTANCE CRITERIA / SPEC MEETS TEST")
    _heading(c, "ACCEPTANCE CRITERIA BRIDGE SPEC & TESTS", dark=False, size=49)
    text(c, 102, 858, "Every Acceptance Criterion becomes an executable test.", size=23, color=CYAN, font="PlexSansBold")
    # Two platforms separated by an intentional gulf.
    left_x, right_x = 105, 1270
    base_y = 300
    plate(c, left_x, base_y, 460, 424, fill=BLACK, stroke=BLACK, accent=CYAN, accent_width=10)
    plate(c, right_x, base_y, 545, 424, fill=BLACK, stroke=BLACK, accent=CYAN, accent_width=10)
    text(c, left_x+40, base_y+370, "THE SPECIFICATION", size=22, color=WHITE, font="ArchivoBlack")
    text(c, left_x+40, base_y+324, "GIVEN / WHEN / THEN", size=16, color=CYAN, font="PlexMonoBold")
    acs = ["AC-1", "AC-2", "AC-3"]
    for i, ac in enumerate(acs):
        y=base_y+250-i*80
        plate(c, left_x+42, y, 350, 51, fill=WHITE, stroke=WHITE, lw=2, rivets=False)
        text(c, left_x+217, y+17, ac, size=20, color=BLACK, font="PlexMonoBold", align="center")
    text(c, right_x+40, base_y+370, "THE TEST SUITE", size=22, color=WHITE, font="ArchivoBlack")
    tests=["test_ac_1_*", "test_ac_2_*", "test_ac_3_*"]
    for i, t in enumerate(tests):
        y=base_y+250-i*80
        plate(c, right_x+38, y, 460, 51, fill=BLACK, stroke=WHITE, lw=2, rivets=False)
        text(c, right_x+268, y+17, t, size=17, color=WHITE, font="PlexMonoBold", align="center")
    # Gantry crane spanning the gap, with suspended transfer hook and AC die.
    beam(c, 624, 801, 1578, 801, color=BLACK, width=18)
    beam(c, 706, 801, 706, 726, color=CYAN, width=9)
    beam(c, 1532, 801, 1532, 726, color=BLACK, width=9)
    c.setStrokeColor(BLACK)
    c.setLineWidth(5)
    c.rect(1040, 759, 225, 70, fill=0, stroke=1)
    text(c, 1152, 784, "AC → TEST", size=16, color=CYAN, font="PlexMonoBold", align="center")
    beam(c, 1152, 758, 1152, 645, color=BLACK, width=8)
    gate(c, 1152, 617, width=67, height=56, label="AC", dark=False)
    arrow(c, 1045, 585, 1166, 585, color=CYAN, lw=5, head=18)
    # copy below platforms
    text(c, 105, 218, "BEHAVIOR IS WRITTEN AS", size=14, color=BLACK, font="PlexMonoBold")
    text(c, 105, 179, "GIVEN  ·  WHEN  ·  THEN", size=24, color=BLACK, font="ArchivoBlack")
    text(c, 725, 179, "TRANSLATION, NOT DUPLICATION.", size=18, color=CYAN, font="PlexMonoBold")


def draw_13(c):
    """Plans, tasks, and atomic work."""
    frame(c, 13, ACT_III, dark=True, kicker="DECOMPOSITION / ATOMIC WORK ORDERS")
    _heading(c, "SPEC → PLAN → TASKS. WORK MUST BECOME ATOMIC.", dark=True, size=43)
    # Three levels of a decomposed steel assembly.
    sx, sy = 650, 730
    plate(c, sx, sy, 620, 132, fill=BLACK, stroke=WHITE, lw=4, accent=CYAN, accent_width=12)
    text(c, 960, sy+80, "SPEC-XXX", size=29, color=WHITE, font="PlexMonoBold", align="center")
    text(c, 960, sy+37, "WHAT & WHY / CONTRACT", size=15, color=CYAN, font="PlexMonoBold", align="center")
    arrow(c, 960, sy, 960, 618, color=WHITE, lw=5, head=18)
    # second stage: ordered plan plate
    plate(c, 475, 475, 970, 130, fill=BLACK, stroke=WHITE, lw=4, accent=CYAN, accent_width=12)
    text(c, 960, 551, "PLAN-XXX", size=26, color=WHITE, font="PlexMonoBold", align="center")
    text(c, 960, 508, "HOW / ORDERED · SIZED · SEQUENCED", size=15, color=CYAN, font="PlexMonoBold", align="center")
    # Parting lines to atomic work units.
    arrow(c, 960, 475, 960, 413, color=CYAN, lw=5, head=17)
    for i, x in enumerate((250, 690, 1130, 1570)):
        arrow(c, 960, 411, x, 352, color=WHITE, lw=3, head=14)
        plate(c, x-178, 228, 356, 106, fill=BLACK, stroke=WHITE, lw=3, accent=CYAN if i == 0 else None, accent_width=8, rivets=True)
        text(c, x, 286, f"TASK {i+1:02d}", size=18, color=CYAN if i == 0 else WHITE, font="PlexMonoBold", align="center")
        text(c, x, 254, "ONE MERGEABLE UNIT", size=12, color=WHITE, font="PlexMonoBold", align="center")
    # Mechanical breakup of a source assembly behind the tree.
    beam(c, 782, 686, 858, 631, color=WHITE, width=10)
    beam(c, 1136, 686, 1062, 631, color=WHITE, width=10)
    text(c, 100, 177, "ONE AGENT SESSION ≈ 1–3 TASKS.", size=19, color=CYAN, font="PlexMonoBold")
    text(c, 770, 177, "IF A TASK IS LARGE, IT MUST BE SPLIT.", size=19, color=WHITE, font="PlexMonoBold")


def draw_14(c):
    """Session protocol flywheel."""
    frame(c, 14, ACT_III, dark=True, kicker="SESSION ENGINE / THE REPEATING TURN OF THE CRANK")
    _heading(c, "THE KONKAUTO SESSION PROTOCOL", dark=True, size=43)
    # Flywheel housing and axle.
    cx, cy, r = 960, 500, 230
    c.setStrokeColor(WHITE)
    c.setLineWidth(9)
    c.circle(cx, cy, r+28, fill=0, stroke=1)
    c.setStrokeColor(CYAN)
    c.setLineWidth(4)
    c.circle(cx, cy, r, fill=0, stroke=1)
    gear(c, cx, cy, r-22, r-42, 28, fill=WHITE, stroke=BLACK, hole=104, lw=4)
    c.setFillColor(BLACK)
    c.setStrokeColor(CYAN)
    c.setLineWidth(5)
    c.circle(cx, cy, 98, fill=1, stroke=1)
    text(c, cx, cy+16, "STATELESS", size=17, color=WHITE, font="PlexMonoBold", align="center")
    text(c, cx, cy-17, "SESSION", size=19, color=CYAN, font="ArchivoBlack", align="center")
    stages=["BOOTSTRAP", "PLAN", "BUILD\n(TEST-FIRST)", "VERIFY", "DOCUMENT", "HANDOFF", "PUSH"]
    for i, label in enumerate(stages):
        a=math.radians(90-i*360/7)
        node_radius = r + 97
        nx=cx+node_radius*math.cos(a)
        ny=cy+node_radius*math.sin(a)
        _line(c, cx+(r-12)*math.cos(a), cy+(r-12)*math.sin(a), nx-46*math.cos(a), ny-30*math.sin(a), WHITE, 3)
        c.setFillColor(CYAN if label.startswith("HANDOFF") else BLACK)
        c.setStrokeColor(CYAN if label.startswith("HANDOFF") else WHITE)
        c.setLineWidth(3)
        c.circle(nx, ny, 52, fill=1, stroke=1)
        if "\n" in label:
            line1,line2=label.split("\n")
            text(c, nx, ny+6, line1, size=12, color=BLACK if label.startswith("HANDOFF") else WHITE, font="PlexMonoBold", align="center")
            text(c, nx, ny-15, line2, size=11, color=BLACK if label.startswith("HANDOFF") else WHITE, font="PlexMonoBold", align="center")
        else:
            size=12 if len(label)>8 else 14
            text(c, nx, ny-5, label, size=size, color=BLACK if label.startswith("HANDOFF") else WHITE, font="PlexMonoBold", align="center")
        # Rotational sequence arrows along a ring.
        a2=math.radians(90-(i+0.45)*360/7)
        arrow(c, cx+(r+44)*math.cos(a), cy+(r+44)*math.sin(a), cx+(r+44)*math.cos(a2), cy+(r+44)*math.sin(a2), color=CYAN if i in (4,5) else WHITE, lw=3, head=12)
    # Handoff commit is mechanically upstream of push.
    plate(c, 100, 225, 460, 96, fill=BLACK, stroke=WHITE, accent=CYAN, rivets=False)
    text(c, 126, 278, "HANDOFF", size=15, color=CYAN, font="PlexMonoBold")
    text(c, 126, 246, "FINAL COMMIT BEFORE PUSH", size=13, color=WHITE, font="PlexMonoBold")
    text(c, 1390, 235, "“Agents are disposable. The repository must outlive every session.”", size=17, color=WHITE, font="PlexSansBold")


def draw_15(c):
    """STATE.md live snapshot versus append-only LEDGER.md history."""
    frame(c, 15, ACT_III, dark=False, kicker="WRITTEN HANDOFF / REPOSITORY MEMORY")
    _heading(c, "CONTINUITY COMES FROM THE REPO, NOT THE CHAT", dark=False, size=45)
    panels=[(100,"STATE.md","A LIVE SNAPSHOT", "Overwritten every session", CYAN),
            (990,"LEDGER.md","AN APPEND-ONLY HISTORY", "Never edited or rewritten", BLACK)]
    for x, file, title, sub, accent in panels:
        plate(c, x, 295, 810, 508, fill=BLACK, stroke=BLACK, lw=3, accent=accent, accent_width=12)
        text(c, x+42, 744, file, size=29, color=WHITE, font="PlexMonoBold")
        text(c, x+42, 699, title, size=16, color=accent, font="PlexMonoBold")
        text(c, x+42, 660, sub, size=17, color=WHITE, font="PlexSans")
    # State control-room instrument panel.
    live=["DONE", "IN-PROGRESS", "BLOCKED", "NEXT UP", "GREEN BASELINE"]
    for i, lab in enumerate(live):
        y=590-i*62
        c.setStrokeColor(WHITE)
        c.setLineWidth(2)
        c.rect(145, y-18, 680, 42, fill=0, stroke=1)
        c.setFillColor(CYAN if i in (0,4) else WHITE)
        c.circle(171, y+3, 8, fill=1, stroke=0)
        text(c, 200, y-3, lab, size=14, color=WHITE, font="PlexMonoBold")
        _line(c, 460, y+3, 790, y+3, WHITE, 2)
    # Ledger chronicle plate stack.
    for i in range(5):
        y=554-i*58
        c.setStrokeColor(WHITE)
        c.setLineWidth(2)
        c.rect(1038, y, 712, 42, fill=0, stroke=1)
        text(c, 1060, y+14, f"SESSION {i+1:02d}", size=11, color=CYAN if i==0 else WHITE, font="PlexMonoBold")
        _line(c, 1184, y+21, 1719, y+21, WHITE, 2)
        for j in range(3):
            _line(c, 1184, y+12-j*7, 1480+j*42, y+12-j*7, WHITE, 1)
    # Center chain link binds current state to the history.
    arrow(c, 860, 530, 1025, 530, color=CYAN, lw=8, head=20, double=True)
    text(c, 100, 223, "Handoffs are written, not remembered.", size=28, color=BLACK, font="ArchivoBlack")
    text(c, 100, 180, "STATE.md summarizes the present. LEDGER.md preserves the sequence of sessions.", size=17, color=BLACK, font="PlexSans")


def draw_16(c):
    """Bidirectional traceability and evidence-based definition of done."""
    frame(c, 16, ACT_IV, dark=True, kicker="TRACEABILITY / VERIFICATION / DEFINITION OF DONE")
    _heading(c, "BIDIRECTIONAL TRACEABILITY. EXECUTED VERIFICATION.", dark=True, size=43)
    chain=["SPEC", "PLAN", "TASK", "BRANCH", "COMMIT", "TEST", "PR", "VERIFIED"]
    x0=100; bw=188; gap=30; y=720
    centers=[]
    for i, label in enumerate(chain):
        x=x0+i*(bw+gap)
        centers.append(x+bw/2)
        c.setFillColor(CYAN if label=="VERIFIED" else BLACK)
        c.setStrokeColor(CYAN if label=="VERIFIED" else WHITE)
        c.setLineWidth(3)
        c.rect(x,y,bw,90,fill=1,stroke=1)
        text(c,x+bw/2,y+35,label,size=15,color=BLACK if label=="VERIFIED" else WHITE,font="PlexMonoBold",align="center")
        if i<7:
            arrow(c,x+bw,y+45,x+bw+gap,y+45,color=WHITE,lw=3,head=12,double=True)
    # Trace.md switchboard matrix linking both directions.
    plate(c, 600, 376, 720, 240, fill=BLACK, stroke=WHITE, lw=4, accent=CYAN, accent_width=12)
    text(c, 960, 559, "TRACE.md", size=30, color=CYAN, font="PlexMonoBold", align="center")
    # wire matrix
    for i in range(4):
        _line(c, 680, 514-i*32, 1240, 514-i*32, WHITE, 2)
    for j in range(7):
        x=710+j*82
        _line(c,x,426,x,526,CYAN if j in (0,6) else WHITE,2)
        c.setFillColor(CYAN if j in (0,6) else WHITE)
        c.circle(x, 514, 7, fill=1, stroke=0)
    text(c, 960, 401, "AUDIT MAP / WALK ANY LINK BACK TO ITS SOURCE", size=12, color=WHITE, font="PlexMonoBold", align="center")
    # short links down from both ends to the matrix
    arrow(c, centers[0], y, 710, 616, color=CYAN, lw=3, head=13)
    arrow(c, centers[-1], y, 1202, 616, color=CYAN, lw=3, head=13)
    # Three proof rules
    rules=[("01", "Traceability is bidirectional. Any link can be walked both ways."),
           ("02", "“Done” is not asserted. “Done” is proven."),
           ("03", "A verification command ran, exited 0, and its output is recorded.")]
    for i,(num,desc) in enumerate(rules):
        y0=294-i*60
        text(c, 102, y0, num, size=16, color=CYAN, font="PlexMonoBold")
        text(c, 154, y0, desc, size=18, color=WHITE, font="PlexSans")


def draw_17(c):
    """Git, branching, PRs, and forge-lint as a physical governance system."""
    frame(c, 17, ACT_IV, dark=False, kicker="GIT / BRANCH PROTECTION / CONTINUOUS INTEGRATION")
    _heading(c, "GOVERNANCE ENFORCED BY GIT, PROCESS & CI", dark=False, size=47)
    # Railway tracks
    rail_x1, rail_x2 = 110, 1800
    tracks=[("feat/<TASK-ID>-<slug>",730,CYAN), ("spec/<SPEC-ID>",545,BLACK), ("main / PROTECTED",360,BLACK)]
    for label,y,col in tracks:
        text(c, 112, y+51, label, size=16, color=CYAN if col==CYAN else BLACK, font="PlexMonoBold")
        beam(c, rail_x1, y, rail_x2, y, color=BLACK, width=8)
        beam(c, rail_x1, y-25, rail_x2, y-25, color=BLACK, width=8)
        for i in range(18):
            x=rail_x1+40+i*94
            beam(c,x,y-33,x,y+7,color=BLACK,width=3)
    # Feature rail passes through PR inspection gate, then a human-only merge turnout.
    gx, gy = 1170, 638
    plate(c, gx, gy, 350, 182, fill=BLACK, stroke=BLACK, accent=CYAN, accent_width=10)
    text(c, gx+175, gy+139, "PR INSPECTION", size=17, color=WHITE, font="ArchivoBlack", align="center")
    text(c, gx+175, gy+99, "TEST / LINT / TYPE / SECRET", size=12, color=CYAN, font="PlexMonoBold", align="center")
    text(c, gx+175, gy+61, "forge-lint", size=22, color=WHITE, font="PlexMonoBold", align="center")
    # Gate blocks any non-conforming branch from main.
    gate(c, 1600, 383, width=92, height=78, label="H", dark=False)
    arrow(c, 1540, 725, 1640, 396, color=CYAN, lw=6, head=20)
    # Protected main rail barrier.
    c.setStrokeColor(CYAN)
    c.setLineWidth(8)
    c.line(1585, 340, 1585, 430)
    c.line(1620, 340, 1620, 430)
    # spec branch ends at docs-only review junction.
    arrow(c, 1065, 540, 1200, 540, color=BLACK, lw=4, head=14)
    text(c, 100, 251, "main", size=15, color=BLACK, font="PlexMonoBold")
    text(c, 220, 251, "Protected. Humans merge only. Always deployable.", size=17, color=BLACK, font="PlexSans")
    text(c, 100, 213, "FEATURE", size=14, color=CYAN, font="PlexMonoBold")
    text(c, 220, 213, "One task. One branch. One PR.", size=17, color=BLACK, font="PlexSans")
    text(c, 100, 175, "SPEC", size=14, color=CYAN, font="PlexMonoBold")
    text(c, 220, 175, "Docs-only specification reviews.", size=17, color=BLACK, font="PlexSans")
    plate(c, 1000, 142, 800, 116, fill=BLACK, stroke=BLACK, accent=CYAN, accent_width=10, rivets=False)
    text(c, 1030, 221, "LINEAR HISTORY · NO FORCE PUSHES", size=14, color=CYAN, font="PlexMonoBold")
    text(c, 1030, 188, "<type>(<scope>): <summary> [TASK-ID] [SPEC-ID]", size=14, color=WHITE, font="PlexMonoBold")
    text(c, 1030, 159, "forge-lint blocks non-conforming work before main.", size=14, color=WHITE, font="PlexSans")


def draw_18(c):
    """Least-privilege deploy key protocol and monthly rotation."""
    frame(c, 18, ACT_IV, dark=True, kicker="PERSISTENT ACCESS / LEAST PRIVILEGE")
    _heading(c, "PERSISTENT WRITE ACCESS WITH DISCIPLINED SECURITY", dark=True, size=41)
    text(c, 100, 850, "The deploy key removes friction. The handoff discipline removes risk.", size=20, color=CYAN, font="PlexSansBold")
    # Private-key vault stays outside the repository boundary.
    vx, vy, vw, vh = 110, 420, 510, 365
    plate(c, vx, vy, vw, vh, fill=BLACK, stroke=WHITE, lw=4, accent=CYAN, accent_width=12)
    text(c, vx+255, vy+vh-58, "PRIVATE KEY VAULT", size=22, color=WHITE, font="ArchivoBlack", align="center")
    # key form (abstract, never displays key material)
    c.setStrokeColor(CYAN)
    c.setLineWidth(20)
    c.circle(vx+150, vy+190, 54, fill=0, stroke=1)
    beam(c,vx+204,vy+190,vx+395,vy+190,color=CYAN,width=16)
    beam(c,vx+330,vy+190,vx+330,vy+150,color=CYAN,width=13)
    beam(c,vx+384,vy+190,vx+384,vy+158,color=CYAN,width=13)
    text(c, vx+255, vy+74, "ED25519 / OUTSIDE REPO / NEVER COMMIT", size=12, color=WHITE, font="PlexMonoBold", align="center")
    # Repo boundary and public conduit.
    bx, by, bw, bh = 900, 357, 900, 465
    c.setStrokeColor(WHITE)
    c.setLineWidth(4)
    c.setDash(14,8)
    c.rect(bx,by,bw,bh,fill=0,stroke=1)
    c.setDash()
    text(c,bx+26,by+bh-35,"REPOSITORY BOUNDARY / PUBLIC KEY ONLY INSIDE",size=14,color=WHITE,font="PlexMonoBold")
    beam(c,vx+vw,vy+210,bx+126,vy+210,color=WHITE,width=17)
    beam(c,vx+vw,vy+210,bx+126,vy+210,color=CYAN,width=5)
    arrow(c,bx+95,vy+210,bx+192,vy+210,color=CYAN,lw=5,head=19)
    text(c, 708, vy+242, "PUBLIC KEY", size=13, color=CYAN, font="PlexMonoBold", align="center")
    # One-repo dock / write permission.
    plate(c,bx+200,by+123,610,238,fill=BLACK,stroke=WHITE,lw=3,accent=CYAN,accent_width=9)
    text(c,bx+505,by+313,"ONE REPOSITORY / ONE AGENT",size=15,color=CYAN,font="PlexMonoBold",align="center")
    text(c,bx+505,by+246,"WRITE DEPLOY KEY",size=23,color=WHITE,font="ArchivoBlack",align="center")
    text(c,bx+505,by+211,"Git push only",size=16,color=WHITE,font="PlexMonoBold",align="center")
    # 30-day gear dial.
    gear(c, 278, 294, 76, 61, 16, fill=WHITE, stroke=BLACK, hole=21, lw=3)
    text(c,278,286,"30",size=23,color=BLACK,font="ArchivoBlack",align="center")
    text(c,278,265,"DAYS",size=11,color=BLACK,font="PlexMonoBold",align="center")
    text(c,382,315,"ROTATE EVERY 30 DAYS",size=14,color=CYAN,font="PlexMonoBold")
    text(c,382,282,"One key per agent and workspace.",size=16,color=WHITE,font="PlexSans")
    text(c,382,250,"Inventory metadata only in ops/KEYS.md.",size=15,color=WHITE,font="PlexSans")
    # Safety chain in lower band.
    claims=["SINGLE REPOSITORY", "PRIVATE KEY NEVER IN GIT", "PROTECTED main", "FORCE-PUSH DISABLED"]
    for i, claim in enumerate(claims):
        x=100+i*427
        plate(c,x,143,385,62,fill=BLACK,stroke=WHITE,lw=2,accent=CYAN if i==0 else None,accent_width=7,rivets=False)
        text(c,x+192,166,claim,size=12,color=WHITE,font="PlexMonoBold",align="center")
    text(c, 1000, 304, "PR API ACCESS IS SEPARATE AUTHORIZATION OR A HUMAN.", size=12, color=CYAN, font="PlexMonoBold")


def draw_19(c):
    """Maturity close — from assistance to governed engineering."""
    frame(c, 19, ACT_V, dark=True, kicker="MATURITY / ENGINEERED INTELLIGENCE")
    _heading(c, "FROM AI ASSISTANCE TO AI GOVERNED ENGINEERING", dark=True, size=43)
    tiers=[
        ("TIER 1","AD-HOC","prompts as memory"),
        ("TIER 2","STRUCTURED","AGENTS.md + handoffs"),
        ("TIER 3","TRACEABLE","IDs + AC tests + forge-lint"),
        ("TIER 4","GOVERNED","human gates + ADRs + key rotation"),
        ("TIER 5","SELF-IMPROVING","metrics + retrospectives"),
    ]
    x0=98; w=326; h=202; gap=18; base=406; rise=82
    # Monumental ascending structure, concrete blocks become precise steel stages.
    for i,(tier,name,cap) in enumerate(tiers):
        x=x0+i*(w+gap); y=base+i*rise
        _pillar(c,x,y,w,h,dark=True,accent=(i>=2))
        text(c,x+22,y+h-42,tier,size=13,color=CYAN,font="PlexMonoBold")
        text(c,x+22,y+h-92,name,size=17 if len(name)<12 else 14,color=WHITE,font="ArchivoBlack")
        paragraph(c,x+22,y+h-128,cap,width=w-44,size=15,leading=20,color=WHITE,font="PlexSans")
        if i<4:
            arrow(c,x+w,y+h-14,x+w+gap+8,y+h+rise-8,color=CYAN,lw=4,head=13)
    # Philosophy quote plate.
    plate(c,98,265,1724,107,fill=BLACK,stroke=WHITE,lw=2,accent=CYAN,accent_width=10,rivets=False)
    text(c,128,326,"“Code is a derivative of specification. The repository is the brain. The agent is the hands. Markdown is the contract.”",size=17,color=WHITE,font="PlexSansBold")
    text(c,98,204,"KONKAUTO IS NOT A PROMPTING FRAMEWORK.",size=18,color=CYAN,font="PlexMonoBold")
    text(c,98,150,"IT IS AN OPERATING SYSTEM FOR SPECIFICATION-DRIVEN AGENTIC DEVELOPMENT.",size=29,color=WHITE,font="ArchivoBlack")
