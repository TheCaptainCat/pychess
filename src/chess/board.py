class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Board ({}, {})".format(self.width, self.height)
