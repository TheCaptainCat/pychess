from .square import Square


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
        for letter in range(0, self.width):
            for number in range(0, self.height):
                self.set_piece(chr(letter + ord('A')), number + 1, None)

    def set_piece(self, letter, number, piece):
        """Set the piece at given coordinates.
        
        :param letter: the column
        :param number: the row
        :param piece: the piece
        :raise ValueError: the coordinates must be valid
        """
        if not self.valid_coordinates(letter.upper(), number):
            raise ValueError('Invalid coordinates')
        self.squares[Square(letter.upper(), number)] = piece

    def get_piece(self, letter, number):
        """Get the piece at given coordinates.
        
        :param letter: the column
        :param number: the row
        :raise ValueError: the coordinates must be valid
        :return: the piece
        """
        if not self.valid_coordinates(letter.upper(), number):
            raise ValueError('Invalid coordinates')
        return self.squares[Square(letter.upper(), number)]

    def valid_coordinates(self, letter, number):
        """Check if the given coordinates are valid in the board.
        
        :param letter: the column
        :param number: the row
        :return true if the given coordinates are valid.
        """
        return isinstance(letter, str) and len(letter) == 1 \
               and isinstance(number, int) and 0 < number <= self.height \
               and 0 <= ord(letter) - ord('A') < self.width

    def __str__(self):
        s = '  ' + ''.join([chr(x + ord('a')).upper() for x in range(0, self.width)]) + '\n'
        for number in range(0, self.width):
            s += str(number + 1) + '-'
            for letter in range(0, self.height):
                cur = self.get_piece(chr(letter + ord('a')).upper(), number + 1)
                if cur is None:
                    s += "."
                else:
                    s += cur.get_char()
            s += '\n'
        return s
