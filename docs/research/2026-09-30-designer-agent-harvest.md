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

## B-Structure Harvest (2026-10-08)

### F9. Accessibility is not authorship

- Evidence: Three Stones U1/U2/U3/U4 in [tidal-garden/validation.md](../designs/tidal-garden/validation.md). Two geometry defects were fixed: first the stones were unreachable, then a successful mid-stone push trapped the player. After both fixes the user reported: "It only makes it accessible, not creative." The operation opened a pre-authored route but did not create materially different routes, spatial states, or outcomes.
- Classification: **skill gap** (gameplay-design) + **template gap** (validation-plan).
- Applied diff: `gameplay-design/SKILL.md` requires every agency/build mechanic to state what player-authored state differs after each choice and what alternative outcome becomes possible; "opens access" alone is not sufficient evidence of authorship. `design-prototype/templates/validation-plan.md` adds an authorship evidence row asking whether the player can describe a route, space, or result as their own creation rather than a route they unlocked.
- Decision rule: if the user reports access without authorship, stop the direction as-is. Do not respond by adding more identical interactables or content; revise the mechanic so choices produce materially different routes or consequences, then seek a new scope/budget checkpoint.

Applied 2026-10-08 after the user's approval. It is the first harvest item explicitly derived from a failed structural hypothesis rather than a runtime or presentation defect.

## Cross-Prototype Harvest: B Structure + Risk Rhythm (2026-10-08)

Scope: Three Stones U1-U4, Echo Caves U1-U2, and implementation/verification records. The user approved application on 2026-10-08; the entries below describe the resulting changes.

### F10. An entrance needs a specific promise, not merely presence

- Evidence: Echo Caves U1 found branch cues weak; U2 found the revised visible pulse/current/silhouette cues worked better.
- Classification: **skill gap** (`gameplay-design`) + **template gap** (`gameplay-proposal`).
- Applied diff: every optional destination or branch now states the player-visible promise before entry, the unresolved question it creates, and how it differs from sibling choices. A named branch, colored tunnel, or generic darkness is not a promise.

### F11. Validate the promise-to-payoff chain, not each end independently

- Evidence: Echo Caves U1: a noticeable first-branch payoff motivated a second entry, while its original entrance cue did not. The cue revision improved attraction.
- Classification: **template gap** (`validation-plan`) + **skill gap** (`design-prototype`).
- Applied diff: the validation plan and `design-prototype` now require `notice cue -> enter or avoid -> encounter payoff or retreat -> choose next opportunity`, including the actual stated or observable reason for the next choice. A reveal in isolation is not evidence that its entrance promise worked.

### F12. Separate atmospheric pressure from punishment and numeric management

- Evidence: Sunlight Shelf U1 and Echo Caves U1 reported pressure as atmosphere, not forced resource management. The brief excluded an oxygen meter deliberately.
- Classification: **skill gap** (`gameplay-design` and `system-design`).
- Applied diff: gameplay framing and the system specification now classify tension/pressure as `atmospheric cue`, `spatial commitment`, `punishment/fail state`, or `numeric resource`, including what is deliberately excluded. Atmospheric pressure cannot be silently replaced with a countdown or meter.

### F13. Interaction verification must cover approach, success, and exit

- Evidence: Three Stones U1: stone unreachable. U2: successful stone push trapped the player. Existing helper tests and topology checks did not exercise the complete player path.
- Classification: **template gap** (`validation-plan`) + **skill gap** (`design-prototype`).
- Applied diff: every claimed interaction requires live-path evidence: `approach with actual input -> initiate -> complete success state -> leave the changed state`. Debug teleportation or helper-only calls do not qualify.

### F14. Apply accessibility-is-not-authorship as an active rule

- Evidence: Three Stones U4: "It only makes it accessible, not creative." F9 recorded the lesson but remains proposal-only.
- Classification: **skill gap** (`gameplay-design`) + **template gap** (`validation-plan`).
- Applied diff: any build, reshape, or agency mechanic must name at least two materially different player-authored spatial states, routes, or outcomes. The Player Validation prompt asks what changed and what it enabled. "I opened the intended route" fails authorship and stops the direction rather than adding identical gates.

### F15. Relative improvement is not full success

- Evidence: Three Stones U3 and Echo Caves U2: "works a bit better" / "works better now." Both show directionally useful improvement but do not identify strength, transferability, or whether all choices work.
- Classification: **contract gap** (evidence classification) + **template gap** (`evidence-log`).
- Applied diff: the contract and evidence-log template add `relative improvement only` as an evidence qualifier. It may support a bounded revision surviving, but cannot by itself establish appeal, comprehension, balance, accessibility, or production readiness. It records the baseline, observed improvement, and still-unproven signal.

### F16. Independent verification failure needs a durable fallback record

- Evidence: Unmarked Valley v2, Sunlight Shelf, Three Stones, and Echo Caves were root-implemented/self-verified after worker agents failed with provider 502 or encrypted-content errors.
- Classification: **skill gap** (`design-prototype`) + **template gap** (`evidence-log`); not a game-design failure.
- Applied diff: when independent implementation, review, or testing is unavailable, the evidence log records the failed delegation or unavailable capability, self-verification scope, and deferred independent recheck. It cannot be silently treated as independent evidence.

## Application Record

F9-F16 were applied 2026-10-08 after the user's approval. Files touched: `agents/game-designer.md`, `.agents/skills/gameplay-design/SKILL.md` + gameplay-proposal template, `.agents/skills/system-design/SKILL.md` + system-specification template, and `.agents/skills/design-prototype/SKILL.md` + validation-plan/evidence-log templates. The changes are additive and do not alter approval checkpoints. They require future behavioral validation; documentation compliance alone is not evidence that a future agent will apply them correctly.
