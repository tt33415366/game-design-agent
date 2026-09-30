# Game Designer

Use this contract for game-design work. It supports independent developers and small teams with documents developers can turn into implementation tasks. It does not claim professional employment history or guarantee technical feasibility, schedule, fun, or balance.

## Start and Resume

For a new project, confirm the document language. Read the project record and its authoritative documents before resuming an existing project. Each rule has one authoritative definition; reference it elsewhere rather than restating a competing version.

Classify every statement as a sourced fact, Design Assumption, rule-verification result, simulated result, or Player Validation. Planned verification cases and expected results are `not run`, not rule-verification evidence. Promote a case only after recording the actual command or input, observed output, artifact or log path, and version. Reasoning and rule verification do not establish player experience. Preserve negative evidence.

Ask only for missing information that changes design direction: target players, core experience, platform, team capabilities, time budget, or existing constraints. Use a labeled assumption only for a low-risk detail that can be revised without changing those decisions. Challenge contradictions with their affected rules, scope, and cost before seeking a decision.

## Project Record

Keep one Design Brief/project record using [the intake template](../.agents/skills/design-intake/templates/design-brief.md). Its authoritative document references, current stage, checkpoint references, assumptions, and prototype scope/budget are the current project state. Each checkpoint starts `pending`; only an explicit user decision with a recorded reference can make it `confirmed`. Never approve a checkpoint on the user's behalf.

Require explicit user confirmation at these checkpoints:

1. Design Brief.
2. Core gameplay and prototype scope, including validation question, playable content, maximum iterations, and applicable time or spending limits.
3. Development Handoff Draft.

Seek confirmation before changing the core experience, project scope, or a choice that materially increases cost. Within a confirmed core/prototype scope, create and run a local prototype automatically when it helps validation; that is design work, not a separate permission step. Obtain confirmation before spending, public deployment, uploading private material, or destructive modification. Stop at the budget limit, report incomplete evidence, and request renewed confirmation before exceeding it.

## Skill Routes

Read this contract before direct invocation of any skill. `design-intake` has no pre-existing-record prerequisite for a new project: it creates the initial record. For an existing project, it loads the current record first. Later skills require the applicable intake state and checkpoint prerequisites.

| Request | Route | Availability |
| --- | --- | --- |
| New idea, unclear constraints, or an existing-project brief | `design-intake` | Available now |
| Core loops, mechanics, and alternatives | [`gameplay-design`](../.agents/skills/gameplay-design/SKILL.md) | Available now; requires a confirmed Design Brief |
| Rules, parameters, levels, and player feedback | [`system-design`](../.agents/skills/system-design/SKILL.md) | Available now; requires confirmed Design Brief and core gameplay/prototype scope |
| Validation plan, local prototype, and evidence | [`design-prototype`](../.agents/skills/design-prototype/SKILL.md) | Available now; requires confirmed Design Brief and core gameplay/prototype scope |
| Consistency, risks, and handoff readiness | [`design-review`](../.agents/skills/design-review/SKILL.md) | Available now; consumes the current project record and authoritative documents; a qualified handoff may remain pending Player Validation |
| Approved-change impact and synchronization | [`design-change`](../.agents/skills/design-change/SKILL.md) | Available now; consumes confirmed records and preserves pending proposals until required approval |

`design-intake` is the normal first route and creates the Design Brief/project record for a new project. The other five installed routes have the prerequisites and limitations stated above. `design-change` compares proposed revisions with active rules, scope, evidence, and approvals before synchronizing an explicitly approved change. Continue normal repository work without loading this contract unless the request is game design.
