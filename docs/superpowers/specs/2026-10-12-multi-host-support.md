# Multi-Host Game Designer Support

**Status:** approved
**Approval:** User reply `Approved` on 2026-10-12, accepting spec revision `509aeba28941fa2816887d455cfaec9e21f6b201`.
**Tracker:** [Implementation tickets](../../../.scratch/multi-host-support/implementation/README.md)
**Plan:** [Implementation plan](../plans/2026-10-12-multi-host-support.md)

## Goal and Scope

Make the six existing Game Designer skills and five supporting roles usable in
Codex, Claude Code CLI, and Google Antigravity CLI, with the Antigravity application
consuming the same agent files. Preserve the current design checkpoints and Codex
configuration. Implement on one local integration branch; do not push or open a PR.

The user approved these answers to the three remaining Wayfinder decisions.
Approval authorizes implementation, not a claim of successful host execution.

## Approved Decisions

### A. Support Contract

- Support the same six routes: `design-intake`, `gameplay-design`, `system-design`,
  `design-prototype`, `design-review`, and `design-change`; preserve their names,
  prerequisites, templates, and three user-confirmation checkpoints.
- Support the existing `explorer`, `worker`, `tester`, `reviewer`, and `researcher`
  responsibilities through each host's native subagent mechanism. Do not build
  a process-launching orchestration service or require preview team features.
- A small task may remain root-only. When a workflow requires delegation or
  independent review and the capability is unavailable, report it and stop that
  requirement; a disclosed self-check may assist but cannot satisfy independence.
- Keep Codex model/reasoning/sandbox settings unchanged. New host roles use
  `model: inherit`; do not translate Codex model names or reasoning levels into
  another provider's settings. User and organization policy remain authoritative.
- Initial qualification targets are the observed local versions: Codex `0.162.1`,
  Claude Code `2.1.285`, and `agy` `1.2.12` on this Linux workspace. These are not
  proven minimum versions or a promise about all newer versions. Other versions,
  operating systems, and the Antigravity application require their own evidence.
- Report support per host as `configured`, `runtime-verified`, or `blocked`.
  Static checks establish only `configured`; runtime evidence establishes
  `runtime-verified`; a known required capability failure is `blocked`.

### B. Shared Sources and Adapters

Keep the current layout where it already supplies one source of truth:

| Authoritative source | Responsibility |
| --- | --- |
| `agents/game-designer.md` | Existing game-design rules and approval/evidence contract |
| `.agents/skills/<design-route>/` | Six canonical skills and all their local resources |
| `.codex/agents/<role>.toml` | Canonical role names, descriptions, and instruction bodies; existing Codex-specific metadata |
| `agents/orchestration.md` (new) | Host-neutral delegation, ownership, context, and evidence policy |
| `agents/host-adapters.json` (new) | Claude/Antigravity native model, tool, and permission metadata only |

Keeping role prose in the existing TOML avoids migrating five working Codex
definitions merely to change their container format. The renderer consumes only
`name`, `description`, and `developer_instructions` as shared role content; it
must not copy Codex model, reasoning, or sandbox keys into other hosts.

| Host | Entry points and role artifacts |
| --- | --- |
| Codex | Root `AGENTS.md`, existing `.codex/agents/`, existing `.agents/skills/` |
| Claude Code CLI | `CLAUDE.md` importing `@AGENTS.md`; generated `.claude/agents/<role>.md` and `.claude/skills/<design-route>/` |
| Antigravity CLI/application | Root `AGENTS.md`, existing `.agents/skills/`, generated `.agents/agents/<role>.md` |

Make root `AGENTS.md` host-neutral and conditionally route complex work to
`agents/orchestration.md`. Keep `.agents/skills/astra-orchestrator/SKILL.md` as a
Codex-only compatibility entry point referencing that policy and the existing
Codex profile. Do not expose that Codex-only skill as a Claude design skill or
trigger its model policy on Antigravity. Do not invent an additional design stage.
Choose a host profile from the active CLI/session identity, not from directory
presence: all three hosts' files coexist. If identity is unknown, ask before
host-specific delegation rather than guessing from the installed adapters.

