"""Imports the unittest framework, the patch Method and the menu class"""
import unittest
from unittest.mock import patch
from view.menu import Menu, ContinueScreen

class TestMenu(unittest.TestCase):
    """Main Test class for testing the Main Class"""
    @patch('builtins.input', side_effect=['1', '2'])
    def test_choose_gamemode(self, mock_input):
        """Test Method for the gamemode"""
        menu = Menu()
        new_load_game, pvp_pve_value = menu.choose_gamemode()
        self.assertEqual(new_load_game, '1')
        self.assertEqual(pvp_pve_value, '2')

    @patch('builtins.input', side_effect=['3', '1', '3', '2'])
    def test_choose_gamemode_invalid_input(self, mock_input):
        """Test Method for the gamemode with invalid input"""
        menu = Menu()
        new_load_game, pvp_pve_value = menu.choose_gamemode()
        self.assertEqual(new_load_game, '1')
        self.assertEqual(pvp_pve_value, '2')

    @patch('builtins.input', return_value='2')
    def test_which_game_to_load(self, mock_input):
        """Test Method for the game loading"""
        menu = Menu()
        game_number = menu.which_game_to_load(True)
        self.assertEqual(game_number, 2)

    @patch('builtins.input', return_value='2')
    def test_which_game_to_load_false(self, mock_input):
        """Test Method for the game loading without having a game to load"""
        menu = Menu()
        game_number = menu.which_game_to_load(False)
        self.assertEqual(game_number, 2)

class TestContinueScreen(unittest.TestCase):
    """Class for testing the ContinueScreen Class"""
    @patch('builtins.input', return_value='y')
    def test_continue_playing_yes(self, mock_input):
        """Method that tests if continuing works"""
        continue_screen = ContinueScreen()
        self.assertTrue(continue_screen.continue_playing())

    @patch('builtins.input', return_value='n')
    def test_continue_playing_no(self, mock_input):
        """Method tests if not continuing works"""
        continue_screen = ContinueScreen()
        self.assertFalse(continue_screen.continue_playing())

    @patch('builtins.input', side_effect=['x', 'y'])
    def test_continue_playing_invalid_input(self, mock_input):
        """Method tests what happens at invalid input"""
        continue_screen = ContinueScreen()
        self.assertTrue(continue_screen.continue_playing())
