class Human(Player):
    def __init__(self):
        pieces = [Rook(1,"a"),Bishop(1,"c"), King(1,"e"), Knight(1,"g"),
                       Pawn(2,"b"), Pawn(2,"d"), Pawn(2,"f"), Pawn(2,"h"),
                       Pawn(3, "a"), Pawn(3,"c"), Pawn(3,"e"),Pawn(3,"g")]
        Player.__init__("w", pieces)

    def __str__(self):
        return "Human ({}, {})".format(self.width, self.height)
