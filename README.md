# Game Designer

This repository-local agent workflow helps independent developers and small teams turn a game idea or existing project into actionable design documents. It is intentionally instruction-driven and does not install anything globally.

For game-design requests, the conditional pointer in [AGENTS.md](AGENTS.md) loads [the shared contract](agents/game-designer.md). The installed routes are [`design-intake`](.agents/skills/design-intake/SKILL.md), which creates or updates a Design Brief/project record; [`gameplay-design`](.agents/skills/gameplay-design/SKILL.md), which requires a confirmed Design Brief; [`system-design`](.agents/skills/system-design/SKILL.md), which requires confirmed Design Brief and core gameplay/prototype scope checkpoints; and [`design-review`](.agents/skills/design-review/SKILL.md), which checks consistency, risks, and a pending Development Handoff Draft against authoritative documents.

The shared contract names the full six-skill workflow: `design-intake`, `gameplay-design`, `system-design`, `design-prototype`, `design-review`, and `design-change`. The first five are installed locally; [`design-prototype`](.agents/skills/design-prototype/SKILL.md) records authorized local validation work, playable prototype scope, and evidence. `design-review` can produce a qualified handoff draft without Player Validation, while retaining that absence as a limitation; `design-change` remains a future routing target.

An authoring-time constructed intake exercise is retained at [tests/scenarios/01-new-game/intake.md](tests/scenarios/01-new-game/intake.md). It is not an independent behavior evaluation or player test.

An existing-system extension fixture keeps raw input separate from constructed expected review output at [tests/scenarios/02-system-extension/input.md](tests/scenarios/02-system-extension/input.md) and [tests/scenarios/02-system-extension/expected-review.md](tests/scenarios/02-system-extension/expected-review.md). It is not an independent behavior evaluation, implementation evidence, or player test.

Some hosts may require a refreshed session before discovering a newly added local skill automatically. The explicit links above remain the local entry points.
