import math
from theme import (
    W, H, MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM,
    COAL, BONE, ORANGE, YELLOW, STEEL, GREEN,
    COAL_LIGHT, COAL_MID, STEEL_DARK, STEEL_LIGHT, BONE_DARK, BONE_MID,
    col_x, col_span_w, draw_slide_frame, draw_halftone_rect, draw_hatch_rect,
    draw_hazard_band, draw_brutalist_plate, draw_arrow, draw_gear, draw_padlock,
    draw_badge, draw_wrapped
)

ACT_I = "ACT I — THE DOCTRINE"


def draw_slide_01(c):
    """01 — The manifesto (Coal background)"""
    draw_slide_frame(c, 1, ACT_I, bg_mode="coal", kicker="KONKAUTO — SPECIFICATION-DRIVEN AGENTIC DEVELOPMENT")

    left_x = col_x(0)
    left_w = col_span_w(7)

    # Kicker badge: KONKAUTO / SDAD + 01 / 20
    draw_badge(c, left_x, 912, "KONKAUTO / SDAD", bg_col=ORANGE, fg_col=COAL, border_col=BONE, font="PlexMonoBold", size=15, pad_x=14, h=32)
    c.setFont("PlexMonoBold", 15)
    c.setFillColor(STEEL_LIGHT)
    c.drawString(left_x + 195, 922, "// SYSTEM DOCTRINE 01 / 20")

    # Three-line Manifesto in enormous Bone-White Archivo Black on Coal
    # Line 1: THE REPO IS THE BRAIN.
    y1 = 790
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 66)
    c.drawString(left_x, y1, "THE REPO")
    c.drawString(left_x, y1 - 70, "IS THE BRAIN.")
    # Steel structural bracket next to BRAIN
    c.setFillColor(STEEL)
    c.rect(left_x, y1 - 88, 180, 6, fill=1, stroke=0)

    # Line 2: THE AGENT IS THE HANDS.
    y2 = 590
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 66)
    c.drawString(left_x, y2, "THE AGENT")
    c.drawString(left_x, y2 - 70, "IS THE HANDS.")
    c.setFillColor(ORANGE)
    c.rect(left_x, y2 - 88, 260, 6, fill=1, stroke=0)

    # Line 3: MARKDOWN IS THE CONTRACT.
    y3 = 390
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 64)
    c.drawString(left_x, y3, "MARKDOWN IS")
    c.drawString(left_x, y3 - 70, "THE CONTRACT.")
    c.setFillColor(YELLOW)
    c.rect(left_x, y3 - 88, 340, 6, fill=1, stroke=0)

    # One-sentence promise at bottom left
    draw_brutalist_plate(c, left_x, 140, left_w - 20, 96, fill_col=COAL_LIGHT, stroke_col=STEEL, lw=2.5, shadow_offset=6, shadow_col=COAL_MID)
    c.setFillColor(ORANGE)
    c.rect(left_x, 140, 10, 96, fill=1, stroke=0)
    c.setFont("PlexSansBold", 24)
    c.setFillColor(BONE)
    c.drawString(left_x + 28, 192, "A workflow designed to outlive every agent session.")
    c.setFont("PlexMono", 14)
    c.setFillColor(STEEL_LIGHT)
    c.drawString(left_x + 28, 160, "HUMAN IDEA → APPROVED SPEC → STATELESS AGENT → COMMITTED HANDOFF → VERIFIED BUILD")

    # -------------------------------------------------------------------------
    # Right 5 Columns: Cutaway Steel Brain-Vault + Industrial Gloved Hand Forge
    # Connected by a single molten-orange seam
    # -------------------------------------------------------------------------
    vx = col_x(7)
    vw = col_span_w(5)
    vy = 140
    vh = 804

    # Outer architectural frame of the illustration
    draw_halftone_rect(c, vx, vy, vw, vh, COAL_MID, spacing=16, radius=2.5)
    c.setStrokeColor(STEEL)
    c.setLineWidth(3)
    c.rect(vx, vy, vw, vh, fill=0, stroke=1)

    # UPPER SECTION: Cutaway Steel Brain-Vault (Cranium-shaped octagonal steel vault)
    vcx = vx + vw * 0.50
    vcy = vy + vh * 0.68
    c.saveState()
    # Outer faceted steel cranium shell
    shell = c.beginPath()
    shell.moveTo(vcx - 240, vcy - 130)
    shell.lineTo(vcx - 260, vcy + 20)
    shell.lineTo(vcx - 190, vcy + 175)
    shell.lineTo(vcx + 150, vcy + 175)
    shell.lineTo(vcx + 250, vcy + 70)
    shell.lineTo(vcx + 250, vcy - 90)
    shell.lineTo(vcx + 140, vcy - 155)
    shell.lineTo(vcx - 180, vcy - 155)
    shell.close()
    c.setFillColor(COAL_LIGHT)
    c.setStrokeColor(BONE)
    c.setLineWidth(4.5)
    c.drawPath(shell, fill=1, stroke=1)

    # Inner cutaway chambers (brain hemisphere compartments)
    draw_hatch_rect(c, vcx - 215, vcy - 115, 425, 250, COAL_MID, spacing=14, lw=1.5)
    c.setStrokeColor(STEEL)
    c.setLineWidth(2.5)
    # Chamber 1: Upper left vault (Intent & Memory)
    c.setFillColor(COAL)
    c.rect(vcx - 210, vcy + 25, 195, 110, fill=1, stroke=1)
    # Vault gear wheel inside Chamber 1
    draw_gear(c, vcx - 112, vcy + 80, 38, 28, 10, 10, fill_col=STEEL_DARK, stroke_col=BONE, lw=2)

    # Chamber 2: Upper right vault (State & Ledger scrolls)
    c.setFillColor(COAL)
    c.rect(vcx + 5, vcy + 25, 205, 110, fill=1, stroke=1)
    for row_i in range(4):
        c.setStrokeColor(STEEL)
        c.setLineWidth(3)
        c.line(vcx + 25, vcy + 110 - row_i * 22, vcx + 185, vcy + 110 - row_i * 22)
        c.setFillColor(YELLOW if row_i == 0 else STEEL)
        c.rect(vcx + 25, vcy + 106 - row_i * 22, 24, 8, fill=1, stroke=0)

    # Chamber 3: Lower Blueprint Compartment (Labeled, holding crisp vector blueprint sheets)
    c.setFillColor(COAL)
    c.setStrokeColor(BONE)
    c.setLineWidth(3)
    c.rect(vcx - 210, vcy - 115, 420, 120, fill=1, stroke=1)
    # Stacked blueprint plates inside compartment (text-free inside art, geometric schematic lines)
    for bp_i in range(3):
        bx = vcx - 190 + bp_i * 125
        by = vcy - 95
        c.setFillColor(COAL_MID)
        c.setStrokeColor(BONE)
        c.setLineWidth(2)
        c.rect(bx, by, 108, 76, fill=1, stroke=1)
        c.setStrokeColor(STEEL_LIGHT)
        c.setLineWidth(1.5)
        c.line(bx + 12, by + 56, bx + 92, by + 56)
        c.line(bx + 12, by + 40, bx + 76, by + 40)
        c.line(bx + 12, by + 24, bx + 88, by + 24)
        c.circle(bx + 84, by + 32, 8, fill=0, stroke=1)

    # Rivets along the brain-vault perimeter
    c.setFillColor(BONE)
    for rx, ry in [
        (vcx - 180, vcy + 158), (vcx - 60, vcy + 158), (vcx + 60, vcy + 158),
        (vcx - 235, vcy + 10), (vcx + 230, vcy + 50), (vcx + 230, vcy - 70),
        (vcx - 160, vcy - 138), (vcx + 120, vcy - 138)
    ]:
        c.circle(rx, ry, 3.5, fill=1, stroke=0)

    # LOWER SECTION: Industrial Gloved Mechanical Hand Forging Clean Software Block
    h_base_y = vy + 45
    # Anvil / Forge Bed at bottom left of illustration frame
    c.setFillColor(STEEL_DARK)
    c.setStrokeColor(BONE)
    c.setLineWidth(3.5)
    anvil = c.beginPath()
    anvil.moveTo(vcx - 240, h_base_y)
    anvil.lineTo(vcx + 10, h_base_y)
    anvil.lineTo(vcx - 15, h_base_y + 55)
    anvil.lineTo(vcx + 25, h_base_y + 95)
    anvil.lineTo(vcx - 220, h_base_y + 95)
    anvil.lineTo(vcx - 200, h_base_y + 55)
    anvil.close()
    c.drawPath(anvil, fill=1, stroke=1)

    # Precision-machined software artifact on the anvil
    c.setFillColor(COAL)
    c.setStrokeColor(BONE)
    c.setLineWidth(3.5)
    c.rect(vcx - 175, h_base_y + 95, 150, 72, fill=1, stroke=1)
    # Crisp geometric circuit lines on forged block
    c.setStrokeColor(BONE)
    c.setLineWidth(2.5)
    c.line(vcx - 155, h_base_y + 142, vcx - 75, h_base_y + 142)
    c.line(vcx - 155, h_base_y + 120, vcx - 45, h_base_y + 120)
    c.setFillColor(BONE)
    c.circle(vcx - 55, h_base_y + 142, 5, fill=1, stroke=0)

    # Articulated Industrial Gloved Hand (right side of lower bay, gripping forge head)
    c.setFillColor(STEEL)
    c.setStrokeColor(COAL)
    c.setLineWidth(3.5)
    # Forearm gauntlet cuff
    c.setFillColor(STEEL_DARK)
    c.setStrokeColor(BONE)
    c.rect(vcx + 115, h_base_y + 90, 130, 110, fill=1, stroke=1)
    # Segmented knuckle plates gripping the forging die
    for k_i in range(4):
        ky = h_base_y + 96 + k_i * 25
        c.setFillColor(STEEL)
        c.setStrokeColor(BONE)
        c.setLineWidth(2.5)
        c.rect(vcx + 45, ky, 72, 21, fill=1, stroke=1)
        c.setFillColor(COAL)
        c.circle(vcx + 60, ky + 10.5, 3, fill=1, stroke=0)
    # Thumb plate clamping top
    c.setFillColor(STEEL)
    c.setStrokeColor(BONE)
    c.rect(vcx + 15, h_base_y + 175, 85, 26, fill=1, stroke=1)

    # Forging hammer/die head driven by the hand onto the software block
    c.setFillColor(BONE)
    c.setStrokeColor(COAL)
    c.setLineWidth(3)
    c.rect(vcx - 25, h_base_y + 108, 70, 58, fill=1, stroke=1)

    # THE SINGLE MOLTEN-ORANGE SEAM connecting Brain-Vault Blueprint Compartment -> Hand -> Forged Software
    c.setStrokeColor(ORANGE)
    c.setLineWidth(10)
    seam = c.beginPath()
    seam.moveTo(vcx, vcy - 115)          # Exits bottom of Blueprint Compartment
    seam.lineTo(vcx, vcy - 210)          # Vertical drop out of Brain-Vault
    seam.lineTo(vcx + 80, vcy - 210)     # Feeds into Industrial Hand gauntlet
    seam.lineTo(vcx + 80, h_base_y + 137)
    seam.lineTo(vcx - 25, h_base_y + 137) # Pulses directly into the forged software block
    c.drawPath(seam, fill=0, stroke=1)

    # Bright inner core on the molten-orange seam for graphic-novel contrast
    c.setStrokeColor(YELLOW)
    c.setLineWidth(2.5)
    c.drawPath(seam, fill=0, stroke=1)

    # Molten contact nodes at both ends of the seam
    c.setFillColor(ORANGE)
    c.setStrokeColor(BONE)
    c.setLineWidth(2.5)
    c.circle(vcx, vcy - 115, 10, fill=1, stroke=1)
    c.circle(vcx - 25, h_base_y + 137, 10, fill=1, stroke=1)
    c.restoreState()

    # Selectable Vector Overlay Labels on the Illustration
    draw_badge(c, vx + 18, vy + vh - 42, "BRAIN-VAULT // REPOSITORY", bg_col=COAL, fg_col=BONE, border_col=BONE, size=12, h=26)
    draw_badge(c, vcx - 195, vcy + 2, "BLUEPRINT COMPARTMENT // MARKDOWN CONTRACT", bg_col=YELLOW, fg_col=COAL, border_col=COAL, size=11, h=22)
    draw_badge(c, vx + 18, vy + 12, "FORGED OUTPUT // DERIVED CODE", bg_col=COAL, fg_col=BONE, border_col=STEEL, size=11, h=24)
    draw_badge(c, vx + vw - 215, vy + 12, "AGENT // STATELESS HANDS", bg_col=COAL, fg_col=BONE, border_col=STEEL, size=11, h=24)


