from theme import (
    W, H, MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM,
    COAL, BONE, ORANGE, YELLOW, STEEL, GREEN,
    COAL_LIGHT, COAL_MID, STEEL_DARK, STEEL_LIGHT, BONE_DARK, BONE_MID,
    col_x, col_span_w, draw_slide_frame, draw_halftone_rect, draw_hatch_rect,
    draw_hazard_band, draw_brutalist_plate, draw_arrow, draw_gear, draw_padlock,
    draw_badge, draw_wrapped
)

ACT_III = "ACT III — THE SESSION"


def draw_slide_11(c):
    """11 — Verification is evidence (Coal background, test-first spread, blank evidence slot)."""
    draw_slide_frame(c, 11, ACT_III, bg_mode="coal", kicker="QUALITY GATE // EVIDENCE, NOT ASSERTION")

    lx = col_x(0)
    full_w = col_span_w(12)

    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 60)
    c.drawString(lx, 915, "DONE MEANS EXIT 0.")
    draw_badge(c, col_x(8) + 20, 918, "REQUIRED PROCEDURE // NO RUN CLAIMED", bg_col=COAL_LIGHT, fg_col=YELLOW,
               border_col=YELLOW, font="PlexMonoBold", size=12.5, pad_x=12, h=34)

    # Two-page graphic novel split: test-first failure -> implementation -> required pass
    split_y = 420
    spread_y = 482
    spread_h = 385
    gap = 28
    half_w = (full_w - gap) / 2
    left_x = lx
    right_x = lx + half_w + gap

    # LEFT PAGE: explicit test-first failure phase (conceptual protocol, not a real test run)
    draw_brutalist_plate(c, left_x, spread_y, half_w, spread_h, fill_col=COAL_LIGHT, stroke_col=ORANGE, lw=4, shadow_offset=8, shadow_col=COAL)
    c.setFillColor(ORANGE)
    c.rect(left_x, spread_y + spread_h - 60, half_w, 60, fill=1, stroke=1)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 28)
    c.drawString(left_x + 24, spread_y + spread_h - 41, "01 // TEST FIRST")

    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 38)
    c.drawString(left_x + 30, spread_y + 255, "FAILING TEST")
    c.setFont("PlexMonoBold", 17)
    c.setFillColor(ORANGE)
    c.drawString(left_x + 30, spread_y + 218, "AC-2 → test_ac_2_expired_token_410")

    # Blank test fixture panel: no fake terminal output, no fabricated counts
    test_x = left_x + 30
    test_y = spread_y + 72
    test_w = half_w - 60
    test_h = 116
    c.setFillColor(COAL)
    c.setStrokeColor(STEEL)
    c.setLineWidth(2)
    c.rect(test_x, test_y, test_w, test_h, fill=1, stroke=1)
    c.setStrokeColor(STEEL_DARK)
    c.setDash(6, 6)
    c.rect(test_x + 14, test_y + 14, test_w - 28, test_h - 28, fill=0, stroke=1)
    c.setDash()
    c.setFillColor(STEEL_LIGHT)
    c.setFont("PlexMonoBold", 14)
    c.drawCentredString(test_x + test_w / 2, test_y + 64, "EVIDENCE SLOT — FILL FROM ACTUAL RUN")
    c.setFont("PlexMono", 12)
    c.drawCentredString(test_x + test_w / 2, test_y + 40, "command · exit code · summary")

    # Step-down label
    c.setFont("PlexMonoBold", 12.5)
    c.setFillColor(STEEL_LIGHT)
    c.drawString(left_x + 30, spread_y + 34, "TEST TARGET ONLY — THIS DIAGRAM IS NOT A TEST RESULT.")

    # CENTRAL SEAM: AC-shaped bolt turns into code, with a one-way chronological arrow
    seam_y = spread_y + spread_h / 2
    draw_arrow(c, left_x + half_w - 12, seam_y, right_x + 12, seam_y, color=ORANGE, lw=8, head_len=24, head_w=15)
    # Bolt at seam center
    bolt_cx = lx + full_w / 2
    c.setFillColor(YELLOW)
    c.setStrokeColor(COAL)
    c.setLineWidth(2)
    bolt = c.beginPath()
    bolt.moveTo(bolt_cx - 22, seam_y + 32)
    bolt.lineTo(bolt_cx - 8, seam_y + 10)
    bolt.lineTo(bolt_cx - 16, seam_y - 10)
    bolt.lineTo(bolt_cx + 15, seam_y - 36)
    bolt.lineTo(bolt_cx + 7, seam_y - 5)
    bolt.lineTo(bolt_cx + 20, seam_y + 8)
    bolt.lineTo(bolt_cx - 4, seam_y + 36)
    bolt.close()
    c.drawPath(bolt, fill=1, stroke=1)

    # RIGHT PAGE: implementation -> required passing test and check chain
    draw_brutalist_plate(c, right_x, spread_y, half_w, spread_h, fill_col=COAL_LIGHT, stroke_col=STEEL, lw=4, shadow_offset=8, shadow_col=COAL)
    c.setFillColor(STEEL)
    c.rect(right_x, spread_y + spread_h - 60, half_w, 60, fill=1, stroke=1)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 28)
    c.drawString(right_x + 24, spread_y + spread_h - 41, "02 // IMPLEMENT + VERIFY")

    # Required sequence
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 30)
    c.drawString(right_x + 30, spread_y + 274, "IMPLEMENT")
    c.setFillColor(STEEL_LIGHT)
    c.setFont("PlexMonoBold", 15)
    c.drawString(right_x + 30, spread_y + 240, "FAILING TEST → IMPLEMENT → PASSING TEST")

    # Passing test target is clearly a procedure, not a displayed result
    c.setFillColor(GREEN)
    c.setStrokeColor(BONE)
    c.setLineWidth(2)
    c.rect(right_x + 30, spread_y + 183, half_w - 60, 40, fill=1, stroke=1)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 14)
    c.drawCentredString(right_x + half_w / 2, spread_y + 197, "REQUIRED PASS — VERIFY BY RUNNING THE TEST")

    # Blank summary/evidence slot
    out_y = spread_y + 72
    c.setFillColor(COAL)
    c.setStrokeColor(STEEL)
    c.setLineWidth(2)
    c.rect(right_x + 30, out_y, half_w - 60, 84, fill=1, stroke=1)
    c.setFillColor(STEEL_LIGHT)
    c.setFont("PlexMonoBold", 13)
    c.drawCentredString(right_x + half_w / 2, out_y + 50, "TARGETED RUN · FULL SUITE · LINT · TYPECHECK · SECRET SCAN")
    c.setFont("PlexMono", 12)
    c.drawCentredString(right_x + half_w / 2, out_y + 28, "Actual command + exit code + summary → PR")

    c.setFont("PlexMonoBold", 12)
    c.setFillColor(STEEL_LIGHT)
    c.drawString(right_x + 30, spread_y + 34, "NO FAKE TERMINAL LINES · NO INVENTED PASS COUNTS.")

    # Bottom evidence statement
    c.setFillColor(ORANGE)
    c.setFont("ArchivoBlack", 28)
    c.drawString(lx, 360, "Paste the actual command, exit code, and summary into the PR.")
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 42)
    c.drawRightString(lx + full_w, 264, "“Looks good” is not evidence.")
    c.setStrokeColor(ORANGE)
    c.setLineWidth(5)
    c.line(lx, 238, lx + full_w, 238)


