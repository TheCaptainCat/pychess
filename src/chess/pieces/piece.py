# -*- coding: utf-8 -*-
class Piece:
    """Represent a chess piece."""

    def __init__(self, square, name, color):
        """Build a new chess piece
        
        :param square: the square where is the piece
        :param name: the name of the piece
        :param color: the color of the piece
        :raise ValueError: the color must be 'w' or 'b'
        """
        self.square = square
        self.name = name
        if color != 'w' and color != 'b':
            raise ValueError("Color must be 'w' or 'b'")
        self.color = color
        self.char = None
        self.board = None

    def get_char(self):
        """Get the character for a console representation.
        
        :return: a character
        """
        return self.char

    def get_color(self):
        """Get the color of the current piece.

        :return: a char
        """
        return self.color

    def add_to_board(self, board):
        board.set_piece(self.square.letter, self.square.number, self)
        self.board = board

    def __str__(self):
        return "{0} {1}".format(self.name, str(self.square))
