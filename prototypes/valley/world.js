(function (root) {
  "use strict";
  const rect = (x, y, width, height, kind) => ({ shape: "rect", x, y, width, height, kind });
  const circle = (x, y, radius, kind, tone) => ({ shape: "circle", x, y, radius, kind, tone });
  const tree = (x, y, radius, tone) => circle(x, y, radius, "tree", tone || "oak");
  const WORLD = {
    width: 2048, height: 1536, spawn: { x: 770, y: 790, facing: "east" },
    water: [rect(930, 0, 150, 410, "water"), rect(930, 474, 150, 506, "water"), rect(930, 1044, 150, 492, "water")],
    narrows: { x: 930, y: 700, width: 150, height: 24 },
    bridges: [{ x: 870, y: 410, width: 270, height: 64, name: "Willow Crossing" }, { x: 870, y: 980, width: 270, height: 64, name: "Stone Ford" }],
    log: { startX: 850, startY: 712, width: 170, height: 26 },
    paths: [
      { points: [[180,1180],[460,970],[770,790],[760,630],[850,500],[935,442],[1090,442],[1320,430],[1530,300]], width: 70 },
      { points: [[770,790],[690,550],[590,420],[500,440]], width: 58 },
      { points: [[770,790],[790,900],[860,970],[935,1012],[1090,1012],[1280,1110],[1530,1160],[1710,1180]], width: 70 },
      { points: [[720,820],[650,1010],[480,1190],[300,1320]], width: 56 },
      { points: [[1090,442],[1250,590],[1450,650],[1670,540]], width: 58 }
    ],
    landmarks: [
      { id:"tower", name:"The Ruined Tower", x:500, y:440, radius:155, reveal:{ x:410, y:300, radius:80, text:"Cold light through broken stone." } },
      { id:"crossing", name:"Willow Crossing", x:1005, y:442, radius:125, reveal:{ x:1005, y:442, radius:70, text:"The current slows around the planks." } },
      { id:"grove", name:"Secluded Grove", x:1710, y:1180, radius:180, reveal:{ x:1704, y:1162, radius:60, text:"Something glints among the roots." } },
      { id:"nook", name:"Fern Nook", x:300, y:1320, radius:135 }
    ],
    blockers: [
      rect(355,225,130,35,"ruin"),rect(350,260,35,125,"ruin"),rect(475,255,42,130,"ruin"),rect(385,365,92,28,"ruin"),
      ...[[290,235,20],[255,300,22],[275,400,23],[570,250,23],[595,345,22],[570,445,25],[1538,1040,28],[1608,1000,28],[1678,980,28],[1748,1000,28],[1818,1040,28],[1873,1110,28],[1878,1190,28],[1858,1270,28],[1798,1330,28],[1698,1360,28],[1608,1335,28],[1543,1275,28],[123,1240,28],[166,1350,26],[226,1440,26],[378,1430,28],[446,1383,26],[510,1305,25],[1185,280,25],[1264,235,24],[1345,285,25]].map((p)=>tree(...p)),
      circle(1471,351,21,"rock"),circle(1391,1127,20,"rock"),circle(638,1105,18,"rock"),
      ...[[118,128],[203,188],[788,148],[858,218],[1418,118],[1528,198],[1908,248],[1938,428],[1828,658],[168,708],[228,808],[108,1008],[1908,878],[1990,1128],[1065,1398],[1185,1458],[758,1448],[608,1488]].map((p)=>tree(p[0],p[1],25,"pine"))
    ],
    flowers: [[690,650],[735,610],[1190,770],[1260,820],[1440,660],[1540,790],[540,930],[465,1035],[1350,1180],[1430,1260],[680,390],[760,450]], grassTiles:[[160,300],[620,160],[1110,180],[1460,480],[320,760],[1160,900],[1720,720],[490,1160],[830,1280],[1230,1370],[1770,1420]]
  };
  function circleHitsRect(x,y,r,s) { const nx=Math.max(s.x,Math.min(x,s.x+s.width)), ny=Math.max(s.y,Math.min(y,s.y+s.height)); return (x-nx)**2+(y-ny)**2<r**2; }
  function shapeBlocks(x,y,r,s) { return s.shape === "circle" ? Math.hypot(x-s.x,y-s.y)<r+s.radius : circleHitsRect(x,y,r,s); }
  function logRect(pos) { const p=pos||{x:WORLD.log.startX,y:WORLD.log.startY}; return rect(p.x-WORLD.log.width/2, p.y-WORLD.log.height/2, WORLD.log.width, WORLD.log.height, "log"); }
  function logIsPlank(pos) { const r=logRect(pos); const n=WORLD.narrows; return r.x<=n.x && r.x+r.width>=n.x+n.width && r.y<=n.y && r.y+r.height>=n.y+n.height; }
  function waterShapes(options) {
    if(!options||!options.plank) return WORLD.water;
    const n=WORLD.narrows, out=[];
    WORLD.water.forEach((s)=>{
      if(s.y<n.y&&s.y+s.height>n.y+n.height){
        out.push(rect(s.x,s.y,s.width,n.y-s.y,"water"),rect(s.x,n.y+n.height,s.width,s.y+s.height-(n.y+n.height),"water"));
      } else out.push(s);
    });
    return out;
  }
  function blockedAt(x,y,r,options) {
    if(x-r<0||y-r<0||x+r>WORLD.width||y+r>WORLD.height)return true;
    const closed=options&&options.closedBridges?WORLD.bridges.map((b)=>rect(930,b.y,150,b.height,"closed-crossing")):[];
    const blocked=waterShapes(options).concat(WORLD.blockers,closed).some((s)=>shapeBlocks(x,y,r,s));
    if(blocked)return true;
    if(options&&options.logBlocked){ const lr=logRect(options.logBlocked); if(shapeBlocks(x,y,r,lr))return true; }
    return false;
  }
  function nearestLandmark(x,y) { return WORLD.landmarks.reduce((closest,l)=>{const distance=Math.hypot(x-l.x,y-l.y);return distance<=l.radius&&(!closest||distance<closest.distance)?{...l,distance}:closest;},null); }
  function revealFor(x,y) { return WORLD.landmarks.reduce((hit,l)=>{ if(!l.reveal)return hit; const d=Math.hypot(x-l.reveal.x,y-l.reveal.y); return d<=l.reveal.radius?{id:l.id,...l.reveal}:hit; },null); }
  root.ValleyWorld={...WORLD,blockedAt,shapeBlocks,circleHitsRect,nearestLandmark,revealFor,logRect,logIsPlank,rect,circle};
})(globalThis);
