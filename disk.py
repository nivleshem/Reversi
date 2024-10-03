class Disk:
    def __init__(self, cell, color):
        self.cell = cell
        self.color = color

    def __str__(self):
        return str(self.cell) + "," + self.color
    def __repr__(self):
        return str(self.cell) + "," + self.color





