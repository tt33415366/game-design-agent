# Game Designer Implementation Plan

> **For agentic workers:** Use subagent-driven-development to execute approved tickets with independent task reviews and a final integrated review.

**Goal:** Deliver a repository-local Game Designer with six dedicated skills, owned document templates, and exercised acceptance scenarios.

**Architecture:** A conditional pointer in the existing AGENTS.md activates a plain Markdown agent contract. Six model-discoverable skills live in .agents/skills; each owns only its relevant templates. Project state is a small Markdown record, not a custom workflow engine.

**Tech Stack:** Markdown and skill frontmatter; standard-library validation where useful; a minimal browser prototype with deterministic rule checks.

**Spec:** prd.txt; domain vocabulary in CONTEXT.md.

## Global Constraints

- The primary Game Designer agent selects skills, maintains overall project context, and enforces confirmation checkpoints.
- Skills are specialized workflows; they do not each require a separate subagent.
- Require confirmation at three checkpoints: the design brief, core gameplay and prototype scope, and the development handoff draft.
- Changes to the core experience, project scope, or choices that materially increase cost require user confirmation.
- Authorize prototype creation automatically as part of design work; no separate prototype-development permission is required.
- This authorization does not remove the confirmed checkpoints or major-decision approval requirements.
- Require confirmation for spending, public deployment, uploading private material, and destructive modifications.
- Distinguish sourced facts, design assumptions, and test results. Reasoning alone is not player validation, and untested designs must not be presented as proven fun or balanced.
- Give each rule one authoritative definition; other documents reference it.
- Do not automatically install into global configuration.
- Use English for repository instructions, templates, fixtures, and reports. Generated project documents follow the project's confirmed language.
- The user authorized local Git initialization. Work on feat/game-designer, commit scoped changes, and use commit diffs for review. Do not push or publish remotely.
- Preserve existing orchestration configuration and unrelated AGENTS.md content. No package/framework scaffolding for the agent itself.
- Workers do not spawn children. The controller owns review and behavioral evaluation dispatches.

## Review Focus

- Requests to skip confirmation must not silently fabricate approval; retain an actionable draft. Task 1.
- Existing-project constraints and conflicting rule definitions must survive system extension. Tasks 2 and 4.
- Exhausted prototype budgets and denied resource access must end with honest partial results. Task 3.
- Untested fun/balance claims and injected failures must not become player evidence. Tasks 3 and 5.
- Core-rule revisions must invalidate affected earlier evidence and approvals, not just update prose. Task 5.

## Task 1: Intake and agent entry point

