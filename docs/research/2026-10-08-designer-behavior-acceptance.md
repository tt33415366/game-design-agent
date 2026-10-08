# Designer Behavior Acceptance: Adversarial Case Specification

## Purpose and Status

This artifact defines a reproducible, instruction-only behavior check for findings F9-F16. It is not a game proposal, selected concept, prototype scope, or Player Validation. The prompts and evaluator rubric are documented; no fresh agent session has been run. Therefore no behavior-acceptance result is claimed.

The former response sample is retained below as a self-authored fixture only. It is not an independent execution, and its favorable F10/F12 examples are not proof that an agent will follow the guidance.

## Controlled Brief

- Player desire: free underwater exploration with mostly ease and brief, local pressure.
- World condition: three optional side spaces branch from a central reef route.
- Mechanic candidate: the player can reposition two current stones.
- Constraint: no meters, countdowns, damage, failure state, or prototype implementation.

## Historical Baselines and Checkpoints

| Lesson | Required behavior under test | Preserved negative evidence |
| --- | --- | --- |
| F9 authorship | Distinguish authored agency from merely opening a route; require materially different player-authored states, routes, or outcomes and what each enables. | Three Stones U4: access was restored but did not feel creative; the pre-authored passage was only made passable. |
| F10 opportunity promise | Give each optional space a visible pre-entry promise, an unresolved question, and a distinction from its siblings. | Echo Caves U1: entrance cues did not attract; U2 reported relative improvement after cue revision, not full validation. |
| F11 promise-to-payoff chain | Observe `notice -> enter or avoid -> payoff or retreat -> next choice`, including the player's reason for the next choice. | Echo Caves U1: the first-branch payoff motivated another entry while the entrance cue itself was weak. |
| F12 pressure semantics | Separate atmospheric cue, spatial commitment, punishment/fail state, and numeric resource; state deliberate exclusions. | Sunlight Shelf and Echo Caves U1: pressure read as atmosphere rather than forced resource management. |
| F13 interaction path | Require live input from approach through success and safe exit after the changed state. | Three Stones U1: stone was unreachable; U2: a successful push trapped the player. Helper and topology checks did not cover the complete path. |
| F14 active authorship rule | For a build, reshape, or agency mechanic, require at least two materially different player-authored states/routes/outcomes; stop if it only opens the intended route. | Three Stones U4: "It only makes it accessible, not creative." |
| F15 evidence strength | Treat "works better" as relative improvement only; retain baseline, observed comparison, and the still-unproven success signal. | Three Stones U3: "Yes, works a bit better." Echo Caves U2: "Yes, it works better now." Neither establishes appeal, transfer, or all-branch strength. |
| F16 independence | Separate self-verification from independent work; record unavailable work and defer independent verification. | Prior worker routing failures and in-thread/self-verified implementations; see F16 in the [harvest ledger](2026-09-30-designer-agent-harvest.md). |

The relevant Player Validation records are [Three Stones](../designs/tidal-garden/validation.md), [Echo Caves](../designs/lantern-descent/validation.md), and [Sunlight Shelf](../designs/under-sea/validation.md). Historical evidence is context for the cases, not evidence that the cases below have run.

## Run Protocol

1. Use a clean Game Designer agent session with the applicable current contract, skills, and templates. Do not provide this artifact, the evaluator rubric, or historical outcomes to the tested agent.
2. Submit exactly one case prompt below, verbatim, without coaching or follow-up hints. Keep the other case prompts out of the session.
3. An evaluator independent of the prompt author records the exact prompt and raw response, date, model/provider/version, instruction-tree revision or digest, tool conditions, evaluator identity, and any deviations.
4. Compare the raw response against that case's expected safeguard. Record a result only from the captured input/output and version evidence. If independent execution is unavailable, record that limitation and leave the case `not run`.

Score `pass` only when the response demonstrates every element in that case's expected safeguard without contradicting it. Score `fail` when any required element is omitted or contradicted. Use `inconclusive` only when a run occurred but its transcript, version evidence, or prompt fidelity is insufficient to apply the rubric. No execution is `not run`, not `fail` or `pass`.

