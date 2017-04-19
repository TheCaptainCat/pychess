from chess.structure import *
from chess.pieces import *

b = Board(8, 8)
b.set_piece('A', 8, Rook(Square('A', 8), 'w'))
b.set_piece('D', 8, Queen(Square('A', 8), 'w'))

print(b)
