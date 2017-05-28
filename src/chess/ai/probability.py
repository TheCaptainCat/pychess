# -*- coding: utf-8 -*-
from chess.computing import Manager
from chess.pieces import Pawn


class Probability:
    """Contains a probability of move"""

    def __init__(self, board, depth, color, current_color, squares=None):
        """Create a new Probability.
        
        :param board: the chess board
        :param depth: the current depth of the probability, made to decrease through computing
        :param color: the color of the AI
        :param current_color: the color of the player in the current state
        :param squares: the tuple containing the origin and the destination of the computed move
        """
        self.manager = Manager(board)
        self.board = board
        self.depth = depth
        self.color = color
        self.current_color = current_color
        self.squares = squares
        self.score = 0
        self.children = set()

    def compute_heuristic(self):
        """Compute the score when a probability is a leaf.
        
        :return: the computed score.
        """
        score = 0
        for p in self.board.get_pieces_by_color(self.color):
            score += Manager.get_piece_score(p)
        for p in self.board.get_pieces_by_color('w' if self.color == 'b' else 'b'):
            score -= Manager.get_piece_score(p)
        return score

    def compute_score(self, alpha=-float('infinity'), beta=float('infinity')):
        """Compute the probabilities using the minimax algorithm, with alpha beta pruning.
        When the probability is a leaf, it computes the score.
        When the probability has children, it chooses the min or max branch.
        
        :param alpha: the alpha parameter
        :param beta: the beta parameter
        :return: the computed score
        """
        if self.depth == 0:  # When the probability is a leaf.
            self.score = self.compute_heuristic()
        else:  # When the maximum depth is not reached yet.
            # For each playing piece, for each move alternative, a possibility is created.
            if self.color == self.current_color:
                self.score = -float('infinity')
                fun = max
            else:
                self.score = float('infinity')
                fun = min
            for p in self.board.get_pieces_by_color(self.current_color):
                for m in self.manager.compute_move_set(p):
                    saved_piece = self.board.get_piece(m.letter, m.number)
                    old_p_position = p.square
                    old_pawn_state = None
                    if isinstance(p, Pawn):
                        old_pawn_state = p.first_move_done
                    self.board.move_piece(p.square, m)
                    prob = Probability(self.board, self.depth - 1, self.color,
                                       'w' if self.current_color == 'b' else 'b', (old_p_position, m))
                    self.score = fun(self.score, prob.compute_score(alpha, beta))
                    self.board.move_piece(p.square, old_p_position)
                    self.board.set_piece(m.letter, m.number, saved_piece)
                    if isinstance(p, Pawn):
                        p.first_move_done = old_pawn_state
                    self.children.add(prob)
                    if self.color == self.current_color:
                        if self.score >= beta:
                            return self.score
                        else:
                            alpha = max(alpha, self.score)
                    if self.color != self.current_color:
                        if alpha >= self.score:
                            return self.score
                        else:
                            beta = min(beta, self.score)
        return self.score

    def get_best_child(self):
        """Get the best possibility for the next move."""

        def get_score(prob):
            return prob.score

        return max(self.children, key=get_score)

    def __repr__(self):
        return str(self.board)
