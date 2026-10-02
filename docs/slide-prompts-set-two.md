# KONKAUTO — slide PDF production blueprint

Create a **20-slide, 16:9 PDF** that explains KONKAUTO as a working system—not as a directory tour. The visual story moves from **why chat-based development fails**, through **the specification and agent workflow**, to **governance, recovery, and adoption**.

The look: **brutalist industrial design meets a high-contrast graphic novel**. Think inked machinery, cutaway diagrams, hazard markings, molten orange seams, and precise vector typography. Every illustration should explain a mechanism.

## 1. Master prompt

Paste this prompt **together with the numbered slide cards below** into your presentation tool.

```text
Act as an award-winning presentation art director, information designer, and
senior software architect. Produce a 20-slide, 16:9 landscape presentation
titled “KONKAUTO — Specification-Driven Agentic Development.” Export it as
KONKAUTO_SDAD_Workflow.pdf.

AUDIENCE
Engineering leaders and developers designing reliable AI-agent workflows.

NARRATIVE
The repository is the brain; the agent is the hands; markdown is the contract.
Show the complete operating loop: human idea → approved specification →
plan/task → agent session → tested branch → written handoff → PR/CI →
human merge and deployed verification → next stateless session.

FOLLOW THE SLIDE CARDS BELOW
Use their slide order, on-slide copy, wireframes, and individual visual prompts.
Preserve exact technical identifiers such as AGENTS.md, STATE.md, LEDGER.md,
SPEC-012, PLAN-004, T-032, AC-2, and forge-lint. Slides 06–12 should use the
password-reset example as a continuous worked example.

ART DIRECTION
Brutalist industrialism fused with a printed graphic novel: oversized
typography, square edges, exposed grids, heavy black contours, vector cutaways,
limited spot colors, restrained vector halftone, dramatic negative space, and
one dominant visual metaphor per slide. Make the deck feel like a designed
technical artifact, not a corporate template.

Palette:
- Coal #101214
- Bone #F2F0E8
- Furnace orange #F05A28: motion, risk, intervention
- Hazard yellow #FFD447: human authority and approval
- Steel gray #748088: agent machinery and neutral infrastructure
- Evidence green #72D48C: passing checks and verified outcomes only

Use Archivo Black for display headings, IBM Plex Sans for body text, and
IBM Plex Mono for IDs, filenames, commands, and status labels. Use suitable
embedded substitutes if necessary. Alternate coal and bone backgrounds;
reserve orange and yellow for decisive accents. Never place light text on
yellow or orange.

COMPOSITION
Use a 12-column grid with generous safe margins. Give every slide one clear
takeaway, a dominant illustration or diagram, and a consistent small footer:
“KONKAUTO / [ACT NAME]                                      NN / 20”.
Vary composition across slides; do not repeat a three-card template.
Keep diagram labels comfortably readable. Move detail into visual structure
rather than shrinking text.

ILLUSTRATION AND PDF PRODUCTION
Create original, crisp vector illustrations. Set all slide text and diagram
labels as real, selectable text layered over the art—do not ask an image model
to draw filenames or code. Build arrows, gates, timelines, and status markers
as vector shapes. Embed fonts in the PDF. If the tool cannot export PDF
directly, build editable slides first and then export.

TECHNICAL ACCURACY
- No product code without an APPROVED spec.
- Humans control REVIEW → APPROVED and IMPLEMENTED → VERIFIED.
- A human verifies acceptance criteria on a deployed build.
- A session follows BOOTSTRAP → PLAN → BUILD → VERIFY → DOCUMENT →
  HANDOFF → PUSH. The handoff commit is made before the branch is pushed.
- STATE.md is overwritten; LEDGER.md is append-only.
- Do not invent test runs, pass counts, commits, or security outcomes.
  Display verification as a required procedure, not as a fabricated result.
- A write deploy key permits Git pushes; opening a PR through the GitHub API
  requires separate authorized credentials or a human.

AVOID
Photorealism, glossy 3D, gradients, cyberpunk glow, cute robots, stock-office
illustrations, generic beige cards, dense paragraphs, fake terminal output,
illegible code, and decorative arrows that do not describe the workflow.

FINAL CHECK
There must be exactly 20 slides. At thumbnail size, each slide's main idea
must be apparent. At full size, every identifier and arrow must be readable.
The PDF must contain selectable text and no invented evidence.
```

