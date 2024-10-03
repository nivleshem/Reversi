from disk import Disk
from cell import Cell


class Board:

    matrix = None
    size = None

    def __init__(self, n, place_starting_disks=True):
        self.matrix = []
        self.size = n
        self.set_board(place_starting_disks)

    def __str__(self):
        result_str = ""
        col_str = " "
        for c in range(self.size):
            col_str = col_str + "  " + self.translateNumToLetter(c).upper()
        result_str += col_str + "\n"

        for r in range(self.size):
            row = self.matrix[r]
            row_str = str(r + 1)
            for c in range(self.size):
                cell_value = row[c]
                if (cell_value == "E"):
                    cell_value = "_"
                row_str = row_str + "  " + cell_value
            result_str += row_str + "\n"

        return result_str

    def set_board(self, place_starting_disks=True):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append("E")
            self.matrix.append(row)

        if (place_starting_disks):
            index = int(self.size / 2)
            self.setCell( index - 1, index - 1, "B")
            self.setCell( index - 1, index,     "W")
            self.setCell( index    , index - 1, "W")
            self.setCell( index    , index    , "B")

        return self.matrix

    def setCell(self, col, row , color):
        self.matrix[row][col] = color

    def SetCell(self, cell, color):
        col, row = self.translateCellToRowCol(cell)
        self.setCell(col, row, color)

    def getCell(self, col, row):
        return self.matrix[row][col]

    def GetCell(self, cell):
        col, row = self.translateCellToRowCol(cell)
        return self.getCell(col, row)



    def translateCellToRowCol(self, cell):
        row = int(cell.row) - 1
        col = self.translateLetterToNum(cell.column) - 1
        return [col, row]

    def translateRowColToCell(self, current_col, current_row):
        letter = self.translateNumToLetter(current_col).upper()
        num = current_row + 1
        return Cell(letter + str(num))

    def number_to_letter(number):
        if 1 <= number <= 26:
            # Convert number to corresponding alphabet letter
            return chr(number + ord('a') - 1)
        else:
            raise ValueError("Number must be between 1 and 26")

    def translateLetterToNum(self, letter):
        letter = letter.lower()
        if letter.isalpha() and len(letter) == 1:
            # Get the position in the alphabet (1-based index)
            return ord(letter) - ord('a') + 1
        else:
            raise ValueError("Input must be a single alphabetic character")

    def translateNumToLetter(self, c):
        if 0 <= c <= 26:
            # Convert number to corresponding alphabet letter
            return chr(c + ord('a'))
        else:
            raise ValueError("Number must be between 1 and 26")

    def IsEmptyCell(self, col, row):
        color = self.getCell(col, row)
        if (color == "E"):
            return True
        return False

    def GetCapturedCells(self, disk, direction):
        captured_disks = []

        current_col, current_row = self.translateCellToRowCol(disk.cell)

        row_delta = 0
        col_delta = 0

        if (direction == "N"):
            row_delta = -1
        if (direction == "S"):
            row_delta = 1
        if (direction == "W"):
            col_delta = -1
        if (direction == "E"):
            col_delta = 1
        if (direction == "NW"):
            row_delta = -1
            col_delta = -1
        if (direction == "NE"):
            row_delta = -1
            col_delta = 1
        if (direction == "SW"):
            row_delta = 1
            col_delta = -1
        if (direction == "SE"):
            row_delta = 1
            col_delta = 1

        my_color = disk.color
        opposite_color = 'W'
        if (my_color == "W"):
            opposite_color = "B"

        current_row += row_delta
        current_col += col_delta

        while ( self.ValidateCell(current_col, current_row) and (not self.IsEmptyCell(current_col, current_row)) and ( self.isColorEqual(current_col, current_row, opposite_color)) ):
            cell = self.translateRowColToCell(current_col, current_row)
            captured_disks.append(Disk(cell, opposite_color))
            current_row += row_delta
            current_col += col_delta

        # append the last disk if it's not empty
        if ( (self.ValidateCell(current_col, current_row)) and (not self.IsEmptyCell(current_col, current_row)) ):
            cell = self.translateRowColToCell(current_col, current_row)
            captured_disks.append(Disk(cell, my_color))

        if ( len(captured_disks) > 0):
            last_disk = captured_disks[-1]
            if (last_disk.color == my_color):
                return captured_disks[0:-1]
            else:
                return []

        return captured_disks

    def ValidateCell(self, col, row):
        if ( (col < 0) or (col >= self.size) or (row < 0) or (row >= self.size) ):
            return False
        return True

    def isColorEqual(self, col, row, color):
        c = self.getCell(col , row)
        if(c == color):
            return True
        return False











