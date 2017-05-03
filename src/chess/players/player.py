# -*- coding: utf-8 -*-
class Player:
    """Represent a player entity, either a human or AI"""

    def __init__(self, board, color):
        self.color = color
        self.board = board

    def choose_move(self):
        pass