### Wireframe key

`H` headline · `A` illustration · `D` diagram · `C` concise copy · `K` code/identifier · `G` human-controlled gate.  
The sketches describe **visual hierarchy**, not literal boxes to draw.

---

# 2. Slide-by-slide storyboard

## ACT I — THE DOCTRINE

### 01 — The manifesto

**On-slide copy**

- `KONKAUTO / SDAD`
- **THE REPO IS THE BRAIN.**
- **THE AGENT IS THE HANDS.**
- **MARKDOWN IS THE CONTRACT.**
- `A workflow designed to outlive every agent session.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ SMALL KICKER                         01 / 20 │
│ H: THREE-LINE MANIFESTO ×7 │ A: FORGE ×5    │
│ C: ONE-SENTENCE PROMISE  │ A: FORGE         │
│ HEAVY BASELINE / RUNNING FOOTER              │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Draw a cutaway steel repository shaped like a brain-vault. From its labeled-but-text-free blueprint compartment, an industrial gloved hand forges a clean piece of software. Use enormous bone-white type on coal, one molten-orange seam connecting vault to hand, and almost no decorative detail.

---

### 02 — Why the old way breaks

**On-slide copy**

- **CHAT MEMORY IS A TRAP.**
- `Prompts evaporate. Decisions drift. Work gets rediscovered.`
- `CHAT-AS-SPEC → LOST CONTEXT`
- `UNTRACED CODE → SPEC DRIFT`
- `UNWRITTEN HANDOFF → AMNESIA`
- **Move intelligence into the repository.**

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H: THE PROBLEM                               │
│ JAGGED PANEL 1 │ JAGGED PANEL 2 │ PANEL 3    │
│     EPHEMERAL CHAT TEARS INTO EMPTY SPACE    │
│ C: THE REPOSITORY IS THE FIX                 │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Make a three-panel industrial comic page. A speech bubble disintegrates in panel one; orphaned code falls off an unmarked conveyor in panel two; an empty workstation faces a dead session in panel three. A solid repository vault spans the bottom edge, visually surviving all three failures.

---

### 03 — The complete loop

**On-slide copy**

- **THE SYSTEM, IN ONE LOOP**
- `IDEA → APPROVED SPEC → PLAN / TASK → BUILD / TEST → HANDOFF`
- `→ PUSH / PR → CI → HUMAN MERGE → DEPLOYED VERIFY`
- `The next agent resumes from committed state.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H: THE SYSTEM, IN ONE LOOP                   │
│ HUMAN LANE    IDEA ── G: APPROVE ───── MERGE │
│ AGENT LANE       PLAN → BUILD → HANDOFF → PR │
│ CI / HUMAN                         CHECK → G │
│ RETURN ARROW: COMMITTED STATE → NEXT SESSION │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Render the workflow as an overhead factory conveyor with three clearly separated actor lanes: HUMAN, AGENT, and CI. Yellow mechanical gates mark approval, merge, and deployed verification. A return belt carries committed state back to the next agent. Keep the path chronological and unobstructed.

---

## ACT II — THE CONTRACT

### 04 — Repository anatomy

**On-slide copy**

- **THE REPO IS THE MACHINE ROOM.**
- `AGENTS.md` — one entry point
- `.forge/` — state, ledger, trace
- `vision/ · brainstorm/ · knowledge/` — intent and context
- `specs/ · decisions/` — contract and decisions
- `plans/ · tasks/` — execution
- `quality/ · ops/ · .github/` — controls
- `src/ · tests/` — derived product

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H ×4          │ A/D: CUTAWAY REPOSITORY ×8  │
│ ENTRY POINT →│ BOOT / INTENT / CONTRACT    │
│              │ WORK / CONTROLS / PRODUCT   │
│ C: CODE IS OUTPUT, NOT AUTHORITY            │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Illustrate a repository as a sectional concrete-and-steel building. `AGENTS.md` is its single front door; `.forge/` is the memory room; specs are the blueprint floor; `src/` and `tests/` are the fabrication floor. Place all directory names afterward as crisp editable labels, never inside generated art.

