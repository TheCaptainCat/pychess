from chess.pieces import *
from chess.structure import *


class Manager:
    """Contains mechanics to move pieces on the chess board."""

    def __init__(self, board):
        self.board = board

    def compute_move_set(self, piece):
        if isinstance(piece, Rook):
            return self.move_rook(piece)
        if isinstance(piece, Bishop):
            return self.move_bishop(piece)
        if isinstance(piece, Queen):
            return self.move_queen(piece)

    def move_queen(self, queen):
        moves = set()
        moves.update(self.move_rook(queen))
        moves.update(self.move_bishop(queen))
        return moves

    def move_rook(self, rook):
        moves = set()
        for i in range(0, self.board.width):
            moves.add(Square(i, rook.square.number))
            moves.add(Square(rook.square.letter, i))
        moves.remove(rook.square)
        return moves

    def move_bishop(self, bishop):
        moves = set()
        for i in range(0, max(self.board.width, self.board.height)):
            if self.board.valid_coordinates(bishop.square.letter + i, bishop.square.number + i):
                moves.add(Square(bishop.square.letter + i, bishop.square.number + i))
            if self.board.valid_coordinates(bishop.square.letter - i, bishop.square.number + i):
                moves.add(Square(bishop.square.letter - i, bishop.square.number + i))
            if self.board.valid_coordinates(bishop.square.letter + i, bishop.square.number - i):
                moves.add(Square(bishop.square.letter + i, bishop.square.number - i))
            if self.board.valid_coordinates(bishop.square.letter - i, bishop.square.number - i):
                moves.add(Square(bishop.square.letter - i, bishop.square.number - i))
        moves.remove(bishop.square)
        return moves
