from pathlib import Path
import json

from playwright.sync_api import sync_playwright

ROOT = Path('/data/lea/Workspace/game_designer/prototypes/valley')
OUT = Path('/tmp/valley-final-v2')
APP = (ROOT / 'index.html').as_uri()

def hold(page, key, seconds):
    page.keyboard.down(key)
    page.wait_for_timeout(round(seconds * 1000))
    page.keyboard.up(key)
    page.wait_for_timeout(100)

def snap(page, name):
    page.screenshot(path=str(OUT / f'{name}.png'), full_page=True)

def observe(page):
    return page.evaluate("""() => ({
      player: __valleyDebug.player, camera: __valleyDebug.camera, held: __valleyDebug.heldKeys,
      place: document.querySelector('#place').textContent, canvas: [game.width,game.height,game.clientWidth,game.clientHeight],
      assetDimensions: {town: [...document.querySelectorAll('img')].map(x => [x.complete,x.naturalWidth]),
        viaDraw: (() => { const c=document.createElement('canvas'); c.width=2;c.height=2;return true; })()}
    })""")

def reset(page):
    page.locator('#reset').click(); page.wait_for_timeout(150)

def topology(page):
    return page.evaluate("""() => {
      const w=ValleyWorld,r=ValleyRules.RADIUS,c=8;
      const reach = (closed) => { const start=[Math.floor(w.spawn.x/c),Math.floor(w.spawn.y/c)], q=[start], seen=new Set([start.join(',')]);
        while(q.length){const [cx,cy]=q.shift();for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const nx=cx+dx,ny=cy+dy,k=nx+','+ny,x=nx*c+c/2,y=ny*c+c/2;if(x<r||y<r||x>w.width-r||y>w.height-r||seen.has(k)||w.blockedAt(x,y,r,closed?{closedBridges:true}:undefined))continue;seen.add(k);q.push([nx,ny]);}}return seen; };
      const seen=reach(false), closed=reach(true), has=(s,x,y)=>s.has(Math.floor(x/c)+','+Math.floor(y/c));
      const tree=w.blockers.find(s=>s.kind==='tree'), rock=w.blockers.find(s=>s.kind==='rock');
      return { landmarks:w.landmarks.map(l=>has(seen,l.x,l.y)),bridges:w.bridges.map(b=>has(seen,b.x+b.width/2,b.y+b.height/2)),
        eastOpen:has(seen,1200,790),eastWhenBridgesClosed:has(closed,1200,790),
        trunkBlocked:w.blockedAt(tree.x,tree.y,0), canopyOutsideWalkable:!w.blockedAt(tree.x+tree.radius+11,tree.y,10),
        rockBlocked:w.blockedAt(rock.x,rock.y,0), waterCenterBlocked:w.blockedAt(1005,790,r),
        bridgeCenters:w.bridges.map(b=>!w.blockedAt(b.x+b.width/2,b.y+b.height/2,r))};
    }""")

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)
    out={}
    for width,height,label,dpr in [(1280,900,'desktop',1),(390,844,'mobile',1),(320,568,'narrow',1),(2400,1800,'oversized',1),(390,844,'mobile-dpr2',2)]:
        page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=dpr)
        errors=[]; warnings=[]; failed=[]
        page.on('pageerror',lambda exc:errors.append(str(exc)))
        page.on('console',lambda msg:warnings.append([msg.type,msg.text]) if msg.type in ('error','warning') else None)
        page.on('requestfailed',lambda req:failed.append([req.url,req.failure]))
        page.goto(APP,wait_until='load');page.wait_for_function('window.__valleyDebug !== undefined');page.wait_for_timeout(600)
        out[label]={'initial':observe(page),'errors':errors,'console':warnings,'failed':failed}
        snap(page,f'{label}-initial')
        if label=='desktop':
            # Direct water at spawn must stop; reset then keyboard navigation, no debug coordinate assignments.
            hold(page,'KeyD',1.4); out['central_water']=observe(page);snap(page,'desktop-central-water')
            reset(page);hold(page,'KeyW',2.18);hold(page,'KeyD',2.75);out['upper_bridge_exit']=observe(page);snap(page,'desktop-upper-bridge-exit')
            reset(page);hold(page,'KeyS',1.40);hold(page,'KeyD',2.75);out['lower_bridge_exit']=observe(page);snap(page,'desktop-lower-bridge-exit')
            reset(page);hold(page,'KeyW',2.18);hold(page,'KeyA',1.70);out['tower']=observe(page);snap(page,'desktop-tower')
            reset(page);hold(page,'KeyS',1.40);hold(page,'KeyD',2.75);hold(page,'KeyS',1.05);hold(page,'KeyD',2.90);out['grove']=observe(page);snap(page,'desktop-grove')
            reset(page);hold(page,'KeyS',3.30);hold(page,'KeyA',3.00);out['nook']=observe(page);snap(page,'desktop-nook')
            # Blur clears currently held input and does not advance during the pause.
            reset(page);page.keyboard.down('KeyD');page.wait_for_timeout(120);before=observe(page);page.evaluate('window.dispatchEvent(new Event("blur"))');page.wait_for_timeout(350);after=observe(page);page.keyboard.up('KeyD')
            page.locator('#reset').focus();page.keyboard.press('Enter');page.wait_for_timeout(150);out['blur_reset']={'before':before,'after':after,'reset':observe(page),'topology':topology(page)}
            # Resize behavior after movement: player persists and camera recalculates.
            hold(page,'KeyD',.5);before_resize=observe(page);page.set_viewport_size({'width':390,'height':844});page.wait_for_timeout(200);out['resize']={'before':before_resize,'after':observe(page)}
        page.close()
    browser.close()
OUT.joinpath('results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
