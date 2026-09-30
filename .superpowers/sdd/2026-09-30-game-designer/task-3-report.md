# Task 3 Report: Prototype and Evidence

## Delivered

- Added `.agents/skills/design-prototype/` with a route contract and validation/evidence templates. The reusable workflow preserves a project-provided iteration cap and does not hardcode the fixture's maximum of two.
- Added direct-open, dependency-free `prototypes/salvage/index.html` and its reusable `salvage-rules.js`. The UI is an original Latchline Salvage wreck-control screen with visible hull/cargo, action log, explicit terminal result, and restart.
- Added browser-executed deterministic tests and reproducible evidence capture under `prototypes/salvage/tests/`, plus desktop/mobile screenshots in `prototypes/salvage/evidence/`.
- Added the fixture validation record at `tests/scenarios/01-new-game/validation.md`.
- Marked `design-prototype` available in `agents/game-designer.md` and summarized it in `README.md`.
- Applied the controller-authorized inherited evidence-labeling correction to `agents/game-designer.md`, `.agents/skills/system-design/templates/system-specification.md`, and the new prototype templates. Planned cases now default to `not run / expected outcome` and need command/input, observed output, artifact/log path, and version before promotion.

## RED and GREEN

1. Initial preliminary browser test invocation exposed a late Playwright browser-path assignment and conflicting synchronous lifecycles. This was a test-environment failure, not a prototype result; the harness was corrected while all production prototype files were absent.
2. Clean RED command:

   ```sh
   PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python -m unittest prototypes/salvage/tests/test_salvage.py
   ```

   Observed: one expected failure, `Latchline Salvage needs its reusable browser rules module`; seven dependent checks skipped.
3. GREEN command: the same unittest command reported `Ran 8 tests ... OK` after implementation and again after the final visual-state correction.

## Browser Evidence

```sh
PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python prototypes/salvage/tests/capture_evidence.py
```

Observed: `Evidence checks passed: desktop/mobile no overflow, no console errors, render no state change, and three terminal paths.`

- `prototypes/salvage/evidence/desktop-initial.png`
- `prototypes/salvage/evidence/desktop-extracted.png`
- `prototypes/salvage/evidence/mobile-initial.png`

## Scope and Limits

- Constructed approval: `SIMULATED USER APPROVAL S2, 2026-09-30`.
- Scope: local-only static browser prototype; actual spend `$0`; no public deployment, upload, or dependency added.
- Iteration 1 implemented rules/UI and passed deterministic checks. Iteration 2 corrected a screenshot-observed disabled-button focus state and recaptured evidence. The fixture's maximum of two iterations is exhausted.
- Rule tests verify `R-01` through `R-09` behavior exercised by `V-01` through `V-05`, the hull cap, terminal input no-op, UI restart, and render without state change. Browser evidence confirms visible extraction, hull-breach priority, and cargo-target-missed results.
- No Player Validation occurred. The result does not demonstrate comprehension of the winning route, fun, balance, accessibility completeness, feasibility, or production readiness.

## Fix Round 1

- Controller-supplied constructed input `SIMULATED USER APPROVAL S3, 2026-09-30` permits exactly one additional local, zero-spend correction iteration for delta feedback, fixed typography, and evidence traceability. It is not an actual user approval; original S2 and its exhausted two-iteration history remain recorded unchanged.
- Code/test source commit: `5304c4d345a5b3b6624033873c436a12567dbcd6` (`Show salvage action deltas`). The action log now displays actual per-event `Cargo` and `Hull` deltas, including capped recovery `Cargo +0 / Hull +0`; it does not alter the canonical event schema or gameplay rules. The `h1` now uses a fixed `2.25rem` size with wrapping instead of viewport-scaled typography.
- RED: the new focused UI test failed because `Cargo +2 / Hull -1` was absent from the original log. GREEN against `5304c4d345a5b3b6624033873c436a12567dbcd6`: `Ran 9 tests ... OK`.
- Evidence command against the same source commit:

  ```sh
  PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python prototypes/salvage/tests/capture_evidence.py
  ```

  Observed: desktop/mobile no overflow or console errors, unchanged render state, and the three terminal paths. Refreshed artifacts: `prototypes/salvage/evidence/desktop-initial.png`, `desktop-extracted.png`, and `mobile-initial.png`. `quick_validate.py .agents/skills/design-prototype` also reported `Skill is valid!`.
