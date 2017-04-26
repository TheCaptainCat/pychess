# -*- coding: utf-8 -*-
from .piece import Piece


class King(Piece):
    def __init__(self, square, color):
        Piece.__init__(self, square, "King", color)
        self.char = '♔' if color == 'w' else '♚'
