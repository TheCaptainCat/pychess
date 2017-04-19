class Square:
    """
    Represents a chess board square
    """
    def __init__(self, column, row):
        if (not isinstance(column, str)) or len(column) != 1:
            raise ValueError("Column must be a character")
        self.column = column
        if not isinstance(row, int):
            raise ValueError("Row must be an integer")
        self.row = row

    def __str__(self):
        return "({}, {})".format(self.column, self.row)

    def __eq__(self, other):
        return isinstance(other, Square) and self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash((self.column, self.row))
