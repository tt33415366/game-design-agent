---
name: system-design
description: Use when a confirmed gameplay and prototype scope needs authoritative game rules, state transitions, parameters, edge cases, or player feedback semantics.
---

# System Design

Read [the shared Game Designer contract](../../../agents/game-designer.md) before acting, including on direct invocation. Read the current Design Brief/project record and gameplay proposal. Require confirmed Design Brief and core gameplay/prototype-scope checkpoints with explicit approval references. Without them, return a draft for confirmation rather than an authoritative specification.

Use [the system specification template](templates/system-specification.md). This is the authoritative home for each rule: assign stable IDs and define state, conditions, transitions, feedback, and edge cases exactly once. Gameplay, prototype, review, and handoff documents must refer to those IDs rather than restating them.

## Specify

1. Define the minimum state and initial parameters needed for the confirmed scope.
2. Give every player action, automatic event, terminal condition, and exceptional condition a deterministic rule ID. State order, legal inputs, tie or boundary handling, and observable result. Reset/restart rules must enumerate transient presentation state (labels, feedback, timers), not just simulation state. Time-based rules must state elapsed-time integration explicitly (fixed-step or per-frame, catch-up limit, and behavior on stall/resume), so implementers cannot silently pick a cap with different gameplay meaning.
3. Include only level, narrative, art, or audio requirements that affect those rules or player feedback. When a visual prototype is in scope, require drawn and collidable geometry to share one authoritative source or an explicit footprint mapping, state any permitted decorative overhang (e.g. tree canopy vs trunk) explicitly, and require obstacles, boundaries, and connections to read correctly at ground level. Mark balance and experience claims as unvalidated unless supported by Player Validation.
4. Add executable-style verification cases and developer questions. Keep architecture and effort notes tentative pending developer confirmation.

## Result

Deliver one implementable system specification and point validation work to its rule IDs. A rule test verifies implementation against this document; it does not prove fun or balance.
