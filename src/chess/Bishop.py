class Bishop(Piece):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Bishop ({}, {})".format(self.width, self.height)
