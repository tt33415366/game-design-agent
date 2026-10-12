# Game Designer

This repository-local agent workflow helps independent developers and small teams turn a game idea or existing project into actionable design documents. It is intentionally instruction-driven and does not install anything globally.

For an open game direction, the workflow starts with the user's taste and exclusions, compares three distinct experiences after brief confirmation, and recommends a primary creative priority with an explicit trade-off. Existing selected concepts and bounded maintenance requests do not require another concept competition. Prototype evaluation separates rule correctness, comprehension, and appeal; a rejected premise calls for reconsideration rather than automatic content expansion. The [studio-process research](docs/research/2026-09-30-studio-design-workflows.md) explains the source evidence and proposed adaptations without claiming studio employment or confidential methods.

For game-design requests, the conditional pointer in [AGENTS.md](AGENTS.md) loads [the shared contract](agents/game-designer.md). The installed routes are [`design-intake`](.agents/skills/design-intake/SKILL.md), which creates or updates a Design Brief/project record; [`gameplay-design`](.agents/skills/gameplay-design/SKILL.md), which requires a confirmed Design Brief; [`system-design`](.agents/skills/system-design/SKILL.md), which requires confirmed Design Brief and core gameplay/prototype scope checkpoints; [`design-prototype`](.agents/skills/design-prototype/SKILL.md), which records authorized local validation; [`design-review`](.agents/skills/design-review/SKILL.md), which checks consistency, risks, and a pending Development Handoff Draft; and [`design-change`](.agents/skills/design-change/SKILL.md), which analyzes proposed revisions before approved synchronization.

The full six-skill workflow is installed locally: `design-intake`, `gameplay-design`, `system-design`, [`design-prototype`](.agents/skills/design-prototype/SKILL.md), `design-review`, and [`design-change`](.agents/skills/design-change/SKILL.md). `design-prototype` records authorized local validation work, playable prototype scope, and evidence. `design-review` can produce a qualified handoff draft without Player Validation while retaining that absence as a limitation. `design-change` keeps proposed deltas separate from active rules until the required explicit approval, then records versioned invalidation and re-review.

An authoring-time constructed intake exercise is retained at [tests/scenarios/01-new-game/intake.md](tests/scenarios/01-new-game/intake.md). It is not an independent behavior evaluation or player test.

An existing-system extension fixture keeps raw input separate from constructed expected review output at [tests/scenarios/02-system-extension/input.md](tests/scenarios/02-system-extension/input.md) and [tests/scenarios/02-system-extension/expected-review.md](tests/scenarios/02-system-extension/expected-review.md). It is not an independent behavior evaluation, implementation evidence, or player test.

A conflicting-revision fixture likewise keeps [raw baseline, specification, and request input](tests/scenarios/03-conflict-revision/input.md) separate from the [constructed impact, approval, synchronization, and re-review output](tests/scenarios/03-conflict-revision/expected-change.md). The three constructed scenarios and retained qualitative behavior evidence are described in [tests/README.md](tests/README.md); neither is real-project or Player Validation.

Some hosts may require a refreshed session before discovering a newly added local skill automatically. The explicit links above remain the local entry points.

## Multi-host entry points

The same six routes are available from each supported host: `design-intake`,
`gameplay-design`, `system-design`, `design-prototype`, `design-review`, and
`design-change`. Use the active session identity to select a host; do not infer
it from which adapter directories happen to exist.

| Host | Start here | Role files |
| --- | --- | --- |
| Codex | `AGENTS.md` and `.agents/skills/<route>/SKILL.md` | `.codex/agents/<role>.toml` |
| Claude Code CLI | `CLAUDE.md` (`@AGENTS.md`) | `.claude/agents/<role>.md` |
| agy CLI | `AGENTS.md` and `.agents/skills/<route>/SKILL.md` | `.agents/agents/<role>.md` |
| Antigravity app | `AGENTS.md` and `.agents/skills/<route>/SKILL.md` | `.agents/agents/<role>.md` |

The five role names are `explorer`, `worker`, `tester`, `reviewer`, and
`researcher`. Only the root delegates. Native child tools are excluded from
all generated roles; read-only roles have read/search tools only, while
`worker` and `tester` require the host's effective edit and test permissions.

## Generated files

Run the renderer with Python 3.11 or newer from any working directory:

```sh
python3.11 scripts/sync_host_adapters.py --check
python3.11 scripts/sync_host_adapters.py --write
```

The checked-in `.claude/` projection, `.agents/agents/` projection, and
`agents/generated-host-files.json` are generated outputs. The manifest owns
their paths and SHA-256 digests. `--check` is read-only; `--write` refuses
malformed input, symlink/path escapes, unmanaged collisions, or local edits,
and writes no partial manifest. A failed application keeps the previous
manifest, but individual files already replaced must be inspected and
`--check` will report the interrupted state. Regeneration never changes
`.codex/config.toml`, the canonical Codex roles, or the six source skill trees.
No global configuration, credentials, hooks, plugins, MCP servers, or agent
memory are installed.

The observed qualification targets are Codex `0.162.1`, Claude Code `2.1.285`,
and `agy` `1.2.12` on this Linux checkout. They are observations, not minimum
versions or a promise about other releases, operating systems, or the
Antigravity application.
