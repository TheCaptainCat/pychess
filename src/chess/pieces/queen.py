from .piece import Piece


class Queen(Piece):
    def __init__(self, square, color):
        Piece.__init__(self, square, "Queen", color)
        self.char = '♕' if color == 'w' else '♛'
