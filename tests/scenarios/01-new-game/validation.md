# Constructed Prototype Validation: Latchline Salvage

## Authority and Classification

This record consumes the authoritative fixture rules in `tests/scenarios/01-new-game/design.md`. The input, approvals, and checkpoint references are constructed: prototype-scope approval is `SIMULATED USER APPROVAL S2, 2026-09-30`. This is local rule verification and developer observation, not Player Validation or evidence of production readiness.

## Authorized Scope and Stop Condition

| Item | Record |
| --- | --- |
| Validation question | Can a player identify the `Retrieve`, `Stabilize`, `Retrieve` route from visible outcomes? |
| Minimum playable content | One direct-open browser screen with three sections, actions, hull/cargo, log, terminal result, and restart. |
| Fidelity | Original static SVG wreck view, keyboard-accessible native buttons, and deterministic rules; no final art, music, research, or localization. |
| Scope decision | Within simulated S2 scope; local-only execution, no network deployment or uploads. |
| Spending | `$0` actual spend; within the `$0` simulated limit. |
| Time limit | Not estimated in the fixture; no estimate is asserted here. |
| Iteration limit | `2` maximum. Stop after the second recorded iteration. |
| Stop condition | Required deterministic and browser checks recorded, or the iteration budget reached. |

## Iteration Accounting

| Iteration | Change or check | Evidence | Result | Budget remaining |
| --- | --- | --- | --- | --- |
| 1 | Implemented the rule module and static local UI after a clean missing-module red test. | `prototypes/salvage/tests/test_salvage.py`; base `dc98f2d` plus Task 3 working tree. | Eight browser-executed checks passed. | 1 |
| 2 | Inspected terminal screenshot; corrected the disabled-action focus state, then recaptured evidence. | `prototypes/salvage/evidence/desktop-extracted.png`; base `dc98f2d` plus Task 3 working tree. | Disabled actions no longer appear selectable; checks passed. | 0 |

## Actual Evidence

| Date | Input or command | Observed output | Artifact/log path and version | Classification | Limitation or negative result |
| --- | --- | --- | --- | --- | --- |
| 2026-09-30 | `PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python -m unittest prototypes/salvage/tests/test_salvage.py` before implementation | `FAIL`: `Latchline Salvage needs its reusable browser rules module`; seven dependent tests skipped. | Terminal log; base `dc98f2d`, before `salvage-rules.js`. | rule-verification setup / expected red | An earlier preliminary run had Playwright environment lifecycle errors; those were corrected while production files were still absent, then the clean red above was captured. |
| 2026-09-30 | Same unittest command after iteration 1 and again after iteration 2 | `Ran 8 tests ... OK`. Covers `V-01` to `V-05`, hull-priority loss, terminal no-op, hull cap, UI win/restart, and render no-state-change. | `prototypes/salvage/tests/test_salvage.py`; base `dc98f2d` plus Task 3 working tree. | rule verification | Rule tests do not establish player comprehension, fun, balance, or accessibility completeness. |
| 2026-09-30 | `PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python prototypes/salvage/tests/capture_evidence.py` | Desktop/mobile no horizontal overflow or console errors; render unchanged; visible extracted, hull-breach, and cargo-target-missed terminals passed. | `prototypes/salvage/evidence/desktop-initial.png`, `desktop-extracted.png`, `mobile-initial.png`; base `dc98f2d` plus Task 3 working tree. | developer observation | Browser automation is not a player study. |

## Planned and Outstanding Validation

The fixture's validation question remains a Design Assumption. No participant was asked to identify the winning route, explain a choice, or report enjoyment; no Player Validation occurred. A separately approved player test should present the visible actions without coaching, record route selection and explanation, and retain misunderstood outcomes as negative evidence.

Verification cases in the authoritative design were simulated expected results before the recorded commands above. This record promotes only the cases exercised by those commands; all other planned cases remain `not run / expected outcome` until they have an actual command or input, observed output, artifact or log path, and version.
