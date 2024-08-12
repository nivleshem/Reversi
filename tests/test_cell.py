from cell import Cell
import unittest

class CellTests(unittest.TestCase):
    def test1(self):
        cell = Cell("B6")
        print(cell)
