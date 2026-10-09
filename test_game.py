import unittest
from shardovyrrix import Game
class Tests(unittest.TestCase):
 def test_launch(self):g=Game(1);g.step(.05);self.assertEqual(g.y,.78);g.launch();g.step(.05);self.assertLess(g.y,.78)
 def test_brick(self):g=Game(1);g.launch();g.x=.05;g.y=.125;g.vx=0;g.vy=0;g.step(.01);self.assertNotIn((0,0),g.bricks);self.assertEqual(g.score,10)
 def test_life(self):g=Game(1);g.launch();g.y=1.1;g.step(.01);self.assertEqual(g.lives,2);self.assertTrue(g.waiting)
 def test_next(self):g=Game(1);g.bricks={(0,0)};g.launch();g.x=.05;g.y=.125;g.vx=g.vy=0;g.step(.01);self.assertEqual(g.level,2);self.assertTrue(g.bricks)
 def test_paddle(self):g=Game(1);g.launch();g.y=.88;g.x=g.paddle;g.vy=.3;g.step(.01);self.assertLess(g.vy,0)
 def test_limit(self):g=Game(1);[g.step(.05,-1) for _ in range(100)];self.assertEqual(g.paddle,.1)
if __name__=='__main__':unittest.main()
