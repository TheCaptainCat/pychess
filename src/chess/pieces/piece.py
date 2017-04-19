class Piece:
    def __init__(self, square, name):
        self.square = square
        self.name = name

    def __str__(self):
        return "{0} {1}".format(self.name, str(self.square))
