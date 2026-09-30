# Final Whole-Branch Review

Reviewed product range: `df031df4aa2c35c0d75927fdb9e18dc86d358372..af872fb6c566b08618fba5978dd9083e6a3604d0`.

The later `1f4011a` commit contains controller-owned ticket and retained evidence updates; product source remains at `af872fb`.

## Findings

### High: `design-change` can falsify the provenance of contradictory historical evidence

- Source: `.agents/skills/design-change/SKILL.md:23-25`.
- The workflow first requires retained inputs, observed outputs, artifacts, and negative outcomes, but then instructs the agent to flag **any** historical observation that contradicts its recorded rules as an `untrusted historical simulation`.
- That label is valid for fixture `C1`, whose original classification is already a simulated result. It is not valid generically. A real prototype log, executed rule-verification result, developer observation, or Player Validation record can contradict the recorded rules because of an implementation defect, stale version metadata, instrumentation error, or an incorrect specification. Relabeling such evidence as a simulation changes its provenance instead of preserving it.
- This conflicts with the shared evidence-honesty requirement and with the same skill's instruction to preserve failed evidence exactly. It can cause real negative evidence to be discounted during a revision.
- Required correction: preserve the item's original classification and provenance. Mark it as contradictory to its recorded rule/version and therefore untrusted for the claimed conclusion; use `untrusted historical simulation` only when the retained item's recorded classification was simulated.

### Medium: the Beacon correction claims to preserve `Gather` while changing its behavior

- Sources: `tests/scenarios/02-system-extension/input.md:32,43`; `tests/scenarios/02-system-extension/expected-review.md:25-28,37-39,55-60`.
- The request explicitly requires `Gather` and `Release` to keep behaving as they do today. The active `R-01` makes `Gather` at Charge `2` an accepted no-op with `Charge full`. The proposed `D-02` instead increments Charge from `2` to `3` and moves the full/no-op boundary to `3`.
- The range/reachability conflict is correctly detected, and the changed rule is approval-gated, but the review calls the corrected result consistent and says it preserves `Gather`. That hides the fact that the proposed resolution violates one of the request's explicit constraints.
- Required correction: retain this as an unresolved requirement conflict until the user explicitly chooses a behavior change. The draft may propose raising the `Gather` cap, but it must state that this changes existing `Gather` behavior at Charge `2`; alternatively, propose another explicitly scoped way to make Charge `3` reachable.

## Verification

Fresh checks against the current product source completed successfully:

- Six skill validators: `6/6` valid.
- Prototype browser unit suite: `9/9` passed.
- Direct-file UI matrix: all `8` action sequences and `3` viewports passed; no horizontal overflow or console errors; SVG content rendered at every viewport.
- Maintained Markdown link audit: `27` files, `44` local targets, `0` broken.
- `git diff --check df031df..af872fb`: exit `0`, no output.

The prototype's deterministic behavior, terminal priority, event ordering/deltas, restart behavior, and desktop/mobile/narrow rendering showed no material defect in this review.

## Residual Validation Limits

- The prototype evidence covers local headless Chromium and deterministic rule behavior, not other browser engines, assistive-technology testing, production readiness, balance, fun, or Player Validation.
- Constructed scenarios and retained qualitative forward tests are simulated evidence. Historical failed outputs remain useful regression evidence but are not current product truths.
- The fresh change forward test exercises the corrected fixture path, including recomputed state, approval retention/invalidation, and unexecuted replacement checks; it does not expose the generic provenance bug above because its contradictory `C1` input is explicitly simulated.

## Scoped Fix Re-Review

Date: 2026-09-30. Reviewed fix range: `1f4011a..a19d0b0`.

- **High finding addressed.** `.agents/skills/design-change/SKILL.md` now preserves each retained item's recorded classification and provenance. A contradiction is labeled against its recorded rule/version and as unreliable for its claimed conclusion; `untrusted historical simulation` is restricted to evidence already classified as simulated. Real observations remain real observations.
- **Medium finding addressed.** `.agents/skills/design-review/SKILL.md` now requires a preservation-versus-reachability conflict to remain unresolved until an explicit decision relaxes the original constraint. The Beacon output identifies the changed `Gather` behavior at Charge `2`, records an exact constructed E3 decision for that behavior change, and does not use handoff approval as a substitute.
- The raw Beacon input is unchanged and contains no E3 approval. The Development Handoff Draft remains `pending` with approval `none`; E3 authorizes only the stated behavior change inside the constructed scenario.
- No new material finding was introduced in the scoped fix.

Scoped verification: both changed skills passed `quick_validate.py`; the constructed scenario assertions passed; `git diff --check 1f4011a..a19d0b0` passed; and the changed-file list is limited to the two skills, the constructed expected review, its scenario check, and the fix report.
