from theme import (
    W, H, MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM,
    COAL, BONE, ORANGE, YELLOW, STEEL, GREEN,
    COAL_LIGHT, COAL_MID, STEEL_DARK, STEEL_LIGHT, BONE_DARK, BONE_MID,
    col_x, col_span_w, draw_slide_frame, draw_halftone_rect, draw_hatch_rect,
    draw_hazard_band, draw_brutalist_plate, draw_arrow, draw_gear, draw_padlock,
    draw_badge, draw_wrapped
)

ACT_III = "ACT III — THE SESSION"


def draw_slide_08(c):
    """08 — One entry point reboots the agent (Bone, master switch feeds seven boot conduits)."""
    draw_slide_frame(c, 8, ACT_III, bg_mode="bone", kicker="SESSION START // ZERO-CONTEXT BOOTSTRAP")

    lx = col_x(0)
    full_w = col_span_w(12)

    # Headline / thesis
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 62)
    c.drawString(lx, 915, "ONE FILE REBOOTS THE AGENT.")
    c.setFillColor(ORANGE)
    c.rect(lx, 893, 264, 7, fill=1, stroke=0)

    # Master Switch Cabinet (AGENTS.md)
    sw_x = lx + 5
    sw_y = 274
    sw_w = 385
    sw_h = 560
    draw_brutalist_plate(c, sw_x, sw_y, sw_w, sw_h, fill_col=COAL, stroke_col=COAL, lw=4, shadow_offset=9, shadow_col=STEEL_DARK)
    draw_hazard_band(c, sw_x, sw_y + sw_h - 20, sw_w, 20, stripe_w=17, bg_col=YELLOW, fg_col=COAL, border_w=2)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 15)
    c.drawString(sw_x + 24, sw_y + sw_h - 58, "PRIMARY BOOT CIRCUIT")

    # Master switch housing
    c.setFillColor(COAL_LIGHT)
    c.setStrokeColor(STEEL)
    c.setLineWidth(3)
    c.rect(sw_x + 45, sw_y + 190, sw_w - 90, 265, fill=1, stroke=1)
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 33)
    c.drawCentredString(sw_x + sw_w / 2, sw_y + 410, "AGENTS.md")
    c.setFillColor(STEEL_LIGHT)
    c.setFont("PlexMono", 13)
    c.drawCentredString(sw_x + sw_w / 2, sw_y + 377, "IDENTITY · AUTHORITY · PROTOCOL")

    # Heavy master knife-switch lever
    c.setStrokeColor(YELLOW)
    c.setLineWidth(13)
    c.line(sw_x + 106, sw_y + 285, sw_x + 230, sw_y + 340)
    c.setFillColor(YELLOW)
    c.setStrokeColor(COAL)
    c.setLineWidth(3)
    c.circle(sw_x + 105, sw_y + 284, 24, fill=1, stroke=1)
    c.circle(sw_x + 235, sw_y + 342, 18, fill=1, stroke=1)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 12)
    c.drawCentredString(sw_x + sw_w / 2, sw_y + 220, "READ FIRST · THEN FOLLOW THE SEQUENCE")

    # Seven conduit ports on right edge of switch cabinet
    for i in range(7):
        py = sw_y + 130 + i * 43
        c.setFillColor(ORANGE if i in (0, 5, 6) else STEEL)
        c.setStrokeColor(COAL)
        c.setLineWidth(2)
        c.circle(sw_x + sw_w, py, 9, fill=1, stroke=1)

    # Seven rungs in a clean industrial boot ladder
    ladder_x = sw_x + sw_w + 65
    ladder_w = full_w - (ladder_x - lx) - 6
    row_top = 790
    row_h = 66
    row_gap = 73
    boot_steps = [
        ("01", "STATE.md", "Where are we?", ORANGE),
        ("02", "Last 3 LEDGER.md entries", "What just happened?", STEEL),
        ("03", "CONVENTIONS.md + GLOSSARY.md", "How do we think and speak?", STEEL),
        ("04", "specs/INDEX.md + assigned spec", "What is the contract?", YELLOW),
        ("05", "tasks/DOING/ → tasks/OPEN/", "Resume first; then pick up.", STEEL),
        ("06", "make bootstrap && make test", "Confirm the baseline; report red before building.", ORANGE),
        ("07", "Print a five-line Session Plan", "Commit to intent before work.", YELLOW),
    ]

    for i, (num, main, note, accent) in enumerate(boot_steps):
        y = row_top - i * row_gap
        # Conduit from source switch to rung plate (rightward, with an elbow for clarity)
        source_y = sw_y + 130 + i * 43
        rung_cy = y + row_h / 2
        c.setStrokeColor(accent)
        c.setLineWidth(3)
        c.line(sw_x + sw_w + 9, source_y, ladder_x - 25, source_y)
        c.line(ladder_x - 25, source_y, ladder_x - 25, rung_cy)
        draw_arrow(c, ladder_x - 25, rung_cy, ladder_x, rung_cy, color=accent, lw=3.2, head_len=11, head_w=7)

        draw_brutalist_plate(c, ladder_x, y, ladder_w, row_h, fill_col=BONE if i % 2 == 0 else BONE_MID,
                             stroke_col=COAL, lw=2.7, shadow_offset=4, shadow_col=COAL)
        # Number stamp
        c.setFillColor(accent)
        c.rect(ladder_x, y, 76, row_h, fill=1, stroke=0)
        c.setFillColor(COAL)
        c.setFont("ArchivoBlack", 25)
        c.drawCentredString(ladder_x + 38, y + 22, num)
        # Main step and explanatory note
        c.setFillColor(COAL)
        c.setFont("PlexMonoBold", 18.5 if len(main) < 29 else 16.5)
        c.drawString(ladder_x + 100, y + 36, main)
        c.setFillColor(STEEL_DARK)
        c.setFont("PlexSansMedium", 15)
        c.drawString(ladder_x + 100, y + 12, note)
        # End-of-conduit relay lamp (not an outcome claim)
        c.setFillColor(accent)
        c.circle(ladder_x + ladder_w - 22, y + row_h / 2, 7, fill=1, stroke=0)

    # Bottom commandment bar
    draw_brutalist_plate(c, lx, 115, full_w, 100, fill_col=COAL, stroke_col=ORANGE, lw=3.5, shadow_offset=6, shadow_col=COAL)
    c.setFillColor(ORANGE)
    c.rect(lx, 115, 14, 100, fill=1, stroke=0)
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 34)
    c.drawString(lx + 42, 153, "START WITH REPO STATE, NOT CHAT MEMORY.")
    c.setFillColor(YELLOW)
    c.setFont("PlexMonoBold", 14)
    c.drawRightString(lx + full_w - 24, 126, "NO BUILD UNTIL BASELINE IS UNDERSTOOD")


