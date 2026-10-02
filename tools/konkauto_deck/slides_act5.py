from theme import (
    W, H, MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM,
    COAL, BONE, ORANGE, YELLOW, STEEL, GREEN,
    COAL_LIGHT, COAL_MID, STEEL_DARK, STEEL_LIGHT, BONE_DARK, BONE_MID,
    col_x, col_span_w, draw_slide_frame, draw_halftone_rect, draw_hatch_rect,
    draw_hazard_band, draw_brutalist_plate, draw_arrow, draw_gear, draw_padlock,
    draw_badge, draw_wrapped
)

ACT_IV = "ACT IV — THE GUARDRAILS"


def draw_slide_13(c):
    """13 — The handoff is the memory (Coal, one shift seals repo state for next session)."""
    draw_slide_frame(c, 13, ACT_IV, bg_mode="coal", kicker="SESSION END // PERSISTENT HANDOFF")

    lx = col_x(0)
    full_w = col_span_w(12)

    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 58)
    c.drawString(lx, 915, "THE HANDOFF IS THE MEMORY.")

    # Handoff conveyor floor
    floor_y = 194
    c.setFillColor(COAL_MID)
    c.setStrokeColor(STEEL_DARK)
    c.setLineWidth(2)
    c.rect(lx, floor_y, full_w, 10, fill=1, stroke=1)
    for i in range(19):
        c.setFillColor(STEEL_DARK)
        c.circle(lx + 35 + i * 92, floor_y + 5, 7, fill=1, stroke=0)

    # Agent A silhouette (left) — human-like shadow, leaving after sealing record
    ax = lx + 65
    ay = 333
    c.setFillColor(STEEL_DARK)
    c.setStrokeColor(BONE)
    c.setLineWidth(3)
    c.circle(ax + 135, ay + 345, 44, fill=1, stroke=1)
    # torso + shoulders
    p = c.beginPath()
    p.moveTo(ax + 68, ay + 110)
    p.lineTo(ax + 83, ay + 260)
    p.lineTo(ax + 110, ay + 300)
    p.lineTo(ax + 163, ay + 300)
    p.lineTo(ax + 193, ay + 260)
    p.lineTo(ax + 207, ay + 110)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    # Legs
    c.setStrokeColor(STEEL_DARK)
    c.setLineWidth(26)
    c.line(ax + 106, ay + 110, ax + 87, ay + 12)
    c.line(ax + 168, ay + 110, ax + 190, ay + 12)
    # One raised hand toward cassette
    c.setStrokeColor(STEEL_DARK)
    c.setLineWidth(19)
    c.line(ax + 182, ay + 250, ax + 275, ay + 213)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 14)
    c.drawCentredString(ax + 135, ay - 27, "AGENT A // SESSION ENDS")

    # Repository cassette — three plates physically inserted into one steel carrier
    cassette_x = lx + 465
    cassette_y = 335
    cassette_w = 855
    cassette_h = 365
    draw_brutalist_plate(c, cassette_x, cassette_y, cassette_w, cassette_h, fill_col=COAL_LIGHT, stroke_col=YELLOW, lw=4, shadow_offset=9, shadow_col=COAL_MID)
    draw_hazard_band(c, cassette_x, cassette_y + cassette_h - 17, cassette_w, 17, stripe_w=17, bg_col=YELLOW, fg_col=COAL, border_w=2)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 14)
    c.drawString(cassette_x + 24, cassette_y + cassette_h - 47, "REPOSITORY CASSETTE // COMMITTED CONTINUITY")

    # Four sealed document rails, one vertical status spine
    rails = [
        ("STATE.md", "current snapshot", "OVERWRITE", YELLOW),
        ("LEDGER.md", "session history", "APPEND ONLY", ORANGE),
        ("TRACE.md", "changed links", "UPDATE MAP", STEEL),
        ("tasks/", "true status folder", "MOVE FILES", BONE),
    ]
    rail_y = cassette_y + 220
    rail_gap = 52
    for i, (f_name, f_desc, f_mode, accent) in enumerate(rails):
        y = rail_y - i * rail_gap
        c.setFillColor(COAL)
        c.setStrokeColor(STEEL_DARK)
        c.setLineWidth(1.8)
        c.rect(cassette_x + 24, y - 26, cassette_w - 48, 42, fill=1, stroke=1)
        c.setFillColor(accent)
        c.rect(cassette_x + 24, y - 26, 10, 42, fill=1, stroke=0)
        c.setFillColor(BONE)
        c.setFont("PlexMonoBold", 17)
        c.drawString(cassette_x + 54, y - 1, f_name)
        c.setFillColor(STEEL_LIGHT)
        c.setFont("PlexSansMedium", 15)
        c.drawString(cassette_x + 300, y - 1, f_desc)
        draw_badge(c, cassette_x + cassette_w - 215, y - 20, f_mode, bg_col=accent,
                   fg_col=COAL, border_col=COAL, size=11, pad_x=10, h=24)

    # Commit seal placed immediately before branch push
    seal_x = cassette_x + 605
    seal_y = 215
    draw_brutalist_plate(c, seal_x, seal_y, 360, 74, fill_col=YELLOW, stroke_col=COAL, lw=3, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 15)
    c.drawCentredString(seal_x + 180, seal_y + 45, "LAST COMMIT // HANDOFF SEALED")
    c.setFont("PlexMonoBold", 13)
    c.drawCentredString(seal_x + 180, seal_y + 20, "STATE + LEDGER + TRACE + TASK STATUS")

    # Direction of transfer: Agent A -> cassette -> last commit -> PUSH -> Agent B
    draw_arrow(c, ax + 300, ay + 202, cassette_x, ay + 202, color=ORANGE, lw=5, head_len=18, head_w=11)
    draw_arrow(c, seal_x + 360, seal_y + 37, lx + full_w - 300, seal_y + 37, color=ORANGE, lw=6, head_len=18, head_w=11)
    draw_badge(c, lx + full_w - 304, seal_y + 20, "PUSH BRANCH", bg_col=ORANGE, fg_col=COAL, border_col=BONE, size=12, pad_x=10, h=30)

    # Agent B silhouette (right), plugging into same cassette
    bx = lx + full_w - 205
    by = 345
    c.setFillColor(STEEL_DARK)
    c.setStrokeColor(BONE)
    c.setLineWidth(3)
    c.circle(bx + 60, by + 310, 38, fill=1, stroke=1)
    body = c.beginPath()
    body.moveTo(bx + 5, by + 100)
    body.lineTo(bx + 15, by + 235)
    body.lineTo(bx + 34, by + 270)
    body.lineTo(bx + 87, by + 270)
    body.lineTo(bx + 108, by + 235)
    body.lineTo(bx + 118, by + 100)
    body.close()
    c.drawPath(body, fill=1, stroke=1)
    c.setStrokeColor(STEEL_DARK)
    c.setLineWidth(22)
    c.line(bx + 32, by + 100, bx + 20, by + 4)
    c.line(bx + 84, by + 100, bx + 98, by + 4)
    c.line(bx + 22, by + 220, bx - 22, by + 178)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 13)
    c.drawCentredString(bx + 60, by - 23, "AGENT B // READS RECORD")

    # Main handoff protocol strip
    draw_brutalist_plate(c, lx, 113, 575, 94, fill_col=ORANGE, stroke_col=COAL, lw=3.5, shadow_offset=6, shadow_col=COAL_MID)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 23)
    c.drawString(lx + 22, 161, "Commit handoff LAST → push branch.")
    c.setFont("PlexMonoBold", 12.5)
    c.drawString(lx + 22, 130, "NEXT: read STATE + latest LEDGER entries.")


