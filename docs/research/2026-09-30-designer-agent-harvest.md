# Designer-Agent Retrospective Harvest: Salvage + Unmarked Valley

Date: 2026-09-30. Scope: findings from the salvage prototype, the Unmarked Valley prototype (iterations 1-2), their independent reviews/verifications, and the user's Player Validation reports. Classification key: `contract gap` ([agents/game-designer.md](../../agents/game-designer.md)), `skill gap` (`.agents/skills/*/SKILL.md`), `template gap` (skill templates), `one-off execution error` (no instruction change warranted). The user approved applying all eight diffs ("All", 2026-09-30). Each finding below now records where its diff landed.

## Findings and Proposed Changes

### F1. Drawn geometry and collision geometry diverged

- Evidence: iteration-1 review — drawn trees walkable, invisible rock corners blocked, terrain trees rendered but never collidable ([valley-review.md](../designs/browser-exploration/evidence/valley-review.md)).
- Classification: **skill gap** (system-design) + **template gap** (validation-plan).
- Proposed diff: in `system-design/SKILL.md` Specify section, add: "When a visual prototype is in scope, require drawn and collidable geometry to share one authoritative source or an explicit footprint mapping; state any permitted decorative overhang (e.g. tree canopy vs trunk) explicitly." In `design-prototype/templates/validation-plan.md` Evidence Plan, add a check row: rendered-vs-collider correspondence, deterministic probe points. **Applied** to both files (system-design Specify step 3 also gained the ground-level readability prompt from F4).

### F2. Transient UI state survived reset until the next frame

- Evidence: stale place-name feedback after restart (same review).
- Classification: **skill gap** (system-design edge-case coverage).
- Proposed diff: `system-design/SKILL.md` step 2 — reset/restart rules must enumerate transient presentation state (labels, feedback, timers), not just simulation state. **Applied.**

### F3. Movement speed became frame-rate dependent below 20 fps

- Evidence: per-frame delta cap discarded active time; only review caught it because tests assumed 60 fps.
- Classification: **skill gap** (system-design timing semantics).
- Proposed diff: `system-design/SKILL.md` step 1-2 — time-based rules must state elapsed-time integration explicitly (fixed-step, catch-up limit, and what happens on stall/resume), so implementers cannot silently pick a cap with different gameplay meaning. **Applied** to Specify step 2.

### F4. Misleading affordances and topology leaks

- Evidence: path drawn into uncrossable water; stream bypassable around its north end; lower bridge exit tighter than its visual width ([valley-verification.md](../designs/browser-exploration/evidence/valley-verification.md)).
- Classification: **template gap** (validation-plan evidence rows) + **skill gap** (system-design readability rules).
- Proposed diff: validation-plan Evidence Plan gains rows for (a) affordance honesty — drawn routes must not imply blocked traversal; (b) intended-connection integrity — required connections exist and cannot be bypassed around authored endpoints. `system-design` gains a readability requirement prompt: obstacles, boundaries, and connections must read correctly at ground level. **Applied** to both files.

### F5. Pure rule tests passed while the real loop crashed

- Evidence: `nearestLandmark` omitted from the world export; 4 grouped tests green, RAF dead on load ([iteration-2-runtime-regression.json](../designs/browser-exploration/evidence/iteration-2-runtime-regression.json)).
- Classification: **skill gap** (design-prototype verification requirements). Already noted in validation.md as a process lesson; promoted here to a durable instruction change.
- Proposed diff: `design-prototype/SKILL.md` — after "run deterministic rule checks before presenting outcomes", add: "for any interactive prototype, also run a real game-loop/render smoke check that collects page/console errors and exercises actual input through the live loop; helper-level tests alone cannot establish playability." **Applied.**

### F6. Appeal validation tested only the start of play, not its continuation

- Evidence: salvage — user confused, theme unappealing, sequence obvious. Valley — user curious at first, bored once landmarks gave no reward (U3/U4 in [validation.md](../designs/browser-exploration/validation.md)). Both prototypes predicted their own uncertainty correctly, but neither plan tested sustained interest until the user played.
- Classification: **skill gap** (gameplay-design) + **template gap** (gameplay-proposal).
- Proposed diff: `gameplay-design/SKILL.md` step 5 — the validation question must name two separate observable signals: initial attraction (does the player start/investigate unprompted) and sustained interest (does the player continue or return after the first payoff-free moment). `templates/gameplay-proposal.md` Core loop row — the risk column must answer "what brings the player back after the first discovery; if nothing, say so explicitly." **Applied** to both files.

### F7. Over-built response to a presentation problem

- Evidence: when the salvage scene didn't read as a ship, the user observed "a legend is a more easy solution, isn't it?" — the simpler fix was available and preferred.
- Classification: **one-off execution error** with a generalizable contract note.
- Proposed diff: `agents/game-designer.md` — under prototype work, prefer the minimal presentational change that resolves a comprehension/legibility finding before structural rework. One sentence; no new checkpoint. **Applied** to the confirmation/prototype paragraph.

### F8. First-session observation sequencing

- Evidence: valley's validation plan separated unassisted exploration from later questions and worked; salvage's confusion was diagnosed live without a planned unassisted-observation step.
- Classification: **template gap** (mild). The validation-plan template already has unassisted/assisted rows; the gap is that no rule requires running the unassisted session *before* any explanation reaches the player.
- Proposed diff: `design-prototype/SKILL.md` — when Player Validation is planned, the first play session must be unassisted and recorded before any designer explanation; explanation afterwards is diagnostic only. **Applied.**

## Positive Patterns (keep)

- Budget ledger with absolute stop caught iteration misuse and forced explicit re-authorization.
- Independent reviewer + independent tester split caught defects the implementer's own suite missed (F1-F5 all surfaced through independent eyes).
- Preserving negative evidence (failed iteration-1 screenshots, runtime-regression JSON) made the correction pass auditable.

## Application Record

All eight diffs applied 2026-09-30 after the user's "All" approval. Files touched: `agents/game-designer.md`, `.agents/skills/system-design/SKILL.md`, `.agents/skills/design-prototype/SKILL.md` + validation-plan template, `.agents/skills/gameplay-design/SKILL.md` + gameplay-proposal template. No checkpoints, approvals, or project records changed. Instruction compliance is not guaranteed by these edits; the next behavioral exercise (e.g. the experience-selection scenarios) can check whether the new instructions change outputs.
