---
name: gameplay-design
description: Use when a confirmed game Design Brief needs core loops, mechanic proposals, or innovation alternatives before prototype scope confirmation.
---

# Gameplay Design

Read [the shared Game Designer contract](../../../agents/game-designer.md) before acting, including on direct invocation. Read the current Design Brief/project record first. Require its confirmed Design Brief checkpoint, document language, and explicit approval reference; otherwise return to `design-intake`.

Use [the gameplay proposal template](templates/gameplay-proposal.md). Keep rule definitions out of this proposal: name the authoritative system-specification rule IDs once they exist.

## Design

1. When the confirmed brief leaves the concept open, compare exactly three materially different experience candidates before describing a singular loop or mechanic. Each names its hook, player action, primary creative priority, intentional sacrifice, and largest uncertainty. Recommend one with rationale, but leave selection and approval to the user. Do not substitute implementation ease, tile changes, or theme wrappers for distinct experiences. Read [design approaches](../../../agents/references/design-approaches.md) only when selecting an experience-specific lens or a smallest experiment.
2. After that comparison, describe only the recommended candidate's provisional player-facing loop, choices, stakes, and observable outcomes. Classify supplied facts, Design Assumptions, and unvalidated experience claims. Keep it proposed until the user explicitly selects it and confirms the existing combined core-gameplay/prototype-scope checkpoint.
3. When the brief already selects a concept, record its explicit selection reference with its primary creative priority and intentional sacrifice, then develop that direction directly. For a bounded in-scope fix, reference those existing choices rather than reopening concept competition or inventing a new selection.
4. Offer alternatives only when they could materially improve the agreed experience, with their benefit, production or learning risk, and low-cost validation experiment.
5. Specify the minimum playable scope, validation question, local technology assumption, excluded work, and the project's supplied iteration limit. The validation question must name two separate observable signals: initial attraction (does the player start or investigate unprompted) and sustained interest (does the player continue or return after the first payoff-free moment). If it is missing, propose a conservative limit for confirmation; never replace an explicit user budget. Treat technical architecture and effort estimates as tentative until developer confirmation. A single solution or no replay loop is valid when it serves the intended experience.
6. Submit core gameplay and prototype scope together for checkpoint confirmation. Keep the checkpoint `pending` until an explicit user approval reference is recorded; do not self-approve or start work that exceeds the confirmed budget.

## Result

Produce a concise proposal developers can challenge and a handoff to `system-design` after the core gameplay and prototype scope checkpoint is confirmed. Keep narrative, art, audio, and level detail only where it affects the loop or readable player feedback.
