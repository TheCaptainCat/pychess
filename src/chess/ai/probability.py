# -*- coding: utf-8 -*-
import copy

from chess.computing import Manager


class Probability:
    """Contains a probability of move"""

    def __init__(self, board, depth, max_depth, color, current_color, squares=None):
        self.manager = Manager(board)
        self.board = board
        self.depth = depth
        self.max_depth = max_depth
        self.color = color
        self.current_color = current_color
        self.squares = squares
        self.score = 0
        self.other_score = 0
        self.children = set()

    def compute_score(self):
        if self.depth == self.max_depth:
            for p in self.board.get_pieces_by_color(self.color):
                self.score += Manager.get_piece_score(p)
            for p in self.board.get_pieces_by_color('w' if self.color == 'b' else 'b'):
                self.other_score += Manager.get_piece_score(p)
        else:
            for p in self.board.get_pieces_by_color(self.current_color):
                for m in self.manager.compute_move_set(p):
                    new_board = copy.deepcopy(self.board)
                    new_board.move_piece(p.square, m)
                    self.children.add(Probability(new_board, self.depth + 1, self.max_depth, self.color,
                                                  'w' if self.current_color == 'b' else 'b', (p.square, m)))
            self.score = float('infinity')
            for prob in self.children:
                self.score = min(self.score, prob.compute_score())
        return self.score

    def get_best_child(self):
        def get_score(prob):
            return prob.score - prob.other_score

        return max(self.children, key=get_score)

    def __repr__(self):
        return str(self.board)
