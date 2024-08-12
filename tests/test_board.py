from board import Board
from disk import Disk
from cell import Cell

import unittest

class BoardTests(unittest.TestCase):
    def testDisplayOf8(self):
        b1 = Board(8)
        expected = '   A  B  C  D  E  F  G  H\n1  _  _  _  _  _  _  _  _\n2  _  _  _  _  _  _  _  _\n3  _  _  _  _  _  _  _  _\n4  _  _  _  B  W  _  _  _\n5  _  _  _  W  B  _  _  _\n6  _  _  _  _  _  _  _  _\n7  _  _  _  _  _  _  _  _\n8  _  _  _  _  _  _  _  _\n'
        self.assertEqual(str(b1), expected)
        print(b1)

    def testDisplayOf6(self):
        b2 = Board(6)
        expected = '   A  B  C  D  E  F\n1  _  _  _  _  _  _\n2  _  _  _  _  _  _\n3  _  _  B  W  _  _\n4  _  _  W  B  _  _\n5  _  _  _  _  _  _\n6  _  _  _  _  _  _\n'
        self.assertEqual(str(b2), expected)
        print(b2)

    def testSetAndGetCells(self):
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
        print(b2)
        self.assertEqual(b2.isColorEqual(2, 3 , "W"), True)
        self.assertEqual(b2.isColorEqual(2, 3 , "B"), False)

    def testGetCell(self):
        b2 = Board(6)
        color = b2.getCell(2,3 )
        self.assertEqual(color, "W")

    def testDisplayAndGetCellOf6(self):
        b2 = Board(6)
        print(b2)
        self.assertEqual(b2.getCell(2, 1), "E")
        self.assertEqual(b2.getCell(2, 2), "B")


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
