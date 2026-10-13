---
name: design-review
description: Use when an existing game-design record needs a consistency, risk, readiness, or development-handoff review.
---

# Design Review

Read [the shared Game Designer contract](../../../agents/game-designer.md), the current Design Brief/project record, and each authoritative document before acting. For an existing system, preserve the current authoritative rule IDs and terminology; treat a requested extension as a proposed delta until the required checkpoint approval is recorded.

Use the [review record template](templates/design-review.md) for formal readiness or handoff work. For a bounded review-only request with no implementation or handoff ask, return a concise advisory conclusion, its assumptions, and what must be checked before implementation; do not require a full record, readiness outcome, or Development Handoff Draft. Use the [Development Handoff Draft template](templates/development-handoff.md) only when a handoff/readiness boundary is requested. Link formal findings to their source rule ID, state definition, input, approval, evidence, or missing dependency. Do not copy competing rule semantics into the review or handoff: identify the authoritative rule and the exact document change required.

## Review

1. For a bounded review-only request, assess directional fit against supplied choices, give a concise conclusion, state assumptions, and name the authoritative source or decision needed before implementation. Missing canonical artifacts qualify implementation readiness; they do not prevent this advisory answer.
2. For formal readiness or handoff work, check consistency among state ranges, legal inputs, ordered transitions, terminal or exceptional behavior, feedback, verification cases, project scope, approvals, and dependencies. For each new input, inspect existing catch-all or dispatch rules: the extension must be reachable and non-conflicting while previous legal-input behavior remains explicit. Trace the changed input from its dispatch through an ordinary case and each affected boundary, including an ignored input where the system defines that behavior; record rule IDs, initial state, intermediate states, and expected result in the existing review or verification cases. Recompute supplied traces against their recorded version before using them as evidence. A reported test pass without execution provenance remains a supplied claim. When a proposed correction makes a behavior reachable by changing behavior the request explicitly requires to preserve, record the preservation-versus-reachability conflict. Do not present it as resolved unless an explicit user approval specifically relaxes that original preservation constraint; a Development Handoff Draft approval cannot substitute for that decision.
3. For formal readiness or handoff work, check actionability: every in-scope implementation item must identify the authoritative rule IDs, inputs, state transitions, visible outcome, edge cases, and unresolved developer questions. Block readiness for a known critical contradiction, missing necessary state/transition, unbounded or incompatible scope, or another condition that makes implementation indeterminate.
4. Record risks, unvalidated claims, evidence limitations, and required follow-up. Evaluate prototype evidence against its intended appeal, observable signals, and `continue | clarify | revise | stop` criteria when present. Keep unassisted observation, assisted understanding, rule correctness, and desirability evidence distinct. A planned case is `not run / expected outcome`, not rule-verification evidence. Rule verification and developer observation do not establish comprehension, fun, balance, accessibility, or feasibility.
5. Missing Player Validation must be named as a qualification and follow-up, but does not by itself block a qualified Development Handoff Draft. Do not require a playable prototype when the confirmed project scope does not require one.
6. Present corrections as explicit deltas to the canonical rule source for formal readiness or handoff work. Keep the Development Handoff Draft checkpoint `pending` until an explicit user confirmation reference is recorded. Never self-approve a draft.

## Result

For a bounded review-only request, deliver the concise advisory conclusion, assumptions, and implementation checks. Otherwise deliver a review record with blocking findings resolved or explicitly retained, a readiness outcome, and a Development Handoff Draft. State the approval or decision still required and any evidence that remains unavailable.