def draw_slide_14(c):
    """14 — Branch, PR, human merge (Bone, two railway tracks with separated deployed check gate)."""
    draw_slide_frame(c, 14, ACT_IV, bg_mode="bone", kicker="BRANCH PROTECTION // HUMANS OWN MAIN")

    lx = col_x(0)
    full_w = col_span_w(12)

    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 56)
    c.drawString(lx, 915, "MAIN NEVER BELONGS TO THE AGENT.")

    # Track system, feature rail in upper half and protected main rail below
    rail_y_top = 695
    rail_y_bot = 405
    rail_x0 = lx + 20
    rail_x1 = lx + full_w - 20

    # Track beds
    for y, accent in [(rail_y_top, ORANGE), (rail_y_bot, COAL)]:
        c.setFillColor(BONE_DARK)
        c.setStrokeColor(COAL)
        c.setLineWidth(3)
        c.rect(rail_x0, y - 34, rail_x1 - rail_x0, 68, fill=1, stroke=1)
        # parallel steel rails
        c.setStrokeColor(accent)
        c.setLineWidth(8)
        c.line(rail_x0 + 18, y - 14, rail_x1 - 18, y - 14)
        c.line(rail_x0 + 18, y + 14, rail_x1 - 18, y + 14)
        # sleepers
        c.setStrokeColor(COAL)
        c.setLineWidth(3)
        for i in range(1, 22):
            sx = rail_x0 + i * (rail_x1 - rail_x0) / 22
            c.line(sx, y - 30, sx, y + 30)

    # Feature train on upper track
    feat_x = rail_x0 + 25
    c.setFillColor(ORANGE)
    c.setStrokeColor(COAL)
    c.setLineWidth(3)
    c.rect(feat_x, rail_y_top + 29, 320, 112, fill=1, stroke=1)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 19)
    c.drawCentredString(feat_x + 160, rail_y_top + 101, "feat/T-###-slug")
    c.setFont("PlexMono", 13)
    c.drawCentredString(feat_x + 160, rail_y_top + 72, "AGENT WRITES FEATURE BRANCH")
    for i in range(3):
        c.setFillColor(COAL)
        c.circle(feat_x + 60 + i * 110, rail_y_top + 26, 17, fill=1, stroke=1)

    # PR Inspection booth on branch track
    booth_x = lx + 510
    booth_y = rail_y_top + 28
    draw_brutalist_plate(c, booth_x, booth_y, 485, 118, fill_col=COAL, stroke_col=COAL, lw=3.5, shadow_offset=5, shadow_col=STEEL_DARK)
    c.setFillColor(YELLOW)
    c.rect(booth_x, booth_y + 82, 485, 36, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 22)
    c.drawString(booth_x + 20, booth_y + 92, "PR INSPECTION BOOTH")
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 12)
    c.drawString(booth_x + 20, booth_y + 58, "TASK · SPEC · ACs · PLAN · ACTUAL VERIFICATION · RISKS")
    c.setFillColor(STEEL_LIGHT)
    c.setFont("PlexSansMedium", 13)
    c.drawString(booth_x + 20, booth_y + 30, "CI inspects. A human reviews. A PR is a request, not permission to merge.")

    # Human-operated yellow merger switch between feature and protected main tracks
    gate_x = lx + 1120
    gate_cy = rail_y_top
    draw_brutalist_plate(c, gate_x, gate_cy + 19, 170, 145, fill_col=YELLOW, stroke_col=COAL, lw=4, shadow_offset=6, shadow_col=COAL)
    draw_hazard_band(c, gate_x, gate_cy + 150, 170, 14, stripe_w=12, bg_col=YELLOW, fg_col=COAL, border_w=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 13)
    c.drawCentredString(gate_x + 85, gate_cy + 118, "G: HUMAN")
    c.setFont("ArchivoBlack", 23)
    c.drawCentredString(gate_x + 85, gate_cy + 80, "MERGE")
    c.setFont("PlexMonoBold", 11.5)
    c.drawCentredString(gate_x + 85, gate_cy + 50, "ONLY TO MAIN")
    # Switch lever routes from feature into main, yellow denotes human decision
    c.setStrokeColor(YELLOW)
    c.setLineWidth(11)
    c.line(gate_x + 85, rail_y_top + 20, gate_x + 240, rail_y_bot + 10)
    c.setFillColor(COAL)
    c.setStrokeColor(YELLOW)
    c.setLineWidth(4)
    c.circle(gate_x + 85, rail_y_top + 20, 22, fill=1, stroke=1)
    draw_arrow(c, booth_x + 485, rail_y_top + 95, gate_x, rail_y_top + 95, color=ORANGE, lw=5, head_len=18, head_w=11)

    # Protected main barrier physically below the join
    main_x = rail_x0 + 20
    main_y = rail_y_bot + 74
    draw_brutalist_plate(c, main_x, main_y, 505, 112, fill_col=COAL, stroke_col=COAL, lw=3, shadow_offset=5, shadow_col=STEEL_DARK)
    draw_hazard_band(c, main_x, main_y + 95, 505, 17, stripe_w=15, bg_col=YELLOW, fg_col=COAL, border_w=2)
    c.setFont("ArchivoBlack", 31)
    c.setFillColor(BONE)
    c.drawString(main_x + 20, main_y + 45, "PROTECTED main")
    c.setFont("PlexMonoBold", 13)
    c.setFillColor(YELLOW)
    c.drawString(main_x + 20, main_y + 19, "NO DIRECT PUSH · NO FORCE-PUSH")

    # The yellow turnout below routes to the right-moving protected-main rail.

    # Distinct downstream deployed-verification station AFTER the human merge join.
    # The merge routes to the main rail; the separate yellow station gates deployed AC checks.
    dep_x = lx + full_w - 420
    dep_y = rail_y_bot + 93
    dep_w = 420
    dep_h = 105
    draw_brutalist_plate(c, dep_x, dep_y, dep_w, dep_h, fill_col=COAL_LIGHT, stroke_col=YELLOW, lw=3.5, shadow_offset=6, shadow_col=COAL)
    c.setFillColor(YELLOW)
    c.rect(dep_x, dep_y + 79, dep_w, 26, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 12)
    c.drawString(dep_x + 14, dep_y + 86, "AFTER MERGE // DEPLOYED BUILD")
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 17)
    c.drawString(dep_x + 14, dep_y + 48, "Human verifies acceptance criteria")
    c.setFont("PlexMonoBold", 12)
    c.setFillColor(GREEN)
    c.drawString(dep_x + 14, dep_y + 20, "THEN: HUMAN MARKS SPEC VERIFIED")

    # Turnout enters main after human merge; main rail continues right to deployed verification.
    draw_arrow(c, gate_x + 240, rail_y_bot, rail_x1 - 22, rail_y_bot, color=COAL, lw=4, head_len=17, head_w=10)
    draw_arrow(c, gate_x + 240, rail_y_bot + 10, dep_x + 58, dep_y, color=YELLOW, lw=4, head_len=14, head_w=9)

    # Human merge vs deployed verification legend between rails
    draw_badge(c, lx + 662, 460, "GATE 1 · HUMAN MERGE", bg_col=YELLOW, fg_col=COAL, border_col=COAL, size=12, pad_x=12, h=28)
    draw_badge(c, lx + 900, 460, "GATE 2 · VERIFY ON DEPLOY", bg_col=YELLOW, fg_col=COAL, border_col=COAL, size=12, pad_x=12, h=28)

    # Operational rules plate
    draw_brutalist_plate(c, lx, 115, full_w, 135, fill_col=COAL, stroke_col=ORANGE, lw=3.5, shadow_offset=6, shadow_col=COAL_MID)
    c.setFillColor(ORANGE)
    c.rect(lx, 115, 14, 135, fill=1, stroke=0)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 17)
    c.drawString(lx + 34, 208, "feat/T-###-slug → PR → protected main")
    c.setFont("PlexSansMedium", 17)
    c.drawString(lx + 34, 177, "No direct push to main. No force-push to protected branches. A human merges.")
    c.setFillColor(YELLOW)
    c.setFont("PlexMonoBold", 15)
    c.drawString(lx + 34, 143, "AFTER MERGE: deploy → human checks deployed ACs → HUMAN-OWNED VERIFIED transition.")


