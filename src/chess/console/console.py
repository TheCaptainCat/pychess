# -*- coding: utf-8 -*-
from chess.structure import *
from chess.computing import *


class Console:
    """Manage a text game."""

    def __init__(self):
        self.current_color = 'w'
        self.board = Board(8, 8)
        self.manager = Manager(self.board)

    def switch_color(self):
        self.current_color = 'w' if self.current_color == 'b' else 'b'

    def launch_game(self):
        self.manager.setup_q_chess_board()
        print("Welcome to PyChess!")
        running = True
        while running:
            print(self.board)
            print(self.current_color)
            print("Enter coordinates: e.g. A1 B2")
            i = input()
            c1 = i.split(" ")[0]
            c2 = i.split(" ")[1]
            print(c1, c2)