def draw_slide_09(c):
    """09 — From plan to mergeable task (Coal, reels feed one punched-metal T-032 work order)."""
    draw_slide_frame(c, 9, ACT_III, bg_mode="coal", kicker="WORK ORDER // ONE TASK, ONE MERGEABLE UNIT")

    lx = col_x(0)
    full_w = col_span_w(12)

    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 52)
    c.drawString(lx, 915, "PLANS TURN SPECS INTO WORK ORDERS.")

    # Three-stage title rail: SPEC → PLAN → TASK
    track_y = 807
    node_w = 405
    node_h = 74
    nodes = [
        (lx + 40, "SPEC-012", "approved contract", YELLOW),
        (lx + 40 + 470, "PLAN-004", "ordered work", STEEL),
        (lx + 40 + 940, "T-032", "single work order", ORANGE),
    ]
    for i, (nx, title, sub, accent) in enumerate(nodes):
        draw_brutalist_plate(c, nx, track_y, node_w, node_h, fill_col=COAL_LIGHT, stroke_col=accent, lw=3, shadow_offset=5, shadow_col=COAL_MID)
        c.setFillColor(accent)
        c.rect(nx, track_y, 12, node_h, fill=1, stroke=0)
        c.setFont("ArchivoBlack", 28)
        c.setFillColor(BONE)
        c.drawString(nx + 28, track_y + 39, title)
        c.setFont("PlexMono", 13)
        c.setFillColor(STEEL_LIGHT)
        c.drawString(nx + 28, track_y + 15, sub)
        if i < 2:
            draw_arrow(c, nx + node_w, track_y + node_h / 2, nodes[i + 1][0], track_y + node_h / 2,
                       color=ORANGE, lw=5, head_len=18, head_w=11)

    # Plan reel on left, with metallic rollers and a single strip feeding the task card
    reel_cx = lx + 180
    reel_cy = 480
    draw_gear(c, reel_cx, reel_cy, 145, 118, 25, 12, fill_col=STEEL_DARK, stroke_col=BONE, lw=3)
    draw_gear(c, reel_cx, reel_cy, 74, 48, 15, 8, fill_col=COAL, stroke_col=YELLOW, lw=2.5, phase=0.1)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 14)
    c.drawCentredString(reel_cx, reel_cy + 8, "PLAN")
    c.drawCentredString(reel_cx, reel_cy - 16, "REEL")
    c.setStrokeColor(STEEL)
    c.setLineWidth(7)
    c.line(reel_cx + 145, reel_cy, lx + 505, reel_cy)
    # Reel paper edge
    c.setStrokeColor(YELLOW)
    c.setLineWidth(3)
    c.line(reel_cx + 75, reel_cy + 95, lx + 520, reel_cy + 95)
    c.line(lx + 520, reel_cy + 95, lx + 520, reel_cy + 15)
    draw_arrow(c, lx + 505, reel_cy, lx + 610, reel_cy, color=ORANGE, lw=6)

    # One giant punched-metal T-032 work order card
    card_x = lx + 565
    card_y = 265
    card_w = full_w - 600
    card_h = 440
    draw_brutalist_plate(c, card_x, card_y, card_w, card_h, fill_col=BONE, stroke_col=COAL, lw=5, shadow_offset=11, shadow_col=COAL_MID)
    draw_hazard_band(c, card_x, card_y + card_h - 18, card_w, 18, stripe_w=18, bg_col=YELLOW, fg_col=COAL, border_w=2)

    # Punch holes along left edge
    for i in range(6):
        c.setFillColor(COAL)
        c.circle(card_x + 26, card_y + 55 + i * 60, 7, fill=1, stroke=0)

    # Header stamps
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 15)
    c.drawString(card_x + 58, card_y + card_h - 58, "WORK ORDER // AUTHORIZED FROM PLAN-004")
    c.setFont("ArchivoBlack", 48)
    c.drawString(card_x + 58, card_y + card_h - 126, "T-032")
    c.setFillColor(ORANGE)
    c.setFont("ArchivoBlack", 27)
    c.drawString(card_x + 250, card_y + card_h - 117, "Reset confirm expiry and single-use")

    # Distinct slots, two-column task card
    slot_top = card_y + card_h - 166
    left_col_x = card_x + 60
    right_col_x = card_x + 790
    # AC slot
    c.setFillColor(BONE_DARK)
    c.setStrokeColor(COAL)
    c.setLineWidth(2)
    c.rect(left_col_x, slot_top - 84, 680, 78, fill=1, stroke=1)
    c.setFillColor(YELLOW)
    c.rect(left_col_x, slot_top - 12, 680, 6, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 13)
    c.drawString(left_col_x + 16, slot_top - 34, "ACCEPTANCE CRITERIA")
    c.setFont("PlexMonoBold", 21)
    c.drawString(left_col_x + 16, slot_top - 64, "AC-2 · AC-3")

    # Branch slot
    c.setFillColor(BONE_DARK)
    c.setStrokeColor(COAL)
    c.rect(right_col_x, slot_top - 84, card_w - 880, 78, fill=1, stroke=1)
    c.setFillColor(ORANGE)
    c.rect(right_col_x, slot_top - 12, card_w - 880, 6, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 13)
    c.drawString(right_col_x + 16, slot_top - 34, "BRANCH")
    c.setFont("PlexMonoBold", 13.5)
    c.drawString(right_col_x + 16, slot_top - 64, "feat/T-032-reset-confirm")

    # Verification full width command slot
    v_y = slot_top - 202
    c.setFillColor(COAL)
    c.setStrokeColor(COAL)
    c.rect(left_col_x, v_y, card_w - 120, 89, fill=1, stroke=1)
    c.setFillColor(STEEL)
    c.rect(left_col_x, v_y + 72, card_w - 120, 17, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 12)
    c.drawString(left_col_x + 14, v_y + 75, "VERIFICATION — RUN; REPORT ACTUAL RESULT")
    c.setFont("PlexMonoBold", 16.5)
    c.setFillColor(BONE)
    c.drawString(left_col_x + 14, v_y + 34, 'pytest tests/auth/test_reset.py -k "ac_2 or ac_3" -v')

    # Scope exclusions
    ex_y = card_y + 31
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 13)
    c.drawString(left_col_x, ex_y + 28, "OUT OF SCOPE")
    c.setFont("PlexMonoBold", 19)
    c.setFillColor(ORANGE)
    c.drawString(left_col_x, ex_y, "Rate limiting (T-033)")
    # One mergeable output at card end
    c.setFillColor(COAL)
    c.setStrokeColor(ORANGE)
    c.setLineWidth(3)
    c.circle(card_x + card_w - 72, card_y + 62, 38, fill=0, stroke=1)
    c.setFillColor(ORANGE)
    c.setFont("PlexMonoBold", 10.5)
    c.drawCentredString(card_x + card_w - 72, card_y + 59, "1 PR")

    # Bottom principle bar
    draw_brutalist_plate(c, lx, 115, full_w, 98, fill_col=ORANGE, stroke_col=COAL, lw=3.5, shadow_offset=6, shadow_col=COAL_MID)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 42)
    c.drawCentredString(lx + full_w / 2, 150, "One task = one mergeable unit.")


