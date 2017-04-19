from .piece import Piece


class Bishop(Piece):
    def __init__(self, square):
        Piece.__init__(self, square, "Bishop")
