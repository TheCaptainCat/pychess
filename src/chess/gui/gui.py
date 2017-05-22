# -*- coding: utf-8 -*-
from chess.structure import *
from chess.computing import *
from chess.pieces import *
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
        self.square_dimension = 80
        self.corners_img = []
        self.white_square_img = None
        self.black_square_img = None
        self.top_board_edge_img = None
        self.right_board_edge_img = None
        self.bottom_board_edge = None
        self.left_board_edge_img = None
        self.right_top_board_corner = None
        self.left_top_board_corner = None
        self.right_bottom_board_corner = None
        self.left_bottom_board_corner = None

    def switch_color(self):
        self.current_color = self.other_color()

    def other_color(self):
        return 'w' if self.current_color == 'b' else 'b'

    def launch_game(self):
        self.manager.setup_q_chess_board()

        self.window = Tk()
        self.window.title('Pychess')



        self.white_square_img = ImageTk.PhotoImage(Image.open("textures/white_square_img.png").resize((80, 80), Image.ANTIALIAS))
        self.black_square_img = ImageTk.PhotoImage(Image.open("textures/black_square_img.png").resize((80, 80), Image.ANTIALIAS))
        self.top_board_edge_img = ImageTk.PhotoImage(Image.open("textures/top_board_edge.png").resize((80, 80), Image.ANTIALIAS))
        self.right_board_edge_img = ImageTk.PhotoImage(Image.open("textures/right_board_edge.png").resize((80, 80), Image.ANTIALIAS))
        self.bottom_board_edge = ImageTk.PhotoImage(Image.open("textures/bottom_board_edge.png").resize((80, 80), Image.ANTIALIAS))
        self.left_board_edge_img = ImageTk.PhotoImage(Image.open("textures/left_board_edge.png").resize((80, 80), Image.ANTIALIAS))
        self.right_top_board_corner = ImageTk.PhotoImage(Image.open("textures/right_top_board_corner.png").resize((80, 80), Image.ANTIALIAS))
        self.left_top_board_corner = ImageTk.PhotoImage(Image.open("textures/left_top_board_corner.png").resize((80, 80), Image.ANTIALIAS))
        self.right_bottom_board_corner = ImageTk.PhotoImage(Image.open("textures/right_bottom_board_corner.png").resize((80, 80), Image.ANTIALIAS))
        self.left_bottom_board_corner = ImageTk.PhotoImage(Image.open("textures/left_bottom_board_corner.png").resize((80, 80), Image.ANTIALIAS))

        self.white_rook = ImageTk.PhotoImage(Image.open("textures/white_rook.png"))
        self.white_bishop = ImageTk.PhotoImage(Image.open("textures/white_bishop.png"))
        self.white_pawn = ImageTk.PhotoImage(Image.open("textures/white_pawn.png"))
        self.white_king = ImageTk.PhotoImage(Image.open("textures/white_king.png"))
        self.white_queen = ImageTk.PhotoImage(Image.open("textures/white_queen.png"))
        self.white_knight = ImageTk.PhotoImage(Image.open("textures/white_knight.png"))

        self.black_rook = ImageTk.PhotoImage(Image.open("textures/black_rook.png"))
        self.black_bishop = ImageTk.PhotoImage(Image.open("textures/black_bishop.png"))
        self.black_pawn = ImageTk.PhotoImage(Image.open("textures/black_pawn.png"))
        self.black_king = ImageTk.PhotoImage(Image.open("textures/black_king.png"))
        self.black_queen = ImageTk.PhotoImage(Image.open("textures/black_queen.png"))
        self.black_knight = ImageTk.PhotoImage(Image.open("textures/black_knight.png"))

        self.corners_img = [self.left_top_board_corner , self.right_top_board_corner,
                            self.left_bottom_board_corner, self.right_bottom_board_corner]

        self.pieces_img = [self.white_rook, self.white_bishop, self.white_pawn, self.white_king, self.white_queen,
                           self.white_knight, self.black_rook, self.black_bishop, self.black_pawn, self.black_king,
                           self.black_queen, self.black_knight]

        self.create_canvas()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.square_on_click)

        self.window.mainloop()

        """

        for number in range(0, self.board.height):
            for letter in range(0, self.board.width):
                cur = self.board.get_piece(letter, number)
                if cur is not None and isinstance(cur, Piece):
                    i = 0
                    if cur.color == 'b':
                        i = i + 6
                    if isinstance(cur, Bishop):
                        i = i + 1
                    elif isinstance(cur, Pawn):
                        i = i + 2
                    elif isinstance(cur, King):
                        i = i + 3
                    elif isinstance(cur, Queen):
                        i = i + 4
                    elif isinstance(cur, Knight):
                        i = i + 5

                    Label(self.window, height=piece_height, width=piece_width, image=pieces_img[i]).grid(row=number + 1, column=letter + 1)


        
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


    def create_canvas(self):
        canvas_width = (self.board.width + 2) * self.square_dimension
        canvas_height = (self.board.height + 2) * self.square_dimension
        self.canvas = Canvas(self.window, width=canvas_width, height=canvas_height)
        self.canvas.pack()

    def draw_board(self):
        i = 0

        for number in range(0, self.board.height + 2):
            for letter in range(0, self.board.width + 2):
                x1, y1 = self.get_x_y_coordinates(number, letter)
                if number in [0, self.board.height + 1] and letter in [0, self.board.width + 1]:
                    self.canvas.create_image(x1, y1, image=self.corners_img[i] , anchor='nw')
                    i = i + 1

                elif ((number in [0, self.board.height + 1] and letter in range(1, self.board.width + 1))
                      or (number in range(1, self.board.height + 1) and letter in [0, self.board.width + 1])):
                    if number == 0:
                        self.canvas.create_image(x1, y1, image=self.top_board_edge_img, anchor='nw')
                    elif number == self.board.height + 1:
                        self.canvas.create_image(x1, y1, image=self.bottom_board_edge, anchor='nw')
                    elif letter == 0:
                        self.canvas.create_image(x1, y1, image=self.left_board_edge_img, anchor='nw')
                    elif letter == self.board.width + 1:
                        self.canvas.create_image(x1, y1, image=self.right_board_edge_img, anchor='nw')

                elif ((number + letter) % 2 == 0):
                    self.canvas.create_image(x1, y1, image=self.white_square_img, anchor='nw')
                else:
                    self.canvas.create_image(x1, y1, image=self.black_square_img, anchor='nw')

    def get_x_y_coordinates(self, row, col):
        x = (col * self.square_dimension)
        y = (row * self.square_dimension)

        return (x, y)

    def square_on_click(self, event):
        x, y = self.get_clicked_square(event)
        print("Clicked square : ({}, {})".format(x, y))

    def get_clicked_square(self, event):
        x = event.x // self.square_dimension
        y = event.y // self.square_dimension

        return (x, y)