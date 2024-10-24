"""Module used to provide a menu and continuence logic"""
class Menu:
    """Class used to provide a user-facing menu"""
    def __init__(self):
        pass

    def choose_gamemode(self):
        """Method for letting the player choose a game(mode)"""
        print("\nWelcome to TIC TAC TOE\n")
        print("1. New Game")
        print("2. Load Game\n")
        new_load_game = input()
        while new_load_game not in ('1', '2'):
            print("Invalid instruction!")
            new_load_game = input()
        print("\nChoose a Gamemode:\n")
        print("1. Player vs. Player")
        print("2. Player vs. AI\n")
        pvp_pve_value = input()
        while pvp_pve_value not in ('1', '2'):
            print("Invalid Gamemode!")
            pvp_pve_value = input()
        return new_load_game, pvp_pve_value

    def which_game_to_load(self, bool_value):
        """Method for letting the player choose a game to load"""
        if bool_value is False:
            print("You haven´t played this many games yet, pick a valid value!")
            #Input is taken to load past game.
        print("Which game do you want to load?")
        print("Choose a number (1 for last game, 2 for second to last game, ...):")
        game_number = input()
        game_number_int = int(game_number)
        return game_number_int

class ContinueScreen:
    """Class used to check in the game should be continued"""
    def __init__(self):
        pass
    def continue_playing(self):
        """Method used to check in the game should be continued"""
        print("\nContinue playing? (y/n)\n")
        continue_playing = input()
        while continue_playing not in ('y', 'n'):
            print("Invalid input!")
            continue_playing = input()
        if continue_playing == "y":
            return True
        else:
            print("\nThank you for playing!\n")
            return False
