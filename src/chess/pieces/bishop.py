# -*- coding: utf-8 -*-
from .piece import Piece


class Bishop(Piece):
    def __init__(self, square, color):
        Piece.__init__(self, square, "Bishop", color)
        self.char = '♗' if color == 'w' else '♝'
