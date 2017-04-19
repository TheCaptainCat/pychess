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

    def get_char(self):
        """Get the character for a console representation.
        
        :return: a character
        """
        return self.char

    def __str__(self):
        return "{0} {1}".format(self.name, str(self.square))
