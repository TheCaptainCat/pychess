from .piece import Piece


class Queen(Piece):
    def __init__(self, square):
        Piece.__init__(self, square, "Queen")
