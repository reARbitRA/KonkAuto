from theme import (
    W, H, MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM,
    COAL, BONE, ORANGE, YELLOW, STEEL, GREEN,
    COAL_LIGHT, COAL_MID, STEEL_DARK, STEEL_LIGHT, BONE_DARK, BONE_MID,
    col_x, col_span_w, draw_slide_frame, draw_halftone_rect, draw_hatch_rect,
    draw_hazard_band, draw_brutalist_plate, draw_arrow, draw_gear, draw_padlock,
    draw_badge, draw_wrapped
)

ACT_V = "ACT V — ADOPTION"


def draw_slide_19(c):
    """19 — The maturity ladder (Coal, five-step staircase from raw concrete to measured governance)."""
    draw_slide_frame(c, 19, ACT_V, bg_mode="coal", kicker="ADOPTION PATH // MEASURED PROCESS MATURITY")

    lx = col_x(0)
    full_w = col_span_w(12)
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 59)
    c.drawString(lx, 915, "FIVE TIERS OF RELIABILITY.")

    # Continuous concrete-to-steel stair stringer behind the level plates
    steps = [
        ("1", "AD-HOC", "prompts as memory", "STARTING STATE", STEEL_DARK, BONE),
        ("2", "STRUCTURED", "AGENTS.md + handoffs", "REPO BOOTSTRAPS", STEEL, COAL),
        ("3", "TRACEABLE", "IDs, AC tests, forge-lint", "LINKS ARE ENFORCED", ORANGE, COAL),
        ("4", "GOVERNED", "human gates, ADRs, key rotation", "POWERS ARE SCOPED", YELLOW, COAL),
        ("5", "SELF-IMPROVING", "metrics + retrospectives", "EVIDENCE FEEDS CHANGE", BONE, COAL),
    ]
    step_w = 300
    step_h = 170
    gap = 35
    base_y = 148
    rise = 119
    first_x = lx + 8

    # Staircase foundation / diagonal progression rail
    c.setStrokeColor(ORANGE)
    c.setLineWidth(5)
    for i in range(4):
        x1 = first_x + i * (step_w + gap) + step_w - 8
        y1 = base_y + i * rise + step_h - 3
        x2 = first_x + (i + 1) * (step_w + gap) + 20
        y2 = base_y + (i + 1) * rise + 16
        c.line(x1, y1, x2, y2)
        draw_arrow(c, x1, y1, x2, y2, color=ORANGE, lw=4, head_len=14, head_w=8)

    for i, (num, title, capability, marker, accent, fg) in enumerate(steps):
        x = first_x + i * (step_w + gap)
        y = base_y + i * rise
        # concrete riser + steel deck blocks form a stepped ascent
        c.setFillColor(STEEL_DARK if i < 2 else COAL_MID)
        c.setStrokeColor(COAL)
        c.setLineWidth(3)
        c.rect(x - 10, y - 10, step_w + 20, 26, fill=1, stroke=1)
        draw_brutalist_plate(c, x, y, step_w, step_h, fill_col=COAL_LIGHT, stroke_col=accent, lw=3.5, shadow_offset=6, shadow_col=COAL)
        # Tier plate cap
        c.setFillColor(accent)
        c.rect(x, y + step_h - 48, step_w, 48, fill=1, stroke=0)
        c.setFillColor(fg)
        c.setFont("PlexMonoBold", 15)
        c.drawString(x + 16, y + step_h - 31, f"TIER {num}")
        c.setFont("ArchivoBlack", 18 if len(title) <= 11 else 15.5)
        c.drawRightString(x + step_w - 16, y + step_h - 32, title)
        # Capability in dominant body type
        c.setFillColor(BONE)
        c.setFont("ArchivoBlack", 19 if len(capability) < 27 else 16.5)
        if i == 3:
            lines = ["human gates, ADRs,", "key rotation"]
        else:
            lines = capability.split(" + ") if " + " in capability else [capability]
        if len(lines) == 1:
            c.drawString(x + 18, y + 76, lines[0])
        else:
            first_line = lines[0] if i == 3 else lines[0] + " +"
            c.drawString(x + 18, y + 83, first_line)
            c.drawString(x + 18, y + 55, lines[1])
        c.setFillColor(accent)
        c.setFont("PlexMonoBold", 11.5)
        c.drawString(x + 18, y + 25, marker)
        # Measurement/retrospective instrument on Tier 5: analytical, not utopian
        if i == 4:
            c.setStrokeColor(STEEL_LIGHT)
            c.setLineWidth(2)
            c.line(x + 225, y + 30, x + 225, y + 74)
            for j, bar_h in enumerate([15, 24, 34, 44]):
                c.setFillColor(STEEL if j < 3 else YELLOW)
                c.rect(x + 236 + j * 12, y + 30, 7, bar_h, fill=1, stroke=0)

    # Evidence-driven metrics panel (not fabricated measurements)
    metric_y = 829
    draw_brutalist_plate(c, lx, metric_y, full_w, 54, fill_col=BONE, stroke_col=COAL, lw=3, shadow_offset=5, shadow_col=COAL_MID)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 16)
    c.drawString(lx + 22, metric_y + 20, "MEASURE:")
    c.setFont("PlexSansBold", 21)
    c.drawString(lx + 170, metric_y + 19, "spec-to-merge time   ·   rework   ·   blocked-task rate")
    c.setFillColor(ORANGE)
    c.rect(lx + full_w - 13, metric_y, 13, 54, fill=1, stroke=0)


