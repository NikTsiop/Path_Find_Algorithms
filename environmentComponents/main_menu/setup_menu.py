import tkinter as tk
from tkinter import *

class SetupDropDown:
    
    def __init__(self, root: Tk, menubar: tk.Menu) -> None:
        self.root = root
        self.menu = menubar
    
    def create_dropdown(self, startPoint, goalPoint, obstaclesPoints):
        '''Setting up menu'''
        
        create_maze_menu = tk.Menu(self.menu, tearoff=False)
        create_maze_menu.add_command(
            label= 'Set Start Point',
            accelerator= 'Ctrl+S',
            command= startPoint
        )
        create_maze_menu.add_command(
            label='Set Goal point',
            accelerator='Ctrl+G',
            command = goalPoint
        )
        create_maze_menu.add_command(
            label='Set Obstacles',
            accelerator='Ctrl+O',
            command = obstaclesPoints
        )
        
        #bind the CTRL+S shorcut to the `startPoint()` function
        self.root.bind_all("<Control-s>", startPoint)
        self.root.bind_all("<Control-S>", startPoint)
        #bind the CTRL+G shorcut to the `goalPoint()` function
        self.root.bind_all("<Control-g>", goalPoint)
        self.root.bind_all("<Control-G>", goalPoint)
        #bind the CTRL+O shorcut to the `obstaclesPoints()` function
        self.root.bind_all("<Control-o>", obstaclesPoints)
        self.root.bind_all("<Control-O>", obstaclesPoints)
        
        self.menu.add_cascade(menu=create_maze_menu, label='Create Maze')
        self.root.config(menu=self.menu)