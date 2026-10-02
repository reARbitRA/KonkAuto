from theme import (
    W, H, MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM,
    COAL, BONE, ORANGE, YELLOW, STEEL, GREEN,
    COAL_LIGHT, COAL_MID, STEEL_DARK, STEEL_LIGHT, BONE_DARK, BONE_MID,
    col_x, col_span_w, draw_slide_frame, draw_halftone_rect, draw_hatch_rect,
    draw_hazard_band, draw_brutalist_plate, draw_arrow, draw_gear, draw_padlock,
    draw_badge
)

ACT_II = "ACT II — THE CONTRACT"


def draw_slide_04(c):
    """04 — Repository anatomy (Bone background, 4-col copy + 8-col cutaway repository building)"""
    draw_slide_frame(c, 4, ACT_II, bg_mode="bone", kicker="STRUCTURAL ANATOMY // DIRECTORY TAXONOMY")

    lx = col_x(0)
    lw = col_span_w(4)

    # Left 4-column Headline & Key
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 48)
    c.drawString(lx, 915, "THE REPO IS")
    c.drawString(lx, 860, "THE MACHINE")
    c.drawString(lx, 805, "ROOM.")

    c.setFillColor(ORANGE)
    c.rect(lx, 782, 180, 7, fill=1, stroke=0)

    # Directory list cards on left column
    dir_items = [
        ("AGENTS.md", "one entry point", ORANGE, COAL),
        (".forge/", "state, ledger, trace", YELLOW, COAL),
        ("vision/ · brainstorm/ · knowledge/", "intent and context", BONE_MID, COAL),
        ("specs/ · decisions/", "contract and decisions", YELLOW, COAL),
        ("plans/ · tasks/", "execution", BONE_MID, COAL),
        ("quality/ · ops/ · .github/", "controls", BONE_MID, COAL),
        ("src/ · tests/", "derived product", STEEL, COAL),
    ]
    cy = 715
    for d_code, d_desc, tag_bg, tag_fg in dir_items:
        draw_brutalist_plate(c, lx, cy, lw, 64, fill_col=COAL, stroke_col=COAL, lw=2.5, shadow_offset=4, shadow_col=STEEL_DARK, rivets=False)
        c.setFillColor(tag_bg)
        c.rect(lx, cy, 10, 64, fill=1, stroke=0)
        c.setFont("PlexMonoBold", 14.5)
        c.setFillColor(tag_bg if tag_bg in (ORANGE, YELLOW) else BONE)
        c.drawString(lx + 20, cy + 36, d_code)
        c.setFont("PlexSansMedium", 14)
        c.setFillColor(BONE_DARK)
        c.drawString(lx + 20, cy + 12, f"— {d_desc}")
        cy -= 76

    # Bottom left principle badge
    draw_brutalist_plate(c, lx, 115, lw, 62, fill_col=ORANGE, stroke_col=COAL, lw=3, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 21)
    c.drawCentredString(lx + lw / 2, 138, "CODE IS OUTPUT, NOT AUTHORITY")

    # -------------------------------------------------------------------------
    # Right 8 Columns: Sectional Concrete-and-Steel Building Cutaway
    # -------------------------------------------------------------------------
    bx = col_x(4) + 10
    bw = col_span_w(8) - 10
    by = 115
    bh = 850

    # Building outer concrete/steel structural shell with pitched roof truss
    c.saveState()
    c.setFillColor(COAL)
    c.rect(bx + 120, by + 8, bw - 120, bh - 8, fill=1, stroke=0)
    draw_brutalist_plate(c, bx + 110, by, bw - 110, bh - 35, fill_col=COAL_LIGHT, stroke_col=COAL, lw=5, shadow_offset=0)

    # Roof structural I-beam header
    draw_hazard_band(c, bx + 110, by + bh - 55, bw - 110, 20, stripe_w=18, bg_col=YELLOW, fg_col=COAL, border_w=3)
    c.setFillColor(COAL)
    c.rect(bx + 110, by + bh - 35, bw - 110, 35, fill=1, stroke=1)
    c.setFont("PlexMonoBold", 14)
    c.setFillColor(BONE)
    c.drawString(bx + 130, by + bh - 23, "SECTIONAL CUTAWAY // SPECIFICATION FOUNDRY & REPOSITORY ARCHITECTURE")

    # SINGLE FRONT DOOR on Left Facade: AGENTS.md
    door_x = bx
    door_y = by + 510
    door_w = 135
    door_h = 220
    draw_brutalist_plate(c, door_x, door_y, door_w, door_h, fill_col=ORANGE, stroke_col=COAL, lw=4, shadow_offset=6, shadow_col=COAL)
    # Blast door vault wheel
    draw_gear(c, door_x + door_w / 2, door_y + 115, 34, 25, 8, 8, fill_col=COAL, stroke_col=BONE, lw=2)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 18)
    c.drawCentredString(door_x + door_w / 2, door_y + 175, "AGENTS.md")
    c.setFont("PlexMonoBold", 11)
    c.drawCentredString(door_x + door_w / 2, door_y + 45, "SINGLE FRONT")
    c.drawCentredString(door_x + door_w / 2, door_y + 28, "ENTRY DOOR")

    # Entry arrow from AGENTS.md into the building's .forge/ memory room
    draw_arrow(c, door_x + door_w - 8, door_y + 115, bx + 165, door_y + 115, color=YELLOW, lw=5)

    # Internal Vertical Elevator / Gantry Spine connecting all floors
    spine_x = bx + 165
    spine_w = 56
    c.setFillColor(COAL)
    c.setStrokeColor(STEEL)
    c.setLineWidth(2.5)
    c.rect(spine_x, by + 30, spine_w, bh - 105, fill=1, stroke=1)
    draw_hatch_rect(c, spine_x + 4, by + 34, spine_w - 8, bh - 113, STEEL_DARK, spacing=12, lw=1.5)
    # Downward flow arrow inside vertical gantry shaft
    draw_arrow(c, spine_x + spine_w / 2, by + bh - 110, spine_x + spine_w / 2, by + 70, color=ORANGE, lw=4)

    # Six Horizontal Floors inside the Cutaway Building (x: spine_x + spine_w + 18 .. bx + bw - 24)
    rx = spine_x + spine_w + 18
    rw = (bx + bw - 24) - rx

    floors = [
        # (y, h, floor_num, code_label, role_title, detail_items, accent_col)
        (by + 665, 110, "FLOOR 05 // BOOT & MEMORY ROOM", ".forge/", "STATE · LEDGER · TRACE", ["STATE.md (snapshot)", "LEDGER.md (append log)", "TRACE.md · CONVENTIONS.md"], YELLOW),
        (by + 540, 110, "FLOOR 04 // INTENT & CONTEXT DECK", "vision/ · brainstorm/ · knowledge/", "WHY & RAW CONTEXT", ["VISION.md · ROADMAP.md", "SEED → GROWING → PROMOTED", "snippets/ · apis/ · research/"], STEEL_LIGHT),
        (by + 405, 120, "FLOOR 03 // BLUEPRINT & CONTRACT FLOOR", "specs/ · decisions/", "AUTHORITATIVE CONTRACT", ["specs/INDEX.md · SPEC-012", "Immutable ADRs (ADR-0001..)", "HUMAN GATED: APPROVED"], ORANGE),
        (by + 280, 110, "FLOOR 02 // WORK ORDER DISPATCH", "plans/ · tasks/", "SIZED EXECUTION UNITS", ["PLAN-004 (ordered tasks)", "tasks/: OPEN → DOING → REVIEW → DONE", "1 task = 1 mergeable branch"], BONE),
        (by + 155, 110, "FLOOR 01 // QUALITY & OPS CONTROL TOWER", "quality/ · ops/ · .github/", "GUARDRAILS & CI", ["DOD.md · TEST-STRATEGY.md", "ENV.md · KEYS.md (public only)", "workflows/ · forge-lint"], YELLOW),
        (by + 25,  115, "GROUND FLOOR // FABRICATION BAY", "src/ · tests/", "DERIVED PRODUCT OUTPUT", ["Every src/ file links # SPEC-###", "Every AC has test_ac_n_*", "Regenerable from specs/"], STEEL),
    ]

    for fy, fh, f_tag, f_code, f_role, f_pills, f_col in floors:
        # Room chamber plate
        c.setFillColor(COAL)
        c.setStrokeColor(f_col)
        c.setLineWidth(3)
        c.rect(rx, fy, rw, fh, fill=1, stroke=1)

        # Left accent bar inside room
        c.setFillColor(f_col)
        c.rect(rx, fy, 12, fh, fill=1, stroke=0)

        # Floor header badge
        c.setFont("PlexMonoBold", 11.5)
        c.setFillColor(STEEL_LIGHT)
        c.drawString(rx + 24, fy + fh - 22, f_tag)

        # Main directory identifier in crisp monospace
        c.setFont("PlexMonoBold", 19)
        c.setFillColor(f_col)
        c.drawString(rx + 24, fy + fh - 50, f_code)

        # Right role badge
        draw_badge(c, rx + rw - 275, fy + fh - 36, f_role, bg_col=f_col, fg_col=COAL, border_col=COAL, font="PlexMonoBold", size=11, pad_x=10, h=24)

        # Sub-compartments (3 internal equipment bays per floor)
        pw = (rw - 56) / 3.0
        for p_i, p_text in enumerate(f_pills):
            px = rx + 24 + p_i * (pw + 8)
            py = fy + 12
            c.setFillColor(COAL_MID)
            c.setStrokeColor(STEEL_DARK)
            c.setLineWidth(1.5)
            c.rect(px, py, pw, 32, fill=1, stroke=1)
            c.setFont("PlexMono", 11.5)
            c.setFillColor(BONE)
            c.drawString(px + 10, py + 10, p_text)

        # Connector conduit from vertical gantry spine into floor
        draw_arrow(c, spine_x + spine_w, fy + fh / 2, rx, fy + fh / 2, color=f_col, lw=3)

    c.restoreState()


