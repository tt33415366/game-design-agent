from pathlib import Path
import json

from playwright.sync_api import sync_playwright

app = 'http://127.0.0.1:8765/index.html'
results = {}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for name, viewport, dpr in [('desktop', {'width': 1280, 'height': 900}, 1), ('mobile-dpr2', {'width': 390, 'height': 844}, 2)]:
        page = browser.new_page(viewport=viewport, device_scale_factor=dpr)
        page.goto(app); page.wait_for_function('window.__valleyDebug !== undefined'); page.wait_for_timeout(500)
        results[name] = page.evaluate("""() => {
          const ctx=game.getContext('2d'), data=ctx.getImageData(0,0,game.width,game.height).data, colors=new Set(), base=[127,187,91], step=20;
          let nonBase=0, opaque=0;
          for(let y=0;y<game.height;y+=step) for(let x=0;x<game.width;x+=step){const i=(y*game.width+x)*4,r=data[i],g=data[i+1],b=data[i+2],a=data[i+3];colors.add(r+','+g+','+b+','+a); if(a)opaque++; if(r!==base[0]||g!==base[1]||b!==base[2])nonBase++;}
          const w=ValleyWorld,r=ValleyRules.RADIUS,c=8;
          const crossesWithOnly = (openIndex) => { const extra=w.bridges.filter((_,i)=>i!==openIndex).map(b=>({x:930,y:b.y,width:150,height:b.height})); const q=[[Math.floor(850/c),Math.floor(790/c)]],seen=new Set([q[0].join(',')]),target=[Math.floor(1200/c),Math.floor(790/c)]; while(q.length){const [cx,cy]=q.shift();if(cx===target[0]&&cy===target[1])return true;for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const nx=cx+dx,ny=cy+dy,k=nx+','+ny,x=nx*c+c/2,y=ny*c+c/2;if(x<r||y<r||x>w.width-r||y>w.height-r||seen.has(k)||w.blockedAt(x,y,r)||extra.some(s=>x+r>s.x&&x-r<s.x+s.width&&y+r>s.y&&y-r<s.y+s.height))continue;seen.add(k);q.push([nx,ny]);}}return false;};
          return {canvas:[game.width,game.height], samples:Math.ceil(game.width/step)*Math.ceil(game.height/step), uniqueSampleColors:colors.size, opaqueSamples:opaque, nonBackgroundSamples:nonBase, upperOnlyCrossing:crossesWithOnly(0), lowerOnlyCrossing:crossesWithOnly(1)};
        }""")
        page.close()
    browser.close()
Path('/tmp/valley-final-v2/pixel-check.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
