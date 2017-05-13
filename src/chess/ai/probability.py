# -*- coding: utf-8 -*-
from chess.computing import Manager


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

    def compute_score(self):
        """Compute the probabilities using the minimax algorithm.
        If the probability is a leaf, the heuristic is computed.
            If the AI is playing, it returns the opponent's score.
            It returns the AI score otherwise.
        If the probability is not at maximum depth, it creates its children.
            If the AI is playing, it minimises the opponent score to focus on eating pieces.
            If not, it maximises the AI's score to focus on saving its own pieces. 
        
        :return: the computed score
        """
        if self.depth == 0:  # When the probability is a leaf.
            if self.color == self.current_color:
                # If the AI is playing, the current score is the opponent's score.
                for p in self.board.get_pieces_by_color('w' if self.color == 'b' else 'b'):
                    self.score += Manager.get_piece_score(p)
            else:
                # If the opponent is playing, the current score is the AI's score.
                for p in self.board.get_pieces_by_color(self.color):
                    self.score += Manager.get_piece_score(p)
        else:  # When the maximum depth is not reached yet.
            # For each playing piece, for each move alternative, a possibility is created.
            if self.color == self.current_color:
                self.score = float('infinity')
                fun = min
            else:
                self.score = -float('infinity')
                fun = max
            for p in self.board.get_pieces_by_color(self.current_color):
                for m in self.manager.compute_move_set(p):
                    saved_piece = self.board.get_piece(m.letter, m.number)
                    old_p_position = p.square
                    self.board.move_piece(p.square, m)
                    prob = Probability(self.board, self.depth - 1, self.color,
                                       'w' if self.current_color == 'b' else 'b', (old_p_position, m))
                    self.score = fun(self.score, prob.compute_score())
                    self.board.move_piece(p.square, old_p_position)
                    self.board.set_piece(m.letter, m.number, saved_piece)
                    self.children.add(prob)
        return self.score

    def get_best_child(self):
        """Get the best possibility for the next move.
        If the AI is playing, it returns the the possibility with the minimum opponent's score.
        It not, it returns the the possibility with the maximum AI's score.
        
        :return: the best possibility
        """
        def get_score(prob):
            return prob.score

        if self.color == self.current_color:
            # If the AI is playing, the best possibility is the one with the minimum opponent's score.
            return min(self.children, key=get_score)
        else:
            # If the opponent is playing, the best possibility is the one with the maximum AI's score.
            return max(self.children, key=get_score)

    def __repr__(self):
        return str(self.board)
