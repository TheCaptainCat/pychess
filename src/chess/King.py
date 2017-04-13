class King(Piece):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "King ({}, {})".format(self.width, self.height)
