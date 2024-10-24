"""Imports json for savegames, time for id generation and os for file saving"""
import json
import time
import os

class Score:
    """Class loading and saving and checking the score"""
    def __init__(self, load_game):

        self.field_upper_left = "1"
        self.field_upper_middle = "2"
        self.field_upper_right = "3"

        self.field_middle_left = "4"
        self.field_middle_middle = "5"
        self.field_middle_right = "6"

        self.field_lower_left = "7"
        self.field_lower_middle = "8"
        self.field_lower_right = "9"

        self.load_game = load_game
        #self.load_game()

    def load_score(self, game_number):
        """Method that loads a game from a file"""
        if self.load_game:
            f = open('scores.json', encoding="utf-8")
            score = json.load(f)
            keys = list(score.keys()) #make list
            length = len(keys)
            if int(game_number) < length:
                which_score_id = keys[length-game_number]
                score_data = score[which_score_id]   #dict of the wanted id with its data
                self.field_upper_left = score_data["field_upper_left"]
                self.field_upper_middle = score_data["field_upper_middle"]
                self.field_upper_right = score_data["field_upper_right"]

                self.field_middle_left = score_data["field_middle_left"]
                self.field_middle_middle = score_data["field_middle_middle"]
                self.field_middle_right = score_data["field_middle_right"]

                self.field_lower_left = score_data["field_lower_left"]
                self.field_lower_middle = score_data["field_lower_middle"]
                self.field_lower_right = score_data["field_lower_right"]
                return self
            return False #if it doesn't exist

    def return_score(self):
        """Method that returns the game data"""
        score_array = [
            self.field_upper_left,
            self.field_upper_middle,
            self.field_upper_right,
            self.field_middle_left,
            self.field_middle_middle,
            self.field_middle_right,
            self.field_lower_left,
            self.field_lower_middle,
            self.field_lower_right
            ]
        return score_array

    def save_game(self):
        """Method that saves the game to a file"""
        timestamp = time.time()
        game_id = {"id_time": timestamp}
        score_dict = self.__dict__.copy()
        score_dict.update(game_id)

        #json_score_with_id = json.dumps(score_dict, indent = 2)
        file_path = "scores.json"

        if not os.path.exists(file_path) or os.path.getsize(file_path)<=0:
        #checks if file exists and if it is empty
            total_dict = {}
        else:
            with open ("scores.json", "r", encoding="utf-8") as file:
            #the dictionary is being read in
                total_dict = json.load(file)

        total_dict[str(timestamp)] = score_dict
        #new entry gets added to the dict

        with open ("scores.json", "w", encoding="utf-8") as file:
            #overwrites the json file with the new content
            json.dump(total_dict, file, indent = 2)

    def set_score(self, field, player):
        """Method that sets the players score"""
        match field:
            case "1": self.field_upper_left = player
            case "2": self.field_upper_middle = player
            case "3": self.field_upper_right = player
            case "4": self.field_middle_left = player
            case "5": self.field_middle_middle = player
            case "6": self.field_middle_right = player
            case "7": self.field_lower_left = player
            case "8": self.field_lower_middle = player
            case "9": self.field_lower_right = player

    def check_if_used(self, field):
        """Method that checks if a field is used"""
        match field:
            case "1": return self.field_upper_left == "1"
            case "2": return self.field_upper_middle == "2"
            case "3": return self.field_upper_right == "3"
            case "4": return self.field_middle_left == "4"
            case "5": return self.field_middle_middle == "5"
            case "6": return self.field_middle_right == "6"
            case "7": return self.field_lower_left == "7"
            case "8": return self.field_lower_middle == "8"
            case "9": return self.field_lower_right == "9"


    def check_if_draw(self):
        """Method that checks if there is a draw"""
        is_draw = (
        self.field_upper_left != "1" and
        self.field_upper_middle != "2" and
        self.field_upper_right != "3" and
        self.field_middle_left != "4" and
        self.field_middle_middle != "5" and
        self.field_middle_right != "6" and
        self.field_lower_left != "7" and
        self.field_lower_middle != "8" and
        self.field_lower_right != "9"
        )
        if is_draw:
            return True

    def check_if_won(self):
        """Method that checks if a player won"""
        line0 = [self.field_upper_left, self.field_upper_middle, self.field_upper_right]
        line1 = [self.field_middle_left, self.field_middle_middle, self.field_middle_right]
        line2 = [self.field_lower_left, self.field_lower_middle, self.field_lower_right]

        #check rows
        if line0.count("O") == 3 or line0.count("X") == 3:
            return True
        if line1.count("O") == 3 or line1.count("X") == 3:
            return True
        if line2.count("O") == 3 or line2.count("X") == 3:
            return True

        #check columns
        elif line0[0] == "X" and line1[0] == "X" and line2[0] == "X":
            return True
        elif line0[1] == "X" and line1[1] == "X" and line2[1] == "X":
            return True
        elif line0[2] == "X" and line1[2] == "X" and line2[2] == "X":
            return True
        elif line0[0] == "O" and line1[0] == "O" and line2[0] == "O":
            return True
        elif line0[1] == "O" and line1[1] == "O" and line2[1] == "O":
            return True
        elif line0[2] == "O" and line1[2] == "O" and line2[2] == "O":
            return True

        #check diagonals
        elif line0[0] == "X" and line1[1] == "X" and line2[2] == "X":
            return True
        elif line0[2] == "X" and line1[1] == "X" and line2[0] == "X":
            return True
        elif line0[0] == "O" and line1[1] == "O" and line2[2] == "O":
            return True
        elif line0[2] == "O" and line1[1] == "O" and line2[0] == "O":
            return True

        else:
            return False
