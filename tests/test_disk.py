from disk import Disk
from cell import Cell
import unittest

class DiskTests(unittest.TestCase):
    def test1(self):
        disk = Disk(Cell("A5"),"W")
        print(disk)