**Ownership:** AGENTS.md (append a conditional pointer only), agents/game-designer.md, README.md, .agents/skills/design-intake/**, tests/scenarios/01-new-game/intake.md. Do not change .codex or the existing orchestration skill.

**Consumes:** Approved PRD and glossary. **Produces:** agent contract, skill routing table, and one reusable Design Brief/project-state template. Preserve six exact skill names from the PRD.

- [ ] Read the skill-authoring instructions and baseline evidence before implementing.
- [ ] Write concise core instructions for senior-level judgment, permission boundaries, staged confirmations, resuming from project files, and conditional skill routing. Non-design repository work must not be forced through this workflow.
- [ ] Define a small project record: authoritative document references, current stage, explicit approval references for each checkpoint, assumptions, and prototype scope/budget. Pending is the default; no self-approval. Direct invocation of a skill must load the shared agent contract and check prerequisites.
- [ ] Add the intake template and an honest constructed scenario input/output. Scenario seed: single-player turn-based salvage game for desktop browser, one developer, short prototype; details not supplied are missing or labeled assumptions.
- [ ] Check frontmatter/links and record actual scenario behavior. Do not claim that authored example prose alone is an independent behavior test; the controller supplies independent evaluation.

## Task 2: Gameplay and system design

**Ownership:** .agents/skills/gameplay-design/**, .agents/skills/system-design/**, tests/scenarios/01-new-game/design.md. Read but do not modify Task 1's shared contract unless requesting a controller ruling.

**Consumes:** agents/game-designer.md and the intake template's project record. **Produces:** gameplay proposal and authoritative system-specification templates plus a concrete salvage-game design reusable by Task 3.

- [ ] Build focused trigger descriptions and shared-contract pointers, not copies of the global policy.
- [ ] Cover core loops, innovation alternatives with trade-offs and experiments, precise state/rule/edge-case semantics, initial parameters, player feedback, and only relevant narrative/art/audio/level details.
- [ ] Keep technical architecture and effort estimates explicitly tentative pending developer confirmation.
- [ ] In the constructed fixture, supply labeled simulated checkpoint approvals, a deterministic minimal turn-based salvage mechanic, observable outcomes, a maximum of two prototype iterations, local-only zero-spend scope, and explicit excluded features. This is an original small mechanic, not a recreation of a game requiring a rules engine.
- [ ] Each rule receives a stable reference within the system specification; other documents refer rather than duplicate. Establish enough precision for deterministic tests and a playable browser implementation.
- [ ] Run skill validation and review scenario consistency; retain evidence and limitations.

## Task 3: Prototype and evidence

**Ownership:** .agents/skills/design-prototype/**, prototypes/salvage/**, tests/scenarios/01-new-game/validation.md. Read authoritative Task 2 rules; do not silently alter them.

**Consumes:** approved fixture scope/budget and authoritative system specification. **Produces:** playable local prototype, deterministic rule tests, validation/evidence templates, actual run evidence.

- [ ] Write executable rule tests first, run to observe failure, then implement only the scoped original mechanic.
- [ ] Provide browser-playable input, feedback, a clear end state and reset. Use custom game-appropriate visual assets, not a marketing page. Prefer native web platform and standard library; no dependencies unless genuinely required.
- [ ] Keep game rules reusable by the deterministic tests. Document launch/use and the prototype's non-production status.
- [ ] Write the skill and owned templates covering authorization, hypothesis, minimum fidelity, scope, iteration accounting, stop conditions, actual evidence and outstanding player validation.
- [ ] Verify browser interaction with available browser automation and desktop/mobile screenshots; report any unavailable tooling honestly. The controller may provide independent browser verification.
- [ ] Explicitly label constructed input/approvals. Record commands, observed outputs, limitations and negative results. Do not infer fun or balance from rule-test success.

## Task 4: Existing-system extension and handoff

**Ownership:** .agents/skills/design-review/**, tests/scenarios/02-system-extension/**.

**Consumes:** shared contract and system-specification template. **Produces:** review/handoff template and an exercised existing-project extension scenario.

- [ ] Review rule consistency, edge cases, dependencies, actionability, scope and evidence. Critical contradictions or unimplementability block readiness; absence of player tests must be labeled but need not block a qualified draft.
- [ ] Create a small pre-existing system fixture and a scoped extension. Preserve canonical rules, identify exactly what changes, and record simulated approval explicitly.
- [ ] Exercise a contradictory extension and its corrected form, recording observed checks and a Development Handoff Draft that remains pending user confirmation.
- [ ] Use the same project record/approval language as Task 1. Do not require Task 3's playable prototype for every handoff.
- [ ] Validate frontmatter/references and record test evidence. Independent forward evaluation is controller-owned.

## Task 5: Conflicts, failed validation, and revision

**Ownership:** .agents/skills/design-change/**, tests/scenarios/03-conflict-revision/**, tests/README.md. Request shared-contract changes if needed; no silent edits to other task ownership.

**Consumes:** shared contract, design templates, prototype/evidence workflow, review/handoff workflow. **Produces:** change-impact/history templates and complete third scenario.

- [ ] Compare change requests with confirmed scope and rules before modifying authoritative documents.
- [ ] Distinguish in-scope local tuning from core-rule/scope/cost changes. Preserve negative evidence; obtain required renewed approval.
- [ ] Define precise invalidation of affected rules, evidence, prototype results and checkpoint approvals; avoid duplicate live rule definitions.
- [ ] Exercise an injected failure plus a conflicting request, pending-approval behavior, and the approved revision. Keep original evidence; label all simulations and injections.
- [ ] Summarize reproducible checks for all three scenarios without claiming manual authoring is independent execution. Real-project and real-player validation remain out of scope for this delivery.
- [ ] Validate skill references and report implementation evidence; controller performs independent behavior evaluation and final integration review.
