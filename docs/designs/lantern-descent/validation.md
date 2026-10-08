# Echo Caves: Validation and Budget

Authority: brief.md, gameplay-proposal.md, system.md v1.0. Start: 2026-10-08 06:55:15 UTC. Absolute stop: 08:55:15 UTC. One iteration, zero spend.

## Experience Question

Initial attraction: does the player voluntarily enter a cave branch? Sustained interest: after the first reveal or retreat, do they choose another branch? Pressure reading: does darkness/narrowing feel atmospheric rather than like numeric oxygen management?

## Implementation and Rule Verification

Completed locally in the approved first iteration. Three browser tests pass: distinct branch cues/reveals, swim inertia/coast/stop, and live keyboard movement/reset without page errors.

Real-browser smoke: entered the Warm Glow branch, triggered its one-time reveal and place feedback, voluntarily returned to the surface, retained the reveal state, and observed zero page/console errors. Screenshots: `prototypes/echo-caves/tests/evidence/surface.png` and `glow-reveal.png`.

Delegation limitation: this implementation was completed in-thread. The earlier worker routing failures in this workspace remain an independence limitation; no claim of independent review is made.

## Player Validation

**U1 report (2026-10-08, current conversation):** The user reported that the branch cues were not very attractive (with the caveat that this is a prototype), but did enter a second branch because the first branch ended with noticeable feedback. The pressure felt atmospheric.

Interpretation by F6 signals:
- Initial attraction: **weak / not established**. The branch entrances did not create enough pull on their own.
- Sustained interest: **partial pass**. A noticeable payoff at the end of the first branch motivated another branch.
- Pressure reading: **pass**. Darkness/narrowing read as atmosphere, not forced resource management.

Decision: **revise**, not stop. The risk-and-release structure has evidence of potential, but the cue/reward chain is weak at the entrance. Do not expand the cave or add more branches yet; a future revision should first make branch promises legible and specific, then retest whether the player enters because of the cue rather than only because the previous branch happened to pay off. This validation used the full approved 2-hour / 1-iteration budget; any revision requires a new scope and budget checkpoint.

### Cue Revision (approved 2026-10-08 08:18 UTC)

Bounded revision: strengthen the existing three branch entrances only, with no new branch, map, mechanic, dependency, or content system. The warm branch now visibly pulses with bioluminescent orbs; the drift branch shows directional particles and current; the shadow branch shows a moving silhouette. Existing endpoint reveals remain unchanged.

Verification: 3 tests pass; final browser smoke entered the Warm Glow branch, triggered its reveal, returned to the surface, and reported zero page/console errors. Evidence: `prototypes/echo-caves/tests/evidence/surface.png` and `glow-reveal.png` (updated revision captures).

Player Validation after the cue revision: not performed. The next unassisted play should test whether the revised entrance cues create initial attraction before interpreting the earlier partial sustained-interest result.
