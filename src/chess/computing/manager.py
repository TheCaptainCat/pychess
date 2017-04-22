from chess.pieces import *
from chess.structure import *


class Manager:
    """Contains mechanics to move pieces on the chess board."""

    def __init__(self, _board):
        self.board = _board

    def compute_move_set(self, _piece):
        if isinstance(_piece, Rook):
            return self.move_rook(_piece)
        if isinstance(_piece, Bishop):
            return self.move_bishop(_piece)
        if isinstance(_piece, Queen):
            return self.move_queen(_piece)
        if isinstance(_piece, King):
            return self.move_king(_piece)
        if isinstance(_piece, Knight):
            return self.move_knight(_piece)
        if isinstance(_piece, Pawn):
            return self.move_pawn(_piece)
        return None

    def move_pawn(self, _pawn):
        moves = set()
        return moves

    def move_knight(self, _knight):
        moves = set()
        squares = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        for (letter, number) in squares:
            letter = _knight.square.letter + letter
            number = _knight.square.number + number
            if self.board.valid_coordinates(letter, number):
                moves.add(Square(letter, number))
        return moves

    def move_king(self, _king):
        moves = set()
        squares = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        for (letter, number) in squares:
            letter = _king.square.letter + letter
            number = _king.square.number + number
            if self.board.valid_coordinates(letter, number):
                moves.add(Square(letter, number))
        return moves

    def move_queen(self, _queen):
        moves = set()
        moves.update(self.move_rook(_queen))
        moves.update(self.move_bishop(_queen))
        return moves

    def move_rook(self, _rook):
        def inc(x):
            return x + 1

        def dec(x):
            return x - 1

        def identity(x):
            return x

        moves = set()
        moves.update(self.strait_blocking_line(_rook.square.letter, inc, _rook.square.number, identity))
        moves.update(self.strait_blocking_line(_rook.square.letter, dec, _rook.square.number, identity))
        moves.update(self.strait_blocking_line(_rook.square.letter, identity, _rook.square.number, inc))
        moves.update(self.strait_blocking_line(_rook.square.letter, identity, _rook.square.number, dec))
        return moves

    def move_bishop(self, _bishop):
        def inc(x):
            return x + 1

        def dec(x):
            return x - 1

        moves = set()
        moves.update(self.strait_blocking_line(_bishop.square.letter, inc, _bishop.square.number, inc))
        moves.update(self.strait_blocking_line(_bishop.square.letter, dec, _bishop.square.number, dec))
        moves.update(self.strait_blocking_line(_bishop.square.letter, inc, _bishop.square.number, dec))
        moves.update(self.strait_blocking_line(_bishop.square.letter, dec, _bishop.square.number, inc))
        return moves

    def strait_blocking_line(self, letter, fl, number, fn):
        squares = set()
        number = fn(number)
        letter = fl(letter)
        while 0 <= number < self.board.height and 0 <= letter < self.board.width:
            if self.board.get_piece(letter, number) is not None:
                break
            squares.add(Square(letter, number))
            number = fn(number)
            letter = fl(letter)
        return squares
