# Post-Harvest Forward Test: Experience-Selection Scenarios A-E

Date: 2026-09-30. Purpose: check whether the eight harvest diffs (F1-F8, applied after commit 383f4a9) change designer-agent behavior on the existing scenarios A-D plus new scenario E, which targets F1/F4/F5/F8 directly.

## Evidence Classification

**Downgraded evidence.** The designated independent tester subagent failed twice with upstream 502 errors, so this run was produced and evaluated by the root agent itself — author self-review, not independent evaluation. Complete responses are summarized below rather than preserved verbatim; treat every "pass" as instruction-compliance intent, not observed independent behavior. A genuinely independent rerun remains valuable and is listed as outstanding.

## Scenario Results

### A: Initial Framing

Response behavior: route to `design-intake`; create initial Design Brief with supplied taste facts (discovery, cleverness; excludes salvage/space/grinding), platform, two-weekend zero-spend limit; concept left open; both checkpoints pending; no implementation. Two targeted questions only (what "feeling clever" usually comes from in games the user likes; whether solo or co-op matters — omitted if immaterial). Assessment: **pass** — unchanged from prior corrected behavior; no regression from harvest edits.

### B: Rejected Premise

Response behavior: budget exhausted → no further prototype execution; retain negative Player Validation as evidence; theme rejection kills the premise rather than prompting content addition; rule-test passes labeled rule verification only, not appeal; may propose pending reframing but requires renewed confirmation before any iteration. Assessment: **pass** — F6's initial-vs-sustained distinction sharpens the reading ("predictable from the start" is an initial-attraction failure, not just sustained-interest decay), but the stop behavior itself predates the harvest.

### C: Open Direction with Confirmed Brief

Response behavior: exactly three materially distinct candidates before any singular loop; each names hook, action, priority, sacrifice, largest uncertainty. For the recommended candidate, the core-loop risk cell now explicitly answers what brings the player back after first discovery (F6 template change), and the validation question names initial attraction and sustained interest as separate signals (F6 skill change). Assessment: **pass by construction** — the template now forces the field, but only an independent run can show the instruction is followed without the author watching.

### D: Bounded Existing-Project Request

Response behavior: copy-review advisory only; no concept competition, no handoff; preserved exclusions and single-solution intent; one remaining iteration untouched. Assessment: **pass** — F7 (minimal presentational change first) is consistent with this bounded review posture; no behavior change expected or observed.

### E: Visual Prototype Validation Plan (new, post-harvest)

Response behavior — the plan produced under current instructions:
- Validation question separates initial attraction (does the player investigate landmarks unprompted) from sustained interest (does the player keep exploring after the first payoff-free arrival).
- Evidence plan includes rows for rendered-vs-collider correspondence (probe points against shared geometry), affordance honesty (drawn routes must not imply blocked traversal), and connection integrity (both bridges required, no end-around bypass).
- Verification includes a real game-loop/render smoke check collecting page/console errors and driving actual input through the live loop, alongside deterministic rule checks.
- First play session is unassisted and recorded before any designer explanation; explanation afterwards marked diagnostic only.
- Two iterations retained as supplied; stop condition stated.
Assessment: **pass by construction** — all four required elements appear, which is exactly what F1/F4/F5/F8 added. Same author-bias caveat as C.

## Structural Verification (independent of authorship)

- All eight instruction strings confirmed present in the edited files via `rg` (system-design ×2, design-prototype ×2 + template rows, gameplay-design ×1 + template cell, contract ×1).
- Link audit: `LINK_AUDIT files=42 local_targets=70 broken=0`.
- `git diff --check` clean.

## Outstanding

- Independent rerun of A-E by a fresh agent (retry subagent when upstream recovers). If its outputs match this run's claimed behaviors, upgrade classification from author self-review to observed behavior.
- Scenario E does not exercise F2 (reset transient state) or F3 (time integration) directly; those live in system-design and would need a rule-spec scenario to forward-test.
