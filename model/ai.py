"""Modal contains the ai object and the min-max-algorithm"""
class GameAI:
    """Class used create and interact with the ai object"""
    def __init__(self, score_object, x_or_o):
        self.score_object = score_object
        self.x_or_o = x_or_o
        self.ai_x = 0
        self.ai_y = 0
        self.empty = "-"
        self.field = []

    def make_move(self):
        """Method used to make a move on the board"""

        self.field = [
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
        ]

        score_array = self.score_object.return_score()
        # O -> 0 und X -> 2 und fieldzahl -> "Empty"
        for i in range(9):
            if score_array[i] == "X":
                score_array[i] = 2
            elif score_array[i] == "O":
                score_array[i] = 0
            else:
                score_array[i] = "-"

        # array gets converted into a two-dimensional one
        current_score_min_max = [[score_array[0], score_array[1], score_array[2]],
                                 [score_array[3], score_array[4], score_array[5]],
                                 [score_array[6], score_array[7], score_array[8]]]

        for i in range(3):
            for j in range(3):
                self.field[i][j] = current_score_min_max[i][j]

        if self.x_or_o == "X":
            self.get_max()
        else:
            self.get_min()

        self.field[self.ai_x][self.ai_y] = 0

        position_map = {
        (0, 0): "1",
        (0, 1): "2",
        (0, 2): "3",
        (1, 0): "4",
        (1, 1): "5",
        (1, 2): "6",
        (2, 0): "7",
        (2, 1): "8",
        (2, 2): "9"
        }
        return position_map.get((self.ai_x, self.ai_y), None)

    def evaluation(self):
        """Method used to evaluate the fields"""
        for s in (0, 2):
            for x in range(3):
                if self.field[x][0] == s and self.field[x][1] == s and self.field[x][2] == s:
                    return s
            for y in range(3):
                if self.field[0][y] == s and self.field[1][y] == s and self.field[2][y] == s:
                    return s
            if self.field[0][0] == s and self.field[1][1] == s and self.field[2][2] == s:
                return s
            if self.field[0][2] == s and self.field[1][1] == s and self.field[2][0] == s:
                return s
        for x in range(3):
            for y in range(3):
                if self.field[x][y] == self.empty:
                    return -1
        return 1

    def max(self):
        """Method contains the max-part of the algorithm"""
        if self.evaluation() != -1:
            return self.evaluation()
        max_score = -999
        for x in range(3):
            for y in range(3):
                if self.field[x][y] == self.empty:
                    self.field[x][y] = 2
                    value = self.min()
                    if value > max_score:
                        max_score = value
                    self.field[x][y] = self.empty
        return max_score

    def min(self):
        """Method contains the min-part of the algorithm"""
        if self.evaluation() != -1:
            return self.evaluation()
        min_score = 999
        for x in range(3):
            for y in range(3):
                if self.field[x][y] == self.empty:
                    self.field[x][y] = 0
                    value = self.max()
                    if value < min_score:
                        min_score = value
                    self.field[x][y] = self.empty
        return min_score

    def get_min(self):
        """Method contains the min-part of the algorithm"""
        if self.evaluation() != -1:
            return self.evaluation()
        min_score = 999
        for x in range(3):
            for y in range(3):
                if self.field[x][y] == self.empty:
                    self.field[x][y] = 0
                    value = self.max()
                    if value < min_score:
                        min_score = value
                        self.ai_x = x
                        self.ai_y = y
                    self.field[x][y] = self.empty
        return min_score

    def get_max(self):
        """Method contains the max-part of the algorithm"""
        if self.evaluation() != -1:
            return self.evaluation()
        max_score = -999
        for x in range(3):
            for y in range(3):
                if self.field[x][y] == self.empty:
                    self.field[x][y] = 2
                    value = self.min()
                    if value > max_score:
                        max_score = value
                        self.ai_x = x
                        self.ai_y = y
                    self.field[x][y] = self.empty
        return max_score
