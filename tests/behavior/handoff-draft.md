# Development Handoff Draft

## Authority

- Project: `Beacon Ledger`
- Project record: `tests/scenarios/02-system-extension/input.md`, `Existing Project Record`
- Design Brief approval: `SIMULATED USER APPROVAL E1, 2026-09-30` (fixture-only authorization)
- Core gameplay and prototype scope approval: `SIMULATED USER APPROVAL E2, 2026-09-30` (fixture-only authorization)
- Review record: `/tmp/game-designer-handoff-eval/design-review.md`
- Authoritative rule source: `tests/scenarios/02-system-extension/input.md`, `S-01`, `R-01`, `R-02`; proposed canonical `R-03`
- Status: `draft pending confirmation`
- Development Handoff Draft approval: none

## Implementation Boundary

| Included item | Authoritative rule/state/feedback IDs | Required behavior and observable outcome | Edge cases | Excluded work |
| --- | --- | --- | --- | --- |
| Conditional `Overload` extension after canonical correction | `D-01`, `D-02`, `D-03`; canonical `S-01`, `R-01`, `R-02`, proposed `R-03` | Support Charge `0..3`; `Gather` increments through `3` and reports `Charge full` at `3`; `Overload` at `3` resets Charge to `0`, adds `3` Score, and reports `Beacon overloaded`; below `3`, retain state and report `Need 3 charge`. | `Release` at `3` still follows `R-02`: Charge becomes `1`, Score increases by `1`. A fourth `Gather` at `3` is an accepted no-op. Unknown inputs remain ignored with no state or feedback change. | Spending, deployment, broader balance work, changes to `Release` semantics, and Player Validation activities. |

## Developer Questions and Dependencies

| Item | Owner | Effect if unresolved | Status |
| --- | --- | --- | --- |
| Canonically adopt `D-01` through `D-03`. | `designer` | Blocks implementation; the current authoritative system cannot reach `Overload` success. | `open` |
| Explicit Development Handoff Draft confirmation. | `user` | Draft does not authorize implementation. | `open` |
| Execute `V-01` and `V-02`-`V-05` against the implementation. | `developer` | No rule-verification claim may be made. | `open` |

## Verification and Qualifications

| Check or claim | Status | Evidence or required next step | Limitation |
| --- | --- | --- | --- |
| Existing `V-01` | `not run / expected outcome` | Fixture expects `Gather`, `Gather`, `Release` to produce `S-01=0,S-02=1`; execute and record actual evidence. | No implementation execution or artifact is supplied. |
| Proposed `V-02`-`V-05` | `not run / expected outcome` | Add and execute the cases specified in `D-03`; record command/input, observed output, artifact/log path, and version. | Proposed correction, not an authoritative update. |
| Player experience | `Player Validation` | Conduct Player Validation before any experience, balance, accessibility, or feasibility claim. | Not performed. |

This draft does not authorize implementation. It remains blocked pending canonical resolution of `F-01` and pending explicit Development Handoff Draft confirmation.
