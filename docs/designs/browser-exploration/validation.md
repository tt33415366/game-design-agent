# Unmarked Valley: Validation and Budget

Actual approvals: U1/U2 in [brief.md](brief.md). Rule authority: [system.md](system.md).

## Budget Ledger

- Local-only, zero spending, at most two prototype iterations.
- Three-hour cap includes implementation and verification, not three hours per iteration.
- Start: 2026-09-30 08:12:39 UTC. Absolute stop: 2026-09-30 11:12:39 UTC.
- Iteration 1: built; four browser tests passed, but independent review found visible/collider mismatch, stale reset feedback, low-frame-rate slowdown, and misleading trail geometry. Preserved screenshots are in `evidence/iteration-1-desktop.png` and `evidence/iteration-1-mobile.png`.
- Iteration 2: preparation started at 2026-09-30 08:28:31 UTC; the single reserved correction pass addressed these observations and independent visual findings. Final verification completed at 08:40:26 UTC, within the same cap. Both approved iterations have been used; further implementation requires a renewed budget decision.
- No public deployment, paid assets, external uploads, or additional gameplay systems authorized.

## Experience Question

Can the user choose a destination and route without a prescribed sequence, and find that choice worth pursuing? Give movement controls but no suggested destination. Keep unassisted exploration separate from subsequent guided explanation. Record the user's actual report before interpreting whether the concept is appealing.

## Evidence

Asset sourcing: two free Kenney atlases are stored locally with original bundled license text and provenance in `prototypes/valley/assets/README.md`. The asset worker inspected the atlases and supplied tile crop coordinates; this is asset inspection, not game rendering or Player Validation.

### Iteration 1: Rule Verification and Developer Inspection

The root ran:

```sh
PLAYWRIGHT_BROWSERS_PATH=/tmp/game-designer-browsers /tmp/game-designer-tools/bin/python -m unittest prototypes/valley/tests/test_valley.py
```

Observed: four tests passed. This suite did not detect the defects found by independent review. The preserved [logic review](evidence/valley-review.md) records concrete collider/render mismatches, stale place feedback after reset, and active movement slowing below 20 fps.

The [independent browser/visual report](evidence/valley-verification.md) records actual keyboard traversal to the tower, crossing, grove, and nook; blur/reset/camera checks; and nonblank, unclipped rendering at 1280x900, 390x844, and 320x568 without page/console/network errors. It also records a misleading central path into blocked water, a north-end stream bypass, tree overlap, and an awkward lower-bridge exit. Screenshots in this directory preserve the initial desktop/mobile view; additional diagnostic images and raw interaction results remain at the temporary paths cited by the report.

Decision: **revise** within the approved second iteration. Version 1.1 of the rules clarifies active-time integration and ground-level collision cues without adding gameplay. The implementation correction covers shared visible geometry, honest trails, bridge clearance, perimeter treatment, reset feedback, and consistent local raster scenery. Tree canopy overhang is allowed; walking through a visible trunk is not.

### Iteration 2

Implementation, final code review, and independent final visual/browser verification are complete.

During integration of the correction pass, root inspection found that `nearestLandmark` had been defined but omitted from the world export while the renderer still called it. The four grouped rule tests could pass despite this frame-loop failure because they exercised debug helpers without asserting browser page errors or sustained actual keyboard movement. Independent verification reproduced the failure; [negative evidence](evidence/iteration-2-runtime-regression.json) is retained. The pass was not accepted until that regression and incomplete visual-footprint/perimeter work were addressed and independently rechecked.

The worker corrected the export and remaining visual-footprint/perimeter omissions, and added a live keyboard/animation-frame check with page-error collection. The root reran the same command above on the resulting source: **five tests passed in 0.857 seconds**. The suite covers deterministic movement, low-frame-rate speed and stall cap, obstacle footprints, reset/blur, reachability and closed-crossing isolation, responsive rendering, and actual keyboard movement through the animation loop. These are five grouped tests, not exhaustive browser coverage.

The [final independent code review](evidence/valley-review-final.md) found no remaining must-fix defect. Preserved final-build screenshots: [desktop](evidence/iteration-2-desktop.png) and [mobile](evidence/iteration-2-mobile.png).

