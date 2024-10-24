"""Model used to provide a human player"""
class Human():
    """Class used to provide a human object"""
    def __init__(self):
        pass

    def make_move(self):
        """Method that provides the ability to make a move"""
        print("Please choose a Field (1-9):")
        cf = input() #chosen field
        while cf not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if cf == "q":
                return "q"
            print("The chosen Field is not valid!, Try Again!")
            cf = input()
        return cf
