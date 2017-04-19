from chess.structure import *
from chess.pieces import *

b = Board(8, 8)
b.set_piece(0, 0, Rook(Square(0, 0), 'w'))
b.set_piece(1, 1, Queen(Square(1, 1), 'w'))

print(b)
