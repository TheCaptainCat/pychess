class Square:
    """Represent a chess board square."""

    def __init__(self, letter, number):
        """Build a new chess board square.
        
        :param letter: the column of the square
        :param number: the row of the square
        :raises ValueError: the coordinates must be valid
        """
        if not isinstance(letter, int):
            raise ValueError("Column must be an integer")
        self.letter = letter
        if not isinstance(number, int):
            raise ValueError("Row must be an integer")
        self.number = number

    def __str__(self):
        return "({}, {})".format(Square.int_to_letter(self.letter), self.number)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, Square) and self.number == other.number and self.letter == other.letter

    def __hash__(self):
        return hash((self.letter, self.number))

    @staticmethod
    def int_to_letter(i):
        return chr(i + ord('A'))

    @staticmethod
    def letter_to_int(l):
        return ord(l) - ord('A')
