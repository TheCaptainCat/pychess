class Pawn(Piece):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Pawn ({}, {})".format(self.width, self.height)
