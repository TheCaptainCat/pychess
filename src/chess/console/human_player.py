# -*- coding: utf-8 -*-
from chess.players import Player
from chess.structure import Square


class HumanPlayer(Player):

    def __init__(self, board, color):
        Player.__init__(self, board, color)

    def choose_move(self):
        ok = False
        old = None
        new = None
        while not ok:
            print("Enter coordinates: e.g. A1 B2")
            try:
                i = raw_input()
                old = Square.str_to_square(i.split(" ")[0])
                new = Square.str_to_square(i.split(" ")[1])
            except:
                print("Please enter valid coordinates! You foolish mortal.")
                continue
            if self.board.valid_coordinates(old.letter, old.number) \
                    and self.board.valid_coordinates(new.letter, new.number):
                ok = True
            else:
                print("Please enter valid coordinates!")
        return old, new
