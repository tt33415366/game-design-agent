---
name: design-prototype
description: Use when a confirmed game-design prototype scope needs a local validation plan, a playable prototype, or evidence records.
---

# Design Prototype

Read `agents/game-designer.md`, the current project record, and the authoritative system rules before acting. Require confirmed Design Brief and core gameplay/prototype-scope checkpoints with recorded approval references. Do not create, spend, deploy, upload, or destructively modify outside those approvals.

Use [the validation plan](templates/validation-plan.md) to record intended appeal, observable signals, a `continue | clarify | revise | stop` decision, minimum fidelity, included and excluded scope, project-supplied iteration/time/spending budgets, and stop condition. Preserve a project-specific iteration limit; propose a conservative limit only when none exists. Do not hardcode a fixture cap.

Implement only the approved playable slice. Keep rule logic testable independently of rendering, run deterministic rule checks before presenting outcomes, and use the smallest local technology that tests the question. For any interactive prototype, also run a real game-loop/render smoke check that collects page/console errors and exercises actual input through the live loop; helper-level tests alone cannot establish playability. Record each actual iteration and scope or spend decision in [the evidence log](templates/evidence-log.md).

Classify inputs, approvals, test results, simulations, and Player Validation separately. A planned verification case remains `not run / expected outcome` until its actual command or input, observed output, artifact or log path, and version are recorded. When Player Validation is planned, the first play session must be unassisted and recorded before any designer explanation reaches the player; explanation afterwards is diagnostic only and cannot establish unassisted comprehension. Separate deterministic rule checks from desirability evidence. Rule tests and developer inspection can verify implementation behavior, not comprehension, fun, balance, or accessibility. Preserve failed or unavailable checks, stop at the approved budget, and request renewed confirmation before exceeding it or changing the core experience.
