from .Piece import Piece


class King(Piece):
    def __init__(self, square):
        Piece.__init__(self, square, "King")
