class Board:

    matrix = None
    size = None

    def __init__(self, n):
        self.matrix = []
        self.size = n
        self.set_board()

    def set_board(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append("E")
            self.matrix.append(row)

        index = int(self.size / 2)
        self.matrix[index - 1][index - 1] = "B"
        self.matrix[index - 1][index] = "W"
        self.matrix[index][index - 1] = "W"
        self.matrix[index][index] = "B"

        return self.matrix

    def display(self):
        print("self.size = ", self.size)
        col_str = " "
        for c in range(self.size):
            col_str = col_str + "  " + str(c + 1)
        print(col_str)

        for r in range(self.size):
            row = self.matrix[r]
            row_str = str(r + 1)
            for c in range(self.size):
                cell_value = row[c]
                if (cell_value == "E"):
                    cell_value = "_"
                row_str = row_str + "  " + cell_value
            print(row_str)