def draw_slide_15(c):
    """15 — CI as an inspector (Coal, five-beam X-ray tunnel + defect diagnostic wall)."""
    draw_slide_frame(c, 15, ACT_IV, bg_mode="coal", kicker="CONTINUOUS INTEGRATION // AUTOMATED INSPECTION")

    lx = col_x(0)
    full_w = col_span_w(12)
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 55)
    c.drawString(lx, 915, "CI IS AN INSPECTOR, NOT A CHEERLEADER.")

    # Required inspector chain at top
    required_y = 812
    draw_brutalist_plate(c, lx, required_y, full_w, 78, fill_col=COAL_LIGHT, stroke_col=STEEL, lw=3, shadow_offset=5, shadow_col=COAL_MID)
    labels = ["test", "lint", "typecheck", "secret-scan", "forge-lint"]
    slot_w = full_w / 5
    for i, label in enumerate(labels):
        sx = lx + i * slot_w
        if i > 0:
            c.setStrokeColor(STEEL_DARK)
            c.setLineWidth(2)
            c.line(sx, required_y + 12, sx, required_y + 66)
        c.setFillColor(YELLOW if label == "forge-lint" else BONE)
        c.setFont("PlexMonoBold", 18)
        c.drawCentredString(sx + slot_w / 2, required_y + 31, label)

    # Five-beam industrial scanner tunnel
    tunnel_x = lx + 18
    tunnel_y = 398
    tunnel_w = 790
    tunnel_h = 365
    draw_brutalist_plate(c, tunnel_x, tunnel_y, tunnel_w, tunnel_h, fill_col=COAL_LIGHT, stroke_col=BONE, lw=3.5, shadow_offset=7, shadow_col=COAL)
    # Scanner portal frame
    c.setFillColor(COAL)
    c.setStrokeColor(STEEL)
    c.setLineWidth(7)
    c.rect(tunnel_x + 40, tunnel_y + 40, tunnel_w - 80, tunnel_h - 80, fill=1, stroke=1)
    # Entry conveyor with anonymous component silhouette
    c.setStrokeColor(STEEL_DARK)
    c.setLineWidth(7)
    c.line(tunnel_x + 72, tunnel_y + 122, tunnel_x + tunnel_w - 72, tunnel_y + 122)
    c.setFillColor(STEEL)
    c.setStrokeColor(COAL)
    c.setLineWidth(3)
    c.rect(tunnel_x + 82, tunnel_y + 136, 174, 92, fill=1, stroke=1)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 14)
    c.drawCentredString(tunnel_x + 169, tunnel_y + 178, "BRANCH")
    c.setFont("PlexMono", 11)
    c.drawCentredString(tunnel_x + 169, tunnel_y + 155, "SPEC-LINKED WORK")

    # Five distinct beams (neutral steel, no unearned green pass)
    beam_names = ["TEST", "LINT", "TYPE", "SECRET", "FORGE"]
    beam_xs = [tunnel_x + 325 + i * 82 for i in range(5)]
    for i, (bx, name) in enumerate(zip(beam_xs, beam_names)):
        c.setFillColor(YELLOW if i == 4 else STEEL)
        c.setStrokeColor(BONE)
        c.setLineWidth(2)
        # Emitter housing
        c.rect(bx - 19, tunnel_y + tunnel_h - 100, 38, 52, fill=1, stroke=1)
        # scanning beam
        c.setStrokeColor(YELLOW if i == 4 else STEEL_LIGHT)
        c.setLineWidth(5 if i == 4 else 3)
        c.line(bx, tunnel_y + tunnel_h - 100, bx, tunnel_y + 130)
        c.setFillColor(BONE)
        c.setFont("PlexMonoBold", 10.5)
        c.drawCentredString(bx, tunnel_y + tunnel_h - 128, name)
        c.setFillColor(COAL)
        c.circle(bx, tunnel_y + 122, 8, fill=1, stroke=0)

    # REJECT wall to the right with exactly five forge-lint conditions
    list_x = lx + 865
    list_y = 398
    list_w = full_w - 865
    list_h = 365
    draw_brutalist_plate(c, list_x, list_y, list_w, list_h, fill_col=COAL, stroke_col=ORANGE, lw=3.5, shadow_offset=7, shadow_col=COAL_MID)
    c.setFillColor(ORANGE)
    c.rect(list_x, list_y + list_h - 54, list_w, 54, fill=1, stroke=1)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 23)
    c.drawString(list_x + 20, list_y + list_h - 36, "forge-lint REJECTS:")

    rejects = [
        "src/ without a spec link",
        "IMPLEMENTED AC without a named test",
        "Invalid document frontmatter",
        "DOING task stale for >48 hours",
        "Source change without a LEDGER append",
    ]
    row_h = 55
    for i, item in enumerate(rejects):
        y = list_y + list_h - 95 - i * row_h
        c.setFillColor(ORANGE)
        c.setFont("PlexMonoBold", 13)
        c.drawString(list_x + 20, y, f"0{i + 1}")
        c.setFillColor(BONE)
        c.setFont("PlexSansMedium", 15)
        c.drawString(list_x + 58, y, item)
        if i < 4:
            c.setStrokeColor(STEEL_DARK)
            c.setLineWidth(1)
            c.line(list_x + 20, y - 13, list_x + list_w - 18, y - 13)

    # Branch decision: reject returns to branch; all required checks exit 0 before human review
    draw_arrow(c, tunnel_x + tunnel_w - 40, tunnel_y + 62, tunnel_x + tunnel_w - 40, tunnel_y + 24, color=ORANGE, lw=3.5, head_len=12, head_w=8)
    c.setFillColor(ORANGE)
    c.setFont("PlexMonoBold", 12)
    c.drawCentredString(tunnel_x + tunnel_w / 2, tunnel_y + 19, "REJECT → FIX ON BRANCH → RE-RUN REQUIRED CHECKS")

    # Conditional path to review, neutral not a depicted pass result
    c.setStrokeColor(STEEL)
    c.setLineWidth(4)
    c.line(lx + 430, 366, lx + full_w - 60, 366)
    draw_arrow(c, lx + full_w - 60, 366, lx + full_w - 60, 306, color=STEEL, lw=4)
    draw_brutalist_plate(c, lx + 730, 270, 755, 66, fill_col=COAL_LIGHT, stroke_col=STEEL, lw=2.5, shadow_offset=4, shadow_col=COAL)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 15)
    c.drawCentredString(lx + 1108, 298, "IF ALL REQUIRED CHECKS EXIT 0 → HUMAN REVIEW")

    # Bottom principle
    draw_brutalist_plate(c, lx, 115, 655, 98, fill_col=YELLOW, stroke_col=COAL, lw=3.5, shadow_offset=6, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 25)
    c.drawCentredString(lx + 327, 153, "No unearned green pass.")
    c.setFont("PlexMonoBold", 12)
    c.drawCentredString(lx + 327, 130, "CI IS PROCEDURE UNTIL OUTPUT EXISTS.")


