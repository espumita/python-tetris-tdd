import pygame
from pygame.locals import *
import time
import sys

from model.Grid import Grid
from model.Piece import Piece
from view.GameDisplay import GameDisplay
from view.GridDisplay import GridDisplay
from view.PygameDisplay import PygameDisplay


class GameController:

    def __init__(self):
        self.grid = Grid(10, 20)
        self.game_display_mode = pygame.display.set_mode((380, 443))
        self.game_display = GameDisplay(self.game_display_mode, (0, 0, 0))
        self.grid_display = GridDisplay(self.game_display_mode, self.grid)
        self.pygame_display = PygameDisplay()
        self.colour = (5, 205, 25)
        self.velocity_time = 0.4

    def start(self):
        self.grid.addObserver(self.game_display)
        self.grid.addObserver(self.grid_display)
        self.grid.addObserver(self.pygame_display)
        self.pygame_display.start()
        self.grid.set_falling_piece(Piece([(5, 1), (5, 2), (6, 1), (6, 2)], self.colour))

    def iterate(self):
        if self.grid.current_piece.block_list:
            self.grid.gravity()
        else:
            self.grid.set_falling_piece(Piece([(5, 1), (5, 2), (6, 1), (6, 2)], self.colour))

    def sleep(self):
        time.sleep(float(self.velocity_time))

    def event_handling_process(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.grid.move_to_left()
                elif event.key == K_RIGHT:
                    self.grid.move_to_right()
                elif event.key == K_DOWN:
                    self.velocity_time = 0.1
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    self.velocity_time = 0.4

