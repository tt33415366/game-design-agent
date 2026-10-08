import unittest
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "index.html"


class TidalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)
        cls.page = cls.browser.new_page(viewport={"width": 1280, "height": 900})
        cls.errors = []
        cls.page.on("pageerror", lambda e: cls.errors.append(str(e)))
        cls.page.goto(APP.as_uri())
        cls.page.wait_for_function("window.__tidalDebug !== undefined")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def evaluate(self, script):
        return self.page.evaluate(script)

    def test_calm_walk_and_collision(self):
        result = self.evaluate("""() => {
          const r = TidalRules, w = TidalWorld, stones = r.resetStones(w);
          let p = { x: 500, y: 500, facing: 'east' };
          const startX = p.x;
          for (let i = 0; i < 10; i += 1) p = r.moveCalm(p, {KeyD: true}, .05, w, stones);
          const reef = w.blockers.find(s => s.kind === 'reef');
          const wall = w.blockers.find(s => s.kind === 'wall');
          return { moved: p.x - startX, reefC: w.blockedAt(reef.x, reef.y, 0.5, {stones}), wallC: w.blockedAt(wall.x+10, wall.y+10, 10, {stones}),
            blockedSeg: w.blockedAt(745, 345, 8, {stones}) };
        }""")
        self.assertAlmostEqual(result["moved"], 80, delta=2)
        self.assertTrue(result["reefC"])
        self.assertTrue(result["wallC"])
        self.assertTrue(result["blockedSeg"])

    def test_drag_opens_segment_one_way(self):
        result = self.evaluate("""() => {
          const d = __tidalDebug, w = TidalWorld, r = TidalRules;
          d.reset(); d.setPlayer(745, 370);
          let stones = r.resetStones(w), player = d.player, placed = -1;
          for (let i = 0; i < 70 && placed < 0; i += 1) {
            const res = r.drag(player, {KeyW: true}, w, stones);
            stones = res.stones; player = res.player; placed = res.placedIndex;
          }
          const opened = !w.segmentBlocked(0, stones);
          const segNowWalkable = !w.blockedAt(745, 345, 8, { stones });
          // One-way: pressing down now should not move the placed stone back.
          const back = r.drag(player, {KeyS: true}, w, stones);
          return { placed, opened, segNowWalkable, backMoved: back.moved };
        }""")
        self.assertEqual(result["placed"], 0)
        self.assertTrue(result["opened"])
        self.assertTrue(result["segNowWalkable"])
        self.assertFalse(result["backMoved"])

    def test_tide_trigger_and_pool_reachability(self):
        result = self.evaluate("""() => {
          const d = __tidalDebug, w = TidalWorld, r = TidalRules;
          d.reset();
          const noneOpen = [0,1,2].map(i => w.segmentBlocked(i, r.resetStones(w)));
          const allOpenStones = w.channels.map(c => ({ ...c.stone.open }));
          const allOpen = [0,1,2].map(i => w.segmentBlocked(i, allOpenStones));
          return { noneOpen, allOpen, phase: d.phase };
        }""")
        self.assertEqual(result["noneOpen"], [True, True, True])
        self.assertEqual(result["allOpen"], [False, False, False])
        self.assertEqual(result["phase"], "calm")

    def test_swim_phase_physics(self):
        result = self.evaluate("""() => {
          const r = TidalRules, w = TidalWorld, stones = w.channels.map(c => ({ ...c.stone.open }));
          let p = { x: 500, y: 745, facing: 'east', vx: 0, vy: 0 };
          for (let i = 0; i < 20; i += 1) p = r.moveSwim(p, {KeyD: true}, .05, w, stones);
          const coast = r.moveSwim(p, {}, .2, w, stones);
          return { vx: p.vx, coastX: coast.x, x: p.x };
        }""")
        self.assertGreater(result["vx"], 0)
        self.assertGreater(result["coastX"], result["x"])

    def test_reset_restores_calm_and_stones(self):
        result = self.evaluate("""() => {
          const d = __tidalDebug, w = TidalWorld;
          d.setStone(0, w.channels[0].stone.open.x, w.channels[0].stone.open.y);
          d.setPlayer(900, 900);
          d.reset();
          const home = w.channels[0].stone.home;
          return { phase: d.phase, stone: d.stones[0], home, player: d.player, place: document.querySelector('#place').textContent };
        }""")
        self.assertEqual(result["phase"], "calm")
        self.assertAlmostEqual(result["stone"]["x"], result["home"]["x"], places=1)
        self.assertEqual(result["player"]["x"], 380)
        self.assertEqual(result["place"], "")

    def test_real_frames_move_without_errors(self):
        self.evaluate("() => __tidalDebug.reset()")
        before = self.evaluate("() => __tidalDebug.player")
        self.page.keyboard.down("KeyD")
        self.page.wait_for_timeout(400)
        self.page.keyboard.up("KeyD")
        after = self.evaluate("() => __tidalDebug.player")
        self.assertGreater(after["x"], before["x"])
        self.assertEqual(self.errors, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
