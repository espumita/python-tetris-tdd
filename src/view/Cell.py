class Cell:

    def __init__(self, row, column):
        self.cell_width = 20
        self.cell_height = 20
        self.cell_margin = 2
        self.x = (self.cell_margin + self.cell_width) * row + self.cell_margin
        self.y = (self.cell_margin + self.cell_height) * column + self.cell_margin

    def info(self):
        return [self.x, self.y, self.cell_width, self.cell_height]