The [final independent browser report](evidence/valley-verification-final.md) records actual keyboard traversal across both bridges, tower/grove approaches, blur/reset/resize, both crossings independently connecting the banks, and isolation when both are closed. It reports no page/console/network errors at 1280x900, 390x844, 320x568, 2400x1800, and DPR 2. Pixel samples confirmed nonblank opaque canvas content; both local atlases loaded. Final raw results, pixel/topology samples, and screenshots are preserved under `evidence/final-browser/` (the report's original temporary paths identify the same artifacts).

Developer visual inspection found recognizable landmarks and traversal surfaces with no HUD clipping or overlap. The scene remains simple custom Canvas art with limited raster decoration, not production-final art. Keyboard input only; mobile dimensions verify layout, not touch play. Tests do not establish cross-browser compatibility, complete accessibility, performance on arbitrary hardware, or genuine hidden-tab lifecycle behavior.

Decision: **continue to Player Validation**, not broader development. Open `prototypes/valley/index.html` directly in a desktop browser, give only WASD/arrow and Restart controls, and ask what attracted the user's attention and whether route choice felt worthwhile. No further implementation, spending, or handoff approval is implied.

Process lesson: retain real animation-loop and page-error checks alongside pure rule tests. Passing debug-helper tests did not prove that the playable loop ran; no such claim was used to bypass the failed integration check.

### Player Validation

**U3 report (2026-09-30, in progress):** The user was "a bit curious" about the gray ruin at the end of the road and the gray blocks in the wild (guessing "a castle?"), and asked what their purpose is if they cannot be interacted with.

Reading: landmark visual curiosity works as designed — the user noticed a destination, investigated on their own, and identified the stonework. However, arrival provides only a place name and no payoff, so the user immediately questioned the purpose of the landmark. This is consistent with the brief's recorded uncertainty ("Do the places inspire personal curiosity, or does moving around merely feel aimless?"). The report does not yet cover route choice, other landmarks, or whether wandering felt worthwhile overall; those questions remain open. Classification: Player Validation, partially collected; appeal of the exploration loop is not established.

**U4 report (2026-09-30, completes Player Validation for this prototype):** The user did explore further, "but found nothing. It's interesting at the beginning, but no rewards make it boring after a while."

Reading: the user engaged voluntarily with the space, so landmark-driven curiosity and free route choice were sufficient to start play. Interest then decayed because arrival yields no reward — no reveal, interaction, or follow-up. The loop's second half ("discover a connection or small scene, then choose another interest") is not substantiated. Decision per the plan: **stop this direction as-is** — the user understands it and finds it uninteresting in sustained play. Per the brief, do not respond by automatically adding a larger map or a checklist.

Recorded stop decision: no further iteration of Candidate A without renewed user confirmation and a revised gameplay proposal. The narrowest future hypotheses, for later user selection only: (a) arrival payoff — landmarks reveal something worth finding; (b) richer space — traversal itself becomes interesting; (c) different theme with stronger inherent pull. None is selected; any would be a revised gameplay/prototype scope requiring a new checkpoint, and none is authorized by this record.

Player Validation for this prototype is complete. Classification: Player Validation, desirability evidence, single first-evaluator user; does not generalize to other players. Development handoff remains pending and is now moot for this direction.

Development handoff remains pending. Do not treat developer inspection, the earlier salvage experience, or constructed agent exercises as observations of this prototype's appeal.

### Iteration v2 (arrival payoff + push micro-interaction), 2026-09-30

Revised scope confirmed 09:25 UTC (2h / 1 iteration / zero spend; absolute stop 11:25:47 UTC). Implemented: three arrival reveals (tower, crossing, grove) with once-only inline flavor text; one pushable log that locks into a plank across the narrows at (930,700) enabling a shortcut to the east bank; reveal/log/place state cleared on restart. Fern Nook intentionally has no reveal.

Verification (root-run, downgraded independence — the delegated worker subagent failed on upstream 502 and implementation was done in-thread):
- Full suite: 7 tests pass (`test_valley.py`), covering v1 movement/collision/topology/reset plus push-to-plank geometry and reveal-once semantics.
- Real-browser smoke: player pushed the log to a locked plank and walked across to the east bank (x=2035) with zero page/console errors; all three reveals fired exactly once with flavor text; screenshots `v2-log-plank.png`, `v2-{tower,crossing,grove}-reveal.png` under `prototypes/valley/tests/evidence/`.
- Debug trail preserved: three push-follow iterations and a narrows-sizing correction (log height < narrows height) were needed; these are recorded as execution errors, not instruction gaps.

Player Validation for v2: **U5 report (2026-09-30 09:50 UTC)**. After an unassisted first play, asked "did you investigate a landmark unprompted, and after the first reveal did you voluntarily seek another?", the user answered "Yes, it does." Both F6 signals are affirmed: initial attraction (unprompted investigation) and sustained interest (seeking another landmark after the first payoff). This is the first time in this project that sustained interest is evidenced rather than assumed. Classification: Player Validation, desirability, single first-evaluator user; "yes" does not quantify strength, and does not generalize beyond this user.

Decision per the v2 plan's stop criterion (stop if the user does NOT seek a second landmark after the first reveal): the stop condition is **not** met. The direction survives this validation round. This does not authorize further implementation, expansion, or handoff — those require their own explicit confirmation.

### Side-Conversation Directive (2026-09-30, user-approved)

Recorded from the user's side-conversation exchange with the assistant. This is context and direction for the next phase, not a checkpoint confirmation.

- The durable goal of this repository is designing and improving the **game designer agent** (contract, skills, templates, orchestration). The Unmarked Valley prototype and the earlier salvage exercise are verification exercises of that workflow, not the product.
- After this prototype's Player Validation concludes, run a retrospective harvest: classify every finding from iteration reviews, independent verification, and the user's playtests into contract gap, skill gap, template gap, or one-off execution error; propose concrete diffs to the designer-agent assets before changing them. Candidate lessons already visible: `system-design` should demand drawn-vs-collidable geometry consistency; `design-prototype` should require real animation-loop and page-error checks alongside pure rule tests; theme/appeal validation needs strengthening.
- Checkpoint confirmations still require the user's explicit decision in the active thread; this note does not approve any checkpoint.
