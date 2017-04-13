class Piece:
    def __init__(self, x, y):
        self.square = Square(x,y)

    def __str__(self):
        return "Piece ({}, {})".format(self.square)
