
class Grid:

    def __init__(self, rows, columns):
        self.observers = []
        self.rows = rows
        self.columns = columns
        self.current_piece = None
        self.base_blocks = []

    def move_to_left(self):
        self.current_piece.move_to_left(self.base_blocks)

    def move_to_right(self):
        self.current_piece.move_to_right(self.base_blocks, self.rows)

    def gravity(self):
        self.current_piece.fall(self.base_blocks, self.columns)
        self.refreshAll()

    def set_falling_piece(self, piece):
        self.current_piece = piece

    def addObserver(self, observer):
        self.observers.append(observer)

    def refreshAll(self):
        for observer in self.observers:
            observer.refresh()
