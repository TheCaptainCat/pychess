#! /usr/bin/python3.5
# -*- coding: utf-8 -*-
import pygame

from chess.computing import *
from chess.pieces import *
from chess.structure import *




b = Board(8, 8)

# White
Rook(Square(7, 0), 'w').add_to_board(b)
Knight(Square(1, 0), 'w').add_to_board(b)
King(Square(3, 0), 'w').add_to_board(b)
Bishop(Square(5, 0), 'w').add_to_board(b)
for i in range(0, 8):
    if i % 2 == 0:
        Pawn(Square(i, 1), 'w').add_to_board(b)
    else:
        Pawn(Square(i, 2), 'w').add_to_board(b)

# Black
Rook(Square(0, 7), 'b').add_to_board(b)
Knight(Square(6, 7), 'b').add_to_board(b)
King(Square(4, 7), 'b').add_to_board(b)
Bishop(Square(2, 7), 'b').add_to_board(b)
for i in range(0, 8):
    if i % 2 != 0:
        Pawn(Square(i, 6), 'b').add_to_board(b)
    else:
        Pawn(Square(i, 5), 'b').add_to_board(b)

print(b)

m = Manager(b)
print(m.compute_move_set(b.get_piece(2, 3)))

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((640,480))
fond = pygame.image.load("background.jpg")

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Boucle infinie
while continuer:
	continue #Je place continue ici pour pouvoir relancer la boucle infinie
                 #mais il est d'habitude remplacé par une suite d'instructions

