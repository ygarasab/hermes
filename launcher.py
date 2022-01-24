from tkinter import *
from table import Table
from board import Board
from snake import Snake
from random import randint
from algorithms import *
from node import Node

class Launcher:

    def __init__(self,side):

        self.side = side

        self.window = Tk()
        self.window.geometry("%sx%s"%(side+200,side))




        side = self.side

        self.speed = 50


        self.table = Table(self.window, 300, side, side)

        self.board = Board(self)


        self.onscreen = [self.table.canvas, self.board.frame]

        self.nvl = 1

        self.window.mainloop()









l = Launcher(700)
