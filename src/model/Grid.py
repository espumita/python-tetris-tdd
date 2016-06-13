from view.Cell import Cell


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.current_piece = None
        self.base_blocks = []
        self.cells = {}
        for row in range(rows):
            for column in range(columns):
                self.cells[(row, column)] = Cell(row, column)

    def move_to_left(self):
        self.current_piece.move_to_left(self.base_blocks)

    def move_to_right(self):
        self.current_piece.move_to_right(self.base_blocks, self.rows)

    def gravity(self):
        self.current_piece.fall(self.base_blocks, self.columns)

    def set_falling_piece(self, piece):
        self.current_piece = piece
