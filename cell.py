class Cell:

    def __init__(self, cell):
        # "B5"
        self.column = cell[0]
        self.row = cell[1]

    def __str__(self):
        return self.column + ":" + self.row