---

### 05 — Promotion is deliberate

**On-slide copy**

- **IDEAS DO NOT SHIP.**
- `brainstorm/: SEED → GROWING → PROMOTED`
- `specs/: DRAFT → REVIEW → APPROVED`
- **Only an APPROVED spec authorizes product code.**
- `Ambiguous? Record the question. Do not guess.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ A: RAW IDEA FRAGMENTS  →  D: SPEC PRESS     │
│ SEED → GROWING → PROMOTED → DRAFT → REVIEW   │
│                         G: HUMAN APPROVAL   │
│ C: NO APPROVAL = NO CODE                    │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Show rough idea fragments being melted and cast into a sharply machined specification sheet. The sheet cannot enter the code foundry until a large yellow human-operated approval press lowers. Make the stop point unmistakable; no agent should appear to operate the approval press.

---

### 06 — A spec that can be tested

**On-slide copy**

- **A SPEC IS A TESTABLE CONTRACT.**
- `SPEC-012 / Password reset`
- `R1: 32 random bytes; store the SHA-256 token hash.`
- `R2: 30-minute TTL; expired → 410.`
- `R3: Single-use; replay → 410.`
- `AC-2: Expired token → 410; password unchanged.`
- `TEST: test_ac_2_expired_token_410`
- `Unresolved behavior → question and ADR before build.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ K: SPEC BLUEPRINT ×7  │ A: LOCK CUTAWAY ×5  │
│ R1 / R2 / R3            │ TOKEN / CLOCK      │
│ AC-2 ───────────────→ NAMED TEST            │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Produce an exploded technical drawing of a password-reset lock: a token die, SHA-256 storage chamber, 30-minute mechanical timer, and one-use latch. Draw one thick trace from the expired-token rule to AC-2 and its named test. The illustration should make “rule becomes test” comprehensible before a viewer reads every word.

---

### 07 — Human-controlled status

**On-slide copy**

