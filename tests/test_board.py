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

    def testIsEmptyCell(self):
        b = Board(6, False)

        b.SetCell(Cell("E4"), "W")
        b.SetCell(Cell("E5"), "W")
        b.SetCell(Cell("E6"), "B")

        res = b.IsEmptyCell(4, 3)
        self.assertEqual(res, False)


    def testGetCapturedCellNorth1(self):
        b = Board(6)
        d = Disk(Cell("C5"), "B")
        print(b)
        captured = b.GetCapturedCells(d , "N")
        print(captured)


    def testGetCapturedCellSouth1(self):
        b = Board(6)
        d = Disk(Cell("C2"), "W")
        captured = b.GetCapturedCells(d , "S")
        print(captured)

    def testGetCapturedCellSouth2(self):
        b = Board(6, False)

        b.SetCell(Cell("E4"), "W")
        b.SetCell(Cell("E5"), "W")
        b.SetCell(Cell("E6"), "B")

        d = Disk(Cell("E3"), "B")
        captured = b.GetCapturedCells(d, "S")
        print(b)
        print(captured)

    def testGetCapturedCellSouth3(self):
        b = Board(6, False)

        b.SetCell(Cell("E4"), "W")
        b.SetCell(Cell("E5"), "W")
        b.SetCell(Cell("E6"), "W")

        d = Disk(Cell("E3"), "B")
        captured = b.GetCapturedCells(d, "S")
        print(b)
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

    def testGetCapturedNorthWest3(self):
        b = Board(6, True)

        b.SetCell(Cell("B2"), "W")


        d = Disk(Cell("E5"), "W")
        captured = b.GetCapturedCells(d, "NW")
        print(b)
        print(captured)


    def testGetCapturedNorthEast3(self):
        b = Board(6, False)

        b.SetCell(Cell("C4"), "W")
        b.SetCell(Cell("D3"), "W")
        b.SetCell(Cell("E2"), "B")


        d = Disk(Cell("B5"), "B")
        captured = b.GetCapturedCells(d, "NE")
        print(b)
        print(captured)


    def testGetCapturedSouthWest3(self):
        b = Board(6, True)

        b.SetCell(Cell("B4"), "W")


        d = Disk(Cell("D2"), "W")
        captured = b.GetCapturedCells(d, "SW")
        print(b)
        print(captured)


    def testGetCapturedSouthEast3(self):
        b = Board(6, True)

        b.SetCell(Cell("E5"), "W")


        d = Disk(Cell("B2"), "W")
        captured = b.GetCapturedCells(d, "SE")
        print(b)
        print(captured)


    def testGetCapturedSouthEastErrors3(self):
        b = Board(6, True)


        b.SetCell(Cell("F6"), "B")


        d = Disk(Cell("E5"), "W")
        captured = b.GetCapturedCells(d, "SE")
        print(b)
        print(captured)

    def testAppendLists(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        list3 = [7, 8, 9]

        combined_list = []
        combined_list += list1
        combined_list += list2
        combined_list += list3

        print(combined_list)

