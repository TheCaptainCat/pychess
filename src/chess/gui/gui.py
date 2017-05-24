# -*- coding: utf-8 -*-
from tkinter import *

from PIL import ImageTk, Image

from chess.computing import *
from chess.pieces import *
from chess.structure import *
from .human_player import HumanPlayer


class GUI():
    """Manage a graphic game."""

    def __init__(self):
        self.current_color = 'w'
        self.board = Board(8, 8)
        self.manager = Manager(self.board)
        self.players = {'w': None, 'b': None}
        self.window = None
        self.square_dimension = 80
        self.corners_img = []
        self.source_of_the_move = None
        self.textures = {}
        self.canvas = None

    def switch_color(self):
        self.current_color = self.other_color()

    def other_color(self):
        return 'w' if self.current_color == 'b' else 'b'

    def load_textures(self):
        self.textures['white_square_img'] = ImageTk.PhotoImage(
            Image.open("textures/white_square_img.png").resize((self.square_dimension, self.square_dimension),
                                                               Image.ANTIALIAS))
        self.textures['black_square_img'] = ImageTk.PhotoImage(
            Image.open("textures/black_square_img.png").resize((self.square_dimension, self.square_dimension),
                                                               Image.ANTIALIAS))
        self.textures['top_board_edge_img'] = ImageTk.PhotoImage(
            Image.open("textures/top_board_edge.png").resize((self.square_dimension, self.square_dimension),
                                                             Image.ANTIALIAS))
        self.textures['right_board_edge_img'] = ImageTk.PhotoImage(
            Image.open("textures/right_board_edge.png").resize((self.square_dimension, self.square_dimension),
                                                               Image.ANTIALIAS))
        self.textures['bottom_board_edge_img'] = ImageTk.PhotoImage(
            Image.open("textures/bottom_board_edge.png").resize((self.square_dimension, self.square_dimension),
                                                                Image.ANTIALIAS))
        self.textures['left_board_edge_img'] = ImageTk.PhotoImage(
            Image.open("textures/left_board_edge.png").resize((self.square_dimension, self.square_dimension),
                                                              Image.ANTIALIAS))
        self.textures['right_top_board_corner_img'] = ImageTk.PhotoImage(
            Image.open("textures/right_top_board_corner.png").resize((self.square_dimension, self.square_dimension),
                                                                     Image.ANTIALIAS))
        self.textures['left_top_board_corner_img'] = ImageTk.PhotoImage(
            Image.open("textures/left_top_board_corner.png").resize((self.square_dimension, self.square_dimension),
                                                                    Image.ANTIALIAS))
        self.textures['right_bottom_board_corner_img'] = ImageTk.PhotoImage(
            Image.open("textures/right_bottom_board_corner.png").resize((self.square_dimension, self.square_dimension),
                                                                        Image.ANTIALIAS))
        self.textures['left_bottom_board_corner_img'] = ImageTk.PhotoImage(
            Image.open("textures/left_bottom_board_corner.png").resize((self.square_dimension, self.square_dimension),
                                                                       Image.ANTIALIAS))
        self.textures['highlighted_black_square_img'] = ImageTk.PhotoImage(
            Image.open("textures/highlighted_black_square_img.png").resize(
                (self.square_dimension, self.square_dimension), Image.ANTIALIAS))
        self.textures['highlighted_white_square_img'] = ImageTk.PhotoImage(
            Image.open("textures/highlighted_white_square_img.png").resize(
                (self.square_dimension, self.square_dimension), Image.ANTIALIAS))
        self.textures['current_piece_black_square_img'] = ImageTk.PhotoImage(
            Image.open("textures/current_piece_black_square.png").resize((self.square_dimension, self.square_dimension),
                                                                         Image.ANTIALIAS))
        self.textures['current_piece_white_square_img'] = ImageTk.PhotoImage(
            Image.open("textures/current_piece_white_square.png").resize((self.square_dimension, self.square_dimension),
                                                                         Image.ANTIALIAS))
        self.textures['highlighted_black_square_with_piece_img'] = ImageTk.PhotoImage(
            Image.open("textures/highlighted_black_square_with_piece_img.png").resize(
                (self.square_dimension, self.square_dimension), Image.ANTIALIAS))
        self.textures['highlighted_white_square_with_piece_img'] = ImageTk.PhotoImage(
            Image.open("textures/highlighted_white_square_with_piece_img.png").resize(
                (self.square_dimension, self.square_dimension), Image.ANTIALIAS))
        for i in range(1, 9):
            self.textures['number_' + str(i) + '_img'] = ImageTk.PhotoImage(
                Image.open('textures/' + str(i) + '.png').resize((self.square_dimension, self.square_dimension),
                                                                 Image.ANTIALIAS))
            self.textures['letter_' + str(i) + '_img'] = ImageTk.PhotoImage(
                Image.open('textures/' + chr(i + ord('a') - 1) + '.png').resize(
                    (self.square_dimension, self.square_dimension), Image.ANTIALIAS))
        self.textures['white_rook'] = ImageTk.PhotoImage(Image.open("textures/white_rook.png"))
        self.textures['white_bishop'] = ImageTk.PhotoImage(Image.open("textures/white_bishop.png"))
        self.textures['white_pawn'] = ImageTk.PhotoImage(Image.open("textures/white_pawn.png"))
        self.textures['white_king'] = ImageTk.PhotoImage(Image.open("textures/white_king.png"))
        self.textures['white_queen'] = ImageTk.PhotoImage(Image.open("textures/white_queen.png"))
        self.textures['white_knight'] = ImageTk.PhotoImage(Image.open("textures/white_knight.png"))
        self.textures['black_rook'] = ImageTk.PhotoImage(Image.open("textures/black_rook.png"))
        self.textures['black_bishop'] = ImageTk.PhotoImage(Image.open("textures/black_bishop.png"))
        self.textures['black_pawn'] = ImageTk.PhotoImage(Image.open("textures/black_pawn.png"))
        self.textures['black_king'] = ImageTk.PhotoImage(Image.open("textures/black_king.png"))
        self.textures['black_queen'] = ImageTk.PhotoImage(Image.open("textures/black_queen.png"))
        self.textures['black_knight'] = ImageTk.PhotoImage(Image.open("textures/black_knight.png"))
        self.corners_img = [self.textures['left_bottom_board_corner_img'],
                            self.textures['right_bottom_board_corner_img'],
                            self.textures['left_top_board_corner_img'], self.textures['right_top_board_corner_img']]

    def launch_game(self):
        self.manager.setup_q_chess_board()
        self.window = Tk()
        self.window.title('PyChess')
        self.load_textures()
        self.create_canvas()
        self.draw_board()
        self.draw_pieces()
        self.canvas.bind("<Button-1>", self.square_on_click)
        self.players[self.current_color] = HumanPlayer(self.board, self.current_color)
        self.players[self.other_color()] = HumanPlayer(self.board, self.other_color())
        self.window.mainloop()

    def create_canvas(self):
        canvas_width = (self.board.width + 2) * self.square_dimension
        canvas_height = (self.board.height + 2) * self.square_dimension
        self.canvas = Canvas(self.window, width=canvas_width, height=canvas_height)
        self.canvas.pack()

    def draw_board(self):
        i = j = k = l = m = 0
        for number in range(0, self.board.height + 2):
            for letter in range(0, self.board.width + 2):
                x, y = self.get_x_y_coordinates(number, letter)
                current_square = Square.canvas_to_square(letter - 1, number - 1)
                if self.source_of_the_move:
                    moves = self.manager.compute_move_set(self.source_of_the_move)
                    eatable_pieces, reachable_squares = \
                        self.manager.split_eatable_pieces_and_reachable_squares(moves, self.current_color)
                if number in [0, self.board.height + 1] and letter in [0, self.board.width + 1]:
                    self.canvas.create_image(x, y, image=self.corners_img[i], anchor='nw')
                    i = i + 1
                elif ((number in [0, self.board.height + 1] and letter in range(1, self.board.width + 1))
                      or (number in range(1, self.board.height + 1) and letter in [0, self.board.width + 1])):
                    if number == 0:
                        self.canvas.create_image(x, y, image=self.textures['bottom_board_edge_img'], anchor='nw')
                        self.canvas.create_image(x, y, image=self.textures['letter_' + str(j + 1) + '_img'],
                                                 anchor='nw')
                        j = j + 1
                    elif number == self.board.height + 1:
                        self.canvas.create_image(x, y, image=self.textures['top_board_edge_img'], anchor='nw')
                        self.canvas.create_image(x, y, image=self.textures['letter_' + str(k + 1) + '_img'],
                                                 anchor='nw')
                        k = k + 1
                    elif letter == 0:
                        self.canvas.create_image(x, y, image=self.textures['left_board_edge_img'], anchor='nw')
                        self.canvas.create_image(x, y, image=self.textures['number_' + str(l + 1) + '_img'],
                                                 anchor='nw')
                        l = l + 1
                    elif letter == self.board.width + 1:
                        self.canvas.create_image(x, y, image=self.textures['right_board_edge_img'], anchor='nw')
                        self.canvas.create_image(x, y, image=self.textures['number_' + str(m + 1) + '_img'],
                                                 anchor='nw')
                        m = m + 1
                elif (number + letter) % 2 == 0:
                    if self.source_of_the_move:
                        if current_square in reachable_squares:
                            self.canvas.create_image(x, y, image=self.textures['highlighted_white_square_img'],
                                                     anchor='nw')
                        elif current_square in eatable_pieces:
                            self.canvas.create_image(x, y,
                                                     image=self.textures['highlighted_white_square_with_piece_img'],
                                                     anchor='nw')
                        elif current_square == self.source_of_the_move.square:
                            self.canvas.create_image(x, y, image=self.textures['current_piece_white_square_img'],
                                                     anchor='nw')
                        else:
                            self.canvas.create_image(x, y, image=self.textures['white_square_img'], anchor='nw')
                    else:
                        self.canvas.create_image(x, y, image=self.textures['white_square_img'], anchor='nw')
                else:
                    if self.source_of_the_move:
                        if current_square in reachable_squares:
                            self.canvas.create_image(x, y, image=self.textures['highlighted_black_square_img'],
                                                     anchor='nw')
                        elif current_square in eatable_pieces:
                            self.canvas.create_image(x, y,
                                                     image=self.textures['highlighted_black_square_with_piece_img'],
                                                     anchor='nw')
                        elif current_square == self.source_of_the_move.square:
                            self.canvas.create_image(x, y, image=self.textures['current_piece_black_square_img'],
                                                     anchor='nw')
                        else:
                            self.canvas.create_image(x, y, image=self.textures['black_square_img'], anchor='nw')
                    else:
                        self.canvas.create_image(x, y, image=self.textures['black_square_img'], anchor='nw')

    def get_x_y_coordinates(self, row, col):
        x = (col * self.square_dimension)
        y = (((self.board.height + 1) - row) * self.square_dimension)
        return x, y

    def square_on_click(self, event):
        x, y = self.get_clicked_square(event)
        current_piece = self.board.get_piece(x - 1, y - 1)
        current_square = Square.canvas_to_square(x - 1, y - 1)
        if self.source_of_the_move:
            if isinstance(current_piece, Piece) and self.source_of_the_move.color == current_piece.color:
                self.source_of_the_move = current_piece
            elif self.validate_move(self.source_of_the_move, current_square):
                self.board.move_piece(self.source_of_the_move.square, current_square)
                self.source_of_the_move = None
                if self.manager.is_checkmate(self.other_color()):
                    print("You lose!")
                else:
                    self.switch_color()
            else:
                self.source_of_the_move = None
        elif self.validate_source(current_piece):
            self.source_of_the_move = current_piece
        self.clear_canvas()
        self.draw_board()
        self.draw_pieces()

    def get_clicked_square(self, event):
        x = event.x // self.square_dimension
        y = (self.board.height + 1) - event.y // self.square_dimension
        return x, y

    def draw_pieces(self):
        for number in range(0, self.board.height):
            for letter in range(0, self.board.width):
                cur = self.board.get_piece(self.board.width - 1 - letter, self.board.height - 1 - number)
                if cur is not None and isinstance(cur, Piece):
                    name = 'white_' if cur.color == 'w' else 'black_'
                    if isinstance(cur, Bishop):
                        name += 'bishop'
                    elif isinstance(cur, Pawn):
                        name += 'pawn'
                    elif isinstance(cur, King):
                        name += 'king'
                    elif isinstance(cur, Queen):
                        name += 'queen'
                    elif isinstance(cur, Knight):
                        name += 'knight'
                    elif isinstance(cur, Rook):
                        name += 'rook'
                    x, y = self.get_x_y_coordinates(self.board.height - number, self.board.width - letter)
                    self.canvas.create_image(x + 40, y + 30, image=self.textures[name], anchor='center')

    def validate_move(self, old, new):
        is_valid = True
        _piece = self.board.get_piece(old.square.letter, old.square.number)
        if not self.validate_source(_piece):
            is_valid = False
        elif new not in self.manager.compute_move_set(_piece):
            print("RTFM!!!")
            is_valid = False
        elif not self.board.valid_coordinates(old.square.letter, old.square.number) \
                or not self.board.valid_coordinates(new.letter, new.number):
            print("Invalid coordinates.")
            is_valid = False
        return is_valid

    def validate_source(self, _piece):
        is_valid = True
        if _piece is None:
            print("First coordinates must designate a piece.")
            is_valid = False
        elif _piece.color != self.current_color:
            print("You must choose your color! Ya dumb fuck...")
            is_valid = False
        return is_valid

    def clear_canvas(self):
        self.canvas.delete("all")
