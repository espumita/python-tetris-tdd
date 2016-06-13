from view.GridDisplay import GridDisplay


class GameDisplay:
    def __init__(self, display, background_color):
        self.background_color = background_color
        self.display = display

    def background_refresh(self):
        self.display.fill(self.background_color)