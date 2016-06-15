import pygame


class PygameDisplay:

    def refresh(self):
        pygame.display.update()

    def start(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
