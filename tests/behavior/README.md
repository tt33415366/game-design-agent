# Qualitative Behavior Evidence

These are retained outputs from constructed agent exercises on 2026-09-30, not an automated regression suite, real-project validation, or Player Validation. Simulated approvals belong only to the fictional exercises. Historical failures remain unchanged so later corrections do not erase evidence.

| Exercise | Retained evidence | Interpretation |
| --- | --- | --- |
| Baseline | [responses](baseline-responses.md), [assessment](baseline-evaluation.md) | Pre-implementation comparison; known approval/budget gaps. |
| Intake | [run](intake-forward-test.md), [draft](intake-draft.md) | Missing constraints and pending checkpoints retained. |
| Gameplay | [initial run](gameplay-forward-test.md) | Historical failure: expected cases mislabeled as verification. |
| Evidence and budget | [run](evidence-budget-forward-test.md) | Exhausted budget respected; first draft subcase inconclusive. |
| Rule draft | [fresh run](rule-draft-forward-test.md) | Supplied budget retained; planned cases explicitly not run. |
| Extension/handoff | [run](handoff-forward-test.md), [review](handoff-review-draft.md), [handoff](handoff-draft.md) | Historical correction missed catch-all dispatch. |
| Extension dispatch | [fresh run](dispatch-forward-test.md) | Both reachability and input dispatch conflicts detected. |
| Revision | [initial runs](change-forward-test.md) | Includes preserved harness-error correction and historical incorrect expected Hull total; not acceptance evidence for arithmetic. |
| Revision recomputation | [fresh run](change-fresh-forward-test.md) | Recomputed ordered transitions, flagged inconsistent history, retained unaffected approvals, and reopened handoff. |

[Independent browser and document verification](final-verification.md) records actual checks at the named revisions, separately from qualitative outputs. Its screenshots are retained in `final-browser/`. Exact temporary verifier copies are retained in `verification-scripts/`; their absolute workspace/tool paths describe the original run and must be adapted in another environment. The maintained prototype regression suite is `prototypes/salvage/tests/test_salvage.py`.

Constructed authoritative examples and executable prototype checks are described separately in [the test overview](../README.md). These qualitative runs establish only the behavior observed under their recorded prompts, not a guarantee for future model outputs.
