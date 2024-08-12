from disk import Disk
from cell import Cell
import unittest

class DiskTests(unittest.TestCase):
    def test1(self):
        disk = Disk(Cell("A5"),"W")
        self.assertEqual(disk.color, "W")
        cell = disk.cell
        self.assertEqual(cell.column, "A")
        self.assertEqual(cell.row, "5")


