import unittest
from game import Game

class GameTests(unittest.TestCase):
    def test_commit_1(self):
        g = Game("Niv", "Uri", 8)
        b = g.board
        print(b)
        d = g.player1.NextMove(b)
        print(d)
        g.commitMove(d)
        print(b)

    def test_play(self):
        g = Game("Niv", "Uri", 8)
        g.play()