Use checked-in generated files, not symlinks or an installation-time dependency.
Claude's skill projection copies the complete six canonical skill directories
byte-for-byte, retaining relative topology and templates. Generated role bodies
retain the canonical instruction text, with only newline normalization allowed.
Only host metadata differs. No global configuration, credentials, hooks, plugins,
MCP server installations, or persistent agent memory are added.

### C. Safety and Acceptance

The new adapters enforce read-only restrictions and exclude native nested-agent
tools through allowlists, not through prose alone:

| Role | Required capabilities | Excluded capabilities |
| --- | --- | --- |
| explorer, reviewer | Read files, list/search repository content | File mutation, shell execution, nested agent spawning |
| researcher | Same reads plus native web search/fetch | File mutation, shell execution, nested agent spawning |
| worker, tester | Repository reads, bounded edits, test commands | Permission bypass settings, native nested-agent tools |

Claude roles explicitly use normal `permissionMode: default` and allowlists;
Antigravity roles use allowlists and `commandExecutionPolicy: sandbox`, with
`subagent: true` and `mainAgent: false`. Shell tools are absent from read-only
roles. Do not claim a repository field can override a more permissive parent or
organization configuration: verification records the effective session policy.
Neither adapter grants extra tools through agent memory, hooks, or MCP servers.
Shell-capable roles still require effective session permissions and explicit user
approval for publication; a tool allowlist alone cannot prohibit every shell
command. Document this boundary rather than claiming a portable security sandbox.
Qualify actual tool identifiers against the installed host and first-party docs;
an unsupported identifier blocks that role rather than broadening its allowlist.

The root supplies bounded tasks, necessary file/context pointers, approval state,
and expected results to children; it does not assume conversation history is
inherited. Only the root delegates. Independent tasks may run concurrently when
the host supports it and file ownership does not overlap. Serial native delegation
is valid; a same-context self-check is not independent review. Resume reloads
project records and evidence, not an assumed cross-host conversation identifier.
For Antigravity, request `inherit` workspace mode when invoking a child; do not
silently select `branch` or `share`, or invent a workspace field in agent YAML.
The root selects the intended checkout before dispatch. A worker's edits must be
visible to its parent and tester there. If isolation is needed, the root explicitly
selects a worktree first and owns any later merge. Live qualification must verify
the actual child working directory and a disposable write/read round trip.
All five new-host roles exclude native delegation tools; tests must cover writers
as well as read-only roles. Shell-launching another agent is not an allowed
workaround, although this instruction is not a claim that a tool list can sandbox
arbitrary shell programs.

## Renderer Contract

Add `scripts/sync_host_adapters.py`, using Python 3.11+ and the standard library.
Read TOML with `tomllib`, metadata with `json`, and emit host frontmatter using
properly escaped scalar/list serialization; do not implement a YAML parser.

- `python3 scripts/sync_host_adapters.py --check` is read-only and exits `0` only
  when expected generated paths, bytes, and the ownership manifest agree.
- `python3 scripts/sync_host_adapters.py --write` renders locally, without network
  or CLI/model invocation. Repeating it must be byte-identical and leave no diff.
- `agents/generated-host-files.json` records generated relative paths and SHA-256
  digests, so regeneration can distinguish its prior output from local edits.
  It contains no timestamps, absolute workspace paths, or credentials.
- Before any write, reject malformed role/metadata input, escaped paths, symlinks
  in managed input/output paths, invalid tool-policy combinations, and collisions
  with unmanaged or locally modified files. On validation failure write nothing;
  print the conflicting paths, with no force-overwrite mode.
- Update only declared generated files and the manifest. Preserve unrelated
  `.claude/` and `.agents/` files. A source change may replace an output only if
  its old digest matches the manifest (or it already equals the desired bytes).
  Remove stale managed files only when their old digest still matches.
- Render completely in memory before applying changes; replace individual files
  atomically and replace the manifest last, only after all output operations
  succeed. Do not promise a filesystem-wide transaction. An interrupted write
  must be detected by `--check` and reported for inspection, not silently repaired.
  An injected failure during application must return nonzero, retain the previous
  manifest, and leave unrelated/locally modified content intact.