def draw_slide_16(c):
    """16 — Write access as a lease (Bone, private key remains outside the repository boundary)."""
    draw_slide_frame(c, 16, ACT_IV, bg_mode="bone", kicker="CREDENTIAL HYGIENE // LEAST PRIVILEGE")

    lx = col_x(0)
    full_w = col_span_w(12)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 60)
    c.drawString(lx, 915, "WRITE ACCESS IS A LEASE.")

    # Architectural repo boundary: private vault is outside; public-only conduit crosses
    boundary_x = lx + 975
    boundary_y = 285
    boundary_w = 720
    boundary_h = 565
    c.setStrokeColor(COAL)
    c.setLineWidth(5)
    c.setDash(12, 7)
    c.rect(boundary_x, boundary_y, boundary_w, boundary_h, fill=0, stroke=1)
    c.setDash()
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 15)
    c.drawString(boundary_x + 18, boundary_y + boundary_h - 30, "REPOSITORY BOUNDARY // PUBLIC KEY ONLY INSIDE")

    # Private key vault visibly outside repo
    vault_x = lx + 30
    vault_y = 470
    vault_w = 450
    vault_h = 310
    draw_brutalist_plate(c, vault_x, vault_y, vault_w, vault_h, fill_col=COAL, stroke_col=ORANGE, lw=4, shadow_offset=8, shadow_col=STEEL_DARK)
    draw_hazard_band(c, vault_x, vault_y + vault_h - 18, vault_w, 18, stripe_w=17, bg_col=YELLOW, fg_col=COAL, border_w=2)
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 25)
    c.drawCentredString(vault_x + vault_w / 2, vault_y + vault_h - 64, "PRIVATE KEY VAULT")
    c.setFont("PlexMonoBold", 13)
    c.setFillColor(ORANGE)
    c.drawCentredString(vault_x + vault_w / 2, vault_y + vault_h - 94, "OUTSIDE THE REPO · NEVER COMMIT")
    # Key silhouette inside vault (abstract, no key material)
    c.setStrokeColor(YELLOW)
    c.setLineWidth(12)
    c.circle(vault_x + 145, vault_y + 100, 45, fill=0, stroke=1)
    c.line(vault_x + 190, vault_y + 100, vault_x + 340, vault_y + 100)
    c.line(vault_x + 300, vault_y + 100, vault_x + 300, vault_y + 72)
    c.line(vault_x + 340, vault_y + 100, vault_x + 340, vault_y + 78)
    c.setFillColor(BONE)
    c.setFont("PlexMonoBold", 15)
    c.drawCentredString(vault_x + vault_w / 2, vault_y + 35, "ONE ed25519 KEY / AGENT / WORKSPACE")

    # Public key transmission conduit crosses into one-repo dock only
    cable_y = 605
    c.setStrokeColor(STEEL_DARK)
    c.setLineWidth(18)
    c.line(vault_x + vault_w, cable_y, boundary_x + 155, cable_y)
    c.setStrokeColor(YELLOW)
    c.setLineWidth(5)
    c.line(vault_x + vault_w, cable_y, boundary_x + 155, cable_y)
    draw_arrow(c, boundary_x + 145, cable_y, boundary_x + 230, cable_y, color=YELLOW, lw=4, head_len=16, head_w=10)
    draw_badge(c, vault_x + vault_w + 155, cable_y + 22, "PUBLIC KEY ONLY", bg_col=YELLOW, fg_col=COAL, border_col=COAL, size=12, pad_x=12, h=29)

    # Single repository dock
    dock_x = boundary_x + 205
    dock_y = boundary_y + 158
    dock_w = 470
    dock_h = 235
    draw_brutalist_plate(c, dock_x, dock_y, dock_w, dock_h, fill_col=COAL, stroke_col=STEEL, lw=3.5, shadow_offset=7, shadow_col=STEEL_DARK)
    c.setFillColor(YELLOW)
    c.rect(dock_x, dock_y + dock_h - 48, dock_w, 48, fill=1, stroke=0)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 15)
    c.drawCentredString(dock_x + dock_w / 2, dock_y + dock_h - 30, "ONE-REPO WRITE DEPLOY KEY")
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 28)
    c.drawCentredString(dock_x + dock_w / 2, dock_y + 116, "git push: authorized")
    c.setFillColor(STEEL_LIGHT)
    c.setFont("PlexMono", 13)
    c.drawCentredString(dock_x + dock_w / 2, dock_y + 80, "branch protection remains the guardrail")
    # Main barrier
    c.setFillColor(ORANGE)
    c.setStrokeColor(BONE)
    c.setLineWidth(3)
    c.rect(dock_x + 70, dock_y + 20, dock_w - 140, 37, fill=1, stroke=1)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 14)
    c.drawCentredString(dock_x + dock_w / 2, dock_y + 33, "PROTECTED main · NO FORCE-PUSH")

    # 30-day rotation dial in left lower section
    dial_cx = lx + 215
    dial_cy = 330
    draw_gear(c, dial_cx, dial_cy, 93, 73, 0, 16, fill_col=STEEL, stroke_col=COAL, lw=3)
    c.setFillColor(BONE)
    c.setStrokeColor(COAL)
    c.setLineWidth(2)
    c.circle(dial_cx, dial_cy, 59, fill=1, stroke=1)
    c.setFont("ArchivoBlack", 25)
    c.setFillColor(COAL)
    c.drawCentredString(dial_cx, dial_cy + 9, "30")
    c.setFont("PlexMonoBold", 12)
    c.drawCentredString(dial_cx, dial_cy - 15, "DAYS")
    c.setStrokeColor(ORANGE)
    c.setLineWidth(6)
    c.line(dial_cx + 30, dial_cy + 50, dial_cx + 72, dial_cy + 77)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 13)
    c.drawString(lx + 340, dial_cy + 5, "ROTATE EVERY 30 DAYS")
    c.setFont("PlexMono", 12.5)
    c.setFillColor(STEEL_DARK)
    c.drawString(lx + 340, dial_cy - 22, "Record fingerprint, dates, status")
    c.drawString(lx + 340, dial_cy - 44, "in ops/KEYS.md — metadata only.")

    # Separate PR API hatch; a deploy key does not authorize opening a PR
    hatch_x = boundary_x + 215
    hatch_y = boundary_y + 32
    draw_brutalist_plate(c, hatch_x, hatch_y, 470, 98, fill_col=ORANGE, stroke_col=COAL, lw=3, shadow_offset=5, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 20)
    c.drawCentredString(hatch_x + 235, hatch_y + 60, "SEPARATE PR API HATCH")
    c.setFont("PlexMonoBold", 11.5)
    c.drawCentredString(hatch_x + 235, hatch_y + 30, "SEPARATE AUTHORIZED CREDENTIAL OR HUMAN")
    # Physical divider between git push and PR access
    c.setStrokeColor(COAL)
    c.setLineWidth(5)
    c.line(hatch_x + 20, dock_y - 5, hatch_x + 450, dock_y - 5)
    draw_arrow(c, dock_x + dock_w / 2, dock_y, hatch_x + 235, hatch_y + 98, color=ORANGE, lw=3.5, dashed=True)

    # Bottom doctrine line
    draw_brutalist_plate(c, lx, 115, full_w, 102, fill_col=COAL, stroke_col=YELLOW, lw=3.5, shadow_offset=6, shadow_col=COAL_MID)
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 30)
    c.drawString(lx + 30, 157, "Deploy key = Git push. PR API access needs separate authorization.")
    c.setFillColor(YELLOW)
    c.setFont("PlexMonoBold", 13)
    c.drawRightString(lx + full_w - 24, 128, "LEAST PRIVILEGE · REVOKABLE · AUDITABLE")


