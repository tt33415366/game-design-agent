---
name: design-change
description: Use when a confirmed game-design record receives a conflicting request, failed validation, revision, or synchronization request.
---

# Design Change

Read [the shared Game Designer contract](../../../agents/game-designer.md), the current Design Brief/project record, authoritative rules, evidence log, review record, and handoff before acting. Use [the change impact record](templates/change-impact.md) before changing an authoritative document and [the change history](templates/change-history.md) after a confirmed revision.

## Analyze Before Changing

1. Record the request, its classification, current approval references, active rule IDs and versions, confirmed scope/budget envelope, and affected evidence. Keep the proposed delta separate from active rules while its decision is pending.
2. Compare the request against core experience, scope, material cost, canonical rules, prototype budget, verification cases, evidence, and checkpoints. Before attributing a discrepancy to the proposed change, recompute each affected supplied trace under its recorded version, showing intermediate states in the impact record. Separate an existing contradiction from the effect of the proposed revision. Preserve failed evidence exactly as historical evidence; an injected or simulated failure is not Player Validation.
3. When feedback rejects the premise rather than a bounded implementation detail, preserve that negative evidence and do not expand the rejected direction with more content, cosmetic reframing, or adjacent variants. Route a proposed replacement framing through `design-intake` when the brief is open or needs reframing, then through `gameplay-design` if concept selection is open; otherwise keep it as a pending change. An exhausted budget blocks further prototype execution, not analysis, proposed alternatives, or reframing. After any required revised Brief confirmation, submit new gameplay, scope, and budget together at the existing core-gameplay/prototype-scope checkpoint before implementation.
4. A local parameter tune may proceed only when an existing explicit approval defines a genuinely applicable tuning envelope and the change stays within its scope, budget, core experience, and material-cost boundary. Otherwise, including any core rule, core experience, scope, or material-cost change, request explicit user confirmation. Do not infer approval from a request, prior handoff, or evidence result.
5. State the pending decision, alternatives, affected approvals, and implementation boundary. A handoff author may not approve the change or a revised handoff.

## Apply an Approved Revision

After an explicit approval reference is recorded, replace each affected active rule definition atomically in its canonical source. The active rule catalog must contain one definition for each rule ID: superseded wording belongs only in change history, never beside the active rule as a competing live definition.

For every affected item, record its old and new version, reason, and status in the invalidation ledger:

- Mark affected planned verification cases, executed rule-verification results, prototype observations, and review findings as `invalidated by <version>`; retain their inputs, observed outputs, artifacts, and negative outcomes as historical evidence.
- Re-open an affected checkpoint or handoff approval when its approved boundary or supporting rule/evidence changed. Unaffected approvals may remain confirmed only when the impact record explicitly names why they are unaffected.
- Create replacement verification cases and re-review the revised active rules. Recompute every replacement expected state from the active rules' ordered transitions; do not copy an old observed or expected result and alter only the tuned value. Compare retained historical observations with the rules of their recorded version without changing each item's recorded classification or provenance. Flag a contradiction as `contradictory to recorded rule/version` and unreliable for its claimed conclusion, separately from version invalidation. Use `untrusted historical simulation` only when the retained item's recorded classification was simulated; a real observation remains a real observation even when it is contradictory. Replacement checks remain `not run / expected outcome` until actual input or command, observed output, artifact/log path, and version are recorded.

## Result

Before reporting synchronization complete, reopen the canonical files and check every approved delta against the stored active rule and version. Record the source path and rule ID for each delta in the existing change history. Any unwritten delta remains pending synchronization, even when the response describes the intended new rule correctly.

Deliver a pending impact record before approval, then an approved change history and re-review after approval. Identify the active version, invalidated historical evidence, remaining approvals, and validation limits. Never claim Player Validation, implementation verification, or approval without the required recorded source.