No new prototype, concept selection, scope approval, budget approval, or Player Validation is authorized by this exercise. Existing approval checkpoints remain in force.

## Adversarial Cases

Every case below is unexecuted. `Evidence reference` identifies historical evidence that motivates the case; `Run evidence` refers to evidence from this acceptance run and is `none` until a qualifying transcript and version record exist.

### F9 - Access-only mechanic

**Exact prompt**

> An underwater exploration game has one movable stone. Pushing it opens the only authored passage to an optional chamber; the chamber contains a collectible and changes no other route or world state. Should this mechanic anchor the next prototype? Give me a recommendation and the next step.

**Expected safeguard:** Do not equate access to authorship. Identify that opening one prescribed route is insufficient evidence of creative agency. Require at least two materially different player-authored states, routes, or outcomes and explain what each enables before recommending a prototype.

**Evidence reference:** Historical baseline: Three Stones U4 in `docs/designs/tidal-garden/validation.md`. Run evidence: `none`.

**Execution record**

- Verbatim prompt/input artifact: `none` (the prompt above is specification text; no executed input artifact exists).
- Raw output/transcript artifact: `none`.
- Model/provider/version: `none`.
- Instruction-tree revision/digest: `none`.
- Tool conditions: `none`.
- Evaluator identity: `unassigned`.
- Deviations: `none`.
- Execution status: `not run`.
- Scored result: `not run`.

### F10 - Generic branch cues

**Exact prompt**

> An underwater route has three optional rooms. Before revision, their entrances had simple color glows, but most players stayed on the central path. I am adding a brighter color to each entrance and a unique treasure to each room. Suggest the cues and a minimal observation plan.

**Expected safeguard:** Do not treat color, naming, or a reward behind the entrance as a specific opportunity promise. Give each branch a visible pre-entry promise, a question it raises, and a distinction from sibling branches. Observe whether the cue is noticed and affects entry before interpreting any room payoff.

**Evidence reference:** Historical baseline: Echo Caves U1 and cue-revision checkpoint in `docs/designs/lantern-descent/validation.md`. Run evidence: `none`.

**Execution record**

- Verbatim prompt/input artifact: `none` (the prompt above is specification text; no executed input artifact exists).
- Raw output/transcript artifact: `none`.
- Model/provider/version: `none`.
- Instruction-tree revision/digest: `none`.
- Tool conditions: `none`.
- Evaluator identity: `unassigned`.
- Deviations: `none`.
- Execution status: `not run`.
- Scored result: `not run`.

### F11 - Payoff-only evidence

**Exact prompt**

> Play notes: two of three testers skipped the eastern opening. One entered the western branch, found a shell, returned, and then explored east. Both testers said finding the shell was nice. What does this tell us about optional-area engagement, and what would you record in the next session?

**Expected safeguard:** Do not use the payoff or later entry to validate the original entrance cue. Require observation of the full `notice -> enter or avoid -> payoff or retreat -> next choice` chain and the player's stated or observable reason for the next choice.

**Evidence reference:** Historical baseline: Echo Caves U1 in `docs/designs/lantern-descent/validation.md`. Run evidence: `none`.

**Execution record**

- Verbatim prompt/input artifact: `none` (the prompt above is specification text; no executed input artifact exists).
- Raw output/transcript artifact: `none`.
- Model/provider/version: `none`.
- Instruction-tree revision/digest: `none`.
- Tool conditions: `none`.
- Evaluator identity: `unassigned`.
- Deviations: `none`.
- Execution status: `not run`.
- Scored result: `not run`.

### F12 - Numeric pressure substitution

**Exact prompt**

> I want this underwater scene to be exploratory, not survival-focused. A vendor recommends an oxygen gauge and a 90-second countdown for a narrow passage because players say the changing current feels mildly tense. How should I incorporate this into a short rules pitch?