def draw_slide_17(c):
    """17 — Separation of duties (Coal, four distinct role workstations, no self-review)."""
    draw_slide_frame(c, 17, ACT_IV, bg_mode="coal", kicker="ROLE BOUNDARIES // SEPARATION OF DUTIES")

    lx = col_x(0)
    full_w = col_span_w(12)
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 56)
    c.drawString(lx, 915, "DIFFERENT HANDS. DIFFERENT POWERS.")

    # Four distinct industrial workstations (2x2 offset composition)
    stations = [
        (lx + 15, 550, 740, 250, "ARCHITECT", "Drafts specs, ADRs, plans", "BLUEPRINT TABLE", YELLOW, "PAPER · PENCIL · DECISION PLATES"),
        (lx + 825, 550, 890, 250, "BUILDER", "Implements approved specs and tests", "CODE FOUNDRY", STEEL, "TOOLS · BRANCH · TEST FIXTURES"),
        (lx + 15, 260, 890, 250, "REVIEWER", "Audits the PR against the spec", "INSPECTION BENCH", ORANGE, "DIFF · SPEC · ACCEPTANCE CRITERIA"),
        (lx + 975, 260, 740, 250, "AUDITOR", "Reads broadly; writes audit findings only", "ARCHIVE / AUDIT ROOM", BONE, "READ WIDE · WRITE FINDINGS ONLY"),
    ]

    for sx, sy, sw, sh, role, duty, station, accent, tools in stations:
        draw_brutalist_plate(c, sx, sy, sw, sh, fill_col=COAL_LIGHT, stroke_col=accent, lw=3.5, shadow_offset=7, shadow_col=COAL_MID)
        c.setFillColor(accent)
        c.rect(sx, sy + sh - 55, sw, 55, fill=1, stroke=0)
        c.setFillColor(COAL)
        c.setFont("ArchivoBlack", 25)
        c.drawString(sx + 24, sy + sh - 37, role)
        c.setFont("PlexMonoBold", 12)
        c.drawRightString(sx + sw - 22, sy + sh - 35, station)

        # Role-specific mechanism icon
        icon_cx = sx + 112
        icon_cy = sy + 106
        if role == "ARCHITECT":
            # Blueprint sheet + compass
            c.setFillColor(COAL)
            c.setStrokeColor(BONE)
            c.setLineWidth(2)
            c.rect(icon_cx - 68, icon_cy - 50, 132, 112, fill=1, stroke=1)
            c.setStrokeColor(STEEL)
            c.line(icon_cx - 48, icon_cy + 34, icon_cx + 43, icon_cy + 34)
            c.line(icon_cx - 48, icon_cy + 8, icon_cx + 6, icon_cy + 8)
            c.line(icon_cx - 48, icon_cy - 20, icon_cx + 44, icon_cy - 20)
            c.setStrokeColor(YELLOW)
            c.setLineWidth(4)
            c.line(icon_cx + 48, icon_cy - 34, icon_cx + 72, icon_cy + 36)
        elif role == "BUILDER":
            # Mechanical press + component block
            c.setFillColor(STEEL_DARK)
            c.setStrokeColor(BONE)
            c.setLineWidth(2.5)
            c.rect(icon_cx - 65, icon_cy - 48, 130, 95, fill=1, stroke=1)
            c.setFillColor(ORANGE)
            c.rect(icon_cx - 42, icon_cy + 18, 84, 19, fill=1, stroke=1)
            c.setFillColor(BONE)
            c.rect(icon_cx - 30, icon_cy - 26, 60, 35, fill=1, stroke=1)
            c.setFillColor(COAL)
            c.circle(icon_cx, icon_cy - 9, 6, fill=1, stroke=0)
        elif role == "REVIEWER":
            # Inspection lens over a document diff
            c.setFillColor(COAL)
            c.setStrokeColor(BONE)
            c.setLineWidth(2)
            c.rect(icon_cx - 67, icon_cy - 44, 92, 100, fill=1, stroke=1)
            c.setStrokeColor(ORANGE)
            c.setLineWidth(3)
            c.line(icon_cx - 49, icon_cy + 30, icon_cx + 5, icon_cy + 30)
            c.line(icon_cx - 49, icon_cy + 11, icon_cx - 4, icon_cy + 11)
            c.setStrokeColor(YELLOW)
            c.setLineWidth(10)
            c.circle(icon_cx + 37, icon_cy - 5, 28, fill=0, stroke=1)
            c.setStrokeColor(YELLOW)
            c.line(icon_cx + 59, icon_cy - 26, icon_cx + 82, icon_cy - 49)
        else:
            # Archive cabinet with read-only lock plate
            c.setFillColor(COAL)
            c.setStrokeColor(BONE)
            c.setLineWidth(2)
            c.rect(icon_cx - 58, icon_cy - 55, 116, 118, fill=1, stroke=1)
            for j in range(3):
                c.setStrokeColor(STEEL)
                c.rect(icon_cx - 42, icon_cy + 23 - j * 30, 84, 20, fill=0, stroke=1)
                c.setFillColor(STEEL)
                c.circle(icon_cx + 28, icon_cy + 33 - j * 30, 3, fill=1, stroke=0)
            draw_padlock(c, icon_cx + 81, icon_cy - 5, w=34, h=28, body_col=YELLOW, stroke_col=COAL, label="R")

        # Role copy + authority label
        c.setFillColor(BONE)
        c.setFont("ArchivoBlack", 19 if role == "AUDITOR" else 23)
        c.drawString(sx + 225, sy + 142, duty)
        c.setFillColor(accent)
        c.setFont("PlexMonoBold", 14)
        c.drawString(sx + 225, sy + 104, tools)
        c.setFillColor(STEEL_LIGHT)
        c.setFont("PlexSansMedium", 14)
        if role == "ARCHITECT":
            c.drawString(sx + 225, sy + 68, "May propose. APPROVED remains human-controlled.")
        elif role == "BUILDER":
            c.drawString(sx + 225, sy + 68, "Only after spec status = APPROVED.")
        elif role == "REVIEWER":
            c.drawString(sx + 225, sy + 68, "Independent session audits behavior against contract.")
        else:
            c.drawString(sx + 225, sy + 68, "Audit findings only; no product or spec edits.")

    # Crossed boundary between Builder and Reviewer — no self-review
    boundary_y = 526
    c.setStrokeColor(ORANGE)
    c.setLineWidth(10)
    c.line(lx + 810, boundary_y - 30, lx + 925, boundary_y + 30)
    c.line(lx + 810, boundary_y + 30, lx + 925, boundary_y - 30)
    draw_badge(c, lx + 676, boundary_y - 16, "NO SELF-REVIEW", bg_col=ORANGE, fg_col=COAL, border_col=BONE, size=13, pad_x=12, h=32)

    # Footer governance bar
    draw_brutalist_plate(c, lx, 115, full_w, 105, fill_col=YELLOW, stroke_col=COAL, lw=3.5, shadow_offset=6, shadow_col=COAL)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 29)
    c.drawCentredString(lx + full_w / 2, 164, "Humans own approval, merge, and verification.")
    c.setFont("PlexMonoBold", 13)
    c.drawCentredString(lx + full_w / 2, 134, "BUILDER ≠ REVIEWER · AUTHORITY DOES NOT TRANSFER BY ROLE")


