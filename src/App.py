import sys
import time

import pygame

from pygame.locals import *

from Grid import Grid
from GridDisplay import GridDisplay

background_color = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((650, 863))
pygame.display.set_caption("Tetris")
grid = Grid(10, 20, [(5, 19), (6, 19)])
display = GridDisplay(window, grid)
grid.add_next_figure([(5, 1), (5, 2), (6, 1), (6, 2)])

while True:
    window.fill(background_color)
    display.refresh()
    pygame.display.update()

    if grid.current_falling_blocks:
        grid.move_current_blocks()
    else:
        grid.add_next_figure([(5, 1), (5, 2), (6, 1), (6, 2)])

    time.sleep(float(0.5))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                grid.move_block_to_left()
            elif event.key == K_RIGHT:
                grid.move_block_to_right()

