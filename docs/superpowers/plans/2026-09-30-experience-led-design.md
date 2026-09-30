# Experience-Led Design Implementation Plan

> **For agentic workers:** Use subagent-driven-development with independent behavioral exercises and a scoped final review. Preserve existing uncommitted prototype work.

**Goal:** Make the existing Game Designer select and reject creative directions based on intended player experience before expanding rules or prototypes.

**Architecture:** Keep the shared agent and six skills. Add one concise, conditionally loaded design-approach reference; update only the existing skills and template fields that consume the new decisions. Keep proposal, approval, executed evidence, and user feedback distinct.

**Tech Stack:** Markdown instructions and templates, existing skill validator, independent qualitative agent exercises.

**Spec:** User approval of the recommendations in `docs/research/2026-09-30-studio-design-workflows.md`, following rejection of the salvage theme and obvious sequence. The research is evidence and proposal, not a claim of internal studio methods.

## Global Constraints

- No new personas, skills, approval checkpoints, workflow runtime, or prototype changes.
- Preserve the three checkpoints and automatic local prototyping within confirmed scope/budget.
- Preserve real versus simulated provenance, negative evidence, canonical rule ownership, and historical fixtures.
- When direction is open, compare three meaningfully different experiences; respect an already selected concept and bounded maintenance requests.
- Collect supplied preferences and exclusions without forcing a questionnaire or inventing taste.
- Select one primary creative priority with an explicit trade-off; source studio-inspired methods as interpretations, not employment or guaranteed outcomes.
- Test the largest uncertainty in appeal, not merely rule correctness. Distinguish comprehension, desirability, and implementation correctness.
- Unique solutions may be valuable; replayability and multiple solutions are not universal requirements.
- Stop expanding a rejected premise; propose revised framing through existing approval and change paths. Do not restart an exhausted prototype budget.
- Lack of Player Validation alone still permits a qualified handoff; a creative recommendation and implementation readiness are separate judgments.

## Review Focus

- Pending brief: short taste framing may proceed, but gameplay/prototype approval cannot be invented.
- Confirmed brief with no concept: ease of coding must not substitute for comparing appeal.
- Already selected concept: no mandatory three-direction restart or extra approval gate.
- Clear but disliked project with exhausted budget: no more content or self-authorized prototype.
- Studio-flavor request: one justified approach and source limits, not six styles mixed together.

## Task 1: Baseline Behavior

- [x] Capture independent outputs using unchanged skills for missing brief, open concept with confirmed brief, and rejected premise with exhausted budget.
- [x] Assess observed gaps against the approved behavior; retain passes and failures honestly.

Baseline evidence: `tests/behavior/experience-selection-baseline.md`. Case C selected one inexpensive deterministic puzzle and offered tile/theme wrappers instead of distinct experiences. Cases A/B retained pending approvals, and B correctly stopped expansion under an exhausted budget. The change strengthens creative selection; it does not claim these existing safeguards were absent.

## Task 2: Update Existing Workflows

**Ownership:** `agents/game-designer.md`, optional `agents/references/design-approaches.md`, intake/gameplay/prototype/review skill files and their relevant existing templates, plus a focused routing addition to design-change if needed. No system-rule or prototype edits.

- [x] Extend intake with taste, exclusions, and attraction without redundant questions.
- [x] Extend concept selection with distinct options, a reasoned recommendation, a primary priority, sacrifice, and uncertainty.
- [x] Extend prototype and review with observable experience questions and continue/clarify/revise/stop outcomes.
- [x] Keep reference guidance small, source-linked, and conditional; validate all six skills and local links.

## Task 3: Verify and Integrate

- [x] Run fresh independent forward exercises including a fixed-concept maintenance case.
- [x] Review spec compliance, authority boundaries, and instruction/template consistency; correct material findings.
- [x] Retain actual behavioral outputs and update the README/PRD description of the delivered agent behavior.
- [x] Run final validators and whitespace checks; report limits without claiming proven fun or general behavioral reliability.

Completion evidence: `tests/behavior/experience-selection-assessment.md` indexes unchanged raw baseline/forward outputs, review corrections, and the focused budget re-test. Six skill validators and the 47-target local-link audit passed. A remaining output-level evidence-labeling limitation is explicit in the assessment. No prototype files, global configuration, or original scenario outputs were changed by this follow-up; prior user-approved working-tree changes remain intact.