def draw_slide_20(c):
    """20 — The operating command (Bone, complete vault + one-line restart, monumental closure)."""
    draw_slide_frame(c, 20, ACT_V, bg_mode="bone", kicker="OPERATING COMMAND // THE SYSTEM CONTINUES")

    lx = col_x(0)
    full_w = col_span_w(12)
    left_w = col_span_w(7)
    rx = col_x(7)
    rw = col_span_w(5)

    # Two-line closing claim
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 62)
    c.drawString(lx, 915, "START WITH ONE FILE.")
    c.drawString(lx, 846, "CONTINUE WITH ONE LINE.")
    c.setFillColor(ORANGE)
    c.rect(lx, 823, 310, 8, fill=1, stroke=0)

    # First-session command plate
    first_y = 632
    first_h = 145
    draw_brutalist_plate(c, lx, first_y, left_w, first_h, fill_col=COAL, stroke_col=COAL, lw=3.5, shadow_offset=7, shadow_col=STEEL_DARK)
    c.setFillColor(YELLOW)
    c.rect(lx, first_y + first_h - 37, left_w, 37, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 14)
    c.drawString(lx + 20, first_y + first_h - 24, "FIRST SESSION // SCAFFOLD THE METHOD, NOT PRODUCT CODE")
    c.setFillColor(BONE)
    c.setFont("PlexSansBold", 19)
    first_line = "Scaffold AGENTS.md, .forge/, templates, and forge-lint. No product code."
    draw_wrapped(c, lx + 22, first_y + 67, first_line, "PlexSansBold", 19, 27, left_w - 44, color=BONE)

    # Recurring one-line prompt plate
    second_y = 417
    second_h = 175
    draw_brutalist_plate(c, lx, second_y, left_w, second_h, fill_col=COAL_LIGHT, stroke_col=ORANGE, lw=3.5, shadow_offset=7, shadow_col=COAL)
    c.setFillColor(ORANGE)
    c.rect(lx, second_y + second_h - 39, left_w, 39, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 14)
    c.drawString(lx + 20, second_y + second_h - 26, "THEN // RECURRING ONE-LINE COMMAND")
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 15)
    recurring = "“Read AGENTS.md and execute the session protocol. Priority: T-032, then T-033. Role: BUILDER.”"
    draw_wrapped(c, lx + 22, second_y + 94, recurring, "PlexMonoBold", 15, 24, left_w - 44, color=BONE)

    # Clear distinction: scaffold repo only, no product code
    draw_badge(c, lx + 4, 364, "FIRST SESSION = METHOD ONLY", bg_col=YELLOW, fg_col=COAL, border_col=COAL, size=12, pad_x=12, h=30)
    draw_badge(c, lx + 285, 364, "PRODUCT CODE REQUIRES APPROVED SPEC", bg_col=COAL, fg_col=BONE, border_col=ORANGE, size=12, pad_x=12, h=30)

    # -------------------------------------------------------------------------
    # Return to Repository Vault — now complete and quietly operating.
    # One worker exits; another reads the same AGENTS.md entry point.
    # -------------------------------------------------------------------------
    vy = 288
    vh = 560
    draw_brutalist_plate(c, rx, vy, rw, vh, fill_col=COAL, stroke_col=COAL, lw=4.5, shadow_offset=9, shadow_col=STEEL_DARK)
    draw_hazard_band(c, rx, vy + vh - 17, rw, 17, stripe_w=17, bg_col=YELLOW, fg_col=COAL, border_w=2)

    # Structural vault compartments (brain/repository complete)
    vault_in_x = rx + 32
    vault_in_y = vy + 112
    vault_in_w = rw - 64
    vault_in_h = 354
    c.setFillColor(COAL_LIGHT)
    c.setStrokeColor(BONE)
    c.setLineWidth(3)
    c.rect(vault_in_x, vault_in_y, vault_in_w, vault_in_h, fill=1, stroke=1)
    # steel beams divide persistent records
    for j in range(1, 4):
        x = vault_in_x + j * vault_in_w / 4
        c.setStrokeColor(STEEL)
        c.setLineWidth(2)
        c.line(x, vault_in_y + 16, x, vault_in_y + vault_in_h - 16)

    # Repository compartments with crisp filenames as text overlay
    comp = [
        ("STATE.md", "snapshot", YELLOW),
        ("LEDGER.md", "append-only", ORANGE),
        ("specs/", "approved contracts", BONE),
        ("TRACE.md", "audit links", STEEL),
    ]
    for j, (name, desc, accent) in enumerate(comp):
        cx = vault_in_x + (j + 0.5) * vault_in_w / 4
        # Geometry: stacks of steel document plates
        for k in range(3):
            px = cx - 53 + k * 7
            py = vault_in_y + 183 - k * 8
            c.setFillColor(COAL_MID)
            c.setStrokeColor(accent)
            c.setLineWidth(2)
            c.rect(px, py, 106, 93, fill=1, stroke=1)
            c.setStrokeColor(STEEL_DARK)
            c.setLineWidth(1.3)
            c.line(px + 12, py + 62, px + 91, py + 62)
            c.line(px + 12, py + 42, px + 76, py + 42)
        c.setFillColor(accent)
        c.setFont("PlexMonoBold", 13)
        c.drawCentredString(cx, vault_in_y + 74, name)
        c.setFillColor(STEEL_LIGHT)
        c.setFont("PlexMono", 10.5)
        c.drawCentredString(cx, vault_in_y + 49, desc)

    # Central lower-entry bay: a continuously illuminated AGENTS.md master door
    door_x = rx + rw / 2 - 146
    door_y = vy + 33
    door_w = 292
    door_h = 100
    draw_brutalist_plate(c, door_x, door_y, door_w, door_h, fill_col=YELLOW, stroke_col=COAL, lw=3.5, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 25)
    c.drawCentredString(door_x + door_w / 2, door_y + 56, "AGENTS.md")
    c.setFont("PlexMonoBold", 11.5)
    c.drawCentredString(door_x + door_w / 2, door_y + 28, "ONE ENTRY POINT · ALWAYS")

    # Worker silhouettes in simple graphic-novel industrial style (not robots)
    # Outgoing worker at left foot of vault
    wx1 = rx + 12
    wy = vy + 12
    c.setFillColor(STEEL)
    c.setStrokeColor(COAL)
    c.setLineWidth(2)
    c.circle(wx1 + 30, wy + 90, 18, fill=1, stroke=1)
    c.rect(wx1 + 11, wy + 25, 38, 55, fill=1, stroke=1)
    c.setStrokeColor(STEEL)
    c.setLineWidth(8)
    c.line(wx1 + 20, wy + 25, wx1 + 12, wy + 3)
    c.line(wx1 + 40, wy + 25, wx1 + 48, wy + 3)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 9)
    c.drawCentredString(wx1 + 31, wy - 2, "SESSION ENDS")

    # Incoming worker at right reading the same entry point
    wx2 = rx + rw - 61
    c.setFillColor(STEEL)
    c.setStrokeColor(COAL)
    c.setLineWidth(2)
    c.circle(wx2 + 30, wy + 90, 18, fill=1, stroke=1)
    c.rect(wx2 + 11, wy + 25, 38, 55, fill=1, stroke=1)
    c.setStrokeColor(STEEL)
    c.setLineWidth(8)
    c.line(wx2 + 20, wy + 25, wx2 + 12, wy + 3)
    c.line(wx2 + 40, wy + 25, wx2 + 48, wy + 3)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 9)
    c.drawCentredString(wx2 + 31, wy - 2, "SESSION STARTS")

    # The unbroken molten-orange seam runs from the persistent vault doorway and through the handoff
    seam = c.beginPath()
    seam.moveTo(vault_in_x + 12, vy + vh - 52)
    seam.lineTo(vault_in_x + 12, vy + vh - 73)
    seam.lineTo(vault_in_x + vault_in_w / 2, vy + vh - 73)
    seam.lineTo(vault_in_x + vault_in_w / 2, door_y + door_h)
    c.setStrokeColor(ORANGE)
    c.setLineWidth(8)
    c.drawPath(seam, fill=0, stroke=1)
    c.setStrokeColor(YELLOW)
    c.setLineWidth(2)
    c.drawPath(seam, fill=0, stroke=1)

    # Bottom monumental final statement across full width (not sentimental)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 48)
    c.drawCentredString(lx + col_span_w(12) / 2, 194, "SESSIONS END. THE SYSTEM DOES NOT.")
    # Unbroken-orange closing baseline / inherited seam motif
    c.setStrokeColor(ORANGE)
    c.setLineWidth(8)
    c.line(lx, 164, lx + full_w, 164)
    c.setFillColor(YELLOW)
    c.circle(lx, 164, 7, fill=1, stroke=0)
    c.circle(lx + full_w, 164, 7, fill=1, stroke=0)
