# Gameplay Revision: Unmarked Valley v2 — Arrival Payoff + One Micro-Interaction

Date: 2026-09-30. Record type: revised gameplay proposal for a selected concept (Candidate A), per user approval 2026-09-30 09:25 UTC of scope and budget (2 hours, 1 iteration, zero spend). Approval reference: user's "Approved" reply to the change-impact proposal. Classification key: sourced fact | Design Assumption | Player Validation | rule verification.

## Direction Record

- Concept status: selected with explicit reference (U2, revised per 2026-09-30 approval).
- Primary creative priority: self-directed spatial exploration (unchanged).
- Intentional sacrifice: compact place, one payoff per landmark, exactly one micro-interaction verb (unchanged in kind, widened from move-only).
- Why no new candidate comparison: bounded in-scope fix to a selected concept (gameplay-design step 3); the rejected alternative was expansion with more content, which U4 evidence forbids.

## What Changed and Why (evidence-backed)

Player Validation U3/U4: landmarks attract initial curiosity but arrival yields nothing, so sustained interest collapses. Two deltas approved: arrival payoff (D-1) and richer traversal (D-2), combined in one slice.

## Core Experience (revised)

| Item | Proposal | Classification | Risk / open question |
| --- | --- | --- | --- |
| Target player | The user as first evaluator | sourced fact | Does not generalize |
| Intended experience | Choose a destination freely; arriving reveals something worth finding; the walk there has at least one moment of physical play | Design Assumption | Payoff quality determines everything; a bad reveal is worse than none |
| Core loop | Notice landmark → pick route → travel (optionally use the micro-interaction) → arrive and trigger a reveal → decide whether the next landmark is worth it | Design Assumption | **Return pull: one reveal per landmark, no repeat content. If reveals don't compel, sustained interest still fails. Say so explicitly: nothing else brings the player back.** |
| Observable outcome | At each landmark, a visible/audible reveal event (not a modal, not a score) | Design Assumption | Must not read as a checklist of collectibles |

## Revised Content (smallest slice)

- Three arrival reveals, one per landmark: tower interior revealed on entry (light/camera/view change inside the ruin), stream-crossing scene (stepping stones shift / splash / brief water parting), grove detail (a hidden object or clearing revealed among trees).
- Exactly one micro-interaction verb: push. One pushable log that, when pushed into the ditch/stream narrows, becomes a walkable shortcut plank. No other interactions.
- Map, movement, camera, bridges, restart unchanged from system.md v1.1 except as required by the above.

## Prototype Scope and Checkpoint (revised; confirmed 2026-09-30 09:25 UTC)

- Validation question, two signals (per F6):
  - Initial attraction: does the user investigate a landmark unprompted after seeing the world?
  - Sustained interest: after the first reveal, does the user voluntarily seek another landmark?
- Minimum playable content: v1.1 prototype + three reveals + one pushable log shortcut.
- Maximum iterations: 1. Time limit: 2 hours from 09:25:47 UTC (absolute stop 11:25:47 UTC). Spending: zero.
- Local technology: same static Canvas/JS; no new dependencies.
- Excluded work: score, inventory, quest log, collectibles counter, additional verbs, new map, audio assets requiring network, touch controls.
- Combined core-gameplay/prototype-scope checkpoint: **confirmed** by the user's 2026-09-30 "Approved" (covers D-1, D-2, D-3, and the 2h/1-iteration/zero budget).
- Stop criterion: if the user does not voluntarily seek a second landmark after the first reveal, the direction stops without automatic content addition.

## Handoff

To system-design: revise R06 (permit arrival reveal events; still forbid score/modal/assigned destination/checklist framing), add push-verb rule IDs, and enumerate reset/transient state for reveals and the log. To design-prototype: validation plan must include rendered-vs-collider probes, affordance honesty, connection integrity, real game-loop smoke check with page errors, and an unassisted first play session (F1/F4/F5/F8).