- **STATUS IS THE CONTROL PLANE.**
- `DRAFT → REVIEW → APPROVED → IMPLEMENTING → IMPLEMENTED → VERIFIED`
- `AGENT: DRAFT → REVIEW; IMPLEMENTING → IMPLEMENTED`
- `HUMAN: REVIEW → APPROVED; IMPLEMENTED → VERIFIED`
- `Changed decision? Propose a new ADR or versioned DRAFT.`
- `Do not silently rewrite approved behavior or old ADRs.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ D: LIFECYCLE ── G: APPROVED ── G: VERIFIED  │
│ AGENT TRANSITIONS     │ HUMAN TRANSITIONS    │
│ ADR SHELF: PROPOSED → ACCEPTED → SUPERSEDED │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Design an industrial switchboard with six large lifecycle positions. Put physical yellow locks on APPROVED and VERIFIED, reachable only from the HUMAN side. Behind it, show a row of immutable decision plates: a newer ADR points back to the one it supersedes rather than erasing it.

---

## ACT III — THE SESSION

### 08 — One entry point reboots the agent

**On-slide copy**

- **ONE FILE REBOOTS THE AGENT.**
- `Read AGENTS.md, then:`
- `1  STATE.md`
- `2  Last 3 LEDGER.md entries`
- `3  CONVENTIONS.md + GLOSSARY.md`
- `4  specs/INDEX.md + assigned spec`
- `5  tasks/DOING/ → tasks/OPEN/`
- `6  make bootstrap && make test`
- `7  Print a five-line Session Plan`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                         K: AGENTS.md      │
│ D: SEVEN-RUNG BOOT LADDER ×8 │ A: SWITCH ×4 │
│ 01 → 02 → 03 → 04 → 05 → 06 → 07            │
│ C: START WITH REPO STATE, NOT CHAT MEMORY   │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Make `AGENTS.md` a massive master switch feeding seven numbered conduits into an otherwise dark industrial control room. The sixth conduit ends at a baseline test gauge; the seventh lights a Session Plan display. Typeset filenames and commands as a separate overlay.

---

### 09 — From plan to mergeable task

**On-slide copy**

- **PLANS TURN SPECS INTO WORK ORDERS.**
- `SPEC-012 → PLAN-004 → T-032`
- `T-032: reset-confirm expiry and single-use`
- `ACs: AC-2, AC-3`
- `Branch: feat/T-032-reset-confirm`
- `Verify: pytest tests/auth/test_reset.py -k "ac_2 or ac_3" -v`
- `Out of scope: rate limiting (T-033)`
- **One task = one mergeable unit.**

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ SPEC REEL → PLAN REEL → K: T-032 CARD ×7    │
│                         ACs / BRANCH / SCOPE │
│ FULL-WIDTH VERIFICATION COMMAND             │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Illustrate the plan as a manufacturing reel feeding a single punched-metal work order, `T-032`. Give the card clearly distinct slots for its ACs, branch, verification, and excluded work. One finished component exits the machine—not a heap of vaguely related features.

---

### 10 — One session, seven moves

**On-slide copy**

- **ONE SESSION. SEVEN MOVES.**
- `01 BOOTSTRAP → 02 PLAN → 03 BUILD → 04 VERIFY`
- `→ 05 DOCUMENT → 06 HANDOFF → 07 PUSH`
- `BUILD: failing AC test → implementation → green`
- `HANDOFF: final commit before push`
- `PUSH: feature branch, then PR`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│        D: SEVEN-TOOTH INDUSTRIAL RATCHET     │
│     01 → 02 → 03 → 04 → 05 → 06 → 07        │
│ RED→GREEN AT BUILD    FINAL COMMIT AT 06    │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Draw an enormous seven-tooth steel ratchet occupying nearly the full slide. Each tooth represents one chronological move. At BUILD, a red test indicator turns evidence green; at HANDOFF, a ledger cassette clicks into place; only then does the PUSH lever engage. Make this the deck’s central hero diagram.

---

### 11 — Verification is evidence

**On-slide copy**

- **DONE MEANS EXIT 0.**
- `AC-2 → test_ac_2_expired_token_410`
- `FAILING TEST → IMPLEMENT → PASSING TEST`
- `Then: targeted verification · full suite · lint · typecheck · secret scan`
- `Paste the actual command, exit code, and summary into the PR.`
- **“Looks good” is not evidence.**

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ RED: EXPECTED FAIL │ GREEN: REQUIRED PASS    │
│      TEST → CODE   │ FULL CHECK CHAIN → PR  │
│ C: ACTUAL OUTPUT REQUIRED; NONE INVENTED    │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Create a sharply divided two-page comic spread: red test-first failure on the left, green verified build on the right. Across the seam, a single AC-shaped bolt becomes a named test, then working code. Depict command output as a blank evidence slot to be filled by a real run—never fabricated terminal lines.

---

### 12 — Bidirectional traceability

**On-slide copy**

- **EVERY LINK WALKS BOTH WAYS.**
- `SPEC-012 ↔ PLAN-004 ↔ T-032`
- `↔ feat/T-032-reset-confirm ↔ COMMIT`
- `↔ test_ac_2_expired_token_410 ↔ SPEC-012`
- `src/auth/reset.py → # SPEC-012`
- `.forge/TRACE.md maintains the audit map.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ D: CLOSED DOUBLE-ARROW TRACE CIRCUIT        │
│ SPEC ↔ PLAN ↔ TASK ↔ BRANCH ↔ COMMIT ↔ TEST │
│      SOURCE FILE ─────→ SPEC ID              │
│ K: TRACE.md / AUDIT MAP                     │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Build a precise reversible transit map from six heavy steel stations, with two-way arrows and no crossing lines. A smaller line brings `src/auth/reset.py` back to `SPEC-012`. The loop must visually prove that a reviewer can start with either the spec or the test and find the other.

---

### 13 — The handoff is the memory

**On-slide copy**

- **THE HANDOFF IS THE MEMORY.**
- `STATE.md — current snapshot; overwrite`
- `LEDGER.md — session history; append only`
- `TRACE.md — update changed links`
- `tasks/ — move files to their true status`
- `Commit handoff LAST → push branch.`
- `Next agent reads the state and latest ledger entries.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ AGENT A → [STATE SNAPSHOT] [LEDGER SCROLL]   │
│          [TRACE MAP] → LAST COMMIT → PUSH    │
│                                    → AGENT B │
│ C: THE SESSION ENDS; THE RECORD PERSISTS    │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Stage a change of shift at a brutalist workstation. One agent silhouette disappears after sealing a snapshot plate, an append-only scroll, and a trace map into a repository cassette. A new silhouette plugs into that same cassette. Put the last-commit seal immediately before the push arrow.

