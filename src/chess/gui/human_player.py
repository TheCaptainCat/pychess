# -*- coding: utf-8 -*-
from chess.players import Player
from chess.structure import Square


class HumanPlayer(Player):

    def __init__(self, board, color):
        Player.__init__(self, board, color)

