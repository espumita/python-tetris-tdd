
class Piece:

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __init__(self, block_list, colour):
        self.block_list = block_list
        self.colour = colour

    def set_colour(self, colour):
        self.colour = colour

    def fall(self, base_blocks, columns):
        if self.down_position_is_not_available(base_blocks, columns):
            self.add_piece_to(base_blocks)
        else:
            self.block_list = self.move_down_piece()

    def down_position_is_not_available(self, base_blocks, columns):
        for block in self.block_list:
            if (block[0], block[1] + 1) in base_blocks or block[1] == columns - 1:
                return True
        return False

    def add_piece_to(self, base_blocks):
        for key in self.block_list:
            base_blocks.append(key)
        self.block_list = []

    def move_down_piece(self):
        next_movement = []
        for block in self.block_list:
            next_movement.append((block[0], block[1] + 1))
        return next_movement

    def move_to_left(self, base_blocks):
        if self.left_position_is_available(base_blocks):
            self.move_left_piece()

    def left_position_is_available(self, base_blocks):
        for block in self.block_list:
            if block[0] - 1 < 0 or (block[0] - 1, block[1]) in base_blocks:
                return False
        return True

    def move_left_piece(self):
        next_movement = []
        for block in self.block_list:
            next_movement.append((block[0] - 1, block[1]))
        self.block_list = next_movement

    def move_to_right(self, base_blocks, rows):
        if self.right_position_is_available(base_blocks, rows):
            self.move_right_piece()

    def move_right_piece(self):
        next_movement = []
        for block in self.block_list:
            next_movement.append((block[0] + 1, block[1]))
        self.block_list = next_movement

    def right_position_is_available(self, base_blocks, rows):
        for block in self.block_list:
            if block[0] + 1 > rows - 1 or (block[0] + 1, block[1]) in base_blocks:
                return False
        return True