def draw_slide_02(c):
    """02 — Why the old way breaks (Bone background, 3 jagged comic panels + intact bottom repo vault)"""
    draw_slide_frame(c, 2, ACT_I, bg_mode="bone", kicker="FAILURE MODE ANALYSIS // EPHEMERAL CHAT")

    # Top Headline & Subcopy
    lx = col_x(0)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 60)
    c.drawString(lx, 912, "CHAT MEMORY IS A TRAP.")

    draw_badge(c, col_x(7) + 30, 918, "Prompts evaporate. Decisions drift. Work gets rediscovered.",
               bg_col=COAL, fg_col=BONE, border_col=COAL, font="PlexSansBold", size=18, pad_x=18, h=42)

    # -------------------------------------------------------------------------
    # Three Jagged Industrial Comic Panels (y: 280..875)
    # -------------------------------------------------------------------------
    p_top = 875
    p_bot = 285
    p_w = col_span_w(4)

    panels = [
        (col_x(0), "PANEL 01 // EPHEMERAL PROMPT", "CHAT-AS-SPEC → LOST CONTEXT", "Prompts evaporate into thin air as soon as the window closes."),
        (col_x(4), "PANEL 02 // UNGOVERNED OUTPUT", "UNTRACED CODE → SPEC DRIFT", "Orphaned code blocks fall off an unmarked conveyor with no spec ID."),
        (col_x(8), "PANEL 03 // SESSION TERMINATION", "UNWRITTEN HANDOFF → AMNESIA", "An empty workstation faces a dead session; the next agent starts blind."),
    ]

    for idx, (px, p_tag, p_title, p_desc) in enumerate(panels):
        # Hard graphic-novel black shadow behind comic panel
        c.setFillColor(COAL)
        c.rect(px + 8, p_bot - 8, p_w, p_top - p_bot, fill=1, stroke=0)

        # Main panel box in Coal with heavy border
        c.setFillColor(COAL_LIGHT)
        c.setStrokeColor(COAL)
        c.setLineWidth(4.5)
        c.rect(px, p_bot, p_w, p_top - p_bot, fill=1, stroke=1)

        # Halftone texture inside top of panel
        draw_halftone_rect(c, px + 6, p_top - 220, p_w - 12, 165, COAL_MID, spacing=14, radius=2.2)

        # Jagged fracture tear cutting diagonally across the middle of the panel
        c.saveState()
        tear = c.beginPath()
        ty = p_bot + 260
        tear.moveTo(px + 4, ty + 20)
        tear.lineTo(px + p_w * 0.22, ty - 15)
        tear.lineTo(px + p_w * 0.38, ty + 28)
        tear.lineTo(px + p_w * 0.58, ty - 22)
        tear.lineTo(px + p_w * 0.78, ty + 18)
        tear.lineTo(px + p_w - 4, ty - 12)
        c.setStrokeColor(ORANGE)
        c.setLineWidth(4)
        c.drawPath(tear, fill=0, stroke=1)
        c.restoreState()

        # Panel top header strip
        c.setFillColor(COAL)
        c.rect(px, p_top - 44, p_w, 44, fill=1, stroke=1)
        c.setFont("PlexMonoBold", 13)
        c.setFillColor(ORANGE)
        c.drawString(px + 16, p_top - 28, p_tag)

        # Panel-specific graphic-novel illustration in upper bay (y: p_bot + 160 .. p_top - 55)
        cx = px + p_w * 0.5
        cy = p_bot + 360

        if idx == 0:
            # Panel 1 Illustration: Speech bubble disintegrating into fragments
            c.saveState()
            # Left half of speech bubble intact
            c.setFillColor(BONE)
            c.setStrokeColor(COAL)
            c.setLineWidth(3.5)
            bub = c.beginPath()
            bub.moveTo(cx - 170, cy + 75)
            bub.lineTo(cx + 10, cy + 75)
            bub.lineTo(cx - 15, cy + 35)
            bub.lineTo(cx + 20, cy + 5)
            bub.lineTo(cx - 5, cy - 35)
            bub.lineTo(cx - 95, cy - 35)
            bub.lineTo(cx - 135, cy - 80)
            bub.lineTo(cx - 125, cy - 35)
            bub.lineTo(cx - 170, cy - 35)
            bub.close()
            c.drawPath(bub, fill=1, stroke=1)
            # Prompt lines inside speech bubble
            c.setStrokeColor(COAL)
            c.setLineWidth(4)
            c.line(cx - 145, cy + 45, cx - 30, cy + 45)
            c.line(cx - 145, cy + 18, cx - 45, cy + 18)
            c.line(cx - 145, cy - 8, cx - 70, cy - 8)
            # Shattered shards floating away to the right in Furnace Orange & Bone
            shards = [
                (cx + 35, cy + 50, 36, 22, ORANGE),
                (cx + 85, cy + 62, 24, 16, BONE),
                (cx + 52, cy + 10, 28, 20, BONE),
                (cx + 105, cy + 20, 18, 14, ORANGE),
                (cx + 38, cy - 30, 30, 18, STEEL),
                (cx + 92, cy - 22, 22, 14, ORANGE),
                (cx + 138, cy + 42, 12, 10, STEEL),
                (cx + 148, cy - 5, 10, 8, BONE),
            ]
            for sx, sy, sw, sh, scol in shards:
                c.setFillColor(scol)
                c.setStrokeColor(COAL)
                c.setLineWidth(2)
                c.rect(sx, sy, sw, sh, fill=1, stroke=1)
            c.restoreState()

        elif idx == 1:
            # Panel 2 Illustration: Unmarked conveyor belt with orphaned code blocks falling into void
            c.saveState()
            # Conveyor frame on left
            c.setFillColor(STEEL_DARK)
            c.setStrokeColor(BONE)
            c.setLineWidth(3)
            c.rect(cx - 190, cy - 10, 210, 36, fill=1, stroke=1)
            # Conveyor rollers
            for r_i in range(4):
                c.setFillColor(COAL)
                c.circle(cx - 165 + r_i * 55, cy + 8, 12, fill=1, stroke=1)
            # Code block still on belt
            c.setFillColor(BONE)
            c.setStrokeColor(COAL)
            c.rect(cx - 165, cy + 28, 70, 48, fill=1, stroke=1)
            c.setFont("PlexMonoBold", 12)
            c.setFillColor(COAL)
            c.drawCentredString(cx - 130, cy + 46, "src/??")
            # Code block tipping at broken edge
            c.saveState()
            c.translate(cx + 25, cy + 25)
            c.rotate(-28)
            c.setFillColor(ORANGE)
            c.setStrokeColor(BONE)
            c.rect(-35, 0, 72, 48, fill=1, stroke=1)
            c.setFillColor(COAL)
            c.setFont("PlexMonoBold", 11)
            c.drawCentredString(0, 18, "NO SPEC")
            c.restoreState()
            # Orphaned code block plummeting into the void below right
            c.saveState()
            c.translate(cx + 115, cy - 55)
            c.rotate(-58)
            c.setFillColor(ORANGE)
            c.setStrokeColor(BONE)
            c.rect(-35, 0, 72, 48, fill=1, stroke=1)
            c.setFillColor(COAL)
            c.setFont("PlexMonoBold", 11)
            c.drawCentredString(0, 18, "DRIFT!")
            c.restoreState()
            # Motion lines
            c.setStrokeColor(ORANGE)
            c.setLineWidth(2.5)
            c.line(cx + 75, cy + 55, cx + 110, cy + 10)
            c.line(cx + 95, cy + 45, cx + 135, cy - 5)
            c.restoreState()

        else:
            # Panel 3 Illustration: Empty workstation facing a dead session monitor
            c.saveState()
            # Dead CRT/Industrial Terminal Monitor
            c.setFillColor(COAL)
            c.setStrokeColor(BONE)
            c.setLineWidth(3.5)
            c.rect(cx - 135, cy - 10, 270, 115, fill=1, stroke=1)
            c.setFillColor(COAL_MID)
            c.rect(cx - 120, cy + 4, 240, 87, fill=1, stroke=1)
            # Dead flatline & X eyes / lost session indicator
            c.setStrokeColor(ORANGE)
            c.setLineWidth(3.5)
            c.line(cx - 105, cy + 45, cx - 30, cy + 45)
            c.line(cx - 30, cy + 45, cx - 15, cy + 72)
            c.line(cx - 15, cy + 72, cx + 5, cy + 20)
            c.line(cx + 5, cy + 20, cx + 20, cy + 45)
            c.line(cx + 20, cy + 45, cx + 105, cy + 45)
            c.setFont("PlexMonoBold", 12)
            c.setFillColor(ORANGE)
            c.drawCentredString(cx, cy + 14, "SESSION DIED // MEMORY = NULL")
            # Empty operator stool & severed cable below monitor
            c.setFillColor(STEEL_DARK)
            c.setStrokeColor(BONE)
            c.setLineWidth(2.5)
            c.rect(cx - 50, cy - 55, 100, 16, fill=1, stroke=1)
            c.line(cx, cy - 55, cx, cy - 90)
            c.line(cx - 40, cy - 90, cx + 40, cy - 90)
            c.restoreState()

        # Lower Caption Box inside each panel with exact required copy
        c.setFillColor(ORANGE)
        c.setStrokeColor(COAL)
        c.setLineWidth(3)
        c.rect(px + 18, p_bot + 82, p_w - 36, 52, fill=1, stroke=1)
        # Dark COAL text on ORANGE (strict contrast rule!)
        c.setFillColor(COAL)
        c.setFont("PlexMonoBold", 19)
        c.drawCentredString(px + p_w / 2.0, p_bot + 100, p_title)

        draw_wrapped(c, px + 22, p_bot + 54, p_desc, "PlexSansMedium", 15, 20, p_w - 44, color=BONE, align="center")

    # -------------------------------------------------------------------------
    # Bottom Solid Steel Repository Vault spanning all 3 panels (survives all failures)
    # -------------------------------------------------------------------------
    vy = 115
    vh = 135
    vw = col_span_w(12)
    draw_brutalist_plate(c, lx, vy, vw, vh, fill_col=COAL, stroke_col=COAL, lw=4.5, shadow_offset=8, shadow_col=STEEL_DARK)
    draw_hazard_band(c, lx, vy + vh - 16, vw, 16, stripe_w=22, bg_col=YELLOW, fg_col=COAL, border_w=2)

    # Vault bolts and structural ribs
    c.setFillColor(YELLOW)
    c.rect(lx + 24, vy + 22, 12, vh - 52, fill=1, stroke=0)

    c.setFont("ArchivoBlack", 42)
    c.setFillColor(BONE)
    c.drawString(lx + 54, vy + 58, "Move intelligence into the repository.")

    c.setFont("PlexMonoBold", 15)
    c.setFillColor(YELLOW)
    c.drawString(lx + 54, vy + 26, "PERSISTENT FOUNDATION // VERSIONED SPECS · IMMUTABLE ADRs · WRITTEN HANDOFFS")

    # Right vault badge inside the foundation bar
    draw_badge(c, lx + vw - 355, vy + 40, "REPO SURVIVES EVERY SESSION", bg_col=STEEL, fg_col=COAL, border_col=BONE, font="PlexMonoBold", size=15, pad_x=16, h=44)


