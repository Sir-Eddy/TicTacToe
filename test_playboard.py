"""Imports the playboard class and the unittest helper classes"""
import unittest
from unittest.mock import patch
from io import StringIO
from view.playboard import Playboard

class TestPlayboard(unittest.TestCase):
    """Class that tests the Playboard class"""
    def setUp(self):
        self.playboard = Playboard()

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_playboard(self, mock_stdout):
        """Method that tests the displayed playboard"""
        current_player = "X"
        field = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.playboard.display_playboard(current_player, field)
        output = mock_stdout.getvalue()
        self.assertIn("Your Turn X !", output)
        self.assertIn("1  | 2 |  3", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_field_occupied(self, mock_stdout):
        """Method tests if a field is already occupied"""
        self.playboard.field_occupied()
        self.assertIn("Field already occupied!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_player_x_won(self, mock_stdout):
        """Method tests if the player X winning works correctly"""
        self.playboard.player_won("X")
        self.assertIn("X won!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_player_y_won(self, mock_stdout):
        """Method tests if the player X winning works correctly"""
        self.playboard.player_won("Y")
        self.assertIn("Y won!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_draw(self, mock_stdout):
        """Method tests if the draw function works correctly"""
        self.playboard.draw()
        self.assertIn("Draw! No Player won!", mock_stdout.getvalue())
