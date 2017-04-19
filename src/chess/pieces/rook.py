from .piece import Piece


class Rook(Piece):
    def __init__(self, square, color):
        Piece.__init__(self, square, "Rook", color)
        self.char = '♖' if color == 'w' else '♜'
