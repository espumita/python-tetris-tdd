import pygame


class GridDisplay:

    def __init__(self, window, grid):
        self.window = window
        self.grid = grid

    def refresh(self):
        for row in range(self.grid.rows):
            for column in range(self.grid.columns):
                colour = (30, 30, 30)
                if (row, column) in self.grid.current_piece.block_list:
                    colour = self.grid.current_piece.colour
                if (row, column) in self.grid.base_blocks:
                    colour = (80, 80, 80)
                pygame.draw.rect(self.window,
                                 colour,
                                 self.matrix_ifo(row, column)
                             )
    def matrix_ifo(self, row, column):
        cell_margin = 2
        cell_width = 20
        cell_height = 20
        self.x = (cell_margin + cell_width) * row + cell_margin
        self.y = (cell_margin + cell_height) * column + cell_margin
        return [self.x, self.y, cell_width, cell_height]