---

## ACT IV — THE GUARDRAILS

### 14 — Branch, PR, human merge

**On-slide copy**

- **MAIN NEVER BELONGS TO THE AGENT.**
- `feat/T-###-slug → PR → protected main`
- `PR: task · spec · ACs · plan · actual verification · risks`
- `No direct push to main. No force-push to protected branches.`
- `A human merges.`
- `After deployed AC checks, a human marks the spec VERIFIED.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ FEATURE RAIL ──→ PR INSPECTION ──→ G: MERGE │
│ MAIN RAIL ═════════════ PROTECTED ═════════│
│                              DEPLOY → G: ✔ │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Draw two railway tracks. The feature branch approaches a PR inspection booth; the protected `main` track remains behind a heavy barrier. Only a human-operated yellow switch can merge them. Farther down the main track, show a separate deployed-build verification gate—not the same gate as merge.

---

### 15 — CI as an inspector

**On-slide copy**

- **CI IS AN INSPECTOR, NOT A CHEERLEADER.**
- `Required: test · lint · typecheck · secret-scan · forge-lint`
- `forge-lint rejects:`
- `src/ without a spec link`
- `IMPLEMENTED AC without a named test`
- `Invalid document frontmatter`
- `DOING task stale for >48 hours`
- `Source change without a LEDGER append`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ A: FIVE-BEAM CI SCANNER ×5 │ REJECT LIST ×7 │
│ TEST / LINT / TYPE / SECRET / FORGE           │
│ PASS ───────────────────────→ HUMAN REVIEW   │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Make CI a harsh industrial X-ray tunnel with five distinct inspection beams. The `forge-lint` beam exposes five specific defects as silhouettes on a diagnostic wall. Passing components continue toward human review; rejected ones return to the branch. Do not show an unearned green pass result.

---

### 16 — Write access as a lease

**On-slide copy**

- **WRITE ACCESS IS A LEASE.**
- `Generate one ed25519 key per agent/workspace—outside the repo.`
- `Register only its public key as a one-repo write deploy key.`
- `ops/KEYS.md stores fingerprint, dates, and status—not secrets.`
- `Rotate every 30 days; protect main.`
- `Deploy key = Git push. PR API access needs separate authorization.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ PRIVATE VAULT │ PUBLIC-ONLY CABLE → REPO KEY │
│ OUTSIDE REPO  │ ONE REPO / ONE WORKSPACE     │
│ 30-DAY DIAL   │ PROTECTED MAIN BARRIER       │
│ C: PR API IS A SEPARATE AUTHORIZATION        │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Illustrate a private key locked in a vault visibly outside the repository boundary. Only a public-key-shaped metal conduit crosses into a single GitHub repository dock. Add a 30-day rotation dial and an immovable protected-main barrier. Show a separate, smaller hatch for PR API authorization to prevent conflating it with Git push access.

---

### 17 — Separation of duties

**On-slide copy**

