#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

from chess.console import Console
from chess.gui import GUI

print("Welcome to PyChess")
print("Select a version:", "1) Console", "2) Graphical", sep='\n')
inp = None
while inp != '1' and inp != '2':
    inp = input("Choice: ")
if inp == '1':
    c = Console()
    c.launch_game()
else:
    gui = GUI()
    gui.launch_game()
