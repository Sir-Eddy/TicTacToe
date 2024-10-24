"""Import used to start and execute the game"""
from view.menu import ContinueScreen
from presenter.game import Game

if __name__ == '__main__':
    game_object = Game()
    continue_object = ContinueScreen()
    while continue_object.continue_playing():
        game_object = Game()
