---
name: system-design
description: Use when a confirmed gameplay and prototype scope needs authoritative game rules, state transitions, parameters, edge cases, or player feedback semantics.
---

# System Design

Read [the shared Game Designer contract](../../../agents/game-designer.md) before acting, including on direct invocation. Read the current Design Brief/project record and gameplay proposal. Require confirmed Design Brief and core gameplay/prototype-scope checkpoints with explicit approval references. Without them, return a draft for confirmation rather than an authoritative specification.

Use [the system specification template](templates/system-specification.md). This is the authoritative home for each rule: assign stable IDs and define state, conditions, transitions, feedback, and edge cases exactly once. Gameplay, prototype, review, and handoff documents must refer to those IDs rather than restating them.

## Specify

1. Define the minimum state and initial parameters needed for the confirmed scope.
2. Give every player action, automatic event, terminal condition, and exceptional condition a deterministic rule ID. State order, legal inputs, tie or boundary handling, and observable result.
3. Include only level, narrative, art, or audio requirements that affect those rules or player feedback. Mark balance and experience claims as unvalidated unless supported by Player Validation.
4. Add executable-style verification cases and developer questions. Keep architecture and effort notes tentative pending developer confirmation.

## Result

Deliver one implementable system specification and point validation work to its rule IDs. A rule test verifies implementation against this document; it does not prove fun or balance.
