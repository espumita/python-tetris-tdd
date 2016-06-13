import unittest

from model.Grid import Grid
from model.Piece import Piece


class _Grid(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.grid = Grid(10, 20)
        cls.DEFAULT_COLOR = (0, 0, 0)

    def test_when_a_piece_falls_from_the_top_y_coordinates_should_be_increased_by_one(self):
        single_block = [(5, 1)]
        self.grid.set_falling_piece(Piece(single_block, self.DEFAULT_COLOR))

        self.grid.gravity()

        expected_block = [(5, 2)]
        self.assertEqual(self.grid.current_piece, Piece(expected_block, self.DEFAULT_COLOR))

    def test_when_piece_falls_to_the_bottom_falling_piece_should_be_empty(self):
        single_block = [(5, 19)]
        self.grid.set_falling_piece(Piece(single_block, self.DEFAULT_COLOR))

        self.grid.gravity()

        self.assertEqual(self.grid.current_piece, Piece([], self.DEFAULT_COLOR))

    def test_when_piece_falls_on_another_figure_falling_piece_should_be_empty(self):
        single_block = [(5, 4)]
        self.grid.set_falling_piece(Piece(single_block, self.DEFAULT_COLOR))
        self.grid.base_blocks = [(5, 5)]

        self.grid.gravity()

        self.assertEqual(self.grid.current_piece, Piece([], self.DEFAULT_COLOR))

    def test_when_the_piece_moves_to_the_right_x_coordinates_should_be_increased_by_one(self):
        single_block = [(5, 1)]
        self.grid.set_falling_piece(Piece(single_block, self.DEFAULT_COLOR))

        self.grid.move_to_right()

        expected_block = [(6, 1)]
        self.assertEqual(self.grid.current_piece, Piece(expected_block, self.DEFAULT_COLOR))

    def test_when_the_piece_moves_to_the_left_x_coordinates_should_be_decreased_by_one(self):
        single_block = [(5, 1)]
        self.grid.set_falling_piece(Piece(single_block, self.DEFAULT_COLOR))

        self.grid.move_to_left()

        expected_block = [(4, 1)]
        self.assertEqual(self.grid.current_piece, Piece(expected_block, self.DEFAULT_COLOR))

    def test_when_the_piece_tries_to_move_against_the_right_border_it_should_not_move(self):
        single_block = [(9, 1)]
        self.grid.set_falling_piece(Piece(single_block, self.DEFAULT_COLOR))

        self.grid.move_to_right()

        self.assertEqual(self.grid.current_piece, Piece(single_block, self.DEFAULT_COLOR))

    def test_when_the_piece_tries_to_move_against_the_left_border_it_should_not_move(self):
        single_block = [(0, 1)]
        self.grid.set_falling_piece(Piece(single_block, self.DEFAULT_COLOR))

        self.grid.move_to_left()

        self.assertEqual(self.grid.current_piece, Piece(single_block, self.DEFAULT_COLOR))
