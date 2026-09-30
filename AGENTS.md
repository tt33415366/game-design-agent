# Codex project instructions

For complex coding tasks, use the `astra-orchestrator` skill when its trigger conditions match.

The root agent owns architecture, decomposition, integration, and final verification.
Prefer specialized subagents for bounded exploration, implementation, testing, review, and technical research.

Do not delegate trivial work merely for parallelism.
Do not let multiple implementation agents edit the same files without explicit ownership boundaries.
User instructions always take precedence over this orchestration policy.

For game-design requests, read [the Game Designer contract](agents/game-designer.md) and route the request through its applicable skill; leave non-design repository work on its normal workflow.
