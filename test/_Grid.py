import pygame

from Grid import Grid
import unittest


class _Grid(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.grid = Grid(10, 20, [])

    def test_when_figure_falls_from_the_top_y_coordinates_should_be_increased_by_one(self):
        self.grid.add_next_figure([(5, 1)])

        self.grid.move_current_blocks()

        self.assertEqual(self.grid.current_falling_blocks, [(5, 2)])

    def test_when_figure_falls_to_the_bottom_falling_blocks_should_be_empty(self):
        self.grid.add_next_figure([(5, 1)])

        for _ in range(19):
            self.grid.move_current_blocks()

        self.assertEqual(self.grid.current_falling_blocks, [])

    def test_when_figure_falls_on_another_figure(self):
        self.grid.add_next_figure([(5, 1)])
        self.grid.base_blocks = [(5, 5)]

        for _ in range(4):
            self.grid.move_current_blocks()

        self.assertEqual(self.grid.current_falling_blocks, [])

    def test_when_the_figure_moves_to_the_right_x_coordinates_should_be_increased_by_one(self):
        self.grid.add_next_figure([(5, 1)])
        self.grid.move_block_to_right()

        self.assertEqual(self.grid.current_falling_blocks, [(6, 1)])

    def test_when_the_figure_moves_to_the_left_x_coordinates_should_be_decreased_by_one(self):
        self.grid.add_next_figure([(5, 1)])
        self.grid.move_block_to_left()

        self.assertEqual(self.grid.current_falling_blocks, [(4, 1)])


    def test_when_a_figure_tries_to_move_against_the_right_border_it_should_not_move(self):
        self.grid.add_next_figure([(9, 1)])
        self.grid.move_block_to_right()

        self.assertEqual(self.grid.current_falling_blocks, [(9, 1)])


    def test_when_a_figure_tries_to_move_against_the_left_border_it_should_not_move(self):
        self.grid.add_next_figure([(0, 1)])
        self.grid.move_block_to_left()

        self.assertEqual(self.grid.current_falling_blocks, [(0, 1)])
