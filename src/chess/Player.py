class Player:
    def __init__(self, color, pieces):
        self.color = color
        self.pieces = pieces



    def __str__(self):
        return "Player ({}, {})".format(self.color)
