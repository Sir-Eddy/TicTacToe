"""Module used to draw the user-facing playboard"""
class Playboard:
    """Class used to draw the user-facing playboard"""
    def __init__(self):
        pass
    def display_playboard(self, current_player, field):
        """Method used to display the playboard"""
        print("\nPress 'q' to save and quit the game\n")
        print("Your Turn " + current_player + " !\n")
        print(field[0] + "  | " + field[1] + " |  " + field[2])
        print("---+---+---")
        print(field[3] + "  | " + field[4] + " |  " + field[5])
        print("---+---+---")
        print(field[6] + "  | " + field[7] + " |  " + field[8] + "\n")

    def field_occupied(self):
        """Method used to report illegal move"""
        print("Field already occupied!")

    def player_won(self, current_player):
        """Method used to display a win"""
        print(current_player + " won!")

    def draw(self):
        """Method used to display a draw"""
        print("Draw! No Player won!")