def draw_slide_10(c):
    """10 — One session, seven moves (Bone, central steel ratchet, 7 sequential actions)."""
    draw_slide_frame(c, 10, ACT_III, bg_mode="bone", kicker="SESSION PROTOCOL // ONE TURN OF THE CRANK")

    lx = col_x(0)
    full_w = col_span_w(12)

    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 58)
    c.drawString(lx, 915, "ONE SESSION. SEVEN MOVES.")

    # Ratchet spine assembly, one continuous toothed steel machine
    machine_x = lx + 50
    machine_y = 355
    machine_w = full_w - 100
    machine_h = 395
    draw_brutalist_plate(c, machine_x, machine_y, machine_w, machine_h, fill_col=COAL_LIGHT, stroke_col=COAL, lw=4, shadow_offset=10, shadow_col=STEEL_DARK)
    draw_hatch_rect(c, machine_x + 8, machine_y + 8, machine_w - 16, machine_h - 16, COAL_MID, spacing=18, lw=1.2)

    # Seven interlocking gear stations along the central ratchet axis
    labels = [
        ("01", "BOOTSTRAP", "AGENTS.md → baseline", STEEL_DARK),
        ("02", "PLAN", "task + scope", STEEL),
        ("03", "BUILD", "failing AC test → implementation", ORANGE),
        ("04", "VERIFY", "required checks", GREEN),
        ("05", "DOCUMENT", "trace + task status", STEEL),
        ("06", "HANDOFF", "STATE + LEDGER · final commit", YELLOW),
        ("07", "PUSH", "feature branch → PR", ORANGE),
    ]
    gear_r = 62
    left_center = machine_x + 130
    spacing = (machine_w - 260) / 6
    gear_cy = machine_y + 183

    for i, (num, title, sub, accent) in enumerate(labels):
        cx = left_center + i * spacing
        # Drawing geometry is steel; evidence green appears only on required passing-check position as a target.
        gear_fill = STEEL_DARK if accent not in (GREEN, YELLOW, ORANGE) else (STEEL if accent == GREEN else accent)
        draw_gear(c, cx, gear_cy, gear_r, gear_r - 15, 19, 11, fill_col=gear_fill, stroke_col=COAL, lw=3, phase=0.12 * i)
        c.setFillColor(COAL)
        c.setStrokeColor(BONE)
        c.setLineWidth(2)
        c.circle(cx, gear_cy, 38, fill=1, stroke=1)
        c.setFillColor(accent)
        c.setFont("ArchivoBlack", 22)
        c.drawCentredString(cx, gear_cy + 3, num)
        c.setFont("PlexMonoBold", 15)
        c.setFillColor(BONE)
        c.drawCentredString(cx, machine_y + 322, title)
        c.setFont("PlexMono", 11.5)
        c.setFillColor(STEEL_LIGHT)
        c.drawCentredString(cx, machine_y + 296, sub)

        # Seven ratchet teeth below each gear: each tooth is a chronological move
        tooth = c.beginPath()
        tooth.moveTo(cx - 22, machine_y + 79)
        tooth.lineTo(cx - 22, machine_y + 133)
        tooth.lineTo(cx - 9, machine_y + 150)
        tooth.lineTo(cx + 12, machine_y + 150)
        tooth.lineTo(cx + 28, machine_y + 133)
        tooth.lineTo(cx + 28, machine_y + 79)
        tooth.close()
        c.setFillColor(accent)
        c.setStrokeColor(COAL)
        c.setLineWidth(2.5)
        c.drawPath(tooth, fill=1, stroke=1)

        # Heavy sequence link
        if i < 6:
            draw_arrow(c, cx + gear_r - 4, gear_cy, cx + spacing - gear_r + 4, gear_cy, color=ORANGE if i == 5 else COAL, lw=4, head_len=13, head_w=8)

    # Workflow detail band beneath ratchet
    # BUILD-to-VERIFY evidence indicator: required state, explicitly not a recorded result
    draw_brutalist_plate(c, machine_x + 30, machine_y + 23, 610, 74, fill_col=COAL, stroke_col=ORANGE, lw=3, shadow_offset=4, shadow_col=COAL)
    c.setFillColor(ORANGE)
    c.rect(machine_x + 30, machine_y + 23, 12, 74, fill=1, stroke=0)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 14)
    c.drawString(machine_x + 58, machine_y + 65, "BUILD: FAILING AC TEST → IMPLEMENT → REQUIRED PASS")
    c.setFillColor(STEEL_LIGHT)
    c.setFont("PlexSansMedium", 13.5)
    c.drawString(machine_x + 58, machine_y + 40, "Evidence target only — no run or outcome is asserted here.")

    # Handoff cassette and mechanical interlock before PUSH
    cassette_x = machine_x + 670
    draw_brutalist_plate(c, cassette_x, machine_y + 23, 545, 74, fill_col=YELLOW, stroke_col=COAL, lw=3, shadow_offset=4, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 13.5)
    c.drawString(cassette_x + 18, machine_y + 64, "HANDOFF: STATE SNAPSHOT + APPEND-ONLY LEDGER")
    c.setFont("PlexMonoBold", 13.5)
    c.drawString(cassette_x + 18, machine_y + 38, "FINAL COMMIT AT 06 → ONLY THEN MAY 07 PUSH ENGAGE")
    # Interlock bar physically between cassette and push
    c.setStrokeColor(COAL)
    c.setLineWidth(6)
    c.line(cassette_x + 535, machine_y + 24, cassette_x + 535, machine_y + 94)
    c.setFillColor(ORANGE)
    c.circle(cassette_x + 535, machine_y + 61, 9, fill=1, stroke=0)

    # Below machine: explicit seven moves in the required chronological wording
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 18)
    c.drawString(lx + 35, 226, "01 BOOTSTRAP → 02 PLAN → 03 BUILD → 04 VERIFY")
    c.drawString(lx + 35, 197, "→ 05 DOCUMENT → 06 HANDOFF → 07 PUSH")

    # Bottom operational line
    c.setFillColor(ORANGE)
    c.setFont("ArchivoBlack", 26)
    c.drawRightString(lx + full_w - 28, 138, "PUSH: feature branch, then PR.")
