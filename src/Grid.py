from Cell import Cell


class Grid:
    def __init__(self, rows, columns, base_blocks):
        self.rows = rows
        self.columns = columns
        self.current_falling_blocks = None
        self.base_blocks = base_blocks
        self.cells = {}
        for row in range(rows):
            for column in range(columns):
                self.cells[(row, column)] = Cell(row, column)

    def move_block_to_left(self):
        for block in self.current_falling_blocks:
            if block[0] - 1 < 0 or (block[0] - 1, block[1]) in self.base_blocks:
                return False
        next_movement = []
        for block in self.current_falling_blocks:
            next_movement.append((block[0] - 1, block[1]))
        self.current_falling_blocks = next_movement

    def move_block_to_right(self):
        for block in self.current_falling_blocks:
            if block[0] + 1 > 9 or (block[0] + 1, block[1]) in self.base_blocks:
                return False
        next_movement = []
        for block in self.current_falling_blocks:
            next_movement.append((block[0] + 1, block[1]))
        self.current_falling_blocks = next_movement

    def move_current_blocks(self):
        for block in self.current_falling_blocks:
            if (block[0], block[1] + 1) in self.base_blocks:
                for key in self.current_falling_blocks:
                    self.base_blocks.append(key)
                self.current_falling_blocks = []
                return False
        next_movement = []
        for block in self.current_falling_blocks:
            if block[1] == self.columns - 1:
                for key in self.current_falling_blocks:
                    self.base_blocks.append(key)
                break
            else:
                next_movement.append((block[0], block[1] + 1))
        self.current_falling_blocks = next_movement

    def add_next_figure(self, figure):
        self.current_falling_blocks = figure
