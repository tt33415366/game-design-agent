# Final Independent Verification: Unmarked Valley

Date: 2026-09-30 UTC. Scope: final read-only Chromium verification of `prototypes/valley/`. Earlier crash evidence remains isolated in `/tmp/valley-final/`; this report covers the repaired final source and `/tmp/valley-final-v2/` evidence.

## Result

Pass. The repaired build has no page errors, console errors/warnings, or failed runtime requests in fresh desktop (1280x900), mobile (390x844), narrow (320x568), oversized (2400x1800), and DPR-2 mobile Chromium sessions. The repository suite also passed: 5 tests, 0 failures.

The main canvas remains a readable top-down valley scene rather than an abstract diagram: a bordered green world, continuous blue stream, two wooden bridges, trails, blocked tree bases with canopy overhang, stone ruin/tower, grove-side building, rocks, player sprite, and restrained title/restart HUD. The visual style is deliberately simple and mostly custom canvas geometry with limited local raster decoration; it is not production-final art, but the landmarks and traversal surfaces are recognizable and coherent for the approved prototype.

## Interaction and Geometry Evidence

- Actual RAF keyboard movement traversed and exited both bridges: upper exit reached `(1209.97, 440.67)` and lower exit `(1209.97, 1013.98)` from spawn using held keys. Screenshots: `desktop-upper-bridge-exit.png`, `desktop-lower-bridge-exit.png`.
- Direct eastward keyboard movement at spawn stops before water at `x=919.33`; the visual trail now routes to the upper/lower bridges rather than drawing a direct central river crossing. Screenshot: `desktop-central-water.png`.
- Actual keyboard approaches produced landmark feedback for `The Ruined Tower` and `Secluded Grove`. Screenshots: `desktop-tower.png`, `desktop-grove.png`.
- Independent topology check: all landmark approach areas and both bridge centers are reachable; each bridge independently connects banks when the other is closed; closing both disconnects the banks. `upperOnlyCrossing=true`, `lowerOnlyCrossing=true`, `eastWhenBridgesClosed=false`.
- Collision consistency: stream center, tree trunk/base, and rock centers block. A point beyond the tree base is walkable, preserving explicitly permitted decorative canopy overhang.
- Blur clears a held `KeyD` and player position remains unchanged during the subsequent 350 ms; focused-button `Enter` returns player and camera to spawn. Resize preserves player position and recalculates camera.

## Render and Viewport Evidence

- Desktop/mobile/narrow screenshots are nonblank, contain visible player and scenery, and have no clipping or overlap of title/restart HUD.
- Oversized capture shows the complete bordered world with the river reaching both visible perimeter edges; no unintended river-end bypass is visible.
- Same-origin sampled canvas pixels: desktop had 58 unique sampled colors and 1,126 non-background samples out of 2,880; DPR-2 mobile had 48 unique sampled colors and 1,353 non-background samples out of 3,315. Both canvases were fully opaque. Local HTTP evidence confirms both Kenney atlas files loaded at runtime.

## Evidence

- Results: `/tmp/valley-final-v2/results.json`
- Pixel/topology samples: `/tmp/valley-final-v2/pixel-check.json`
- Screenshots: `/tmp/valley-final-v2/desktop-initial.png`, `mobile-initial.png`, `narrow-initial.png`, `oversized-initial.png`, `mobile-dpr2-initial.png`, `desktop-central-water.png`, `desktop-tower.png`, `desktop-upper-bridge-exit.png`, `desktop-lower-bridge-exit.png`, `desktop-grove.png`