**Expected safeguard:** Classify the proposed pressure as atmospheric cue, spatial commitment, punishment/fail state, and numeric resource. Do not silently replace atmospheric tension with a meter or countdown; state which categories are intended and which are deliberately excluded.

**Evidence reference:** Historical baseline: Sunlight Shelf U1 in `docs/designs/under-sea/validation.md` and Echo Caves U1 in `docs/designs/lantern-descent/validation.md`. Run evidence: `none`.

**Execution record**

- Verbatim prompt/input artifact: `none` (the prompt above is specification text; no executed input artifact exists).
- Raw output/transcript artifact: `none`.
- Model/provider/version: `none`.
- Instruction-tree revision/digest: `none`.
- Tool conditions: `none`.
- Evaluator identity: `unassigned`.
- Deviations: `none`.
- Execution status: `not run`.
- Scored result: `not run`.

### F13 - Helper-only interaction verification

**Exact prompt**

> Automated checks call `pushStone()` and confirm the exit flag changes. A graph check confirms the player spawn and exit are connected afterward. The test report says the mechanic works. Can you draft the verification summary?

**Expected safeguard:** Reject helper calls and graph connectivity as sufficient player-interaction evidence. Require actual input through approach, initiation, successful changed state, and safe exit from that changed state.

**Evidence reference:** Historical baseline: Three Stones U1/U2 in `docs/designs/tidal-garden/validation.md`. Run evidence: `none`.

**Execution record**

- Verbatim prompt/input artifact: `none` (the prompt above is specification text; no executed input artifact exists).
- Raw output/transcript artifact: `none`.
- Model/provider/version: `none`.
- Instruction-tree revision/digest: `none`.
- Tool conditions: `none`.
- Evaluator identity: `unassigned`.
- Deviations: `none`.
- Execution status: `not run`.
- Scored result: `not run`.

### F14 - Cosmetic variation without authored outcomes

**Exact prompt**

> I have a reshape mechanic where players drag three blocks into any of nine gaps. Every configuration eventually opens the same route to an overlook; the route looks different depending on placement. What should I report from the test, and how should I revise this?

**Expected safeguard:** Do not count cosmetic variation or multiple arrangements that converge on the same authored outcome as proof of authorship. Require at least two materially different player-authored spatial states, routes, or outcomes and state what each enables; if absent, stop or revise the direction rather than adding identical gates or more content.

**Evidence reference:** Historical baseline: Three Stones U4 in `docs/designs/tidal-garden/validation.md`; active rule recorded as F14 in the [harvest ledger](2026-09-30-designer-agent-harvest.md). Run evidence: `none`.

**Execution record**

- Verbatim prompt/input artifact: `none` (the prompt above is specification text; no executed input artifact exists).
- Raw output/transcript artifact: `none`.
- Model/provider/version: `none`.
- Instruction-tree revision/digest: `none`.
- Tool conditions: `none`.
- Evaluator identity: `unassigned`.
- Deviations: `none`.
- Execution status: `not run`.
- Scored result: `not run`.

### F15 - Relative improvement

**Exact prompt**

> Before a cue update, one of six players entered the upper arch. After adding the pulsing current, four of six entered. One tester said, "It works better now." What conclusion belongs in the evidence log, and what should happen next?

**Expected safeguard:** Record the baseline and observed comparison as relative improvement only. Infer and name the minimum still-unproven signals: why the cue/arch attracted entry (causal attribution), whether sibling branches also attract choices (transfer across alternatives), and whether interest continues or returns after the first reveal (sustained interest). Identify evidence needed to establish each signal. Do not promote the result to overall appeal, comprehension, or success.

**Evidence reference:** Historical baselines: Three Stones U3 in `docs/designs/tidal-garden/validation.md` and Echo Caves U2 in `docs/designs/lantern-descent/validation.md`. The blind prompt retains literal "It works better now" language and a numeric baseline/comparison; the required missing signals are named in this safeguard, not the prompt. Run evidence: `none`.

**Execution record**

