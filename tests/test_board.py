from board import Board
import unittest

class BoardTests(unittest.TestCase):
    def testDisplayOf8(self):
        b1 = Board(8)
        b1.display()

    def testDisplayOf6(self):
        b2 = Board(6)
        b2.display()
