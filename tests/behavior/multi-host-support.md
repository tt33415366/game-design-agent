# Multi-host support qualification

This record covers offline qualification for the approved multi-host support
contract. Static checks establish `configured` only; they do not establish
runtime compatibility. No paid or authenticated calls, credential changes,
permission bypass, network publication, or automation of an existing
Antigravity application session were authorized.

The six routes are `design-intake`, `gameplay-design`, `system-design`,
`design-prototype`, `design-review`, and `design-change`. The five roles are
`explorer`, `worker`, `tester`, `reviewer`, and `researcher`.

## Configuration result

| Host | Status | Executable/version observation | Tested commit | Evidence |
| --- | --- | --- | --- | --- |
| Codex | configured | `/data/lea/.local/bin/codex --version` -> `codex-cli 0.162.1` (also emitted a read-only-filesystem PATH warning) | `13a2fa4` integration tip plus this working tree | offline result records below |
| Claude Code CLI | configured | `/data/lea/.local/bin/claude --version` -> `2.1.285 (Claude Code)` | `13a2fa4` integration tip plus this working tree | offline result records below |
| agy CLI | configured | `/data/lea/.local/bin/agy --version` -> `1.2.12` | `13a2fa4` integration tip plus this working tree | offline result records below |
| Antigravity app | configured | version unobserved; no application session opened | `13a2fa4` integration tip plus this working tree | offline result records below |

These are observed local versions, not minimum-version claims. The app row is
separate from the `agy` CLI row. There is no `runtime-verified` or `blocked`
claim in this record because live-test authorization was not provided.

## Live case matrix

Every required live case is recorded separately for every host. `NOT RUN` is a
missing authorization/access result, never a pass. The prompts and commands
below are the cases that require explicit host authorization before execution.

| Host | all six routes | all five roles | direct skill invocation | checkpoint 1 | checkpoint 2 | checkpoint 3 | each role invocation | effective permissions | native nested delegation excluded | read-only write rejection | worker/tester inherit roundtrip | independent reviewer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Codex | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Claude Code CLI | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| agy CLI | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Antigravity app | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN | NOT RUN |

The Antigravity round-trip case must request inherited workspace mode, verify
the actual child working directory, and use a disposable write/read fixture.
The independent-reviewer case must be a separate native reviewer invocation;
a same-context self-check does not satisfy it. Effective permissions are
recorded from the active session, not inferred from repository frontmatter.
Shell-capable roles still depend on host and organization policy; a tool
allowlist is not claimed to be a portable shell sandbox.

### Codex case records

| Case | Result | Command or input | Observed output | Artifact path |
| --- | --- | --- | --- | --- |
| all six routes | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| all five roles | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| direct skill invocation | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 1 | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 2 | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 3 | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| each role invocation | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| effective permissions | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| native nested delegation excluded | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| read-only write rejection | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| worker/tester inherit roundtrip | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| independent reviewer | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |

### Claude Code CLI case records

| Case | Result | Command or input | Observed output | Artifact path |
| --- | --- | --- | --- | --- |
| all six routes | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| all five roles | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| direct skill invocation | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 1 | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 2 | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 3 | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| each role invocation | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| effective permissions | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| native nested delegation excluded | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| read-only write rejection | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| worker/tester inherit roundtrip | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| independent reviewer | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |

### agy CLI case records

| Case | Result | Command or input | Observed output | Artifact path |
| --- | --- | --- | --- | --- |
| all six routes | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| all five roles | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| direct skill invocation | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 1 | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 2 | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 3 | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| each role invocation | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| effective permissions | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| native nested delegation excluded | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| read-only write rejection | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| worker/tester inherit roundtrip | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |
| independent reviewer | NOT RUN | no live host command; authorization not granted | NOT RUN | not applicable (not run) |

### Antigravity app case records

| Case | Result | Command or input | Observed output | Artifact path |
| --- | --- | --- | --- | --- |
| all six routes | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| all five roles | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| direct skill invocation | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 1 | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 2 | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| checkpoint 3 | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| each role invocation | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| effective permissions | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| native nested delegation excluded | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| read-only write rejection | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| worker/tester inherit roundtrip | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |
| independent reviewer | NOT RUN | no application session; authorization not granted | NOT RUN | not applicable (not run) |

## Antigravity tool/schema qualification

The configured Antigravity allowlists remain exactly those in
`agents/host-adapters.json`; this section records their static qualification
basis and does not broaden them. The first-party schema/tool references are
[Antigravity subagents](https://antigravity.google/docs/subagents/),
[Antigravity hooks and tool names](https://antigravity.google/docs/hooks), and
[Antigravity skills](https://antigravity.google/docs/skills). The checked-in
research records are `docs/research/2026-10-12-multi-host-orchestration.md`
and `docs/research/2026-10-12-multi-host-instruction-discovery.md`.

| Role | Configured native tools |
| --- | --- |
| explorer/reviewer | `view_file`, `list_dir`, `find_by_name`, `grep_search` |
| researcher | `view_file`, `list_dir`, `find_by_name`, `grep_search`, `search_web`, `read_url_content` |
| worker/tester | `view_file`, `list_dir`, `find_by_name`, `grep_search`, `write_to_file`, `replace_file_content`, `multi_replace_file_content`, `run_command`, `manage_task` |

`/data/lea/.local/bin/agy --version` was observed as `1.2.12`, but no live schema or session test ran. Therefore the Antigravity rows remain configured, not runtime-verified. The ephemeral `/tmp/multi-host-native-metadata.md` is
not checked in and is not the sole evidence; the first-party URLs and
checked-in research paths above are the retained source references.

## Offline evidence

Each record retains the exact command, observed result, and artifact path. The
commands are local/offline checks and do not invoke a model or host session.

| ID | Exact command | Observed output | Artifact path | Classification |
| --- | --- | --- | --- | --- |
| O-01 | `python3.11 -m unittest discover -s tests/host_support -p 'test_*.py' -v` | `Ran 38 tests in 2.101s; OK` | `tests/host_support/` and this record | configured evidence |
| O-02 | `python3.11 scripts/sync_host_adapters.py --check` | `PASS; exit 0; no stdout/stderr` | `agents/generated-host-files.json` and generated projections | configured evidence |
| O-03 | `python3.11 tests/behavior/verification-scripts/check_game_designer_links.py` | `LINK_AUDIT files=88 local_targets=117 broken=0` | `tests/behavior/verification-scripts/check_game_designer_links.py` | configured evidence |
| O-04 | `git diff --check` | `PASS; exit 0; no whitespace errors` | this checkout's Git diff | configured evidence |
| O-05 | from `/tmp`: `python3.11 '/tmp/multi-host-check.c85SEZ/repository with spaces/scripts/sync_host_adapters.py' --check` | `exit 0; no stdout/stderr` | temporary copy `/tmp/multi-host-check.c85SEZ/repository with spaces` (not retained); checked-in regression `tests/host_support/test_adapter_sync.py` | configured evidence |

The qualification suite covers route/role completeness, foreign-host setting
exclusion, and refusal to claim runtime verification without evidence. The
renderer suite covers repeatable writes, ownership/conflict detection,
rollback/manifest preservation, path/symlink rejection, and the temporary
space-containing checkout. The shared-contract suite compares canonical paths
and bytes against the immutable `509aeba` baseline, including Codex settings
and design-rule sources. Link audit and `git diff --check` are required before
handoff.
