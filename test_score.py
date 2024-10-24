"""Imports the unittest framework, the Class Score and os."""
import unittest
import os
from model.score import Score

class TestScore(unittest.TestCase):
    """Class for testing the Score Class"""
    def setUp(self):
        self.score = Score(load_game=False)

    def test_initial_score(self):
        """Method for testing the initial score"""
        expected_score = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.assertEqual(self.score.return_score(), expected_score)

    def test_set_score(self):
        """Method for testing to set a value"""
        self.score.set_score("1", "X")
        self.assertEqual(self.score.field_upper_left, "X")
        self.score.set_score("5", "O")
        self.assertEqual(self.score.field_middle_middle, "O")

    def test_check_if_used(self):
        """Method for testing if a field is already in use"""
        self.assertTrue(self.score.check_if_used("1"))
        self.score.set_score("1", "X")
        self.assertFalse(self.score.check_if_used("1"))

    def test_check_if_draw(self):
        """Method for testing if a draw gets recognized"""
        self.assertFalse(self.score.check_if_draw())
        for i in range(1, 10):
            self.score.set_score(str(i), "X")
        self.assertTrue(self.score.check_if_draw())

    def test_check_if_won(self):
        """Method for testing if a win gets recognized"""
        self.assertFalse(self.score.check_if_won())
        self.score.set_score("1", "X")
        self.score.set_score("2", "X")
        self.score.set_score("3", "X")
        self.assertTrue(self.score.check_if_won())

    def test_load_score_game_number_too_large(self):
        """Method for testing the loading number mechanism"""
        self.score.save_game()
        # Trying to load a game that doesn't exist
        result = self.score.load_score(999)
        self.assertFalse(result)

    def test_save_game_creates_file(self):
        """Method for testing if a file gets saved correctly"""
        if os.path.exists("scores.json"):
            os.remove("scores.json")
        self.assertFalse(os.path.exists("scores.json"))
        self.score.save_game()
        self.assertTrue(os.path.exists("scores.json"))

    def test_check_if_used_various_fields(self):
        """Method for testing various fields to ensure coverage"""
        fields = ["2", "3", "4", "5", "6", "7", "8", "9"]
        for field in fields:
            self.assertTrue(self.score.check_if_used(field))
            self.score.set_score(field, "X")
            self.assertFalse(self.score.check_if_used(field))
