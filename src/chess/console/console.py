# -*- coding: utf-8 -*-
from chess.ai import AI
from chess.computing import *
from chess.structure import *


class Console:
    """Manage a text game."""

    def __init__(self):
        self.current_color = 'w'
        self.board = Board(8, 8)
        self.manager = Manager(self.board)
        self.players = {'w': None, 'b': None}

    def switch_color(self):
        self.current_color = self.other_color()

    def other_color(self):
        return 'w' if self.current_color == 'b' else 'b'

    def launch_game(self):
        self.manager.setup_chess_board()
        print("Welcome to PyChess!")
        self.players[self.current_color] = AI(self.board, self.current_color, 1)
        self.players[self.other_color()] = AI(self.board, self.other_color(), 3)
        running = True
        turn = 0
        while running:
            print(self.board)
            print("{0} player, it is your turn.".format('White' if self.current_color == 'w' else 'Black'))
            old, new = self.players[self.current_color].choose_move()
            turn += 0.5
            piece = self.board.get_piece(old.letter, old.number)
            if piece is None:
                print("First coordinates must designate a piece.")
                continue
            if piece.color != self.current_color:
                print("You must choose your color! Ya dumb fuck...")
                continue
            if new not in self.manager.compute_move_set(piece):
                print("RTFM!!!")
                continue
            self.board.move_piece(old, new)
            if self.manager.is_checkmate(self.other_color()):
                running = False
            else:
                self.switch_color()
        print(self.board)
        print('Well done {0} player, you won in {1} turns! Now you can execute your opponent and rape his wife.'
              .format('White' if self.current_color == 'w' else 'Black', turn))
