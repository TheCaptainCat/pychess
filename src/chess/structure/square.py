class Square:
    """Represent a chess board square."""

    def __init__(self, letter, number):
        """Build a new chess board square.
        
        :param letter: the column of the square
        :param number: the row of the square
        :raises ValueError: the coordinates must be valid
        """
        if (not isinstance(letter, str)) or len(letter) != 1:
            raise ValueError("Column must be a character")
        self.letter = letter
        if not isinstance(number, int):
            raise ValueError("Row must be an integer")
        self.number = number

    def __str__(self):
        return "({}, {})".format(self.letter, self.number)

    def __eq__(self, other):
        return isinstance(other, Square) and self.number == other.number and self.letter == other.letter

    def __hash__(self):
        return hash((self.letter, self.number))
