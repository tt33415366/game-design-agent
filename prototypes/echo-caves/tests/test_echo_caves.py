import unittest
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class EchoCavesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)
        cls.page = cls.browser.new_page(viewport={"width": 1280, "height": 900})
        cls.errors = []
        cls.page.on("pageerror", lambda error: cls.errors.append(str(error)))
        cls.page.goto((ROOT / "index.html").as_uri())
        cls.page.wait_for_function("window.__echoDebug !== undefined")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def test_branches_reachable_and_distinct(self):
        result = self.page.evaluate("""() => {
          const w = EchoWorld;
          return { names: w.branches.map(b => b.name), cues: w.branches.map(b => b.cue),
            blocked: w.blockedAt(700, 605, 10), open: !w.blockedAt(700, 605, 10),
            revealIds: w.branches.map(b => w.revealFor(b.reveal.x,b.reveal.y).id) };
        }""")
        self.assertEqual(len(set(result["cues"])), 3)
        self.assertEqual(result["revealIds"], ["glow", "drift", "shadow"])

    def test_swim_coasts_and_stops(self):
        result = self.page.evaluate("""() => {
          const r=EchoRules,w=EchoWorld; let p=r.reset(w);
          for(let i=0;i<20;i++)p=r.move(p,{KeyD:true},.05,w);
          const x=p.x, coast=r.move(p,{},.2,w);
          for(let i=0;i<60;i++)p=r.move(p,{},.05,w);
          return {coast:coast.x>x, stop:Math.hypot(p.vx,p.vy)};
        }""")
        self.assertTrue(result["coast"])
        self.assertLess(result["stop"], 1)

    def test_reset_and_live_input(self):
        self.page.evaluate("() => __echoDebug.reset()")
        before = self.page.evaluate("() => __echoDebug.player")
        self.page.keyboard.down("KeyD")
        self.page.wait_for_timeout(350)
        self.page.keyboard.up("KeyD")
        after = self.page.evaluate("() => __echoDebug.player")
        self.assertGreater(after["x"], before["x"])
        self.page.evaluate("() => __echoDebug.reset()")
        reset = self.page.evaluate("() => __echoDebug.player")
        self.assertEqual(reset["x"], 460)
        self.assertEqual(self.errors, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