def draw_slide_03(c):
    """03 — The complete loop (Coal background, 3 actor lanes + return state belt)"""
    draw_slide_frame(c, 3, ACT_I, bg_mode="coal", kicker="CLOSED-LOOP OPERATING ARCHITECTURE")

    lx = col_x(0)
    full_w = col_span_w(12)

    # Headline
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 54)
    c.drawString(lx, 940, "THE SYSTEM, IN ONE LOOP")

    # Full chronological chain sits in its own rail beneath the headline.
    chain_box_x = lx
    chain_box_w = full_w
    draw_brutalist_plate(c, chain_box_x, 858, chain_box_w, 64, fill_col=COAL_LIGHT, stroke_col=STEEL, lw=2.5, shadow_offset=4, shadow_col=COAL_MID)
    c.setFont("PlexMonoBold", 14)
    c.setFillColor(YELLOW)
    c.drawString(chain_box_x + 18, 898, "IDEA → APPROVED SPEC → PLAN / TASK → BUILD / TEST → HANDOFF")
    c.setFillColor(BONE)
    c.drawString(chain_box_x + 18, 874, "→ PUSH / PR → CI → HUMAN MERGE → DEPLOYED VERIFY")

    # -------------------------------------------------------------------------
    # Three Horizontal Actor Lanes + Bottom Return Conveyor
    # -------------------------------------------------------------------------
    lane_label_w = 210
    track_x = lx + lane_label_w + 16
    track_w = full_w - lane_label_w - 16

    lanes = [
        ("HUMAN LANE", "AUTHORITY & GATES", 695, 155, YELLOW, COAL),
        ("AGENT LANE", "STATELESS EXECUTION", 505, 165, STEEL, COAL),
        ("CI LANE", "AUTOMATED INSPECTOR", 325, 155, ORANGE, COAL),
    ]

    for l_title, l_sub, ly, lh, badge_col, badge_fg in lanes:
        # Left lane header block
        draw_brutalist_plate(c, lx, ly, lane_label_w, lh, fill_col=COAL_LIGHT, stroke_col=badge_col, lw=3, shadow_offset=4, shadow_col=COAL_MID)
        c.setFillColor(badge_col)
        c.rect(lx, ly + lh - 34, lane_label_w, 34, fill=1, stroke=0)
        c.setFillColor(badge_fg)
        c.setFont("ArchivoBlack", 18)
        c.drawString(lx + 14, ly + lh - 24, l_title)
        c.setFillColor(BONE)
        c.setFont("PlexMonoBold", 12)
        c.drawString(lx + 14, ly + lh - 58, l_sub)

        # Conveyor lane bed
        c.setFillColor(COAL_LIGHT)
        c.setStrokeColor(STEEL_DARK)
        c.setLineWidth(2.5)
        c.rect(track_x, ly, track_w, lh, fill=1, stroke=1)
        draw_halftone_rect(c, track_x + 4, ly + 4, track_w - 8, lh - 8, COAL_MID, spacing=18, radius=1.8)

    # Coordinate anchors along X for the chronological workflow stages (strictly left to right!)
    # S1: IDEA (x=340) -> S2: G:APPROVE / APPROVED SPEC (x=520) -> S3: PLAN/TASK (x=690)
    # -> S4: BUILD/TEST (x=885) -> S5: HANDOFF (x=1080) -> S6: PUSH/PR (x=1265)
    # -> S7: CI (x=1435) -> S8: HUMAN MERGE (x=1590) -> S9: DEPLOYED VERIFY (x=1745)

    # --- HUMAN LANE STATIONS (y=695..850, cy=772) ---
    hy = 730
    bh = 86
    # 1. IDEA
    draw_brutalist_plate(c, track_x + 18, hy, 130, bh, fill_col=BONE, stroke_col=COAL, lw=3, shadow_offset=4, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 20)
    c.drawCentredString(track_x + 83, hy + 46, "IDEA")
    c.setFont("PlexMonoBold", 11)
    c.drawCentredString(track_x + 83, hy + 22, "brainstorm/")

    # Arrow IDEA -> APPROVED SPEC
    draw_arrow(c, track_x + 148, hy + 43, track_x + 195, hy + 43, color=YELLOW, lw=4)

    # 2. G: APPROVE -> APPROVED SPEC (Human Gate #1)
    gx1 = track_x + 195
    gw1 = 210
    draw_brutalist_plate(c, gx1, hy, gw1, bh, fill_col=YELLOW, stroke_col=COAL, lw=3.5, shadow_offset=5, shadow_col=COAL)
    draw_hazard_band(c, gx1, hy + bh - 12, gw1, 12, stripe_w=10, bg_col=YELLOW, fg_col=COAL, border_w=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 12)
    c.drawCentredString(gx1 + gw1 / 2, hy + 54, "G: HUMAN APPROVAL")
    c.setFont("ArchivoBlack", 18)
    c.drawCentredString(gx1 + gw1 / 2, hy + 24, "APPROVED SPEC")

    # Vertical chute from APPROVED SPEC down into AGENT LANE (PLAN / TASK)
    draw_arrow(c, gx1 + gw1 / 2, hy, gx1 + gw1 / 2, 635, color=YELLOW, lw=4)

    # --- AGENT LANE STATIONS (y=505..670, boxes at y=542, bh=88) ---
    ay = 542
    agent_nodes = [
        (track_x + 215, 185, "PLAN / TASK", "PLAN-004 → T-032", BONE, COAL),
        (track_x + 440, 195, "BUILD / TEST", "Test-first AC → verify", BONE, COAL),
        (track_x + 675, 195, "HANDOFF", "STATE + LEDGER commit", ORANGE, COAL),
        (track_x + 910, 175, "PUSH / PR", "feat/ branch → PR", BONE, COAL),
    ]
    for idx, (nx, nw, ntitle, nsub, nbg, nfg) in enumerate(agent_nodes):
        draw_brutalist_plate(c, nx, ay, nw, bh, fill_col=nbg, stroke_col=COAL, lw=3.5, shadow_offset=5, shadow_col=COAL)
        c.setFillColor(nfg)
        c.setFont("ArchivoBlack", 19)
        c.drawCentredString(nx + nw / 2, ay + 48, ntitle)
        c.setFont("PlexMonoBold", 11.5)
        c.drawCentredString(nx + nw / 2, ay + 20, nsub)
        if idx < len(agent_nodes) - 1:
            next_x = agent_nodes[idx + 1][0]
            draw_arrow(c, nx + nw, ay + 44, next_x, ay + 44, color=ORANGE if idx == 1 else BONE, lw=4)

    # Chute from PUSH / PR down to CI LANE
    push_cx = track_x + 910 + 87
    draw_arrow(c, push_cx, ay, push_cx, 448, color=ORANGE, lw=4)

    # --- CI LANE STATION (y=325..480) ---
    ci_x = track_x + 875
    ci_w = 275
    ci_y = 358
    draw_brutalist_plate(c, ci_x, ci_y, ci_w, bh, fill_col=COAL, stroke_col=ORANGE, lw=3.5, shadow_offset=5, shadow_col=COAL_MID)
    c.setFillColor(ORANGE)
    c.rect(ci_x, ci_y + bh - 24, ci_w, 24, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 12)
    c.drawCentredString(ci_x + ci_w / 2, ci_y + bh - 17, "AUTOMATED GATE // INSPECTOR")
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 22)
    c.drawCentredString(ci_x + ci_w / 2, ci_y + 34, "CI CHECKS")
    c.setFont("PlexMono", 11.5)
    c.setFillColor(STEEL_LIGHT)
    c.drawCentredString(ci_x + ci_w / 2, ci_y + 12, "test · lint · type · secret · forge-lint")

    # Left side of CI lane: legend explaining gate discipline
    c.setFont("PlexMonoBold", 13)
    c.setFillColor(STEEL_LIGHT)
    c.drawString(track_x + 24, ci_y + 52, "CHRONOLOGICAL DISCIPLINE:")
    c.setFont("PlexSans", 15)
    c.setFillColor(BONE)
    c.drawString(track_x + 24, ci_y + 26, "• Handoff commit is recorded BEFORE branch push.")
    c.drawString(track_x + 24, ci_y + 2, "• Human merge & deployed verification are distinct gates.")

    # Arrow from CI up to HUMAN MERGE in HUMAN LANE
    merge_x = track_x + 1105
    merge_w = 170
    draw_arrow(c, ci_x + ci_w, ci_y + 44, merge_x + 45, ci_y + 44, color=STEEL_LIGHT, lw=4)
    draw_arrow(c, merge_x + 45, ci_y + 44, merge_x + 45, hy, color=STEEL_LIGHT, lw=4)

    # --- HUMAN LANE FINAL GATES: HUMAN MERGE -> DEPLOYED VERIFY ---
    # 3. G: HUMAN MERGE
    draw_brutalist_plate(c, merge_x, hy, merge_w, bh, fill_col=YELLOW, stroke_col=COAL, lw=3.5, shadow_offset=5, shadow_col=COAL)
    draw_hazard_band(c, merge_x, hy + bh - 12, merge_w, 12, stripe_w=10, bg_col=YELLOW, fg_col=COAL, border_w=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 11.5)
    c.drawCentredString(merge_x + merge_w / 2, hy + 54, "G: PROTECTED MAIN")
    c.setFont("ArchivoBlack", 18)
    c.drawCentredString(merge_x + merge_w / 2, hy + 24, "HUMAN MERGE")

    # Arrow HUMAN MERGE -> DEPLOYED VERIFY
    verify_x = track_x + 1300
    verify_w = 185
    draw_arrow(c, merge_x + merge_w, hy + 43, verify_x, hy + 43, color=YELLOW, lw=4)

    # 4. G: DEPLOYED VERIFY
    draw_brutalist_plate(c, verify_x, hy, verify_w, bh, fill_col=YELLOW, stroke_col=COAL, lw=3.5, shadow_offset=5, shadow_col=COAL)
    draw_hazard_band(c, verify_x, hy + bh - 12, verify_w, 12, stripe_w=10, bg_col=YELLOW, fg_col=COAL, border_w=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 11.5)
    c.drawCentredString(verify_x + verify_w / 2, hy + 54, "G: HUMAN ON DEPLOY")
    c.setFont("ArchivoBlack", 16.5)
    c.drawCentredString(verify_x + verify_w / 2, hy + 24, "DEPLOYED VERIFY")

    # -------------------------------------------------------------------------
    # Bottom Return Belt: COMMITTED STATE -> NEXT STATELESS SESSION
    # -------------------------------------------------------------------------
    ret_y = 135
    ret_h = 145
    draw_brutalist_plate(c, lx, ret_y, full_w, ret_h, fill_col=COAL_LIGHT, stroke_col=BONE, lw=3.5, shadow_offset=6, shadow_col=COAL_MID)

    # Downward return conduit from DEPLOYED VERIFY & HANDOFF into the return belt
    draw_arrow(c, verify_x + verify_w / 2, hy, verify_x + verify_w / 2, ret_y + ret_h, color=YELLOW, lw=3.5, dashed=True)
    handoff_cx = track_x + 675 + 97
    draw_arrow(c, handoff_cx, ay, handoff_cx, ret_y + ret_h, color=ORANGE, lw=3.5, dashed=True)

    # Return conveyor gears & belt track running RIGHT to LEFT
    draw_gear(c, lx + 95, ret_y + 72, 42, 32, 12, 12, fill_col=STEEL, stroke_col=COAL, lw=2.5)
    draw_gear(c, lx + full_w - 95, ret_y + 72, 42, 32, 12, 12, fill_col=STEEL, stroke_col=COAL, lw=2.5)

    # Heavy return arrow from right to left
    draw_arrow(c, lx + full_w - 160, ret_y + 92, lx + 160, ret_y + 92, color=ORANGE, lw=6, head_len=20, head_w=12)

    # Upward boot arrow from left of Return Belt back into AGENT LANE
    draw_arrow(c, track_x + 95, ret_y + ret_h, track_x + 95, ay + 44, color=ORANGE, lw=4.5)
    draw_arrow(c, track_x + 95, ay + 44, track_x + 215, ay + 44, color=ORANGE, lw=4.5)

    # Return belt copy
    c.setFont("ArchivoBlack", 28)
    c.setFillColor(BONE)
    c.drawCentredString(lx + full_w / 2, ret_y + 44, "The next agent resumes from committed state.")
    draw_badge(c, lx + full_w / 2 - 260, ret_y + 100, "RETURN BELT // .forge/STATE.md + .forge/LEDGER.md → NEXT STATELESS SESSION",
               bg_col=YELLOW, fg_col=COAL, border_col=COAL, font="PlexMonoBold", size=12, pad_x=14, h=28)
