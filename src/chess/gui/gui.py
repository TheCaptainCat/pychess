# -*- coding: utf-8 -*-
from tkinter import *

from PIL import ImageTk, Image

from chess.ai import AI
from chess.computing import *
from chess.pieces import *
from chess.structure import *
from .human_player import HumanPlayer


class GUI:
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
        self.game_over = False

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
        self.textures['table'] = ImageTk.PhotoImage(Image.open("textures/table.jpg"))
        self.textures['grey_square'] = ImageTk.PhotoImage(Image.open("textures/grey_square.png"))
        self.textures['restart_button'] = ImageTk.PhotoImage(Image.open("textures/restart_button.png"))
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
        self.players[self.other_color()] = AI(self.board, self.other_color(), 2)
        self.draw_eaten_pieces()
        self.draw_right_area()
        self.window.mainloop()

    def create_canvas(self):
        self.canvas_width = (self.board.width + 2) * self.square_dimension * 2
        self.canvas_height = (self.board.height + 2) * self.square_dimension
        self.canvas = Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def draw_board(self):
        self.canvas.create_image(0, 0, image=self.textures['table'], anchor='nw')
        i = j = k = l = m = 0
        for number in range(0, self.board.height + 2):
            for letter in range(0, self.board.width + 2):
                x, y = self.get_x_y_coordinates(number, letter + 5)
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
        if isinstance(self.players[self.current_color], AI):
            moves = self.players[self.current_color].choose_move()
            self.board.move_piece(moves[0], moves[1])
            self.switch_color()
        else:
            if not self.game_over:
                x, y = self.get_clicked_square(event)
                current_piece = self.board.get_piece(x - 1 - 5, y - 1)
                current_square = Square.canvas_to_square(x - 1 - 5, y - 1)
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
            self.draw_eaten_pieces()
            self.draw_right_area()

            if self.board.get_first_piece(King, 'b') == None or self.manager.is_checkmate('b'):
                self.display_game_over("Le joueur noir a perdu")
            elif self.board.get_first_piece(King, 'w') == None or self.manager.is_checkmate('w'):
                self.display_game_over("Le joueur blanc a perdu")

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
                    x, y = self.get_x_y_coordinates(self.board.height - number, self.board.width - letter + 5)
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

    def draw_right_area(self):
        restart_button = Button(self.window, text="Recommencer", command=self.restart)
        restart_button.configure( activebackground="#33B5E5", relief=FLAT, image=self.textures['restart_button'])
        self.canvas.create_window(self.canvas_width * 0.875 , self.canvas_height * 0.75, window=restart_button,)

    def draw_eaten_pieces(self):
        xb = xw = 1
        yb = 8
        yw = 4

        for piece in self.board.eaten_pieces:
            if piece is not None and isinstance(piece, Piece):
                name = 'white_' if piece.color == 'w' else 'black_'
                if isinstance(piece, Bishop):
                    name += 'bishop'
                elif isinstance(piece, Pawn):
                    name += 'pawn'
                elif isinstance(piece, King):
                    name += 'king'
                elif isinstance(piece, Queen):
                    name += 'queen'
                elif isinstance(piece, Knight):
                    name += 'knight'
                elif isinstance(piece, Rook):
                    name += 'rook'

                if piece.color == 'b':
                    x, y = self.get_x_y_coordinates(yb, xb)
                    if xb == 4:
                        xb = 1
                        yb = yb - 1
                    else:
                        xb = xb + 1
                else:
                    x, y = self.get_x_y_coordinates(yw, xw)
                    if xw == 4:
                        xw = 1
                        yw = yw - 1
                    else:
                        xw = xw + 1
                self.canvas.create_image(x, y, image=self.textures[name], anchor='center')

    def display_game_over(self, text):
        x_canvas = self.canvas_width / 2
        y_canvas = self.canvas_height / 2
        self.game_over = True

        for number in range(0, self.board.height + 2):
            for letter in range(0, self.board.width + 2):
                x, y = self.get_x_y_coordinates(number, letter + 5)
                self.canvas.create_image(x, y, image=self.textures['grey_square'], anchor='nw')
        self.canvas.create_text(x_canvas, y_canvas, text=text, fill="black", font=('Calibri', -80, 'bold'))

    def restart(self):
        self.clear_canvas()
        self.current_color = 'w'
        self.board = Board(8, 8)
        self.manager = Manager(self.board)
        self.manager.setup_q_chess_board()
        self.source_of_the_move = None
        self.game_over = False
        self.draw_board()
        self.draw_pieces()
        print("Restart")
        self.draw_eaten_pieces()
        self.draw_right_area()