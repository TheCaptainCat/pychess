# -*- coding: utf-8 -*-
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
            if self.board.valid_coordinates(letter, number) \
                    and (self.board.get_piece(letter, number) is None \
                    or self.board.get_piece(letter,number).get_color() != _knight.get_color()):
                moves.add(Square(letter, number))
        return moves

    def move_king(self, _king):
        moves = set()
        squares = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        for (letter, number) in squares:
            letter = _king.square.letter + letter
            number = _king.square.number + number
            if self.board.valid_coordinates(letter, number) \
                and ( self.board.get_piece(letter, number) is None \
                or self.board.get_piece(letter, number).get_color() != _king.get_color() ):
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
        moves.update(self.strait_blocking_line(_rook, inc, identity))
        moves.update(self.strait_blocking_line(_rook, dec, identity))
        moves.update(self.strait_blocking_line(_rook, identity, inc))
        moves.update(self.strait_blocking_line(_rook, identity, dec))
        return moves

    def move_bishop(self, _bishop):
        def inc(x):
            return x + 1

        def dec(x):
            return x - 1

        moves = set()
        moves.update(self.strait_blocking_line(_bishop, inc, inc))
        moves.update(self.strait_blocking_line(_bishop, dec, dec))
        moves.update(self.strait_blocking_line(_bishop, inc, dec))
        moves.update(self.strait_blocking_line(_bishop, dec, inc))
        return moves

    def strait_blocking_line(self, piece, fl, fn):
        squares = set()
        number = fn(piece.square.number)
        letter = fl(piece.square.letter)
        while self.board.valid_coordinates(letter, number):
            if self.board.get_piece(letter, number) is not None:
                if self.board.get_piece(letter, number).get_color() != piece.get_color() :
                    squares.add(Square(letter, number))
                break
            squares.add(Square(letter, number))
            number = fn(number)
            letter = fl(letter)
        return squares
