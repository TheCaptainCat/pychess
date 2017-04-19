from .Piece import Piece


class Knight(Piece):
    def __init__(self, square):
        Piece.__init__(self, square, "Knight")
