import unittest
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "index.html"


class UnderseaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)
        cls.page = cls.browser.new_page(viewport={"width": 1280, "height": 900})
        cls.errors = []
        cls.page.on("pageerror", lambda e: cls.errors.append(str(e)))
        cls.page.goto(APP.as_uri())
        cls.page.wait_for_function("window.__underseaDebug !== undefined")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def evaluate(self, script):
        return self.page.evaluate(script)

    def test_swim_inertia_and_low_fps(self):
        result = self.evaluate("""() => {
          const r = UnderseaRules, w = UnderseaWorld;
          let p = r.reset(w);
          for (let i = 0; i < 20; i += 1) p = r.move(p, {KeyD: true}, .05, w);
          const afterAccel = { x: p.x, vx: p.vx };
          const coast = r.move(p, {}, .2, w);
          const stopped = (() => { let q = p; for (let i = 0; i < 40; i += 1) q = r.move(q, {}, .05, w); return q; })();
          let slow = r.reset(w);
          for (let i = 0; i < 10; i += 1) slow = r.move(slow, {KeyD: true}, .1, w);
          return { accelX: afterAccel.x, vx: afterAccel.vx, coastX: coast.x, stopV: Math.hypot(stopped.vx, stopped.vy), slowX: slow.x, cap: r.move(r.reset(w), {KeyD: true}, 9, w).x };
        }""")
        self.assertGreater(result["accelX"], 700)
        self.assertGreater(result["vx"], 0)
        self.assertGreater(result["coastX"], result["accelX"])
        self.assertAlmostEqual(result["stopV"], 0, places=1)
        self.assertGreater(result["slowX"], 700)
        self.assertLessEqual(result["cap"], 750)

    def test_collision_reset_and_blur(self):
        result = self.evaluate("""() => {
          const d = __underseaDebug, w = UnderseaWorld, r = UnderseaRules;
          const rock = w.blockers.find(s => s.kind === 'rock');
          const coral = w.blockers.find(s => s.kind === 'coral');
          window.dispatchEvent(new KeyboardEvent('keydown', {code:'KeyD'})); window.dispatchEvent(new Event('blur'));
          d.reset();
          return { rockC: w.blockedAt(rock.x, rock.y, 0), coralC: w.blockedAt(coral.x, coral.y, 0),
            wall: w.blockedAt(940, 300, 10), keys: d.heldKeys.length, player: d.player, place: document.querySelector('#place').textContent };
        }""")
        self.assertTrue(result["rockC"])
        self.assertTrue(result["coralC"])
        self.assertTrue(result["wall"])
        self.assertEqual(result["keys"], 0)
        self.assertEqual(result["player"]["x"], 700)
        self.assertEqual(result["place"], "")

    def test_topology_sights_crevice_and_arch(self):
        result = self.evaluate("""() => {
          const w = UnderseaWorld, cell = 14;
          const reach = (options) => {
            const start = [Math.floor(w.spawn.x/cell), Math.floor(w.spawn.y/cell)];
            const q=[start], s=new Set([start.join(',')]);
            while(q.length){const [x,y]=q.shift();for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const n=[x+dx,y+dy],px=n[0]*cell+7,py=n[1]*cell+7,k=n.join(',');if(px<0||py<0||px>=w.width||py>=w.height||w.blockedAt(px,py,10,options)||s.has(k))continue;s.add(k);q.push(n)}}
            return s;
          };
          const has = (seen,x,y) => seen.has(Math.floor(x/cell)+','+Math.floor(y/cell));
          const open = reach();
          const h = w.crevice.heart;
          return {
            sights: w.sights.map(s => has(open, s.x, s.y)),
            heart: has(open, h.x, h.y),
            eastWithArch: has(open, 1200, 760)
          };
        }""")
        self.assertEqual(result["sights"], [True, True, True, True])
        self.assertTrue(result["heart"])
        self.assertTrue(result["eastWithArch"])

    def test_narrows_gap_is_open_and_arch_is_optional(self):
        result = self.evaluate("""() => {
          const w = UnderseaWorld, n = w.narrows;
          return {
            gapOpen: !w.blockedAt(n.x+n.width/2, n.y+n.height/2, 8),
            wallBlocks: w.blockedAt(940, 300, 10) && w.blockedAt(940, 900, 10)
          };
        }""")
        self.assertTrue(result["gapOpen"])
        self.assertTrue(result["wallBlocks"])

    def test_push_boulder_locks_arch(self):
        result = self.evaluate("""() => {
          const d = __underseaDebug, w = UnderseaWorld, r = UnderseaRules;
          d.reset(); d.setPlayer(818, 725);
          const pushed = r.push(d.player, {KeyD: true}, w, d.boulder);
          const n = w.narrows;
          return { moved: pushed.moved, boulder: pushed.boulder,
            wallBlocks: w.blockedAt(940, 300, 10),
            boulderNearNarrows: Math.abs(pushed.boulder.x - 850) > 0 };
        }""")
        self.assertTrue(result["moved"])
        self.assertTrue(result["wallBlocks"])
        self.assertTrue(result["boulderNearNarrows"])

    def test_reveals_once_and_crevice(self):
        result = self.evaluate("""() => {
          const w = UnderseaWorld;
          const heart = w.crevice.heart;
          return {
            arch: w.revealFor(480, 420) ? w.revealFor(480, 420).id : null,
            crevice: w.revealFor(heart.x, heart.y) ? w.revealFor(heart.x, heart.y).id : null,
            flat: w.revealFor(760, 1240),
            count: w.sights.filter(s => s.reveal).length
          };
        }""")
        self.assertEqual(result["arch"], "arch")
        self.assertEqual(result["crevice"], "crevice")
        self.assertIsNone(result["flat"])
        self.assertEqual(result["count"], 3)

    def test_canvas_resize_and_no_objective_ui(self):
        self.page.set_viewport_size({"width": 390, "height": 844})
        result = self.evaluate("""() => { __underseaDebug.reset(); return { canvas: [game.width, game.height], buttons: document.querySelectorAll('button').length, text: document.body.innerText }; }""")
        self.assertGreater(result["canvas"][0], 0)
        self.assertEqual(result["buttons"], 1)
        self.assertNotIn("objective", result["text"].lower())

    def test_real_frames_move_without_errors(self):
        self.page.set_viewport_size({"width": 1280, "height": 900})
        self.evaluate("() => __underseaDebug.reset()")
        before = self.evaluate("() => __underseaDebug.player")
        self.page.keyboard.down("KeyD")
        self.page.wait_for_timeout(400)
        self.page.keyboard.up("KeyD")
        after = self.evaluate("() => __underseaDebug.player")
        self.assertGreater(after["x"], before["x"])
        self.assertEqual(self.errors, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
