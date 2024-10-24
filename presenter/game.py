"""Imports random to make the beginning random and imports all the other code"""
import random

from view.menu import Menu
from view.playboard import Playboard
from model.human import Human
from model.ai import GameAI
from model.score import Score

class Game:
    """Class that provides the essential game logic"""
    def __init__(self):
        self.new_load_game, self.pvp_pve_value= self.get_start_values()
        self.score_object = self.load_score()
        self.player1, self.player2 = self.generate_players(self.score_object)
        self.start_game(self.player1, self.player2, self.score_object)
        self.save_game(self.score_object)

    def get_start_values(self):
        """Method that returns the choosen gamemode"""
        menu_object = Menu()
        return menu_object.choose_gamemode()

    # Player 1 (X) always begins - Spieler 2 (O)
    def generate_players(self, score_object):
        """Method that generates the player objects and chooses who starts"""
        if self.pvp_pve_value == "1":
            player1 = Human()
            player2 = Human()
            return player1, player2
            # Random choice of whether player or AI starts
        random_num = random.randint(0, 1)
        if random_num == 0:
            player1 = Human()
            player2 = GameAI(score_object, "O")
            return player1, player2
        player1 = GameAI(score_object, "X")
        player2 = Human()
        return player1, player2

    def load_score(self):
        """Method that loads the game from a file"""
        if self.new_load_game == "2":
            load_game = True
            new_menu_object = Menu()
            game_number = new_menu_object.which_game_to_load(True)
            score_object = Score(load_game)
            while score_object.load_score(game_number) is False:
                new_menu_object.which_game_to_load(False)
            score_object = score_object.load_score(game_number)
            return score_object
        load_game = False
        score_object = Score(load_game)
        return score_object

    def save_game(self, score_object):
        """Method that calls the savegame method"""
        score_object.save_game()


    def start_game(self, player1, player2, score_object):
        """Method that starts a new game"""
        playboard_object = Playboard()
        current_player = "Player 1"

        if score_object.check_if_won():
            playboard_object.display_playboard(current_player, score_object.return_score())
            playboard_object.player_won(current_player)
            return

        if score_object.check_if_draw():
            playboard_object.display_playboard(current_player, score_object.return_score())
            playboard_object.draw()
            return

        while not score_object.check_if_won():
            current_player = "Player 1 (X)"
            playboard_object.display_playboard(current_player, score_object.return_score())
            p_input = player1.make_move()
            while p_input != "q" and not score_object.check_if_used(p_input):
            # checks if used returned True if unused
                playboard_object.field_occupied()
                p_input = player1.make_move()
            if p_input == "q":
                self.save_game(score_object)
                break
            score_object.set_score(p_input, "X")
            if score_object.check_if_won():
                playboard_object.display_playboard(current_player, score_object.return_score())
                playboard_object.player_won(current_player)
                break
            if score_object.check_if_draw():
                playboard_object.display_playboard(current_player, score_object.return_score())
                playboard_object.draw()
                break

            current_player = "Player 2 (O)"
            playboard_object.display_playboard(current_player, score_object.return_score())
            p_input = player2.make_move()
            while p_input != "q" and not score_object.check_if_used(p_input):
                playboard_object.field_occupied()
                p_input = player2.make_move()
            if p_input == "q":
                self.save_game(score_object)
                break
            score_object.set_score(p_input, "O")
            if score_object.check_if_won():
                playboard_object.display_playboard(current_player, score_object.return_score())
                playboard_object.player_won(current_player)
                break
            if score_object.check_if_draw():
                playboard_object.display_playboard(current_player, score_object.return_score())
                playboard_object.draw()
                break
