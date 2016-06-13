import pygame


class GridDisplay:

    def __init__(self, window, grid):
        self.window = window
        self.grid = grid

    def refresh(self):
        for key in self.grid.cells:
            colour = (30, 30, 30)
            if key in self.grid.current_piece.block_list:
                colour = self.grid.current_piece.colour
            if key in self.grid.base_blocks:
                colour = (80, 80, 80)
            pygame.draw.rect(self.window,
                             colour,
                             self.grid.cells[key].info()
                             )