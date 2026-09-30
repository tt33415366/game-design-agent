# Independent Browser and Visual Verification: Unmarked Valley

Date: 2026-09-30 UTC. Scope: read-only independent verification of `prototypes/valley/`; temporary harnesses and evidence only in `/tmp/valley-independent/`.

## Result

The prototype loads and renders at desktop, mobile, and narrow mobile dimensions without console errors, page errors, failed network requests, blank canvas, dashboard/card framing, or a tutorial overlay. `WASD` and arrow movement, reset by focused button + `Enter`, blur key clearing, camera following/clamping, tower arrival, Willow Crossing arrival, Secluded Grove arrival, and Fern Nook arrival were exercised in Chromium.

The scene is readable as a small top-down countryside/valley: blue stream, wooden bridges, gray ruined tower, trees, pixel player, and a small pixel building inside the grove. It is nevertheless predominantly flat canvas geometry; the sole visible atlas-style scenery object is the small grove building. This is materially less specific than the requested local raster-art presentation, but it does not resemble the rejected abstract-ship presentation.

## Material Findings

1. The central drawn path falsely implies a direct stream crossing. From spawn, actual `KeyD` movement stops at `x=911.33, y=790` against water while the visible horizontal path leads into the water. Evidence: `/tmp/valley-independent/desktop-central-path-blocked.png`; interaction result in `/tmp/valley-independent/focused.json` under `blocked_central_path`.

2. The stream can be bypassed around its north end, so its two visible bridges are not the only bank connections. Actual keyboard route from spawn (`KeyW` 4.62 s, then `KeyD` 2.3 s) reached the east bank at `x=1137.98, y=48.70` without a bridge. Independently, a grid reachability check still connected west/east banks after both bridge gaps were closed (`bothBridgesClosed: true`). Evidence: `/tmp/valley-independent/desktop-north-bank-bypass.png` and `/tmp/valley-independent/focused.json`.

3. Some drawn tree canopies have no matching collision. `ValleyWorld.blockedAt(770,140,10)` reports walkable, and real `KeyW` movement placed the player at `x=770, y=142.03`, visibly inside the rendered tree canopy. Evidence: `/tmp/valley-independent/desktop-tree-overlap.png` and `/tmp/valley-independent/focused.json` under `walk_through_drawn_tree`.

4. Lower crossing traversal has an unusually narrow exit because the collision gap is exactly bounded by the player radius. A simple south-then-east attempt reaches the lower bridge but cannot travel south until the player first moves beyond the right water edge. This does not make the grove unreachable, but it conflicts with the visual reading of a broad bridge/path. Evidence: first independent sequence in `/tmp/valley-independent/result.json` (`desktop-lower-crossing` at `x=985.98, y=1005.98`) and the successful longer route required for `/tmp/valley-independent/desktop-grove-approach.png`.

## Positive Checks

- Keyboard: `KeyD` moved spawn from `x=770` to `x=834`; `ArrowLeft` returned it to about `x=770`. Held keys were empty after synthetic browser blur and position stayed stable.
- Reset: focus `#reset`, press `Enter`; player returned to authored spawn and camera returned to `{x:130,y:340}` at 1280x900.
- Topology: independent grid checks reached all four authored approach areas. With either one bridge closed, the other bridge still connected banks; this is separate from the unintended end-around bypass when both are closed.
- Visual sizes: 1280x900, 390x844, and 320x568 have visible player/scenery and no text or control overlap. The viewport remains a canvas scene with only title, place feedback, and restart; mobile is visual-only as scoped.

## Evidence Paths

- `/tmp/valley-independent/desktop-initial.png`
- `/tmp/valley-independent/mobile-initial.png`
- `/tmp/valley-independent/narrow-initial.png`
- `/tmp/valley-independent/desktop-tower.png`
- `/tmp/valley-independent/desktop-upper-crossing.png`
- `/tmp/valley-independent/desktop-lower-crossing.png`
- `/tmp/valley-independent/desktop-grove-approach.png`
- `/tmp/valley-independent/desktop-nook-approach.png`
- `/tmp/valley-independent/desktop-central-path-blocked.png`
- `/tmp/valley-independent/desktop-north-bank-bypass.png`
- `/tmp/valley-independent/desktop-tree-overlap.png`
- `/tmp/valley-independent/result.json`
- `/tmp/valley-independent/focused.json`
