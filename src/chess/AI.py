class AI(Player):
    def __init__(self):
        pieces = [Rook(8, "a"), Bishop(8, "c"), King(8, "e"), Knight(8, "g"),
                       Pawn(7, "b"), Pawn(7, "d"), Pawn(7, "f"), Pawn(7, "h"),
                       Pawn(6, "a"), Pawn(6, "c"), Pawn(6, "e"), Pawn(6, "g")]
        Player.__init__("b", pieces)


    def __str__(self):
        return "AI ({}, {})".format(self.width, self.height)
