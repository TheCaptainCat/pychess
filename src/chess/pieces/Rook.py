from . import Piece


class Rook(Piece):
    def __init__(self, square):
        Piece.__init__(self, square, "Rook")
