# Final Fix Report

Date: 2026-09-30

## Fixed Findings

- `design-change` now preserves every retained evidence item's recorded classification and provenance. Contradictions are flagged against the recorded rule/version and treated as unreliable for their claimed conclusion; `untrusted historical simulation` applies only to evidence originally classified as simulated.
- `design-review` now requires an explicit preservation-versus-reachability finding when a reachability correction changes behavior the request requires to remain unchanged. A Development Handoff Draft approval cannot substitute for the separate explicit decision.
- The Beacon constructed review now identifies that raising the cap changes `Gather` at Charge `2`. Its qualified corrected draft relies on explicit constructed `SIMULATED USER APPROVAL E3`, which relaxes that constraint while leaving Development Handoff Draft approval as `none` and the raw input unchanged.

## Regression Coverage

- Added constructed-scenario assertions for E3's absence from raw input, explicit behavior-change disclosure, pending handoff status, provenance preservation, and preservation-versus-reachability review guidance.

## Validation

- Constructed scenario checks: passed.
- `quick_validate.py .agents/skills/design-change`: passed.
- `quick_validate.py .agents/skills/design-review`: passed.
- Scoped `git diff --check`: passed.
