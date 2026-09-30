---
name: gameplay-design
description: Use when a confirmed game Design Brief needs core loops, mechanic proposals, or innovation alternatives before prototype scope confirmation.
---

# Gameplay Design

Read [the shared Game Designer contract](../../../agents/game-designer.md) before acting, including on direct invocation. Read the current Design Brief/project record first. Require its confirmed Design Brief checkpoint, document language, and explicit approval reference; otherwise return to `design-intake`.

Use [the gameplay proposal template](templates/gameplay-proposal.md). Keep rule definitions out of this proposal: name the authoritative system-specification rule IDs once they exist.

## Design

1. State the player-facing core loop, choices, stakes, and observable outcomes. Classify supplied facts, Design Assumptions, and unvalidated experience claims.
2. Offer only alternatives that could materially improve the agreed experience. For each, record benefit, production or learning risk, and a low-cost validation experiment.
3. Specify the minimum playable scope, validation question, local technology assumption, excluded work, and the project's supplied iteration limit. If it is missing, propose a conservative limit for confirmation; never replace an explicit user budget. Treat technical architecture and effort estimates as tentative until developer confirmation.
4. Submit core gameplay and prototype scope together for checkpoint confirmation. Keep the checkpoint `pending` until an explicit user approval reference is recorded; do not self-approve or start work that exceeds the confirmed budget.

## Result

Produce a concise proposal developers can challenge and a handoff to `system-design` after the core gameplay and prototype scope checkpoint is confirmed. Keep narrative, art, audio, and level detail only where it affects the loop or readable player feedback.
