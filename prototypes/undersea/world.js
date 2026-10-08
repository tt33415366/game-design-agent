(function (root) {
  "use strict";
  const rect = (x, y, width, height, kind) => ({ shape: "rect", x, y, width, height, kind });
  const circle = (x, y, radius, kind, tone) => ({ shape: "circle", x, y, radius, kind, tone });
  const coral = (x, y, radius, tone) => circle(x, y, radius, "coral", tone || "reef");
  const WORLD = {
    width: 2048, height: 1536, spawn: { x: 700, y: 760, facing: "east" },
    // The current channel is a rock wall (not water) crossing the shelf; the boulder
    // bridges a collapsed gap (narrows) in it to form a swim-through arch shortcut.
    channel: [rect(920, 0, 40, 690, "rockwall"), rect(920, 760, 40, 776, "rockwall")],
    narrows: { x: 920, y: 690, width: 40, height: 70 },
    boulder: { startX: 850, startY: 725, radius: 26 },
    crevice: { x: 1560, y: 1180, radius: 150, heart: { x: 1630, y: 1250, radius: 45 } },
    sights: [
      { id: "arch", name: "The Reef Arch", x: 480, y: 420, radius: 150, reveal: { x: 480, y: 420, radius: 70, text: "Light bends through living stone." } },
      { id: "wreck", name: "The Silent Hull", x: 320, y: 1180, radius: 160, reveal: { x: 330, y: 1170, radius: 70, text: "Barnacles where hands once worked." } },
      { id: "garden", name: "The Anemone Garden", x: 1520, y: 380, radius: 170, reveal: { x: 1520, y: 380, radius: 75, text: "A hundred small mouths open at once." } },
      { id: "flat", name: "The Empty Flat", x: 760, y: 1240, radius: 140 }
    ],
    blockers: [
      ...[[200,180,30],[300,260,26],[420,180,28],[560,300,30],[640,200,26],[180,420,28],[240,540,30],[380,600,26],[520,700,28],[620,560,26],[180,820,28],[260,940,30],[140,1060,26],[420,900,28],[560,1040,30],[640,1180,28],[520,1330,30],[300,1340,26],[180,1250,28]].map((p)=>coral(...p)),
      ...[[1180,200,30],[1300,140,28],[1420,240,32],[1560,180,28],[1700,260,30],[1840,180,30],[1920,320,28],[1800,420,32],[1930,560,30],[1720,600,28],[1600,540,26],[1450,640,30],[1300,560,28],[1180,640,30],[1260,760,32],[1400,840,28],[1560,780,30],[1700,880,28],[1850,800,30],[1930,980,28]].map((p)=>coral(p[0],p[1],p[2],"fan")),
      ...[[1200,1100,30],[1320,1200,28],[1440,1120,26],[1180,1320,30],[1340,1420,28],[1500,1360,26],[1860,1300,30],[1940,1440,28],[1720,1430,26]].map((p)=>coral(p[0],p[1],p[2],"brain")),
      // Crevice wall ring: solid coral except the mouth opening on the west side.
      ...[[1490,1080,30],[1600,1050,32],[1710,1080,30],[1760,1170,32],[1730,1290,30],[1630,1340,32],[1520,1330,30]].map((p)=>coral(p[0],p[1],p[2],"dark")),
      circle(700,300,24,"rock"), circle(900,500,22,"rock"), circle(1100,900,24,"rock"), circle(500,1450,26,"rock"), circle(1050,1300,22,"rock")
    ],
    fans: [[620,420],[700,480],[1180,480],[1620,340],[380,1090],[290,1260],[1480,300],[1690,1180],[1640,1240]]
  };
  function circleHitsRect(x,y,r,s) { const nx=Math.max(s.x,Math.min(x,s.x+s.width)), ny=Math.max(s.y,Math.min(y,s.y+s.height)); return (x-nx)**2+(y-ny)**2<r**2; }
  function shapeBlocks(x,y,r,s) { return s.shape === "circle" ? Math.hypot(x-s.x,y-s.y)<r+s.radius : circleHitsRect(x,y,r,s); }
  function boulderCircle(pos) { const p=pos||{x:WORLD.boulder.startX,y:WORLD.boulder.startY}; return circle(p.x,p.y,WORLD.boulder.radius,"boulder"); }
  function boulderIsArch(pos) { const n=WORLD.narrows; return Math.hypot(pos.x-(n.x+n.width/2),pos.y-(n.y+n.height/2))<=WORLD.boulder.radius*.5; }
  function channelShapes(options) {
    if(!options||!options.arch) return WORLD.channel;
    const n=WORLD.narrows, out=[];
    WORLD.channel.forEach((s)=>{
      if(s.y<n.y&&s.y+s.height>n.y+n.height){
        out.push(rect(s.x,s.y,s.width,n.y-s.y,"rockwall"),rect(s.x,n.y+n.height,s.width,s.y+s.height-(n.y+n.height),"rockwall"));
      } else out.push(s);
    });
    return out;
  }
  function blockedAt(x,y,r,options) {
    if(x-r<0||y-r<0||x+r>WORLD.width||y+r>WORLD.height)return true;
    const closed=options&&options.closedArch?[rect(WORLD.narrows.x,WORLD.narrows.y,WORLD.narrows.width,WORLD.narrows.height,"closed")]:[];
    if(channelShapes(options).concat(WORLD.blockers,closed).some((s)=>shapeBlocks(x,y,r,s)))return true;
    if(options&&options.boulderBlocked){ const b=boulderCircle(options.boulderBlocked); if(shapeBlocks(x,y,r,b))return true; }
    return false;
  }
  function nearestSight(x,y) { return WORLD.sights.reduce((closest,s)=>{const d=Math.hypot(x-s.x,y-s.y);return d<=s.radius&&(!closest||d<closest.distance)?{...s,distance:d}:closest;},null); }
  function revealFor(x,y) {
    const h=WORLD.crevice.heart; if(Math.hypot(x-h.x,y-h.y)<=h.radius)return {id:"crevice",x:h.x,y:h.y,radius:h.radius,text:"In the dark, the shelf exhales."};
    return WORLD.sights.reduce((hit,s)=>{ if(!s.reveal)return hit; const d=Math.hypot(x-s.reveal.x,y-s.reveal.y); return d<=s.reveal.radius?{id:s.id,...s.reveal}:hit; },null);
  }
  function inCrevice(x,y) { const c=WORLD.crevice; return Math.hypot(x-c.x,y-c.y)<=c.radius; }
  root.UnderseaWorld={...WORLD,blockedAt,shapeBlocks,circleHitsRect,nearestSight,revealFor,inCrevice,boulderCircle,boulderIsArch,rect,circle};
})(globalThis);