def draw_slide_18(c):
    """18 — When the crank stalls (Bone, four fracture panels recover into the written repo)."""
    draw_slide_frame(c, 18, ACT_IV, bg_mode="bone", kicker="INCIDENT ROUTING // FAIL CLOSED")

    lx = col_x(0)
    full_w = col_span_w(12)
    c.setFillColor(COAL)
    c.setFont("ArchivoBlack", 60)
    c.drawString(lx, 915, "FAIL CLOSED. RECOVER IN WRITING.")

    # Four jagged comic panels around an intact repository hub
    cards = [
        (lx + 12, 575, 820, 255, "01 // AMBIGUITY", "AMBIGUOUS → mark BLOCKED; move task to REVIEW; ask.", "QUESTION / TASK CARD / HUMAN RESPONSE", ORANGE),
        (lx + 900, 575, 820, 255, "02 // BASELINE RED", "BASELINE RED → report before building.", "REPORT THE BASELINE / DO NOT BUILD", ORANGE),
        (lx + 12, 280, 820, 255, "03 // SESSION DIES", "SESSION DIES → resume from committed STATE + LEDGER.", "READ SNAPSHOT + LAST LEDGER ENTRIES", YELLOW),
        (lx + 900, 280, 820, 255, "04 // KEY SUSPECT", "KEY SUSPECT → revoke, rotate, inspect activity.", "REVOKE / ROTATE / AUDIT", YELLOW),
    ]

    for i, (x, y, w, h, title, action, detail, accent) in enumerate(cards):
        # Jagged frame polygon, black outside contour, panel fill inside
        c.saveState()
        p = c.beginPath()
        p.moveTo(x + 10, y + 2)
        p.lineTo(x + w - 14, y + 8)
        p.lineTo(x + w - 3, y + h - 22)
        p.lineTo(x + w - 28, y + h - 4)
        p.lineTo(x + 22, y + h - 12)
        p.lineTo(x + 3, y + 24)
        p.close()
        c.setFillColor(COAL)
        c.setStrokeColor(COAL)
        c.setLineWidth(4)
        c.drawPath(p, fill=1, stroke=1)
        # Inset surface
        c.setFillColor(COAL_LIGHT)
        c.setStrokeColor(accent)
        c.setLineWidth(2.5)
        c.rect(x + 18, y + 20, w - 36, h - 40, fill=1, stroke=1)
        # Fracture lightning seam
        c.setStrokeColor(ORANGE)
        c.setLineWidth(5)
        c.line(x + w - 54, y + h - 20, x + w - 88, y + h - 72)
        c.line(x + w - 88, y + h - 72, x + w - 62, y + h - 104)
        c.line(x + w - 62, y + h - 104, x + w - 101, y + h - 145)
        c.restoreState()

        # Classification strip
        c.setFillColor(accent)
        c.rect(x + 18, y + h - 67, w - 36, 47, fill=1, stroke=0)
        c.setFillColor(COAL)
        c.setFont("PlexMonoBold", 15)
        c.drawString(x + 38, y + h - 48, title)

        # Recovery arrow from fracture to written action
        draw_arrow(c, x + 87, y + 117, x + 180, y + 117, color=accent, lw=4.5, head_len=15, head_w=9)
        draw_wrapped(c, x + 205, y + 137, action, "PlexSansBold", 16, 18, w - 250, color=BONE)
        c.setFillColor(STEEL_LIGHT)
        c.setFont("PlexMonoBold", 12.5)
        c.drawString(x + 205, y + 103, detail)

        # Broken mechanism icon within panel left of arrow
        c.setStrokeColor(ORANGE)
        c.setLineWidth(3)
        c.circle(x + 72, y + 117, 26, fill=0, stroke=1)
        c.setFillColor(accent)
        c.setFont("ArchivoBlack", 22)
        c.drawCentredString(x + 72, y + 109, "!" if i < 2 else "↻")

    # Central repository vault as intact spine between the incident panels
    repo_y = 522
    repo_x = lx + 702
    repo_w = 328
    repo_h = 73
    draw_brutalist_plate(c, repo_x, repo_y, repo_w, repo_h, fill_col=YELLOW, stroke_col=COAL, lw=3, shadow_offset=5, shadow_col=COAL)
    draw_gear(c, repo_x + 40, repo_y + repo_h / 2, 25, 19, 6, 8, fill_col=STEEL_DARK, stroke_col=COAL, lw=2)
    c.setFillColor(COAL)
    c.setFont("PlexMonoBold", 16)
    c.drawString(repo_x + 76, repo_y + 43, "REPOSITORY")
    c.setFont("PlexMono", 11.5)
    c.drawString(repo_x + 76, repo_y + 20, "STATE · LEDGER · KEYS · TASKS")

    # Four inward recovery arrows terminating at durable records, no decorative motion
    draw_arrow(c, lx + 415, 575, repo_x + 15, repo_y + repo_h, color=YELLOW, lw=3.5)
    draw_arrow(c, lx + 1315, 575, repo_x + repo_w - 15, repo_y + repo_h, color=YELLOW, lw=3.5)
    draw_arrow(c, lx + 415, 535, repo_x + 15, repo_y, color=STEEL, lw=3.5)
    draw_arrow(c, lx + 1315, 535, repo_x + repo_w - 15, repo_y, color=STEEL, lw=3.5)

    # Bottom doctrine
    draw_brutalist_plate(c, lx, 115, full_w, 105, fill_col=COAL, stroke_col=ORANGE, lw=3.5, shadow_offset=6, shadow_col=COAL_MID)
    c.setFillColor(BONE)
    c.setFont("ArchivoBlack", 34)
    c.drawCentredString(lx + full_w / 2, 163, "Never substitute a guess for a record.")
    c.setFillColor(YELLOW)
    c.setFont("PlexMonoBold", 14)
    c.drawCentredString(lx + full_w / 2, 132, "EVERY FAILURE HAS A WRITTEN REPOSITORY PATH")
