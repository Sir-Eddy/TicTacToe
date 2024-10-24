"""Imports the unittest framework, the patch function, MagicMock class"""
import unittest
from unittest.mock import patch, MagicMock
from presenter.game import Game

class TestGame(unittest.TestCase):
    """Class for testing the Game Class"""
    @patch('presenter.game.Menu')
    @patch('presenter.game.Playboard')
    @patch('presenter.game.Human')
    @patch('presenter.game.GameAI')
    @patch('presenter.game.Score')
    def test_game_initialization_and_flow(self,
                                            mock_score,
                                            mock_game_ai,
                                            mock_human,
                                            mock_playboard,
                                            mock_menu):
        """Method testing the get_start_values method and sets up mocked objects"""
        # Mock the Menu.choose_gamemode() method
        mock_menu_instance = mock_menu.return_value
        mock_menu_instance.choose_gamemode.return_value = ("1", "1")  # New game, PvP

        # Mock the Score class
        mock_score_instance = mock_score.return_value
        mock_score_instance.check_if_won.side_effect = [False, False, True]
        mock_score_instance.check_if_draw.return_value = False
        mock_score_instance.check_if_used.return_value = True
        mock_score_instance.return_score.return_value = [" "] * 9

        # Mock the Human class
        mock_human_instance = mock_human.return_value
        mock_human_instance.make_move.side_effect = ["1", "2", "3"]

        # Mock the Playboard class
        mock_playboard_instance = mock_playboard.return_value

        # Create a Game instance
        game = Game()

        # Assertions
        self.assertEqual(game.new_load_game, "1")
        self.assertEqual(game.pvp_pve_value, "1")
        self.assertIsInstance(game.player1, MagicMock)
        self.assertIsInstance(game.player2, MagicMock)

        # Check if methods were called
        mock_menu_instance.choose_gamemode.assert_called_once()
        mock_score.assert_called_once()
        mock_human.assert_called()
        mock_playboard.assert_called_once()
        mock_playboard_instance.display_playboard.assert_called()
        mock_playboard_instance.player_won.assert_called_once()
        mock_score_instance.save_game.assert_called_once()

    @patch('presenter.game.Menu')
    @patch('presenter.game.Human')
    @patch('presenter.game.GameAI')
    @patch('presenter.game.Score')
    @patch('random.randint')
    def test_generate_players_pve(self,
                                  mock_randint,
                                  mock_score,
                                  mock_game_ai,
                                  mock_human,
                                  mock_menu):
        """Method testing player generation in a Pve Scenarion where the human starts"""
        mock_menu_instance = mock_menu.return_value
        mock_menu_instance.choose_gamemode.return_value = ("1", "2")  # New game, PvE
        mock_randint.return_value = 0  # Human starts

        game = Game()

        self.assertIsInstance(game.player1, MagicMock)
        self.assertIsInstance(game.player2, MagicMock)
        mock_score.assert_called()

        mock_randint.return_value = 0  # Human starts
        game2 = Game()
        self.assertIsInstance(game2.player1, MagicMock)
        self.assertIsInstance(game2.player2, MagicMock)
        mock_score.assert_called()

    @patch('presenter.game.Menu')
    @patch('presenter.game.Score')
    def test_load_game(self, mock_score, mock_menu):
        """Method testing the loading of games from file"""
        mock_menu_instance = mock_menu.return_value
        mock_menu_instance.choose_gamemode.return_value = ("2", "1")  # Load game, PvP
        mock_menu_instance.which_game_to_load.return_value = "1"

        mock_score_instance = mock_score.return_value
        mock_score_instance.load_score.return_value = mock_score_instance

        game = Game()

        self.assertEqual(game.new_load_game, "2")
        mock_score_instance.load_score.assert_called_with("1")

    @patch('presenter.game.Menu')
    @patch('presenter.game.Score')
    def test_save_game(self, mock_score, mock_menu):
        """Method testing the saving of a game, especially if called once"""
        mock_menu_instance = mock_menu.return_value
        mock_menu_instance.choose_gamemode.return_value = ("1", "1")  # New game, PvP

        mock_score_instance = mock_score.return_value

        game = Game()

        game.save_game(mock_score_instance) #check if called once
        self.assertEqual(mock_score_instance.save_game.call_count, 2)
        # One during init, one during explicit call

    @patch('presenter.game.Menu')
    @patch('presenter.game.Human')
    @patch('presenter.game.GameAI')
    @patch('presenter.game.Score')
    @patch('random.randint')
    def test_start_game_draw(self, mock_randint, mock_score, mock_game_ai, mock_human, mock_menu):
        """Method testing if a draw gets recognized and if the draw function gets called"""
        mock_menu_instance = mock_menu.return_value
        mock_menu_instance.choose_gamemode.return_value = ("1", "1")  # New game, PvP

        mock_score_instance = mock_score.return_value
        mock_score_instance.check_if_won.side_effect = [False] * 9
        mock_score_instance.check_if_draw.return_value = True
        mock_score_instance.return_score.return_value = [
            "X", "O", "X", "X", "X", "O", "O", "X", "O"
            ]

        mock_playboard_instance = MagicMock()
        with patch('presenter.game.Playboard', return_value=mock_playboard_instance):
            game = Game()

            mock_playboard_instance.display_playboard.assert_called()
            mock_playboard_instance.draw.assert_called_once()

    @patch('presenter.game.Menu')
    @patch('presenter.game.Human')
    @patch('presenter.game.GameAI')
    @patch('presenter.game.Score')
    @patch('random.randint')
    def test_start_game_quit_mid_game(self,
                                      mock_randint,
                                      mock_score,
                                      mock_game_ai,
                                      mock_human,
                                      mock_menu):
        """Method testing if quitting midgame works accordingly"""
        mock_menu_instance = mock_menu.return_value
        mock_menu_instance.choose_gamemode.return_value = ("1", "1")  # New game, PvP

        mock_score_instance = mock_score.return_value
        mock_score_instance.check_if_won.return_value = False
        mock_score_instance.check_if_draw.return_value = False

        mock_human_instance = mock_human.return_value
        mock_human_instance.make_move.side_effect = ["1", "q"]  # Player quits

        mock_playboard_instance = MagicMock()
        with patch('presenter.game.Playboard', return_value=mock_playboard_instance):
            game = Game()

            # Now, check the explicit call during quitting
            self.assertEqual(mock_score_instance.save_game.call_count, 2)
            # One during init, one during quit
