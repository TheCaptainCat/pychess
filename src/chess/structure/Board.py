from . import Square


class Board:
    """
    Represents a chess board.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.squares = {}
        for letter in range(0, self.width):
            for number in range(0, self.height):
                self.squares[Square(number, letter)] = None

    def __str__(self):
        return "Board ({}, {})".format(self.width, self.height)