- **DIFFERENT HANDS. DIFFERENT POWERS.**
- `ARCHITECT — drafts specs, ADRs, plans`
- `BUILDER — implements approved specs and tests`
- `REVIEWER — audits the PR against the spec`
- `AUDITOR — reads broadly; writes audit findings only`
- **A builder does not review its own task.**
- `Humans own approval, merge, and verification.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ ARCHITECT ×6       │ BUILDER ×6              │
│ REVIEWER ×6        │ AUDITOR ×6              │
│ FULL-WIDTH RULE: NO SELF-REVIEW              │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Create four distinct graphic-novel workstations: blueprint table, code foundry, inspection bench, and archive. Give each role a different tool and an explicit visual boundary. A thick crossed line between Builder and Reviewer should make the no-self-review rule immediate, without depicting agents as cute robots.

---

### 18 — When the crank stalls

**On-slide copy**

- **FAIL CLOSED. RECOVER IN WRITING.**
- `AMBIGUOUS → mark BLOCKED; move task to REVIEW; ask.`
- `BASELINE RED → report before building.`
- `SESSION DIES → resume from committed STATE + LEDGER.`
- `KEY SUSPECT → revoke, rotate, inspect activity.`
- **Never substitute a guess for a record.**

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│ FRACTURE 1 → RECOVERY │ FRACTURE 2 → RECOVERY│
│ FRACTURE 3 → RECOVERY │ FRACTURE 4 → RECOVERY│
│ C: EVERY FAILURE HAS A REPOSITORY PATH      │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Draw four jagged incident panels around one intact central repository: ambiguity, failing baseline, dead session, and suspect key. Each panel must have a clear recovery arrow into a written action. Use orange for the break and yellow or green only for the controlled recovery.

---

## ACT V — ADOPTION

### 19 — The maturity ladder

**On-slide copy**

- **FIVE TIERS OF RELIABILITY**
- `1 AD-HOC — prompts as memory`
- `2 STRUCTURED — AGENTS.md + handoffs`
- `3 TRACEABLE — IDs, AC tests, forge-lint`
- `4 GOVERNED — human gates, ADRs, key rotation`
- `5 SELF-IMPROVING — metrics + retrospectives`
- `Measure spec-to-merge time, rework, and blocked-task rate.`

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H                                            │
│                         ┌── TIER 5 / METRICS│
│                  ┌──────┘ TIER 4 / GOVERNANCE│
│           ┌──────┘ TIER 3 / TRACEABILITY    │
│    ┌──────┘ TIER 2 / STRUCTURE               │
│ ───┘ TIER 1 / AD-HOC                         │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Construct a five-level staircase from raw concrete into increasingly disciplined steel infrastructure. Each level adds a real capability—handoff cabinet, trace rails, human-controlled gates, then measurement instruments. Keep Tier 5 analytical rather than utopian; it improves the process using measured evidence.

---

### 20 — The operating command

**On-slide copy**

- **START WITH ONE FILE.**
- **CONTINUE WITH ONE LINE.**
- `FIRST SESSION: Scaffold AGENTS.md, .forge/, templates, and forge-lint. No product code.`
- `THEN: “Read AGENTS.md and execute the session protocol. Priority: T-032, then T-033. Role: BUILDER.”`
- **SESSIONS END. THE SYSTEM DOES NOT.**

**Wireframe**

```text
┌──────────────────────────────────────────────┐
│ H: TWO-LINE CLOSING CLAIM ×7 │ A: VAULT ×5  │
│ K: FIRST-SESSION COMMAND                      │
│ K: RECURRING ONE-LINE COMMAND                 │
│ FINAL FULL-BLEED STATEMENT / 20 OF 20         │
└──────────────────────────────────────────────┘
```

**Unique slide prompt:** Return to the repository vault from slide 01, now complete and quietly operating. One worker exits; another enters and reads the same illuminated `AGENTS.md` entry point. Carry the molten-orange seam from the first slide through the vault and end it in a solid, unbroken line. Make the final statement monumental, not sentimental.

---

## 3. PDF acceptance check

Before delivery, verify:

- **20 slides exactly**, in the specified order.
- Filenames, statuses, IDs, commands, and actor permissions are correct.
- Handoff appears **before** push; deployed human verification appears **after** merge.
- No fictional test output or pass counts appear anywhere.
- Text is selectable; diagrams and essential arrows remain sharp when zoomed.
- Every slide communicates its main point at thumbnail size—and every technical label is readable at presentation size.
