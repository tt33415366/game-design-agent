# Browser Exploration: Brief and Direction Proposal

Updated: 2026-09-30. This is an actual project discussion, not a constructed acceptance fixture. Candidate A is selected by U2.

## Project Record

- Current stage: Player Validation complete; direction stopped as-is, pending user decision on whether to reframe.
- Document language: English, confirmed with the brief.
- Canonical framing and current proposal: this document.
- Authoritative system rules: [system.md](system.md).
- Prototype and evidence: `prototypes/valley/` and [validation.md](validation.md); both approved iterations complete, final rule/browser verification passed. Player Validation (U3/U4) recorded in [validation.md](validation.md): initial curiosity confirmed, sustained interest not established without arrival payoff; direction stopped as-is per the plan's stop criterion.
- Design Brief: confirmed by `U1`, the user's `Confirmed` reply to the proposed brief and limits in this conversation on 2026-09-30.
- Core gameplay and prototype scope: confirmed by `U2`, the user's `A` response on 2026-09-30 to the explicit question selecting A and confirming its stated scope for implementation.
- Development Handoff Draft: pending.

## Confirmed Framing

| Topic | Information | Source |
| --- | --- | --- |
| Intended player | The user as the first evaluator; a broader audience has not been established. | Current discussion; audience boundary is a design assumption. |
| Attraction | Freedom while exploring; Breath of the Wild is the user's reference. | User's explicit preference, not a claim that all its features are desired. |
| Design priority | Player-directed exploration; freedom over content volume. | U1 |
| Exclusion | Salvage theme. | User rejection and U1; do not import exclusions from fictional test cases. |
| Platform | Browser. | User: `a browser would be fine` |
| First-prototype implementation | Assistant implements locally here; user evaluates the experience. | U1 |
| Budget envelope | Three hours total prototype work, zero spending, at most two iterations. | U1; limits rather than a delivery guarantee. |

The brief does not establish a 3D requirement, a large world, combat, crafting, or a complete game. U2 confirms the proposed 2D keyboard-browser slice. Implementation feasibility remains bounded by the budget; iteration 1 started at 08:12:39 UTC on 2026-09-30, with an absolute stop no later than 11:12:39 UTC.

## Three Experience Candidates

The following is the retained comparison. Attractions and feasibility judgments are Design Assumptions. U2 selected A; B and C are not authorized for implementation. No candidate is player-validated.

| Candidate | Hook and defining action | Primary priority | Intentional sacrifice | Largest uncertainty |
| --- | --- | --- | --- | --- |
| A. The Unmarked Valley | Enter a small valley with a ruined tower, a stream crossing, and a secluded grove. Pick a visible destination, take either side of the stream, and discover connections or detours rather than follow a prescribed route. | Freedom of movement, destination, and pace, driven by landmarks. | A small authored 2D place instead of extensive terrain, vertical traversal, or deep interactions. | Do the places inspire personal curiosity, or does moving around merely feel aimless? |
| B. The Rearrangeable Garden | Carry and place two bridge pieces to change how a garden's islands connect; try a layout because it reaches a place you want to visit, not to satisfy a single final arrangement. | Freedom to change the space and invent a route. | Very little territory and only one reusable manipulation verb; less scenic wandering. | Does rearrangement feel like personal agency rather than a disguised mandatory bridge puzzle? |
| C. The Lantern District | Wander a small evening neighborhood, approach light or conversation that interests you, and encounter three independent vignettes in any order; no investigation score or required solution. | Freedom of attention and interpretation, with personal stories as reasons to explore. | Little traversal challenge or systemic manipulation; greater reliance on writing and readable presentation. | Do the vignettes invite exploration, or does the experience feel like visiting dialogue buttons? |

## Selected Direction: A

A directly tests the user's stated attraction: deciding where to go and how to get there. B prioritizes manipulating a world; C prioritizes choosing what to notice and interpret. Neither is a cosmetic variant of A, and neither is assumed to match the user's taste better.

- Primary creative priority: self-directed spatial exploration.
- Deliberate sacrifice: a compact place and limited verbs rather than broad content or systemic depth.
- Adapted approach: intention and readable exceptions from [the design-approach reference](../../../agents/references/design-approaches.md). Test whether apparent routes support expected movement and whether boundaries are understandable; this is an adaptation, not a claim to reproduce Nintendo's process or production values.
- Provisional loop: notice something interesting, choose a destination and route, travel, discover a connection or small scene, then choose whether to detour or pursue another interest.
- Decisions: destination, route, optional detour, and when to stop. No mandatory objective order, score threshold, or completion checklist is proposed.
- Observable reward: arriving changes the view or reveals a connection or distinctive scene, rather than merely incrementing a collectible count.

## A Scope: Confirmed by U2

- Validation question: Can this user form a personal destination, choose a route, and describe the experience as self-directed rather than a prescribed sequence or empty walking?
- Minimum playable content: one compact 2D top-down map; a controllable character and following camera; three recognizable landmarks; two connected approaches through the area and one optional secluded detour; restart.
- Presentation: simple readable terrain and landmark art. No abstract ship diagram, large-world promise, final-art claim, or unexplained invisible route gates. Custom assets are limited to what communicates the places and traversal.
- Proposed controls: keyboard movement for the initial desktop-browser experiment. Mobile touch support is outside this proposed slice, not an exclusion inferred from the user's browser preference.
- Technical assumption: local native browser rendering with simple terrain collision is the tentative smallest implementation. No dependency or architecture commitment is made by this proposal.
- Excluded: full 3D, climbing, gliding, combat, inventory, crafting, procedural generation, dialogue systems, saved progression, public deployment, paid assets, and additional maps.
- Budget: the confirmed three-hour total cap includes prototype implementation and verification across at most two iterations, not three hours per iteration. Stop with an honest partial result if it is insufficient; no automatic extension.
- Iteration allocation: first establish the playable exploration slice; use the second, only if needed and within the same cap, for corrections informed by observation. New core mechanics require renewed confirmation.
- Core gameplay/prototype-scope approval: U2 confirms this scope and the unchanged U1 budget envelope.

## Planned Evaluation, Not Results

Give basic movement controls, but no destination or route recommendation. Observe the first exploration attempt before offering navigation hints. Record separately any later guided understanding.

| Evidence | Planned observation | Interpretation limit |
| --- | --- | --- |
| Traversal verification | Check routes, collision, restart, camera, and browser errors. | Correct movement is not evidence of freedom or appeal. |
| Unassisted comprehension | Can the user identify a destination and understand traversable space without a suggested route? | One user's behavior does not establish general usability. |
| Agency and attraction | Ask what the user chose to investigate and why; note voluntary detours or decisions to stop. | Detours alone do not prove enjoyment; retain the user's explanation and negative feedback. |

- Continue if the user reports that destination and route choices feel personal and worth exploring; this is an evaluation criterion, not permission for more scope.
- Clarify within the remaining budget if interest exists but movement or visual cues are unclear.
- Propose a core revision if the layout effectively prescribes one route or gives choices no experiential value.
- Stop the direction if the user understands it but finds it uninteresting; do not respond by automatically adding a larger map or checklist.

These are planned checks, not results. Actual execution and iteration accounting are recorded in [validation.md](validation.md). No Player Validation is claimed; development handoff remains pending.
