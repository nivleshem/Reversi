import board
from playerA import PlayerA
from playerB import PlayerB
from board import Board
from disk import Disk
class Game:

    def __init__(self , name1, name2, size):
        self.player1 = PlayerA(name1, "W")
        self.player2 = PlayerB(name2, "B")
        self.board = Board(size)
        self.winner = None


    def gameNotOver(self):
        if(self.current_player.NextMove(self.board) != None):
            return True
        return False

    def commitMove(self, disk):
        all_captured_disks = []
        for direction in ["N", "W", "E", "S", "NW", "SW", "NE", "SE"]:
            disks_to_flip = self.board.GetCapturedCells(disk, direction)
            all_captured_disks += disks_to_flip

        # remove duplications
        all_captured_disks = list(set(all_captured_disks))
        for d in all_captured_disks:
            cell = d.cell
            self.board.SetCell(cell, disk.color)
        self.board.SetCell(disk.cell, disk.color)


    def CalculateWinner(self):
        count_white = 0
        count_black = 0
        for row in range(self.board.size):
            for col in range(self.board.size):
                if(self.board.getCell(col, row) == "W"):
                    count_white += 1
                if (self.board.getCell(col, row) == "B"):
                    count_black += 1
        if(count_white > count_black):
            #print("The winner is, White, with a total of: ", count_white, " cells captured")
            return [self.player1.name, self.player1.color, count_white]
        if (count_white < count_black):
            #print("The winner is, Black, with a total of: ", count_black, " cells captured")
            return [self.player2.name, self.player2.color, count_black]
        else:
            return []


    def play(self, debug=False):
        if (debug): print(self.board)
        iterationCount = 1
        self.current_player = self.player1

        while (self.gameNotOver()):
            if (debug): print("Iteration #", iterationCount)
            iterationCount += 1
            disk = self.current_player.NextMove(self.board)
            self.commitMove(disk)
            if(self.current_player == self.player1):
                self.current_player = self.player2
            else:
                self.current_player = self.player1

            if (debug):
                print(self.board)
                input("Press Any Key to Continue...")

        print("Game Over (Took ", iterationCount, "iteration)", "The winner is", self.CalculateWinner())








