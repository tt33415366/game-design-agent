# Lantern Descent: Gameplay Proposal

Date: 2026-10-08. Brief: [brief.md](brief.md), confirmed 2026-10-08. Structure under exploration: risk-and-release rhythm. All experience claims are Design Assumptions; no Player Validation exists yet for this structure.

## Experience Candidates

| Candidate | Hook | Player action | Primary creative priority | Intentional sacrifice | Largest uncertainty | Decision status |
| --- | --- | --- | --- | --- | --- | --- |
| A. Lantern Descent | Carry one lantern down a vertical reef shaft. Darkness thickens below; choose when to turn back before the light fades. Each depth has a visual discovery. | Swim down, read light/current cues, choose a return point | Personal risk tolerance and tension-release | One spatial axis; choices are primarily "deeper or back" | Does choosing a depth feel free, or like managing a meter? | proposed |
| B. Echo Caves | At a forked cave system, sound reveals which tunnel contains something alive, unstable, or empty. Pressure comes from committing to a narrow branch; surfacing resets the cave's audible clues. | Listen, choose branches, retreat or press onward | Curiosity and interpretation under pressure | Less pure rhythm; navigation becomes a deduction layer | Do sound cues become an obvious puzzle sequence? | proposed |
| C. The Rising Bloom | Descend through a peaceful kelp column as bioluminescent blooms open only while you stay near them; deeper blooms are brighter but currents pull harder. Surface whenever you decide the view is enough. | Ride currents, linger near blooms, decide when to leave | Sensory awe and voluntary stopping | Little mechanical pressure; may become passive sightseeing | Is the pressure strong enough to create a meaningful release? | proposed |

These are materially different: A is a depth/return decision under a single dwindling resource, B is branching interpretation and retreat, C is a sensory stay-or-leave trade-off. They share under-sea pressure but not the same core decision.

## Recommendation

**B. Echo Caves.** A risks turning into the numeric oxygen-management loop the brief specifically wanted to avoid. C may preserve ease but under-test pressure. B creates pressure from spatial commitment rather than a meter, retains real freedom to retreat, and can give each descent a distinct reason to continue without salvage, upgrades, or grinding.

Smallest experiment: one compact cave with three forked branches, a lantern cone, environmental sound/visual pulses, and two reveals. No procedural generation, monsters, inventory, oxygen meter, or fail state. Return to the surface voluntarily; the test is whether a player chooses to enter a second branch after the first reveal.

## Core Experience and Mechanic Proposal (recommended candidate only; provisional)

| Item | Proposal | Classification | Risk / open question |
| --- | --- | --- | --- |
| Target player | User as first evaluator | sourced fact | Does not generalize |
| Intended experience | Calm surface freedom interrupted by self-chosen cave commitment and relief on retreat | Design Assumption | Branches must feel tempting rather than like a puzzle quiz |
| Core loop | Notice a cave cue → choose a branch → enter as pressure rises → find a reveal or retreat → resurface → decide whether another branch is worth it | Design Assumption | **Return pull: each branch promises a different unresolved cue. If that only reads as a prescribed correct answer, the structure fails.** |
| Observable outcome | Reaching a branch reveal alters the surface/cave soundscape, but gives no score or inventory item | Design Assumption | Must not become a checklist |

## Prototype Scope and Checkpoint (pending)

- Validation question (F6): initial attraction — does the user voluntarily enter a cave branch; sustained interest — after the first reveal or retreat, does the user choose a second branch; pressure reading — does narrowing/darkness create tension without a numeric oxygen meter?
- Minimum playable content: compact cave, three branches, lantern cone, two reveal events, voluntary surface return, restart.
- Maximum iterations: propose 1. Time limit: propose 2 hours. Spending: zero.
- Excluded: damage, monsters, oxygen meter, upgrades, loot, procedural cave generation, checklist UI, touch controls.
- Core gameplay/prototype-scope checkpoint: `pending` until user selects A/B/C and confirms the proposed budget.
