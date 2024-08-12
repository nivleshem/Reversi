from board import Board
from disk import Disk
from cell import Cell

import unittest

class BoardTests(unittest.TestCase):
    def testDisplayOf8(self):
        b1 = Board(8)
        print(b1)

    def testDisplayOf6(self):
        b2 = Board(6)
        print(b2)

    def testTranlation(self):
        b = Board(6)
        result = b.translateLetterToNum("B")
        self.assertEqual(result, 2)


    def testTranslateCellToColRow(self):
        b = Board(6)
        col, row = b.translateCellToRowCol(Cell("B5"))
        self.assertEqual(col, 1)
        self.assertEqual(row, 4)


    def testTranslateRowColToCell(self):
        b = Board(6)
        cell = b.translateRowColToCell(3, 4)
        self.assertEqual(cell.column, "D")
        self.assertEqual(cell.row, "5")

    def testDisplayAndSetCellOf6(self):
        b2 = Board(6)
        b2.SetCell("A", 6, "W")
        b2.SetCell("c", 4, "B")
        b2.SetCell("A", 6, "W")
        b2.display()

    def testValidateCell(self):
        b2 = Board(6)
        self.assertEqual(b2.ValidateCell(4, 5), True)
        self.assertEqual(b2.ValidateCell(4, 6), False)
        self.assertEqual(b2.ValidateCell(0, 0), True)
        self.assertEqual(b2.ValidateCell(-1, 0), False)

    def testIsEmptyCell(self):
        b2 = Board(6)
        self.assertEqual(b2.IsEmptyCell(4, 5), True)
        self.assertEqual(b2.IsEmptyCell(2, 3), False)

    def testIsColorEqual(self):
        b2 = Board(6)
        self.assertEqual(b2.isColorEqual(2, 4 , "W"), True)
        self.assertEqual(b2.isColorEqual(2, 4 , "B"), False)

    def testGetCell(self):
        b2 = Board(6)
        color = b2.GetCell(2,3 )

        self.assertEqual(color, "W")


    def testDisplayAndGetCellOf6(self):
        b2 = Board(6)
        print(b2.GetCell("c", 1))
        print(b2)

    def testGetCapturedCellNorth1(self):
        b = Board(6)
        d = Disk(Cell("C5"), "B")
        captured = b.GetCapturedCells(d , "N")
        print(captured)
        d2 = Disk(Cell("D5"), "W")
        captured2 = b.GetCapturedCells(d2, "N")
        print(captured2)

    def testGetCapturedCellSouth1(self):
        b = Board(6)
        d = Disk(Cell("C2"), "W")
        captured = b.GetCapturedCells(d , "S")
        print(captured)

    def testGetCapturedCellWest1(self):
        b = Board(6)
        d = Disk(Cell("E3"), "B")
        captured = b.GetCapturedCells(d , "W")
        print(captured)

    def testGetCapturedCellEast1(self):
        b = Board(6)
        d = Disk(Cell("B4"), "B")
        captured = b.GetCapturedCells(d , "E")
        print(captured)
