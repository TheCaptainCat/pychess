#! /usr/bin/python3.5

from chess.computing import *
from chess.pieces import *
from chess.structure import *

b = Board(8, 8)
r = Queen(Square(1, 1), 'w')
b.set_piece(1, 1, r)

print(b)

m = Manager(b)
print(m.compute_move_set(r))
