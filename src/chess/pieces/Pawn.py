from .Piece import Piece


class Pawn(Piece):
    def __init__(self, square):
        Piece.__init__(self, square, "Pawn")
