"""Imports the GameAI class and the unittest helper classes"""
import unittest
from unittest.mock import Mock
from model.ai import GameAI

class TestGameAI(unittest.TestCase):
    """Class that tests the GameAI Class"""
    def setUp(self):
        self.mock_score_object = Mock()
        self.mock_score_object.return_score.return_value = ['-'] * 9

    def test_make_move_x(self):
        """Method for testing the ability to make moves as X"""
        ai = GameAI(self.mock_score_object, 'X')
        self.mock_score_object.return_score.return_value = [
            'X', '-', '-', '-', '-', '-', '-', '-', '-'
        ]
        move = ai.make_move()
        self.assertIn(move, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_make_move_o(self):
        """Method for testing the ability to make moves as O"""
        ai = GameAI(self.mock_score_object, 'O')
        self.mock_score_object.return_score.return_value = [
            'O', '-', '-', '-', '-', '-', '-', '-', '-'
        ]
        move = ai.make_move()
        self.assertIn(move, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_evaluation_win_row(self):
        """Method to test win detection when having a row"""
        ai = GameAI(self.mock_score_object, 'X')
        ai.field = [[2, 2, 2], ['-', '-', '-'], ['-', '-', '-']]
        self.assertEqual(ai.evaluation(), 2)

    def test_evaluation_win_column(self):
        """Method to test win detection when having a column"""
        ai = GameAI(self.mock_score_object, 'O')
        ai.field = [[0, '-', '-'], [0, '-', '-'], [0, '-', '-']]
        self.assertEqual(ai.evaluation(), 0)

    def test_evaluation_win_diagonal(self):
        """Method to test win detection when having a diagonal"""
        ai = GameAI(self.mock_score_object, 'X')
        ai.field = [[2, '-', '-'], ['-', 2, '-'], ['-', '-', 2]]
        self.assertEqual(ai.evaluation(), 2)

    def test_evaluation_draw(self):
        """Method to test detection when having a draw"""
        ai = GameAI(self.mock_score_object, 'X')
        ai.field = [[2, 0, 2], [0, 2, 0], [0, 2, 0]]
        self.assertEqual(ai.evaluation(), 1)

    def test_evaluation_ongoing(self):
        """Method that tests the detection of a running game"""
        ai = GameAI(self.mock_score_object, 'X')
        ai.field = [[2, 0, 2], [0, '-', 0], ['-', 2, 0]]
        self.assertEqual(ai.evaluation(), -1)

    def test_max(self):
        """Method for testing the max part of the alogrithm"""
        ai = GameAI(self.mock_score_object, 'X')
        ai.field = [[2, 0, '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.assertIn(ai.max(), [0, 1, 2])

    def test_get_max_not_running(self):
        """Method for testing detection of a running game in the max-alogrithm"""
        ai = GameAI(self.mock_score_object, 'O')
        ai.field = [[2, 0, 2], [0, 2, 0], [0, 2, 0]]
        self.assertEqual(ai.get_max(), 1)

    def test_min(self):
        """Method for testing the min part of the alogrithm"""
        ai = GameAI(self.mock_score_object, 'O')
        ai.field = [[2, 0, '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.assertIn(ai.min(), [0, 1, 2])

    def test_get_min_not_running(self):
        """Method for testing detection of a running game in the min-alogrithm"""
        ai = GameAI(self.mock_score_object, 'O')
        ai.field = [[2, 0, 2], [0, 2, 0], [0, 2, 0]]
        self.assertEqual(ai.get_min(), 1)
