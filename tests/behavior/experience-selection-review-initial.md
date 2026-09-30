# Experience-Led Workflow Review

## Findings

### High: The shared contract makes the confirmed brief both the prerequisite for and a prohibition on gameplay proposal work

- `agents/game-designer.md:23` says a confirmed Design Brief "does not ... authorize gameplay/prototype work," while `agents/game-designer.md:32` and `.agents/skills/gameplay-design/SKILL.md:8` make that same confirmation the prerequisite for entering `gameplay-design`.
- Read literally, an open concept can never reach the three-direction proposal without another authorization. That creates the circular prerequisite/additional gate the approved follow-up explicitly forbids.
- Narrow the prohibition to what is actually intended: brief confirmation does not select/approve gameplay or authorize prototype implementation. Explicitly allow gameplay proposals after brief confirmation, with the existing core-gameplay/prototype-scope checkpoint remaining pending.

### High: Open-concept work commits to one loop before comparing the three experiences

- `.agents/skills/gameplay-design/SKILL.md:14` requires a singular core loop, choices, and stakes before line 15 requires comparison "before expanding mechanics."
- `.agents/skills/gameplay-design/templates/gameplay-proposal.md:11-22` likewise places the singular Core Experience and Mechanic Proposal before the candidate table at lines 24-30; the table also shows only one placeholder row despite the exact-three instruction.
- The fresh forward exercise demonstrates the effect at `/tmp/experience-forward.md:163-170`: it defines the clue-inspection/answer loop that belongs to Candidate 1 before presenting the experimental-machine and timeline alternatives. This anchors the alternatives around a preselected solution and weakens the requirement for three genuinely different experiences.
- Put the exact-three comparison first for an open concept. Only after the comparison should the document describe the recommended candidate's provisional loop and scope, clearly pending the existing combined checkpoint; this does not require a separate concept checkpoint.

### High: A bounded review-only fix is forced through a blocked Development Handoff Draft

- `.agents/skills/design-review/SKILL.md:10` and lines 18-22 unconditionally require both the full review record and Development Handoff Draft, even when the user asks only for advice on a bounded in-scope correction and explicitly does not request implementation or handoff.
- The forward exercise at `/tmp/experience-forward.md:249-269` marks a label-review request `blocked` and requires handoff approval solely because no canonical rule ID was supplied, then emits a full handoff at lines 286-319. This is disproportionate to the question and effectively applies the third checkpoint to a review that did not ask to cross an implementation boundary.
- Make the handoff draft conditional on a handoff/readiness request. A bounded review can return a scoped advisory conclusion with assumptions and identify what must be checked before implementation; missing canonical artifacts should block implementation readiness, not the ability to answer whether the proposed copy is directionally appropriate.

### Medium: The selected direction loses its primary creative priority and deliberate sacrifice

- `.agents/skills/gameplay-design/SKILL.md:15` requires priority and sacrifice only for open-concept candidate rows. Line 16 lets selected concepts and bounded fixes bypass that section, and `.agents/skills/gameplay-design/templates/gameplay-proposal.md:11-18` has no selected-direction fields for either decision.
- `.agents/skills/gameplay-design/templates/gameplay-proposal.md:28-30` also omits `selected` from candidate decision status, so the record has no coherent place to preserve which priority/trade-off survived selection.
- Carry the chosen concept's primary creative priority and intentional sacrifice into the Core Experience/recommendation record, including when the brief already contains a selected concept. Bounded copy or parameter fixes can reference the existing values instead of reopening concept competition.

## Checks and Limitations

- All six skill directories pass `quick_validate.py`.
- `git diff --check` passes for the reviewed non-prototype scope.
- The new `agents/references/design-approaches.md` links resolve by inspection, is conditionally referenced from `gameplay-design`, limits use to one experience-specific lens, and clearly avoids claims of studio employment, confidential practice, or guaranteed outcomes.
- The workflow does preserve the other requested boundaries: rejected premises stop expansion, exhausted budgets require renewed approval, rule correctness is distinguished from appeal, assisted and unassisted observation are distinguished, single-solution/non-replay designs remain valid, and absent Player Validation alone does not block a qualified handoff.
- This was a read-only instruction/spec review. Prior prototype UI changes and external source verification were excluded as requested. The forward exercise is a constructed behavior sample, not proof of general model behavior or Player Validation.
