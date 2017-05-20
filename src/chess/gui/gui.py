# -*- coding: utf-8 -*-
from chess.structure import *
from chess.computing import *
from tkinter import *
from PIL import ImageTk, Image
from .human_player import HumanPlayer


class GUI():
    """Manage a graphic game."""

    def __init__(self):
        self.current_color = 'w'
        self.board = Board(8, 8)
        self.manager = Manager(self.board)
        self.players = {'w': None, 'b': None}
        self.window = None

    def switch_color(self):
        self.current_color = self.other_color()

    def other_color(self):
        return 'w' if self.current_color == 'b' else 'b'

    def launch_game(self):
        self.manager.setup_q_chess_board()

        self.window = Tk()
        self.window.title('Pychess')

        white_square_img = ImageTk.PhotoImage(Image.open("white_square_img.png"))
        black_square_img = ImageTk.PhotoImage(Image.open("black_square_img.png"))
        top_board_edge_img = ImageTk.PhotoImage(Image.open("top_board_edge.png"))
        right_board_edge_img = ImageTk.PhotoImage(Image.open("right_board_edge.png"))
        bottom_board_edge = ImageTk.PhotoImage(Image.open("bottom_board_edge.png"))
        left_board_edge_img = ImageTk.PhotoImage(Image.open("left_board_edge.png"))
        right_top_board_corner = ImageTk.PhotoImage(Image.open("right_top_board_corner.png"))
        left_top_board_corner = ImageTk.PhotoImage(Image.open("left_top_board_corner.png"))
        right_bottom_board_corner = ImageTk.PhotoImage(Image.open("right_bottom_board_corner.png"))
        left_bottom_board_corner = ImageTk.PhotoImage(Image.open("left_bottom_board_corner.png"))

        corners_img = [left_top_board_corner, right_top_board_corner, left_bottom_board_corner,
                       right_bottom_board_corner]
        i = 0
        image_size = 80

        for number in range(0, self.board.height + 2):
            for letter in range(0, self.board.width + 2):

                if number in [0, self.board.height + 1] and letter in [0, self.board.width + 1]:
                    Label(self.window, height=image_size, width=image_size, image=corners_img[i]).grid(row=number,
                                                                                                       column=letter)
                    i = i + 1

                elif ((number in [0, self.board.height + 1] and letter in range(1, self.board.width + 1))
                      or ((number in range(1, self.board.height + 1) and letter in [0, self.board.width + 1]))):
                    if number == 0:
                        Label(self.window, height=image_size, width=image_size, image=top_board_edge_img).grid(
                            row=number,
                            column=letter)
                    elif number == self.board.height + 1:
                        Label(self.window, height=image_size, width=image_size, image=bottom_board_edge).grid(
                            row=number,
                            column=letter)
                    elif letter == 0:
                        Label(self.window, height=image_size, width=image_size, image=left_board_edge_img).grid(
                            row=number,
                            column=letter)
                    elif letter == self.board.width + 1:
                        Label(self.window, height=image_size, width=image_size, image=right_board_edge_img).grid(
                            row=number,
                            column=letter)

                elif ((number + letter) % 2 == 0):
                    Label(self.window, height=image_size, width=image_size, image=white_square_img).grid(row=number,
                                                                                                         column=letter)
                else:
                    Label(self.window, height=image_size, width=image_size, image=black_square_img).grid(row=number,
                                                                                                         column=letter)


        for number in range(0, self.board.height):
            for letter in range(0, self.board.width):
                cur = self.board.get_piece(letter, number)
                if cur is not None:
                    Label(self.window, text=cur).grid(row=number + 1, column=letter + 1)





        self.window.mainloop()



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

    def generateBoard(self):
        pass
    def printPieces(self):
        Label(self.window, text="Salut les Zér0s !").grid(row=2,column=2)
