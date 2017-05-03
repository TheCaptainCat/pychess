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
        if _pawn.color == 'w':
            if _pawn.first_move_done is False:
                squares = [(0, 1), (0, 2)]
            else:
                squares = [(0, 1)]
            diagonales = [(-1, 1), (1, 1)]

        else:
            if _pawn.first_move_done is False:
                squares = [(0, -1), (0, -2)]
            else:
                squares = [(0, -1)]
            diagonales = [(-1, -1), (1, -1)]
        for (letter, number) in diagonales:
            letter = _pawn.square.letter + letter
            number = _pawn.square.number + number
            if self.board.valid_coordinates(letter, number) \
                    and self.board.get_piece(letter, number) is not None \
                    and self.board.get_piece(letter, number).color != _pawn.color:
                moves.add(Square(letter, number))
        for (letter, number) in squares:
            letter = _pawn.square.letter + letter
            number = _pawn.square.number + number
            if self.board.valid_coordinates(letter, number) \
                    and self.board.get_piece(letter, number) is None:
                moves.add(Square(letter, number))
        return moves

    def move_knight(self, _knight):
        moves = set()
        squares = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        for (letter, number) in squares:
            letter = _knight.square.letter + letter
            number = _knight.square.number + number
            if self.board.valid_coordinates(letter, number) \
                    and (self.board.get_piece(letter, number) is None
                         or self.board.get_piece(letter, number).color != _knight.color):
                moves.add(Square(letter, number))
        return moves

    def move_king(self, _king):
        moves = set()
        squares = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        for (letter, number) in squares:
            letter = _king.square.letter + letter
            number = _king.square.number + number
            if self.board.valid_coordinates(letter, number) \
                    and (self.board.get_piece(letter, number) is None
                         or self.board.get_piece(letter, number).color != _king.color):
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

    def strait_blocking_line(self, _piece, fl, fn):
        squares = set()
        number = fn(_piece.square.number)
        letter = fl(_piece.square.letter)
        while self.board.valid_coordinates(letter, number):
            if self.board.get_piece(letter, number) is not None:
                if self.board.get_piece(letter, number).color != _piece.color:
                    squares.add(Square(letter, number))
                break
            squares.add(Square(letter, number))
            number = fn(number)
            letter = fl(letter)
        return squares

    def is_checkmate(self, color):
        _king = self.board.get_first_piece(King, color)
        moves = self.compute_move_set(_king)
        moves.add(_king.square)
        o_moves = set()
        for _piece in self.board.get_pieces_by_color('b' if color == 'w' else 'w'):
            o_moves.update(self.compute_move_set(_piece))
        return len(moves.difference(o_moves)) == 0

    def is_check(self, color):
        _king = self.board.get_first_piece(King, color)
        for _piece in self.board.get_pieces_by_color('b' if color == 'w' else 'w'):
            if _king.square in self.compute_move_set(_piece):
                return True
        return False
