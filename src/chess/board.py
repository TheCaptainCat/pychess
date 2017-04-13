class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.squares = []

        for letter in "abcdefgh":
            for number in range(1,9):
                self.squares.append(Square(number,letter))

    def __str__(self):
        return "Board ({}, {})".format(self.width, self.height)

    def printboard(self):
        for square in squares:
            print('(' +  square.x + ',' + square.y + ')')