def draw_slide_12(c):
    """12 — Bidirectional traceability (Bone background, closed double-arrow transit map)."""
    draw_slide_frame(c, 12, ACT_III, bg_mode="bone", kicker="WORKED EXAMPLE // AUDITABLE TRACE CIRCUIT")

    lx = col_x(0)
    full_w = col_span_w(12)

    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 56)
    c.drawString(lx, 915, "EVERY LINK WALKS BOTH WAYS.")

    # Primary closed circuit: SPEC -> PLAN -> TASK -> BRANCH -> COMMIT -> TEST -> SPEC
    nodes = [
        ("SPEC", "SPEC-012", "Password reset", YELLOW),
        ("PLAN", "PLAN-004", "ordered work", STEEL),
        ("TASK", "T-032", "AC-2 · AC-3", ORANGE),
        ("BRANCH", "feat/T-032-", "reset-confirm", STEEL),
        ("COMMIT", "COMMIT", "handoff included", COAL_LIGHT),
        ("TEST", "test_ac_2_", "expired_token_410", STEEL),
    ]
    box_y = 550
    box_h = 195
    box_w = 240
    gap = (full_w - 6 * box_w) / 5
    centers = []

    for i, (kind, ident, sub, accent) in enumerate(nodes):
        x = lx + i * (box_w + gap)
        centers.append(x + box_w / 2)
        # Steel station shell
        draw_brutalist_plate(c, x, box_y, box_w, box_h, fill_col=COAL, stroke_col=COAL, lw=3.5, shadow_offset=7, shadow_col=STEEL_DARK)
        c.setFillColor(accent)
        c.rect(x, box_y + box_h - 44, box_w, 44, fill=1, stroke=0)
        c.setFillColor(COAL if accent in (YELLOW, ORANGE, GREEN, STEEL) else BONE)
        c.setFont("PlexMonoBold", 15)
        c.drawCentredString(x + box_w / 2, box_y + box_h - 29, kind)
        c.setFont("ArchivoBlack", 24 if len(ident) < 15 else 17)
        c.setFillColor(BONE)
        c.drawCentredString(x + box_w / 2, box_y + 91, ident)
        c.setFont("PlexMono", 13 if len(sub) < 20 else 11.5)
        c.setFillColor(STEEL_LIGHT)
        c.drawCentredString(x + box_w / 2, box_y + 57, sub)
        # Station side rails / rivets
        c.setFillColor(accent)
        c.rect(x + 12, box_y + 12, 5, box_h - 68, fill=1, stroke=0)
        c.rect(x + box_w - 17, box_y + 12, 5, box_h - 68, fill=1, stroke=0)

    # Bidirectional heavy links between every station
    link_y = box_y + box_h / 2
    for i in range(5):
        draw_arrow(c, centers[i] + box_w / 2 + 6, link_y, centers[i + 1] - box_w / 2 - 6, link_y,
                   color=ORANGE, lw=4, head_len=12, head_w=7, bidirectional=True)

    # Return line from TEST back to the originating SPEC station — no crossings
    return_y = box_y - 64
    c.setStrokeColor(ORANGE)
    c.setLineWidth(5)
    c.line(centers[0], box_y, centers[0], return_y)
    c.line(centers[0], return_y, centers[5], return_y)
    c.line(centers[5], box_y, centers[5], return_y)
    draw_arrow(c, centers[5], return_y, centers[0], return_y, color=ORANGE, lw=5, head_len=17, head_w=10)
    c.setFont("PlexMonoBold", 13)
    c.setFillColor(ORANGE)
    c.drawCentredString((centers[0] + centers[5]) / 2, return_y - 26, "TEST ↔ SPEC // TRACEABLE IN BOTH DIRECTIONS")

    # Lower source-file line leading back to spec ID
    src_y = 272
    draw_brutalist_plate(c, lx + 35, src_y, 720, 92, fill_col=COAL_LIGHT, stroke_col=STEEL, lw=3, shadow_offset=5, shadow_col=COAL)
    c.setFont("PlexMonoBold", 19)
    c.setFillColor(BONE)
    c.drawCentredString(lx + 395, src_y + 54, "src/auth/reset.py")
    c.setFillColor(YELLOW)
    c.setFont("PlexMonoBold", 15)
    c.drawCentredString(lx + 395, src_y + 25, "# SPEC-012")
    draw_arrow(c, lx + 755, src_y + 46, lx + 950, src_y + 46, color=YELLOW, lw=4)
    draw_brutalist_plate(c, lx + 950, src_y, 465, 92, fill_col=YELLOW, stroke_col=COAL, lw=3, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 18)
    c.drawCentredString(lx + 1182, src_y + 53, "SPEC-012")
    c.setFont("PlexMono", 13)
    c.drawCentredString(lx + 1182, src_y + 25, "source comment resolves to contract")

    # TRACE map plate
    draw_brutalist_plate(c, lx + 1430, src_y, 302, 92, fill_col=COAL, stroke_col=ORANGE, lw=3, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 16)
    c.drawCentredString(lx + 1581, src_y + 54, ".forge/TRACE.md")
    c.setFillColor(ORANGE)
    c.setFont("PlexMonoBold", 12.5)
    c.drawCentredString(lx + 1581, src_y + 26, "maintains the audit map")

    # Bottom thesis repeats the exact end-to-end identifiers on two readable lines.
    c.setFont("PlexMonoBold", 15)
    c.setFillColor(COAL)
    c.drawString(lx + 35, 169, "SPEC-012 ↔ PLAN-004 ↔ T-032 ↔ feat/T-032-reset-confirm")
    c.drawString(lx + 35, 143, "↔ COMMIT ↔ test_ac_2_expired_token_410 ↔ SPEC-012")
