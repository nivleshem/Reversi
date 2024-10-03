from playerA import PlayerA
from playerB import PlayerB
from board import Board
from cell import Cell
import unittest

class DiskTests(unittest.TestCase):
    def test1(self):
        player = PlayerA("Niv", "B")
        self.assertEqual(player.name, "Niv")
        self.assertEqual(player.color, "B")

    def testIsLegal1(self):
        player = PlayerB("Niv", "B")
        board = Board(6)
        res = player.IsLegal(board, 0, 0)
        print(res)

    def testNextMove(self):
        player = PlayerA("Niv", "W")
        board = Board(6)
        print(player.NextMove(board))

    def testNextMove(self):
        player = PlayerB("Niv", "W")
        board = Board(6)
        board.SetCell(Cell("C2"), "B")
        print(board)
        print(player.NextMove(board))



