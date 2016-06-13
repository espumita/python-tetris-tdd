
class Piece:
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __init__(self, block_list, colour):
        self.block_list = block_list
        self.colour = colour

    def fall(self, base_blocks, columns):
        for block in self.block_list:
            if (block[0], block[1] + 1) in base_blocks:
                for key in self.block_list:
                    base_blocks.append(key)
                self.block_list = []
                return False
        next_movement = []
        for block in self.block_list:
            if block[1] == columns - 1:
                for key in self.block_list:
                    base_blocks.append(key)
                break
            else:
                next_movement.append((block[0], block[1] + 1))
        self.block_list = next_movement

    def move_to_left(self, base_blocks):
        for block in self.block_list:
            if block[0] - 1 < 0 or (block[0] - 1, block[1]) in base_blocks:
                return False
        next_movement = []
        for block in self.block_list:
            next_movement.append((block[0] - 1, block[1]))
        self.block_list = next_movement

    def move_to_right(self, base_blocks, rows):
        for block in self.block_list:
            if block[0] + 1 > rows - 1  or (block[0] + 1, block[1]) in base_blocks:
                return False
        next_movement = []
        for block in self.block_list:
            next_movement.append((block[0] + 1, block[1]))
        self.block_list = next_movement

    def set_colour(self, colour):
        self.colour = colour