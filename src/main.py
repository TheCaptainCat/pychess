#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

from chess.computing import *
from chess.pieces import *
from chess.structure import *


b = Board(8, 8)

# White
King(Square(0, 0), 'w').add_to_board(b)
"""Rook(Square(7, 0), 'w').add_to_board(b)
Knight(Square(1, 0), 'w').add_to_board(b)
Bishop(Square(5, 0), 'w').add_to_board(b)
for i in range(0, 8):
    if i % 2 == 0:
        Pawn(Square(i, 1), 'w').add_to_board(b)
    else:
        Pawn(Square(i, 2), 'w').add_to_board(b)"""

# Black
Rook(Square(2, 1), 'b').add_to_board(b)
Knight(Square(6, 7), 'b').add_to_board(b)
King(Square(4, 7), 'b').add_to_board(b)
Bishop(Square(2, 7), 'b').add_to_board(b)
for i in range(0, 8):
    if i % 2 != 0:
        Pawn(Square(i, 6), 'b').add_to_board(b)
    else:
        Pawn(Square(i, 5), 'b').add_to_board(b)

m = Manager(b)
print(b)
print(m.is_check('w'))
