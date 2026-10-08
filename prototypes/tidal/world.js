(function (root) {
  "use strict";
  const rect = (x, y, width, height, kind) => ({ shape: "rect", x, y, width, height, kind });
  const circle = (x, y, radius, kind) => ({ shape: "circle", x, y, radius, kind });
  const WORLD = {
    width: 2048, height: 1536, spawn: { x: 380, y: 760, facing: "east" },
    // Three channels run west->east. Each has one blocked segment with a stone in a notch.
    // Stone home notch blocks; open notch is 70px to the side, freeing the segment.
    channels: [
      // Stone home sits just below its blocked segment (inside the channel, reachable
      // from below); the open notch is just above the segment. Pushing the stone up past
      // the segment and into the notch opens the channel.
      { id: "north", rect: rect(300, 300, 1300, 90, "channel"), blockedSeg: rect(700, 300, 90, 90, "blocked"), stone: { home: { x: 745, y: 430 }, open: { x: 745, y: 250 } } },
      { id: "mid", rect: rect(700, 700, 900, 90, "channel"), blockedSeg: rect(1000, 700, 90, 90, "blocked"), stone: { home: { x: 1045, y: 830 }, open: { x: 1045, y: 650 } } },
      { id: "south", rect: rect(1100, 1100, 500, 90, "channel"), blockedSeg: rect(1300, 1100, 90, 90, "blocked"), stone: { home: { x: 1345, y: 1230 }, open: { x: 1345, y: 1050 } } }
    ],
    startRock: rect(340, 700, 80, 90, "startrock"),
    pool: { x: 1700, y: 745, radius: 60 },
    sights: [
      { id: "pool", name: "The Stranded Pool", x: 1700, y: 745, radius: 120, reveal: { x: 1700, y: 745, radius: 55, text: "Small fish turn in the last of the tide." } },
      { id: "arch", name: "The Tide Arch", x: 1150, y: 480, radius: 130, reveal: { x: 1150, y: 480, radius: 60, text: "The sea remembers every path twice." } }
    ],
    blockers: [
      // Reef rock scattered on the flat (always solid).
      ...[[200,180,28],[400,220,26],[600,150,30],[900,180,28],[1200,150,26],[1500,200,30],[1800,160,28],[1900,400,26],[1800,600,30],[1900,900,28],[1800,1300,26],[1600,1400,30],[1200,1420,26],[800,1400,30],[400,1420,28],[150,1200,26],[180,900,30],[150,500,28]].map((p)=>circle(p[0],p[1],p[2],"reef")),
      // Channel side-walls drawn as thin rock strips between channels (leave channel rects open).
      rect(300, 390, 1300, 26, "wall"), rect(300, 674, 1300, 26, "wall"), rect(300, 790, 1300, 26, "wall"), rect(300, 1074, 1300, 26, "wall")
    ],
    grassTiles: [[250,300],[560,900],[980,560],[1400,900],[700,1240],[1650,500],[450,1240],[1250,1240]]
  };
  function circleHitsRect(x,y,r,s) { const nx=Math.max(s.x,Math.min(x,s.x+s.width)), ny=Math.max(s.y,Math.min(y,s.y+s.height)); return (x-nx)**2+(y-ny)**2<r**2; }
  function shapeBlocks(x,y,r,s) { return s.shape === "circle" ? Math.hypot(x-s.x,y-s.y)<r+s.radius : circleHitsRect(x,y,r,s); }
  // stonesState: array of {x,y} current positions; a stone still at home blocks its segment.
  function segmentBlocked(i, stonesState) {
    const ch = WORLD.channels[i];
    const pos = stonesState && stonesState[i] ? stonesState[i] : ch.stone.home;
    const dx = pos.x - ch.stone.open.x, dy = pos.y - ch.stone.open.y;
    return Math.hypot(dx, dy) > 0.5; // still blocking unless snapped onto the open notch
  }
  function blockedAt(x,y,r,options) {
    if(x-r<0||y-r<0||x+r>WORLD.width||y+r>WORLD.height)return true;
    const opts = options || {};
    if(WORLD.blockers.some((s)=>shapeBlocks(x,y,r,s)))return true;
    for (let i = 0; i < WORLD.channels.length; i += 1) {
      const ch = WORLD.channels[i];
      if (opts.stones && segmentBlocked(i, opts.stones) && shapeBlocks(x,y,r,ch.blockedSeg)) return true;
      if (opts.stones && !segmentBlocked(i, opts.stones)) continue;
      // Stone entity itself blocks the player while in calm phase.
      if (opts.stones && opts.calm) { const pos = opts.stones[i] || ch.stone.home; if (Math.hypot(x-pos.x,y-pos.y) < r + 16) return true; }
    }
    return false;
  }
  function nearestSight(x,y) { return WORLD.sights.reduce((c,s)=>{const d=Math.hypot(x-s.x,y-s.y);return d<=s.radius&&(!c||d<c.distance)?{...s,distance:d}:c;},null); }
  function revealFor(x,y) { return WORLD.sights.reduce((hit,s)=>{ if(!s.reveal)return hit; const d=Math.hypot(x-s.reveal.x,y-s.reveal.y); return d<=s.reveal.radius?{id:s.id,...s.reveal}:hit; },null); }
  root.TidalWorld = { ...WORLD, blockedAt, shapeBlocks, circleHitsRect, nearestSight, revealFor, segmentBlocked, rect, circle };
})(globalThis);