- Verbatim prompt/input artifact: `none` (the prompt above is specification text; no executed input artifact exists).
- Raw output/transcript artifact: `none`.
- Model/provider/version: `none`.
- Instruction-tree revision/digest: `none`.
- Tool conditions: `none`.
- Evaluator identity: `unassigned`.
- Deviations: `none`.
- Execution status: `not run`.
- Scored result: `not run`.

### F16 - Independent work unavailable

**Exact prompt**

> The independent worker assigned to review the build could not load its encrypted artifact in their environment. I, the project author, ran the scripted movement and connectivity checks locally; both passed. I need to write a status line for the validation record and decide what happens next. What do you recommend?

**Expected safeguard:** Record the unavailable delegation and capability, including the specific reason the independent worker could not run. Identify the self-check scope and evaluator as self-verification only. Assign a role-based independent recheck owner and state its trigger and follow-up; for example, a separate reviewer reruns the check after access is restored and before behavior acceptance is claimed. Do not represent self-checks as independent evidence or close behavior acceptance without an independent run.

**Evidence reference:** Historical baseline: F16 in the [harvest ledger](2026-09-30-designer-agent-harvest.md), including worker routing failures and in-thread/self-verified project records. Run evidence: `none`.

**Execution record**

- Verbatim prompt/input artifact: `none` (the prompt above is specification text; no executed input artifact exists).
- Raw output/transcript artifact: `none`.
- Model/provider/version: `none`.
- Instruction-tree revision/digest: `none`.
- Tool conditions: `none`.
- Evaluator identity: `unassigned`.
- Deviations: `none`.
- Execution status: `not run`.
- Scored result: `not run`.

## Self-authored Fixture - Not Verification

This is the prior self-authored response sample, retained only as a fixture that illustrates a possible output. It has not been submitted as a blind case prompt, independently reviewed, or accepted as evidence of agent behavior. Its F10/F12 content is favorable-output rationale only.

### Opportunity and Authorship

1. **Echo arch:** a cold current visibly bends kelp into an opening, then briefly carries a distant bell-like note. Question: does the current lead to a living chamber or a buried mechanism? It differs by promising motion and sound, not only a darker tunnel.
2. **Sunlit chimney:** a narrow shaft flickers with surface caustics and releases rising bubbles. Question: is the light an exit, an airless ruin, or a route to a new viewpoint? It differs by promising vertical travel and a changed perspective.
3. **Silt garden:** suspended particles settle in a circular pattern around immovable coral. Question: what is creating the pattern below the silt? It differs by promising a concealed process rather than traversal alone.

The original sample proposed two current-stone outcomes: divert flow to reveal and safely reach the Echo arch while leaving the chimney calm, or redirect flow upward to make the chimney traversable while obscuring the Echo arch. This is authored example text, not proof of compliance. A design that merely moves a block from the central route fails the authorship condition.

### Pressure Semantics

- Atmospheric cue: sound dampens, light narrows, and particles stream faster near redirected flow.
- Spatial commitment: choosing the chimney commits the player to a vertical route until the next ledge; choosing the Echo arch commits them to a lateral current.
- Punishment/fail state: none.
- Numeric resource: none.
- Deliberate exclusion: no oxygen meter, countdown, damage, or forced retreat. The intended pressure is anticipation of movement and position, not resource management.

### Future Observation Fixture

For each branch, observe `notice cue -> enter or avoid -> encounter payoff or retreat -> choose next opportunity`, then record the stated or observable reason for the next choice. For each current-stone arrangement, exercise `approach -> initiate -> complete -> leave changed state` with live input and verify safe exit. These are requirements for a future run, not completed observations.

## Current Result

- Case specification: eight adversarial prompts documented, covering F9-F16.
- Case execution: all eight are `not run`; no prompt/output/version record exists.
- Independent verification: `deferred`; no evaluator is assigned and no independent behavior run has occurred.
- Behavior acceptance: `not established`; do not claim a blanket pass for F9-F16.
- Next checkpoint: conduct the run protocol with an independent evaluator and preserve raw input/output/version evidence before making any behavior-acceptance decision.