def draw_slide_05(c):
    """05 — Promotion is deliberate (Coal background, raw idea fragments -> spec press -> yellow human approval gate)"""
    draw_slide_frame(c, 5, ACT_II, bg_mode="coal", kicker="PROMOTION PROTOCOL // GATEKEEPING")

    lx = col_x(0)
    full_w = col_span_w(12)

    # Headline
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 58)
    c.drawString(lx, 912, "IDEAS DO NOT SHIP.")

    # Top lifecycle badges
    draw_badge(c, col_x(5), 918, "brainstorm/: SEED → GROWING → PROMOTED", bg_col=COAL_LIGHT, fg_col=BONE, border_col=STEEL, font="PlexMonoBold", size=14, pad_x=14, h=36)
    draw_badge(c, col_x(8) + 55, 918, "specs/: DRAFT → REVIEW → APPROVED", bg_col=YELLOW, fg_col=COAL, border_col=COAL, font="PlexMonoBold", size=14, pad_x=14, h=36)

    # -------------------------------------------------------------------------
    # Main Foundry & Hydraulic Approval Press Diagram (y: 255..875)
    # -------------------------------------------------------------------------
    dy = 265
    dh = 605
    draw_brutalist_plate(c, lx, dy, full_w, dh, fill_col=COAL_LIGHT, stroke_col=STEEL, lw=3.5, shadow_offset=8, shadow_col=COAL_MID)
    draw_halftone_rect(c, lx + 8, dy + 8, full_w - 16, dh - 16, COAL_MID, spacing=18, radius=2.0)

    # Conveyor baseline running across the foundry
    conv_y = dy + 230
    c.setFillColor(STEEL_DARK)
    c.setStrokeColor(BONE)
    c.setLineWidth(3)
    c.rect(lx + 40, conv_y - 28, full_w - 80, 28, fill=1, stroke=1)
    for r_i in range(14):
        c.setFillColor(COAL)
        c.circle(lx + 75 + r_i * 122, conv_y - 14, 9, fill=1, stroke=1)

    # STAGE 1 (Left): Raw Idea Fragments in `brainstorm/` Hopper (SEED -> GROWING -> PROMOTED)
    s1_x = lx + 45
    s1_w = 390
    draw_brutalist_plate(c, s1_x, conv_y + 15, s1_w, 310, fill_col=COAL, stroke_col=STEEL, lw=3, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(STEEL)
    c.rect(s1_x, conv_y + 290, s1_w, 35, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 16)
    c.drawString(s1_x + 14, conv_y + 300, "01 // RAW IDEA FRAGMENTS (brainstorm/)")

    # Irregular polygon ore fragments representing SEED -> GROWING -> PROMOTED
    ore_stages = [
        (s1_x + 70, conv_y + 185, "SEED", STEEL_DARK, BONE),
        (s1_x + 195, conv_y + 185, "GROWING", STEEL, COAL),
        (s1_x + 320, conv_y + 185, "PROMOTED", ORANGE, COAL),
    ]
    for idx, (ox, oy, olabel, ocol, ofg) in enumerate(ore_stages):
        c.saveState()
        c.setFillColor(ocol)
        c.setStrokeColor(BONE)
        c.setLineWidth(2.5)
        p = c.beginPath()
        p.moveTo(ox - 48, oy - 35)
        p.lineTo(ox - 55, oy + 20)
        p.lineTo(ox - 15, oy + 48)
        p.lineTo(ox + 45, oy + 32)
        p.lineTo(ox + 52, oy - 22)
        p.lineTo(ox + 10, oy - 45)
        p.close()
        c.drawPath(p, fill=1, stroke=1)
        c.setFillColor(ofg)
        c.setFont("PlexMonoBold", 13)
        c.drawCentredString(ox, oy - 5, olabel)
        c.restoreState()
        if idx < 2:
            draw_arrow(c, ox + 54, oy, ox + 70, oy, color=BONE, lw=3, head_len=10, head_w=6)

    c.setFont("PlexMonoBold", 14)
    c.setFillColor(BONE)
    c.drawCentredString(s1_x + s1_w / 2, conv_y + 82, "brainstorm/: SEED → GROWING → PROMOTED")
    c.setFont("PlexSans", 14)
    c.setFillColor(STEEL_LIGHT)
    c.drawCentredString(s1_x + s1_w / 2, conv_y + 52, "Low ceremony thinking. Never authorizes code.")

    # Molten conduit pouring from PROMOTED into STAGE 2 Spec Casting Press
    draw_arrow(c, s1_x + s1_w, conv_y + 165, s1_x + s1_w + 55, conv_y + 165, color=ORANGE, lw=6)

    # STAGE 2 (Center): Spec Casting Die (`specs/: DRAFT -> REVIEW`)
    s2_x = s1_x + s1_w + 55
    s2_w = 430
    draw_brutalist_plate(c, s2_x, conv_y + 15, s2_w, 310, fill_col=COAL, stroke_col=BONE, lw=3, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(BONE)
    c.rect(s2_x, conv_y + 290, s2_w, 35, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 16)
    c.drawString(s2_x + 14, conv_y + 300, "02 // SPEC CASTING DIE (specs/)")

    # Machined Spec Sheets: DRAFT -> REVIEW
    draw_brutalist_plate(c, s2_x + 30, conv_y + 135, 160, 120, fill_col=COAL_MID, stroke_col=BONE, lw=2.5, shadow_offset=4, shadow_col=COAL)
    c.setFont("ArchivoBlack", 20)
    c.setFillColor(BONE)
    c.drawCentredString(s2_x + 110, conv_y + 195, "DRAFT")
    c.setFont("PlexMono", 12)
    c.setFillColor(STEEL_LIGHT)
    c.drawCentredString(s2_x + 110, conv_y + 165, "Agent/Human drafts")

    draw_arrow(c, s2_x + 195, conv_y + 195, s2_x + 240, conv_y + 195, color=ORANGE, lw=4)

    draw_brutalist_plate(c, s2_x + 240, conv_y + 135, 160, 120, fill_col=ORANGE, stroke_col=BONE, lw=2.5, shadow_offset=4, shadow_col=COAL)
    c.setFont("ArchivoBlack", 20)
    c.setFillColor(COAL)
    c.drawCentredString(s2_x + 320, conv_y + 195, "REVIEW")
    c.setFont("PlexMonoBold", 12)
    c.setFillColor(COAL)
    c.drawCentredString(s2_x + 320, conv_y + 165, "Awaiting Human")

    c.setFont("PlexMonoBold", 14)
    c.setFillColor(YELLOW)
    c.drawCentredString(s2_x + s2_w / 2, conv_y + 82, "specs/: DRAFT → REVIEW → APPROVED")

    # Ambiguity Diverter Chute below STAGE 2 (below conveyor)
    amb_y = dy + 28
    draw_brutalist_plate(c, s1_x + 120, amb_y, 720, 145, fill_col=COAL, stroke_col=ORANGE, lw=3, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(ORANGE)
    c.rect(s1_x + 120, amb_y, 14, 145, fill=1, stroke=0)
    draw_arrow(c, s2_x + 215, conv_y - 28, s2_x + 215, amb_y + 145, color=ORANGE, lw=4)
    c.setFont("ArchivoBlack", 24)
    c.setFillColor(ORANGE)
    c.drawString(s1_x + 155, amb_y + 92, "Ambiguous? Record the question. Do not guess.")
    c.setFont("PlexMonoBold", 14)
    c.setFillColor(BONE)
    c.drawString(s1_x + 155, amb_y + 54, "PROTOCOL: Log Open Question in §9 / mark task BLOCKED → move to tasks/REVIEW/.")
    c.setFillColor(STEEL_LIGHT)
    c.drawString(s1_x + 155, amb_y + 24, "Never invent business rules or silently resolve underspecified behavior.")

    # STAGE 3 (Right): Colossal Hazard-Yellow Human-Operated Approval Press + Code Foundry Gate
    s3_x = s2_x + s2_w + 55
    s3_w = (lx + full_w - 40) - s3_x

    # Heavy vertical steel press columns
    c.setFillColor(STEEL_DARK)
    c.setStrokeColor(BONE)
    c.setLineWidth(3)
    c.rect(s3_x + 30, conv_y, 32, 370, fill=1, stroke=1)
    c.rect(s3_x + 350, conv_y, 32, 370, fill=1, stroke=1)

    # Top Hydraulic Crown of Human Approval Press
    draw_brutalist_plate(c, s3_x + 10, conv_y + 310, 392, 65, fill_col=YELLOW, stroke_col=COAL, lw=3.5, shadow_offset=5, shadow_col=COAL)
    draw_hazard_band(c, s3_x + 10, conv_y + 360, 392, 15, stripe_w=14, bg_col=YELLOW, fg_col=COAL, border_w=0)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 19)
    c.drawCentredString(s3_x + 206, conv_y + 328, "G: HUMAN APPROVAL PRESS")

    # Hydraulic Piston Shaft & Lowering Yellow Stamp Head
    c.setFillColor(STEEL)
    c.setStrokeColor(COAL)
    c.setLineWidth(3)
    c.rect(s3_x + 176, conv_y + 225, 60, 85, fill=1, stroke=1)

    draw_brutalist_plate(c, s3_x + 75, conv_y + 135, 262, 95, fill_col=YELLOW, stroke_col=COAL, lw=4, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 28)
    c.drawCentredString(s3_x + 206, conv_y + 185, "APPROVED")
    c.setFont("PlexMonoBold", 12)
    c.drawCentredString(s3_x + 206, conv_y + 154, "HUMAN ONLY · NO AGENT ACCESS")

    # Downward force arrows on press
    draw_arrow(c, s3_x + 115, conv_y + 295, s3_x + 115, conv_y + 238, color=YELLOW, lw=4)
    draw_arrow(c, s3_x + 297, conv_y + 295, s3_x + 297, conv_y + 238, color=YELLOW, lw=4)
    draw_arrow(c, s2_x + s2_w, conv_y + 180, s3_x + 75, conv_y + 180, color=YELLOW, lw=4.5)

    # Stop gate / Authorized output box to right of press
    code_x = s3_x + 415
    code_w = (lx + full_w - 40) - code_x
    draw_brutalist_plate(c, code_x, conv_y + 15, code_w, 310, fill_col=COAL, stroke_col=STEEL, lw=3.5, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(STEEL)
    c.rect(code_x, conv_y + 290, code_w, 35, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 15)
    c.drawCentredString(code_x + code_w / 2, conv_y + 301, "03 // CODE FOUNDRY")

    draw_padlock(c, code_x + code_w / 2, conv_y + 215, w=54, h=44, body_col=YELLOW, stroke_col=COAL, label="G")
    c.setFont("ArchivoBlack", 18)
    c.setFillColor(BONE)
    c.drawCentredString(code_x + code_w / 2, conv_y + 135, "src/ & tests/")
    c.setFont("PlexMonoBold", 12)
    c.setFillColor(BONE)
    c.drawCentredString(code_x + code_w / 2, conv_y + 105, "AUTHORIZED")
    c.drawCentredString(code_x + code_w / 2, conv_y + 85, "ONLY WHEN")
    c.setFillColor(YELLOW)
    c.drawCentredString(code_x + code_w / 2, conv_y + 65, "SPEC = APPROVED")

    draw_arrow(c, s3_x + 337, conv_y + 180, code_x, conv_y + 180, color=STEEL_LIGHT, lw=4.5)

    # Bottom right gate rule box inside foundry
    draw_brutalist_plate(c, s3_x + 30, amb_y, (lx + full_w - 40) - (s3_x + 30), 145, fill_col=YELLOW, stroke_col=COAL, lw=4, shadow_offset=5, shadow_col=COAL)
    draw_hazard_band(c, s3_x + 30, amb_y + 125, (lx + full_w - 40) - (s3_x + 30), 20, stripe_w=16, bg_col=YELLOW, fg_col=COAL, border_w=2)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 34)
    c.drawCentredString(s3_x + 30 + ((lx + full_w - 40) - (s3_x + 30)) / 2, amb_y + 68, "NO APPROVAL = NO CODE")
    c.setFont("PlexMonoBold", 14)
    c.drawCentredString(s3_x + 30 + ((lx + full_w - 40) - (s3_x + 30)) / 2, amb_y + 30, "GATE LOCKED TO HUMANS // AGENTS CANNOT SELF-APPROVE")

    # -------------------------------------------------------------------------
    # Bottom Full-Width Mandate Bar
    # -------------------------------------------------------------------------
    draw_brutalist_plate(c, lx, 115, full_w, 115, fill_col=COAL, stroke_col=YELLOW, lw=3.5, shadow_offset=6, shadow_col=COAL_MID)
    c.setFillColor(YELLOW)
    c.rect(lx, 115, 16, 115, fill=1, stroke=0)
    c.setFont("ArchivoBlack", 40)
    c.setFillColor(BONE)
    c.drawString(lx + 42, 160, "Only an APPROVED spec authorizes product code.")
    c.setFont("PlexMonoBold", 15)
    c.setFillColor(YELLOW)
    c.drawString(lx + 42, 130, "HARD RULE P1 & P7 // IF NO APPROVED SPEC EXISTS, DRAFT ONE IN specs/ AND STOP FOR HUMAN APPROVAL.")


def draw_slide_06(c):
    """06 — A spec that can be tested (Bone background, 7-col spec blueprint + 5-col exploded lock cutaway)"""
    draw_slide_frame(c, 6, ACT_II, bg_mode="bone", kicker="WORKED EXAMPLE // PASSWORD RESET (SLIDES 06–12)")

    lx = col_x(0)
    left_w = col_span_w(7)

    # Headline
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 50)
    c.drawString(lx, 915, "A SPEC IS A TESTABLE CONTRACT.")

    # -------------------------------------------------------------------------
    # Left 7 Columns: SPEC-012 Blueprint Sheet + Rule-to-Test Trace
    # -------------------------------------------------------------------------
    spec_y = 235
    spec_h = 650
    draw_brutalist_plate(c, lx, spec_y, left_w, spec_h, fill_col=COAL, stroke_col=COAL, lw=4, shadow_offset=8, shadow_col=STEEL_DARK)

    # Blueprint top title bar
    c.setFillColor(YELLOW)
    c.rect(lx, spec_y + spec_h - 62, left_w, 62, fill=1, stroke=1)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 28)
    c.drawString(lx + 24, spec_y + spec_h - 42, "SPEC-012 / Password reset")
    draw_badge(c, lx + left_w - 220, spec_y + spec_h - 49, "STATUS: APPROVED", bg_col=COAL, fg_col=YELLOW, border_col=COAL, font="PlexMonoBold", size=13, pad_x=12, h=36)

    # Numbered Behavioral Rules R1, R2, R3
    c.setFont("PlexMonoBold", 13)
    c.setFillColor(STEEL_LIGHT)
    c.drawString(lx + 26, spec_y + spec_h - 92, "§5.2 BEHAVIORAL CONTRACT RULES (NUMBERED, DETERMINISTIC):")

    rules = [
        ("R1", "R1: 32 random bytes; store the SHA-256 token hash.", COAL_LIGHT, BONE, STEEL),
        ("R2", "R2: 30-minute TTL; expired → 410.", ORANGE, COAL, BONE),
        ("R3", "R3: Single-use; replay → 410.", COAL_LIGHT, BONE, STEEL),
    ]
    ry = spec_y + spec_h - 175
    r2_box_y = 0
    for r_id, r_text, r_bg, r_fg, r_border in rules:
        draw_brutalist_plate(c, lx + 26, ry, left_w - 52, 66, fill_col=r_bg, stroke_col=r_border, lw=3, shadow_offset=4, shadow_col=COAL_MID, rivets=False)
        c.setFont("PlexMonoBold", 20)
        c.setFillColor(r_fg)
        c.drawString(lx + 46, ry + 24, r_text)
        if r_id == "R2":
            r2_box_y = ry
        ry -= 84

    # Acceptance Criterion AC-2 Box
    ac_y = spec_y + 185
    draw_brutalist_plate(c, lx + 26, ac_y, left_w - 52, 86, fill_col=COAL_LIGHT, stroke_col=ORANGE, lw=3.5, shadow_offset=5, shadow_col=COAL_MID)
    c.setFillColor(ORANGE)
    c.rect(lx + 26, ac_y, 14, 86, fill=1, stroke=0)
    c.setFont("PlexMonoBold", 12)
    c.setFillColor(ORANGE)
    c.drawString(lx + 52, ac_y + 58, "§6 ACCEPTANCE CRITERION (GIVEN / WHEN / THEN):")
    c.setFont("PlexMonoBold", 22)
    c.setFillColor(BONE)
    c.drawString(lx + 52, ac_y + 22, "AC-2: Expired token → 410; password unchanged.")

    # Named Test Box: TEST: test_ac_2_expired_token_410
    test_y = spec_y + 32
    draw_brutalist_plate(c, lx + 26, test_y, left_w - 52, 96, fill_col=BONE, stroke_col=COAL, lw=3.5, shadow_offset=5, shadow_col=COAL_MID)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 13)
    c.drawString(lx + 48, test_y + 64, "§10 EXECUTABLE VERIFICATION TARGET (tests/auth/test_reset.py):")
    c.setFont("PlexMonoBold", 25)
    c.drawString(lx + 48, test_y + 24, "TEST: test_ac_2_expired_token_410")

    # Thick Furnace-Orange Trace Spine connecting R2 -> AC-2 -> TEST
    trace_x = lx + left_w - 75
    draw_arrow(c, trace_x, r2_box_y, trace_x, ac_y + 86, color=ORANGE, lw=6, head_len=16, head_w=10)
    draw_arrow(c, trace_x, ac_y, trace_x, test_y + 96, color=ORANGE, lw=6, head_len=16, head_w=10)

    # Bottom left callout for unresolved behavior
    draw_brutalist_plate(c, lx, 115, left_w, 92, fill_col=YELLOW, stroke_col=COAL, lw=3.5, shadow_offset=6, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 24)
    c.drawString(lx + 24, 158, "Unresolved behavior → question and ADR before build.")
    c.setFont("PlexMonoBold", 13.5)
    c.drawString(lx + 24, 130, "OQ-1: Should reset invalidate sessions? → Record the question and an ADR before build.")

    # -------------------------------------------------------------------------
    # Right 5 Columns: Exploded Technical Drawing of the Password-Reset Lock
    # -------------------------------------------------------------------------
    rx = col_x(7)
    rw = col_span_w(5)
    ry_bot = 115
    rh = 850

    draw_brutalist_plate(c, rx, ry_bot, rw, rh, fill_col=COAL_LIGHT, stroke_col=COAL, lw=4, shadow_offset=8, shadow_col=COAL)
    draw_halftone_rect(c, rx + 8, ry_bot + 8, rw - 16, rh - 16, COAL_MID, spacing=16, radius=2.0)

    # Top title banner inside cutaway drawing
    c.setFillColor(COAL)
    c.rect(rx, ry_bot + rh - 54, rw, 54, fill=1, stroke=1)
    c.setFont("PlexMonoBold", 14)
    c.setFillColor(YELLOW)
    c.drawString(rx + 20, ry_bot + rh - 34, "FIG 06.A // EXPLODED LOCK MECHANISM (SPEC-012)")

    # Center explosion axis line (dashed)
    cx = rx + rw * 0.54
    c.saveState()
    c.setStrokeColor(STEEL)
    c.setLineWidth(2)
    c.setDash(10, 6)
    c.line(cx, ry_bot + 50, cx, ry_bot + rh - 75)
    c.restoreState()

    # MODULE 1 (Top): 32-Byte Token Die + SHA-256 Storage Chamber (R1)
    m1_y = ry_bot + 620
    draw_brutalist_plate(c, rx + 40, m1_y, rw - 80, 145, fill_col=COAL, stroke_col=BONE, lw=3, shadow_offset=5, shadow_col=COAL)
    # Isometric-style machined token cylinder + hash grid
    c.setFillColor(STEEL)
    c.setStrokeColor(BONE)
    c.setLineWidth(2.5)
    c.rect(rx + 62, m1_y + 24, 130, 96, fill=1, stroke=1)
    draw_hatch_rect(c, rx + 68, m1_y + 30, 118, 84, COAL, spacing=10, lw=1.5)
    c.setFillColor(COAL)
    c.rect(rx + 80, m1_y + 52, 94, 40, fill=1, stroke=1)
    c.setFont("PlexMonoBold", 14)
    c.setFillColor(BONE)
    c.drawCentredString(rx + 127, m1_y + 66, "32 BYTES")

    draw_arrow(c, rx + 198, m1_y + 72, rx + 245, m1_y + 72, color=BONE, lw=3.5)

    # SHA-256 Chamber
    c.setFillColor(COAL_MID)
    c.setStrokeColor(YELLOW)
    c.setLineWidth(2.5)
    c.rect(rx + 250, m1_y + 24, 385, 96, fill=1, stroke=1)
    c.setFont("ArchivoBlack", 18)
    c.setFillColor(YELLOW)
    c.drawString(rx + 270, m1_y + 86, "SHA-256 STORAGE CHAMBER")
    c.setFont("PlexMono", 13)
    c.setFillColor(BONE)
    c.drawString(rx + 270, m1_y + 58, "R1: Store token_hash UNIQUE")
    c.setFillColor(STEEL_LIGHT)
    c.drawString(rx + 270, m1_y + 36, "Raw token never persisted in DB")

    # MODULE 2 (Middle — Highlighted with Molten Orange Seam to AC-2 & Test): 30-Minute Mechanical Timer (R2)
    m2_y = ry_bot + 355
    draw_brutalist_plate(c, rx + 40, m2_y, rw - 80, 210, fill_col=COAL, stroke_col=ORANGE, lw=4, shadow_offset=6, shadow_col=COAL)
    # Mechanical Clock / Escapement Gear & Dial
    clock_cx = rx + 145
    clock_cy = m2_y + 105
    draw_gear(c, clock_cx, clock_cy, 72, 58, 0, 16, fill_col=ORANGE, stroke_col=COAL, lw=2.5)
    c.setFillColor(COAL)
    c.setStrokeColor(BONE)
    c.setLineWidth(3)
    c.circle(clock_cx, clock_cy, 48, fill=1, stroke=1)
    # Clock ticks & 30-min sector in Orange
    c.setFillColor(ORANGE)
    p = c.beginPath()
    p.moveTo(clock_cx, clock_cy)
    p.arc(clock_cx - 40, clock_cy - 40, clock_cx + 40, clock_cy + 40, -90, 90)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setStrokeColor(BONE)
    c.setLineWidth(3)
    c.line(clock_cx, clock_cy, clock_cx, clock_cy + 38)
    c.line(clock_cx, clock_cy, clock_cx, clock_cy - 38)
    c.setFillColor(COAL)
    c.circle(clock_cx, clock_cy, 6, fill=1, stroke=0)

    c.setFont("ArchivoBlack", 20)
    c.setFillColor(ORANGE)
    c.drawString(rx + 245, m2_y + 155, "30-MINUTE TTL TIMER (R2)")
    c.setFont("PlexMonoBold", 15)
    c.setFillColor(BONE)
    c.drawString(rx + 245, m2_y + 120, "IF now() > expires_at:")
    draw_badge(c, rx + 245, m2_y + 72, "RETURN HTTP 410 GONE", bg_col=ORANGE, fg_col=COAL, border_col=BONE, font="PlexMonoBold", size=14, pad_x=12, h=34)
    c.setFont("PlexMono", 13)
    c.setFillColor(STEEL_LIGHT)
    c.drawString(rx + 245, m2_y + 38, "ASSERT: user.password_hash UNCHANGED")

    # MODULE 3 (Bottom): Single-Use Ratchet Latch (R3)
    m3_y = ry_bot + 145
    draw_brutalist_plate(c, rx + 40, m3_y, rw - 80, 155, fill_col=COAL, stroke_col=BONE, lw=3, shadow_offset=5, shadow_col=COAL)
    # One-way pawl & latch diagram
    draw_gear(c, rx + 135, m3_y + 78, 46, 34, 12, 10, fill_col=STEEL, stroke_col=COAL, lw=2)
    c.setFillColor(YELLOW)
    c.setStrokeColor(COAL)
    c.setLineWidth(2.5)
    c.rect(rx + 175, m3_y + 88, 48, 18, fill=1, stroke=1)
    c.setFont("ArchivoBlack", 18)
    c.setFillColor(BONE)
    c.drawString(rx + 245, m3_y + 108, "ONE-USE RATCHET LATCH (R3)")
    c.setFont("PlexMono", 13.5)
    c.setFillColor(STEEL_LIGHT)
    c.drawString(rx + 245, m3_y + 76, "used_at != NULL → REPLAY BLOCKED")
    c.setFillColor(ORANGE)
    c.setFont("PlexMonoBold", 14)
    c.drawString(rx + 245, m3_y + 44, "SECOND CONFIRM → HTTP 410 GONE")

    # Rule-to-test path on the cutaway, paired with the larger R2 → AC-2 → named-test trace
    # on the left blueprint; the adjacent panels stay unobstructed and fully readable.
    draw_brutalist_plate(c, rx + 40, ry_bot + 28, rw - 80, 86, fill_col=ORANGE, stroke_col=COAL, lw=3.5, shadow_offset=4, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 18)
    c.drawString(rx + 60, ry_bot + 76, "RULE BECOMES EXECUTABLE TEST")
    c.setFont("PlexMonoBold", 13.5)
    c.drawString(rx + 60, ry_bot + 46, "R2 (30m Timer) → AC-2 → test_ac_2_expired_token_410")


