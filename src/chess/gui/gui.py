# -*- coding: utf-8 -*-
from chess.structure import *
from chess.computing import *
from tkinter import *
from PIL import ImageTk, Image
from .human_player import HumanPlayer


class GUI:
    """Manage a graphic game."""

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
        self.manager.setup_q_chess_board()

        window = Tk()
        window.title('Pychess')

        white_square_img = ImageTk.PhotoImage(Image.open("white_square_img.png"))
        black_square_img = ImageTk.PhotoImage(Image.open("black_square_img.png"))

        for number in range(0, self.board.height):
            for letter in range(0, self.board.width):
                if((number + letter) % 2 == 0):
                    Label(window, height=80, width=80,  image=white_square_img).grid(row=number, column=letter)
                else:
                    Label(window, height=80, width=80, image=black_square_img).grid(row=number, column=letter)


        window.mainloop()


        """
        
        self.players[self.current_color] = HumanPlayer(self.board, self.current_color)
        self.players[self.other_color()] = HumanPlayer(self.board, self.other_color())
        running = True

        
        while running:
            print(self.board)
            print("{0} player, it is your turn.".format('White' if self.current_color == 'w' else 'Black'))
            old, new = self.players[self.current_color].choose_move()
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
        print('Well done {0} player! Now you can execute your opponent and rape his wife.'.format('White' if self.current_color == 'w' else 'Black'))
        """
