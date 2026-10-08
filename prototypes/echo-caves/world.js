(function(root){"use strict";
const rect=(x,y,width,height,kind)=>({shape:"rect",x,y,width,height,kind});
const circle=(x,y,radius,kind)=>({shape:"circle",x,y,radius,kind});
const W={width:2048,height:1536,spawn:{x:460,y:760,facing:"east"},mouth:{x:540,y:760,radius:90},
branches:[{id:"glow",name:"Warm Glow Branch",cue:"warm",bounds:rect(650,560,780,90,"cave"),reveal:{x:1320,y:605,radius:48,text:"A hidden reef burns without flame."}},{id:"drift",name:"Drift Branch",cue:"drift",bounds:rect(650,710,900,90,"cave"),reveal:{x:1500,y:755,radius:48,text:"The particles turn against the current."}},{id:"shadow",name:"Shadow Branch",cue:"shadow",bounds:rect(650,860,780,90,"cave"),reveal:{x:1320,y:905,radius:48,text:"Something large passed through here."}}],
walls:[rect(650,470,900,30,"wall"),rect(650,650,900,30,"wall"),rect(650,800,900,30,"wall"),rect(650,950,900,30,"wall"),rect(1550,470,30,510,"wall")],rocks:[circle(260,240,30,"rock"),circle(420,1180,28,"rock"),circle(1780,300,30,"rock"),circle(1800,1200,28,"rock")]};
function circleHitsRect(x,y,r,s){const nx=Math.max(s.x,Math.min(x,s.x+s.width)),ny=Math.max(s.y,Math.min(y,s.y+s.height));return(x-nx)**2+(y-ny)**2<r*r;}
function shapeBlocks(x,y,r,s){return s.shape==="circle"?Math.hypot(x-s.x,y-s.y)<r+s.radius:circleHitsRect(x,y,r,s);}
function blockedAt(x,y,r){if(x-r<0||y-r<0||x+r>W.width||y+r>W.height)return true;return W.walls.concat(W.rocks).some(s=>shapeBlocks(x,y,r,s));}
function branchAt(x,y){return W.branches.find(b=>x>b.bounds.x&&x<b.bounds.x+b.bounds.width&&y>b.bounds.y&&y<b.bounds.y+b.bounds.height)||null;}
function revealFor(x,y){for(const b of W.branches){if(Math.hypot(x-b.reveal.x,y-b.reveal.y)<=b.reveal.radius)return{id:b.id,...b.reveal};}return null;}
function nearest(x,y){return W.branches.reduce((c,b)=>{const d=Math.hypot(x-b.reveal.x,y-b.reveal.y);return d<80&&(!c||d<c.distance)?{...b,distance:d}:c;},null);}
root.EchoWorld={...W,blockedAt,shapeBlocks,circleHitsRect,branchAt,revealFor,nearest,rect,circle};})(globalThis);