def draw_slide_07(c):
    """07 — Human-controlled status (Coal background, 6-state switchboard + yellow human locks + immutable ADR shelf)"""
    draw_slide_frame(c, 7, ACT_II, bg_mode="coal", kicker="GOVERNANCE // LIFECYCLE STATE MACHINE")

    lx = col_x(0)
    full_w = col_span_w(12)

    # Headline
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 54)
    c.drawString(lx, 915, "STATUS IS THE CONTROL PLANE.")

    # The six labeled switch positions below present the complete lifecycle in order.

    # -------------------------------------------------------------------------
    # Upper Section: Six-Position Industrial Switchboard (y: 440..875)
    # -------------------------------------------------------------------------
    sb_y = 445
    sb_h = 430
    draw_brutalist_plate(c, lx, sb_y, full_w, sb_h, fill_col=COAL_LIGHT, stroke_col=STEEL, lw=3.5, shadow_offset=8, shadow_col=COAL_MID)
    draw_halftone_rect(c, lx + 8, sb_y + 8, full_w - 16, sb_h - 16, COAL_MID, spacing=18, radius=2.0)

    # Top Bus: HUMAN AUTHORITY BUS (Hazard Yellow)
    bus_x = lx + 36
    bus_w = full_w - 72
    draw_brutalist_plate(c, bus_x, sb_y + sb_h - 76, bus_w, 52, fill_col=YELLOW, stroke_col=COAL, lw=3, shadow_offset=4, shadow_col=COAL)
    draw_hazard_band(c, bus_x, sb_y + sb_h - 36, bus_w, 12, stripe_w=16, bg_col=YELLOW, fg_col=COAL, border_w=0)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 18)
    c.drawString(bus_x + 20, sb_y + sb_h - 62, "HUMAN: REVIEW → APPROVED; IMPLEMENTED → VERIFIED")
    c.setFont("PlexMonoBold", 13)
    c.drawRightString(bus_x + bus_w - 20, sb_y + sb_h - 60, "PHYSICAL KEY LOCKS // HUMAN AUTHORITY ONLY")

    # Six Switchboard Bays
    states = [
        ("01", "DRAFT", "Spec authored", STEEL, BONE),
        ("02", "REVIEW", "Ready for review", ORANGE, COAL),
        ("03", "APPROVED", "Contract locked", YELLOW, COAL),
        ("04", "IMPLEMENTING", "Active session", STEEL, BONE),
        ("05", "IMPLEMENTED", "PR + checks green", ORANGE, COAL),
        ("06", "VERIFIED", "Checked on deploy", GREEN, COAL),
    ]
    bay_w = 225
    gap_w = (bus_w - 6 * bay_w) / 5.0  # ~62pt gap between bays where transition locks live
    bay_y = sb_y + 108
    bay_h = 210

    for i, (s_num, s_name, s_desc, s_col, s_fg) in enumerate(states):
        bx = bus_x + i * (bay_w + gap_w)
        is_human_target = s_name in ("APPROVED", "VERIFIED")
        border_c = YELLOW if s_name == "APPROVED" else (GREEN if s_name == "VERIFIED" else BONE)
        draw_brutalist_plate(c, bx, bay_y, bay_w, bay_h, fill_col=COAL, stroke_col=border_c, lw=3.5 if is_human_target else 2.5, shadow_offset=5, shadow_col=COAL)

        # Top status nameplate inside bay
        c.setFillColor(s_col)
        c.rect(bx + 10, bay_y + bay_h - 52, bay_w - 20, 40, fill=1, stroke=1)
        c.setFillColor(s_fg)
        c.setFont("ArchivoBlack", 18 if len(s_name) < 11 else 15.5)
        c.drawCentredString(bx + bay_w / 2, bay_y + bay_h - 38, s_name)

        # Industrial Knife Switch / Rotary Breaker inside bay
        sw_cx = bx + bay_w / 2
        sw_cy = bay_y + 92
        c.setFillColor(COAL_MID)
        c.setStrokeColor(STEEL)
        c.setLineWidth(2.5)
        c.rect(sw_cx - 42, sw_cy - 38, 84, 76, fill=1, stroke=1)
        # Switch throw handle
        c.setFillColor(s_col)
        c.setStrokeColor(COAL)
        c.rect(sw_cx - 14, sw_cy - 10, 28, 38, fill=1, stroke=1)
        c.setFont("PlexMonoBold", 12)
        c.setFillColor(STEEL_LIGHT)
        c.drawString(bx + 14, bay_y + 18, f"POS {s_num} // {s_desc}")

        # Transition arrows & locks between bays
        if i < 5:
            tx1 = bx + bay_w
            tx2 = tx1 + gap_w
            t_cx = (tx1 + tx2) / 2.0
            t_cy = bay_y + bay_h / 2.0

            if i in (1, 4):
                # HUMAN-CONTROLLED TRANSITIONS: REVIEW -> APPROVED (i=1) and IMPLEMENTED -> VERIFIED (i=4)
                draw_arrow(c, tx1 + 2, t_cy, tx2 - 2, t_cy, color=YELLOW, lw=5, head_len=14, head_w=9)
                # Vertical drop from HUMAN BUS to the physical yellow padlock
                c.setStrokeColor(YELLOW)
                c.setLineWidth(3.5)
                c.line(t_cx, sb_y + sb_h - 76, t_cx, t_cy + 25)
                draw_padlock(c, t_cx, t_cy + 4, w=44, h=36, body_col=YELLOW, stroke_col=COAL, label="G")
            else:
                # AGENT TRANSITIONS: DRAFT -> REVIEW (i=0), APPROVED -> IMPLEMENTING (i=2), IMPLEMENTING -> IMPLEMENTED (i=3)
                a_col = ORANGE if i in (0, 3) else STEEL_LIGHT
                draw_arrow(c, tx1 + 2, t_cy, tx2 - 2, t_cy, color=a_col, lw=4, head_len=12, head_w=8)
                if i in (0, 3):
                    # Downward drop to AGENT BUS
                    c.setStrokeColor(ORANGE)
                    c.setLineWidth(3)
                    c.line(t_cx, t_cy - 10, t_cx, sb_y + 72)
                    draw_badge(c, t_cx - 28, t_cy - 14, "AGENT", bg_col=ORANGE, fg_col=COAL, border_col=COAL, size=10, pad_x=6, h=20)

    # Bottom Bus inside Switchboard: AGENT TRANSITION BUS
    draw_brutalist_plate(c, bus_x, sb_y + 20, bus_w, 52, fill_col=COAL, stroke_col=ORANGE, lw=3, shadow_offset=4, shadow_col=COAL)
    c.setFillColor(ORANGE)
    c.rect(bus_x, sb_y + 20, 14, 52, fill=1, stroke=0)
    c.setFont("ArchivoBlack", 18)
    c.setFillColor(BONE)
    c.drawString(bus_x + 28, sb_y + 38, "AGENT: DRAFT → REVIEW; IMPLEMENTING → IMPLEMENTED")
    c.setFont("PlexMonoBold", 13)
    c.setFillColor(ORANGE)
    c.drawRightString(bus_x + bus_w - 20, sb_y + 40, "PROPOSES TRANSITIONS // CANNOT UNLOCK YELLOW GATES")

    # -------------------------------------------------------------------------
    # Lower Section: Immutable ADR Shelf (y: 115..415)
    # -------------------------------------------------------------------------
    adr_y = 115
    adr_h = 295
    draw_brutalist_plate(c, lx, adr_y, full_w, adr_h, fill_col=COAL_LIGHT, stroke_col=BONE, lw=3.5, shadow_offset=8, shadow_col=COAL_MID)

    # Left Copy Block on ADR Discipline (6 columns)
    c.setFillColor(YELLOW)
    c.rect(lx, adr_y, 14, adr_h, fill=1, stroke=0)
    c.setFont("PlexMonoBold", 14)
    c.setFillColor(YELLOW)
    c.drawString(lx + 34, adr_y + adr_h - 38, "IMMUTABLE DECISION RECORDS // ADR LIFECYCLE: PROPOSED → ACCEPTED → SUPERSEDED")

    c.setFont("ArchivoBlack", 29)
    c.setFillColor(BONE)
    c.drawString(lx + 34, adr_y + adr_h - 92, "Changed decision? Propose a new ADR")
    c.drawString(lx + 34, adr_y + adr_h - 130, "or versioned DRAFT.")

    draw_brutalist_plate(c, lx + 34, adr_y + 28, 760, 102, fill_col=COAL, stroke_col=ORANGE, lw=3, shadow_offset=4, shadow_col=COAL)
    c.setFont("ArchivoBlack", 23)
    c.setFillColor(ORANGE)
    c.drawString(lx + 54, adr_y + 82, "Do not silently rewrite approved behavior")
    c.drawString(lx + 54, adr_y + 48, "or old ADRs.")

    # Right Visual Shelf: Three Riveted Steel ADR Plates with Supersedes Pointer
    sx = lx + 835
    sw = full_w - 835 - 30
    sy = adr_y + 28
    sh = 215
    draw_brutalist_plate(c, sx, sy, sw, sh, fill_col=COAL, stroke_col=STEEL, lw=2.5, shadow_offset=4, shadow_col=COAL)

    plates = [
        ("ADR-0001", "Use Postgres", "SUPERSEDED", STEEL_DARK, BONE),
        ("ADR-0002", "SQLite for MVP", "ACCEPTED", STEEL, COAL),
        ("ADR-0008", "Invalidate sessions", "PROPOSED", YELLOW, COAL),
    ]
    pw = 245
    pgap = 32
    for idx, (a_id, a_title, a_stat, a_col, a_fg) in enumerate(plates):
        px = sx + 28 + idx * (pw + pgap)
        py = sy + 48
        ph = 142
        draw_brutalist_plate(c, px, py, pw, ph, fill_col=COAL_LIGHT, stroke_col=a_col if a_stat != "SUPERSEDED" else STEEL, lw=3, shadow_offset=4, shadow_col=COAL)
        c.setFont("PlexMonoBold", 18)
        c.setFillColor(BONE)
        c.drawString(px + 18, py + ph - 34, a_id)
        c.setFont("PlexSansMedium", 14)
        c.setFillColor(STEEL_LIGHT)
        c.drawString(px + 18, py + ph - 62, a_title)
        draw_badge(c, px + 18, py + 18, a_stat, bg_col=a_col, fg_col=a_fg, border_col=COAL, font="PlexMonoBold", size=12, pad_x=10, h=26)

    # Immutable Supersedes Pointer Arch from ADR-0002 back to ADR-0001
    p1_cx = sx + 28 + pw / 2
    p2_cx = sx + 28 + pw + pgap + pw / 2
    c.saveState()
    c.setStrokeColor(ORANGE)
    c.setLineWidth(3.5)
    c.line(p2_cx, sy + 48, p2_cx, sy + 20)
    c.line(p2_cx, sy + 20, p1_cx, sy + 20)
    draw_arrow(c, p1_cx, sy + 20, p1_cx, sy + 48, color=ORANGE, lw=3.5, head_len=12, head_w=8)
    c.restoreState()
    c.setFont("PlexMonoBold", 11.5)
    c.setFillColor(ORANGE)
    c.drawString(p1_cx + 18, sy + 25, "supersedes: [ADR-0001] (HISTORY PRESERVED)")
