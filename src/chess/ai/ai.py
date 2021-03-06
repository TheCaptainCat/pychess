# -*- coding: utf-8 -*-
from chess.players import Player
from .probability import Probability


class AI(Player):
    """Manage the AI of the game"""

    def __init__(self, board, color, depth):
        Player.__init__(self, board, color)
        self.depth = depth

    def choose_move(self):
        p = Probability(self.board, self.depth, self.color, self.color)
        p.compute_score()
        sq = p.get_best_child().squares
        print("{0}->{1}".format(sq[0], sq[1]))
        return sq
