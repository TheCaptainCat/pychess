# -*- coding: utf-8 -*-
from .piece import Piece


class Pawn(Piece):
    def __init__(self, square, color):
        Piece.__init__(self, square, "Pawn", color)
        self.char = '♙' if color == 'w' else '♟'
        self.first_move_done = False
