# -*- coding: utf-8 -*-
from .piece import Piece


class Knight(Piece):
    def __init__(self, square, color):
        Piece.__init__(self, square, "Knight", color)
        self.char = '♘' if color == 'w' else '♞'
