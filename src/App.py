import sys
import time

import pygame
from pygame.locals import *

from model.Piece import Piece
from view.GameDisplay import GameDisplay
from view.GridDisplay import GridDisplay
from model.Grid import Grid

game_display_mode = pygame.display.set_mode((380, 443))
game_display = GameDisplay(game_display_mode, (0, 0, 0))

grid = Grid(10, 20)
grid_display = GridDisplay(game_display_mode, grid)


pygame.init()
pygame.display.set_caption("Tetris")
colour = (5, 205, 25)
grid.set_falling_piece(Piece([(5, 1), (5, 2), (6, 1), (6, 2)], colour))
time_2 = 0.4

while True:
    game_display.background_refresh()
    grid_display.refresh()
    pygame.display.update()

    if grid.current_piece.block_list:
        grid.gravity()
    else:
        grid.set_falling_piece(Piece([(5, 1), (5, 2), (6, 1), (6, 2)], colour))

    time.sleep(float(time_2))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                grid.move_to_left()
            elif event.key == K_RIGHT:
                grid.move_to_right()
            elif event.key == K_DOWN:
                time_2 = 0.1
        if event.type == KEYUP:
            if event.key == K_DOWN:
                time_2 = 0.4
