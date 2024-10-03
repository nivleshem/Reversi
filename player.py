from disk import Disk
class Player:

    def __init__(self, name):
        self.name = name

    def displayName(self):
        print("The Base Player name is ", self.name)

    def IsLegal(self, board, col, row):
        for direction in ["N", "W", "E", "S", "NW", "SW", "NE", "SE"]:
            cell = board.translateRowColToCell(col, row)
            captured = board.GetCapturedCells(Disk(cell, self.color), direction)
            if (len(captured) > 0):
                return True
        return False

    def NextMove(self, board):
        for row in range(board.size):
            for col in range(board.size):
                if ((board.IsEmptyCell(col, row)) and self.IsLegal(board, col, row)):
                    cell = board.translateRowColToCell(col, row)
                    desired_disk = Disk(cell, self.color)
                    return desired_disk
        return None
