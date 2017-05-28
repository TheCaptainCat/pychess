from .square import Square
from chess.pieces import *

class Board:
    """Represent a chess board."""

    def __init__(self, width, height):
        """Build a new chess board.
        
        :param width: the width of the board
        :param height: the height of the board
        """
        self.width = width
        self.height = height
        self.squares = {}
        self.eaten_pieces = []
        for letter in range(0, self.width):
            for number in range(0, self.height):
                self.set_piece(letter, number, None)

    def set_piece(self, letter, number, piece):
        """Set the piece at given coordinates.
        
        :param letter: the column
        :param number: the row
        :param piece: the piece
        :raise ValueError: the coordinates must be valid
        """
        if not self.valid_coordinates(letter, number):
            raise ValueError('Invalid coordinates')
        self.squares[Square(letter, number)] = piece

    def get_piece(self, letter, number):
        """Get the piece at given coordinates.
        
        :param letter: the column
        :param number: the row
        :raise ValueError: the coordinates must be valid
        :return: the piece
        """
        if not self.valid_coordinates(letter, number):
            raise ValueError('Invalid coordinates')
        return self.squares[Square(letter, number)]

    def valid_coordinates(self, letter, number):
        """Check if the given coordinates are valid in the board.
        
        :param letter: the column
        :param number: the row
        :return true if the given coordinates are valid.
        """
        return (isinstance(letter, int) and isinstance(number, int)
                and 0 <= number < self.height and 0 <= letter < self.width)

    def move_piece(self, old_c, new_c):
        """Move the piece at old_c to new_c.

        :param old_c: a Square
        :param new_c: a Square
        :raise ValueError: the coordinates must be valid
        """
        if not (self.valid_coordinates(old_c.letter, old_c.number)
                or self.valid_coordinates(new_c.letter, new_c.number)):
            raise ValueError('Invalid coordinates')
        p = self.squares[old_c]
        self.squares[old_c] = None
        if  isinstance(self.squares[new_c], Piece):
            self.eaten_pieces.append(self.squares[new_c])
        self.squares[new_c] = p
        p.square = new_c
        if isinstance(p, Pawn):
            p.first_move_done = True

    def get_pieces_by_color(self, color):
        pieces = []
        for square in self.squares:
            if self.squares[square] is not None and self.squares[square].color == color:
                pieces.append(self.squares[square])
        return pieces

    def get_first_piece(self, piece_type, color):
        for piece in self.get_pieces_by_color(color):
            if isinstance(piece, piece_type):
                return piece

    def count_pieces_by_color(self, color):
        return len(self.get_pieces_by_color(color))

    def __str__(self):
        s = '  ' + ''.join([Square.int_to_letter(x) for x in range(0, self.width)]) + '\n'
        for number in range(0, self.height):
            s += str(number + 1) + '-'
            for letter in range(0, self.width):
                cur = self.get_piece(letter, number)
                if cur is None:
                    s += "."
                else:
                    s += cur.char
            s += '\n'
        return s
