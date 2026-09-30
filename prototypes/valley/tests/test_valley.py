import os
import unittest
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "index.html"


class ValleyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)
        cls.page = cls.browser.new_page(viewport={"width": 1280, "height": 900})
        cls.errors = []
        cls.page.on("pageerror", lambda error: cls.errors.append(str(error)))
        cls.page.goto(APP.as_uri())
        cls.page.wait_for_function("window.__valleyDebug !== undefined")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def evaluate(self, script):
        return self.page.evaluate(script)

    def test_rules_cardinal_diagonal_low_fps_and_frame_cap(self):
        result = self.evaluate("""() => {
          const r = ValleyRules, w = ValleyWorld, p = {x: 700, y: 700, facing: 'east'};
          const east = r.move(p, {KeyD: true}, 1, w);
          const diagonal = r.move(p, {KeyD: true, KeyS: true}, .05, w);
          const tenFps = Array.from({length: 10}).reduce((q) => r.move(q, {KeyD:true}, .1, w), p);
          return { east: east.x - p.x, diagonal: Math.hypot(diagonal.x-p.x, diagonal.y-p.y), tenFps: tenFps.x-p.x, cap: r.move(p, {KeyD:true}, 9, w).x-p.x };
        }""")
        self.assertAlmostEqual(result["east"], 40, places=4)
        self.assertAlmostEqual(result["diagonal"], 8, places=4)
        self.assertAlmostEqual(result["tenFps"], 160, places=4)
        self.assertAlmostEqual(result["cap"], 40, places=4)

    def test_collision_reset_and_focus_key_clear(self):
        result = self.evaluate("""() => {
          const d = __valleyDebug, w = ValleyWorld, r = ValleyRules;
          const water = r.move({x: 910,y:700,facing:'east'}, {KeyD:true}, .05, w);
          window.dispatchEvent(new KeyboardEvent('keydown', {code:'KeyD'})); window.dispatchEvent(new Event('blur'));
          d.reset(); const reset = d.player;
          const tree = w.blockers.find(s => s.kind === 'tree');
          const rock = w.blockers.find(s => s.kind === 'rock');
          return { waterX: water.x, keys: d.heldKeys.length, reset, place: document.querySelector('#place').textContent,
            treeCenter: w.blockedAt(tree.x, tree.y, 0), treeOutside: w.blockedAt(tree.x + tree.radius + 11, tree.y, 10),
            rockCenter: w.blockedAt(rock.x, rock.y, 0), rockCorner: w.blockedAt(rock.x + rock.radius, rock.y + rock.radius, 0) };
        }""")
        self.assertLessEqual(result["waterX"], 920)
        self.assertEqual(result["keys"], 0)
        self.assertEqual(result["reset"], {"x": 770, "y": 790, "facing": "east"})
        self.assertEqual(result["place"], "")
        self.assertTrue(result["treeCenter"])
        self.assertFalse(result["treeOutside"])
        self.assertTrue(result["rockCenter"])
        self.assertFalse(result["rockCorner"])

    def test_push_log_becomes_plank_and_blocks_otherwise(self):
        result = self.evaluate("""() => {
          const d = __valleyDebug, w = ValleyWorld, r = ValleyRules;
          d.reset(); d.setPlayer(753, 712);
          const pushed = r.push(d.player, {KeyD: true}, w, d.log);
          const before = d.log;
          const plankPos = { x: 1005, y: 722 };
          return {
            startLog: before, pushedLog: pushed.log, moved: pushed.moved,
            narrowsBlocked: w.blockedAt(1005, 660, 10),
            plankWalkable: !w.blockedAt(1005, 712, 10, { plank: true }),
            logBlocksPlayer: w.blockedAt(850, 700, 10, { logBlocked: before })
          };
        }""")
        self.assertTrue(result["moved"])
        self.assertGreater(result["pushedLog"]["x"], result["startLog"]["x"])
        self.assertTrue(result["narrowsBlocked"])
        self.assertTrue(result["plankWalkable"])
        self.assertTrue(result["logBlocksPlayer"])

    def test_reveal_fires_once_and_resets(self):
        result = self.evaluate("""() => {
          const d = __valleyDebug, w = ValleyWorld;
          d.reset();
          const reveal = w.revealFor(1005, 442);
          const nook = w.revealFor(300, 1320);
          d.setPlayer(1005, 442);
          return { revealId: reveal ? reveal.id : null, nookReveal: nook,
            landmarksWithReveal: w.landmarks.filter(l => l.reveal).length };
        }""")
        self.assertEqual(result["revealId"], "crossing")
        self.assertIsNone(result["nookReveal"])
        self.assertEqual(result["landmarksWithReveal"], 3)

    def test_bfs_reaches_landmarks_detour_and_each_crossing(self):
        result = self.evaluate("""() => {
          const w = ValleyWorld, cell = 12, radius = 10;
          const walkable = (x,y) => !w.blockedAt(x,y,radius);
          const reach = (start) => {
            const key = (x,y) => x + ',' + y, queue = [start], seen = new Set([key(...start)]);
            while (queue.length) { const [x,y] = queue.shift(); for (const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]) { const n=[x+dx,y+dy], px=n[0]*cell+cell/2, py=n[1]*cell+cell/2; if (px<0||py<0||px>=w.width||py>=w.height||!walkable(px,py)||seen.has(key(...n))) continue; seen.add(key(...n)); queue.push(n); } }
            return seen;
          };
          const seen = reach([Math.floor(w.spawn.x/cell), Math.floor(w.spawn.y/cell)]);
          const has = (x,y) => seen.has(Math.floor(x/cell)+','+Math.floor(y/cell));
          const east = has(1200,790), closedReach = (() => { const q=[[Math.floor(w.spawn.x/cell),Math.floor(w.spawn.y/cell)]], s=new Set([q[0].join(',')]); while(q.length){const [x,y]=q.shift();for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const n=[x+dx,y+dy],px=n[0]*cell+6,py=n[1]*cell+6,k=n.join(',');if(px<0||py<0||px>=w.width||py>=w.height||w.blockedAt(px,py,10,{closedBridges:true})||s.has(k))continue;s.add(k);q.push(n)}} return s.has(Math.floor(1200/cell)+','+Math.floor(790/cell)); })();
          return { landmarks: w.landmarks.map(l => has(l.x,l.y)), bridges: w.bridges.map(b => has(b.x+b.width/2,b.y+b.height/2)), bridgeOpen: w.bridges.map(b => !w.blockedAt(b.x+b.width/2,b.y+b.height/2,10)), east, closedReach };
        }""")
        self.assertEqual(result["landmarks"], [True, True, True, True])
        self.assertEqual(result["bridges"], [True, True])
        self.assertEqual(result["bridgeOpen"], [True, True])
        self.assertTrue(result["east"])
        self.assertFalse(result["closedReach"])

    def test_canvas_resizes_and_place_feedback_is_not_a_goal(self):
        self.page.set_viewport_size({"width": 390, "height": 844})
        result = self.evaluate("""() => { __valleyDebug.reset(); return { canvas: [game.width, game.height], controls: document.querySelectorAll('button').length, text: document.body.innerText }; }""")
        self.assertGreater(result["canvas"][0], 0)
        self.assertEqual(result["controls"], 1)
        self.assertNotIn("objective", result["text"].lower())

    def test_real_animation_frames_move_without_page_errors(self):
        self.page.set_viewport_size({"width": 1280, "height": 900})
        self.evaluate("() => __valleyDebug.reset()")
        before = self.evaluate("() => __valleyDebug.player")
        self.page.keyboard.down("KeyD")
        self.page.wait_for_timeout(120)
        self.page.keyboard.up("KeyD")
        after = self.evaluate("() => __valleyDebug.player")
        self.assertGreater(after["x"], before["x"])
        self.assertEqual(self.errors, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
