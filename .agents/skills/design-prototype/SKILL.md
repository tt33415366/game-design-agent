---
name: design-prototype
description: Use when a confirmed game-design prototype scope needs a local validation plan, a playable prototype, or evidence records.
---

# Design Prototype

Read `agents/game-designer.md`, the current project record, and the authoritative system rules before acting. Require confirmed Design Brief and core gameplay/prototype-scope checkpoints with recorded approval references. Do not create, spend, deploy, upload, or destructively modify outside those approvals.

Use [the validation plan](templates/validation-plan.md) to record the validation question, minimum fidelity, included and excluded scope, project-supplied iteration/time/spending budgets, and stop condition. Preserve a project-specific iteration limit; propose a conservative limit only when none exists. Do not hardcode a fixture cap.

Implement only the approved playable slice. Keep rule logic testable independently of rendering, run deterministic rule checks before presenting outcomes, and use the smallest local technology that tests the question. Record each actual iteration and scope or spend decision in [the evidence log](templates/evidence-log.md).

Classify inputs, approvals, test results, simulations, and Player Validation separately. A planned verification case remains `not run / expected outcome` until its actual command or input, observed output, artifact or log path, and version are recorded. Rule tests and developer inspection can verify implementation behavior, not comprehension, fun, balance, or accessibility. Preserve failed or unavailable checks, stop at the approved budget, and request renewed confirmation before exceeding it or changing the core experience.
