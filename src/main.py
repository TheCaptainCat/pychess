#! /usr/bin/python3.5

from chess.computing import *
from chess.pieces import *
from chess.structure import *

b = Board(8, 8)
# White
r = Rook(Square(0, 0), 'w')
kn = Knight(Square(0, 6), 'w')
ki = King(Square(0, 4), 'w')
bi = Bishop(Square(0, 2), 'w')
b.set_piece(0, 0, r)
b.set_piece(6, 0, kn)
b.set_piece(4, 0, ki)
b.set_piece(2, 0, bi)
for i in range(0,8):
    if i % 2 != 0:
        b.set_piece(i, 1, Pawn(Square(i,1), 'w'))
    else:
        b.set_piece(i, 2, Pawn(Square(i, 2), 'w'))



# Black
r = Rook(Square(0, 7), 'b')
kn = Knight(Square(6, 7), 'b')
ki = King(Square(4, 7), 'b')
bi = Bishop(Square(2, 7), 'b')
b.set_piece(0, 7, r)
b.set_piece(6, 7, kn)
b.set_piece(4, 7, ki)
b.set_piece(2, 7, bi)
for i in range(0,8):
    if i % 2 != 0:
        b.set_piece(i, 6, Pawn(Square(i,6), 'b'))
    else:
        b.set_piece(i, 5, Pawn(Square(i, 5), 'b'))

print(b)

m = Manager(b)
print(m.compute_move_set(r))