- Keep `.codex/config.toml` and all five `.codex/agents/*.toml` unchanged. The
  generator is maintenance tooling, not a prerequisite for using checked-in agents.

## Verification and Completion

Offline acceptance requires the following, without paid model calls:

1. Standard-library unit tests cover canonical role preservation, five-role and
   six-skill completeness, frontmatter generation, permission metadata, and absence
   of foreign-host model settings. Negative cases cover malformed TOML/JSON,
   missing templates, edits to generated files, stale outputs, collisions, and
   symlink/path escapes; failures preserve existing bytes.
2. Renderer checks pass in this checkout and a temporary copy whose path contains
   spaces, regardless of current working directory. Repeated writes are identical.
3. Make the existing link checker derive its repository root from `__file__`
   rather than `/data/lea/Workspace/game_designer`. Add a regression proving it
   checks the selected worktree, including generated Claude skill resources.
4. Verify unchanged Codex configuration and design-rule/approval semantics against
   the integration branch's recorded starting commit. Ticket one records that
   immutable commit and SHA-256 digests for `.codex/config.toml`, the five Codex
   role files, `agents/game-designer.md`, and every file in the six canonical skill
   trees in `tests/host_support/preservation-baseline.json`. Tests compare both
   path sets and bytes, failing on additions, removals, or modifications. Do not
   regenerate the baseline from a changed checkout merely to make a test pass.
   Retain historical fixtures and failed evidence; do not modify the unrelated
   prototype/UI verification. The Codex-only orchestration skill is intentionally
   outside this immutable set because its routing facade changes.

Live acceptance is a separately authorized, bounded exercise. Record executable
and version, effective permissions, commit, exact input/command, actual output,
and artifact path for every result; missing access is `not run`, never a pass.
Exercise each host's discovery of all six skills/five roles, representative direct
skill invocation, all three pending approval checkpoints, each role's invocation,
read-only write rejection, a worker/tester round trip in a disposable fixture,
and a separate reviewer. Check Antigravity application discovery independently.

Spec approval does not authorize paid calls, credential changes, permission bypass,
network publication, or UI automation against an existing personal session. Without
live-test authorization, close implementation with passing offline checks and an
explicit `configured` result; do not claim `runtime-verified` compatibility.
Evidence is recorded in `tests/behavior/multi-host-support.md`, with a per-host
result matrix and exact unrun cases. A failed required live case remains a visible
blocker for that host; fixing code must not erase its original failure record.

## Delivery and Non-Goals

After approval, use the requested `implement-spec` workflow on a local
`feat/multi-host-support` integration branch. Each implementation ticket gets a
separate branch/worktree, TDD, a merge back through a merger, and final standards
and spec review. Follow the graph; do not manufacture concurrency across shared
renderer ownership. Record local resolution comments and commits; no PR is needed.
Remove only clean implementation worktrees after their work is safely merged.

Rollback reverts implementation commits; global configuration is untouched. Keep
the research branch separate and unmerged. Do not add a global installer, package
manager dependency, new game rules, a runtime orchestration framework, or blanket
support claims about other hosts/versions.

## Evidence and Approval

Local research remains at commit `71f8bffdb85e7032bbe9bb7fa4c4f5c8b480e522`:
`docs/research/2026-10-12-multi-host-instruction-discovery.md` and
`docs/research/2026-10-12-multi-host-orchestration.md` (read with `git show`).
The research distinguishes documented capabilities from local version observations.
First-party schema checks during drafting also used [Claude subagents](https://code.claude.com/docs/en/sub-agents),
[Claude skills](https://code.claude.com/docs/en/skills),
[Antigravity subagents](https://antigravity.google/docs/subagents/), and
[Antigravity tool names](https://antigravity.google/docs/hooks), retrieved 2026-10-12.
Recheck tool/schema facts during implementation against the actual target versions.

The user reply `Approved` accepted decisions A, B, and C and this bounded delivery
contract after presentation of revision `509aeba28941fa2816887d455cfaec9e21f6b201`.
This approval does not authorize paid/live exercises, permission bypass, or push.
