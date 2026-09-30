---
name: design-review
description: Use when an existing game-design record needs a consistency, risk, readiness, or development-handoff review.
---

# Design Review

Read [the shared Game Designer contract](../../../agents/game-designer.md), the current Design Brief/project record, and each authoritative document before acting. For an existing system, preserve the current authoritative rule IDs and terminology; treat a requested extension as a proposed delta until the required checkpoint approval is recorded.

Use the [review record template](templates/design-review.md) and [Development Handoff Draft template](templates/development-handoff.md). Link each finding to its source rule ID, state definition, input, approval, evidence, or missing dependency. Do not copy competing rule semantics into the review or handoff: identify the authoritative rule and the exact document change required.

## Review

1. Check consistency among state ranges, legal inputs, ordered transitions, terminal or exceptional behavior, feedback, verification cases, project scope, approvals, and dependencies. For each new input, inspect existing catch-all or dispatch rules: the extension must be reachable and non-conflicting while previous legal-input behavior remains explicit. When a proposed correction makes a behavior reachable by changing behavior the request explicitly requires to preserve, record the preservation-versus-reachability conflict. Do not present it as resolved unless an explicit user approval specifically relaxes that original preservation constraint; a Development Handoff Draft approval cannot substitute for that decision.
2. Check actionability: every in-scope implementation item must identify the authoritative rule IDs, inputs, state transitions, visible outcome, edge cases, and unresolved developer questions. Block readiness for a known critical contradiction, missing necessary state/transition, unbounded or incompatible scope, or another condition that makes implementation indeterminate.
3. Record risks, unvalidated claims, evidence limitations, and required follow-up. A planned case is `not run / expected outcome`, not rule-verification evidence. Rule verification and developer observation do not establish comprehension, fun, balance, accessibility, or feasibility.
4. Missing Player Validation must be named as a qualification and follow-up, but does not by itself block a qualified Development Handoff Draft. Do not require a playable prototype when the confirmed project scope does not require one.
5. Present corrections as explicit deltas to the canonical rule source. Keep the Development Handoff Draft checkpoint `pending` until an explicit user confirmation reference is recorded. Never self-approve a draft.

## Result

Deliver a review record with blocking findings resolved or explicitly retained, a readiness outcome, and a Development Handoff Draft. State the approval or decision still required and any evidence that remains unavailable.
