"""Imports the unittest framework, the patch Method and the human class"""
import unittest
from unittest.mock import patch
from model.human import Human

class TestHuman(unittest.TestCase):
    """Class for testing the human class"""
    def setUp(self):
        self.human = Human()

    @patch('builtins.input', return_value='5')
    def test_make_move_valid(self, mock_input):
        """Method testing valid input"""
        self.assertEqual(self.human.make_move(), '5')

    @patch('builtins.input', side_effect=['10', '5'])
    def test_make_move_invalid_then_valid(self, mock_input):
        """Method testing unvalid and then valid input"""
        self.assertEqual(self.human.make_move(), '5')

    @patch('builtins.input', return_value='q')
    def test_make_move_quit(self, mock_input):
        """Method testing the quitting mechanism"""
        self.assertEqual(self.human.make_move(), 'q')
