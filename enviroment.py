from tkinter import *
import tkinter as tk
from enum import Enum
import random

class TileType:
    TILE = 0
    START = 1
    TARGET = 2
    OBSTACLE = 3

class Tile:
    def __init__(self, point_type: TileType, widget: tk.Frame) -> None:
        self.type: TileType = point_type
        self.widget: tk.Frame = widget
        self.isSetted = False
        self.point = (-1, -1)

class Maze:
    def __init__(self, rows: int, cols: int, name, start_color, step_color, tile_color, target_color, obstacle_color):
        self.root = Tk()
        self.name = name
        self.start_isSetted = False
        self.target_isSetted = False
        self.start_point = (-1, -1)
        self.target_point = (-1, -1)
        self.start_color = start_color
        self.step_color = step_color
        self.tile_color = tile_color
        self.target_color = target_color
        self.obstacle_color = obstacle_color
        self.start_point_clicked = False
        self.goal_point_clicked = False
        self.obstacle_clicked = False
        self.grid_rows = rows
        self.grid_cols = cols
        self.tile_width = 50
        self.tile_height = 50
        self.window_width = int((self.grid_rows*self.tile_width))
        self.window_height = int((self.grid_cols*self.tile_height))
        self.root.title(self.name)
        self.root.geometry(f'{self.window_width}x{self.window_height}')
        
        self.create_menu()
        
    def create_menu(self):
        #setup menu
        menubar = tk.Menu()
        maze_menu = tk.Menu(menubar, tearoff=False)
        maze_menu.add_command(
            label= 'Set Start Point',
            accelerator= 'Ctrl+S',
            command= self.startPoint
        )
        maze_menu.add_command(
            label='Set Goal point',
            accelerator='Ctrl+G',
            command = self.goalPoint
        )
        maze_menu.add_command(
            label='Set Obstacles',
            accelerator='Ctrl+O',
            command = self.obstaclesPoints
        )
        menubar.add_cascade(menu=maze_menu, label='Maze')
        self.root.config(menu=menubar)
        
        #bind the CTRL+S shorcut to the `startPoint()` function
        self.root.bind_all("<Control-s>", self.startPoint)
        self.root.bind_all("<Control-S>", self.startPoint)
        #bind the CTRL+G shorcut to the `goalPoint()` function
        self.root.bind_all("<Control-g>", self.goalPoint)
        self.root.bind_all("<Control-G>", self.goalPoint)
        #bind the CTRL+O shorcut to the `obstaclesPoints()` function
        self.root.bind_all("<Control-o>", self.obstaclesPoints)
        self.root.bind_all("<Control-O>", self.obstaclesPoints)
    
    def startPoint(self):
        self.start_point_clicked = True
    
    def goalPoint(self):
        self.goal_point_clicked = True
    
    def obstaclesPoints(self):
        self.obstacle_clicked = True
    
    def create_grid(self):
        '''Configure the maze grid'''
        self.tiles: list[list[Tile]] = [[None for _ in range(self.grid_rows)] for _ in range(self.grid_cols)]
        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                tile = tk.Frame(self.root, width=self.tile_width, height=self.tile_height, bg=self.tile_color)
                tile.bind("<ButtonPress-1>", lambda event, x = row, y = col : self.on_frame_clicked(event, x, y))
                tile.bind("<ButtonPress-3>", lambda event, x = row, y = col : self.on_frame_clicked(event, x, y))
                tile.config(bd=1, relief='raised')
                tile.grid(row=row, column=col)
                tile_obj = Tile(TileType.TILE, tile)
                tile_obj.point = (row, col)
                self.tiles[row][col] = tile_obj
    
    def on_frame_clicked(self, event, x, y):
        if event.num == 1 :
            if self.start_point_clicked and not self.start_isSetted:
                self.set_point(x, y, TileType.START, self.start_color)
            elif self.goal_point_clicked and not self.target_isSetted:
                self.set_point(x, y, TileType.TARGET, self.target_color)
            elif self.obstacle_clicked:
                self.set_point(x, y, TileType.OBSTACLE, self.obstacle_color)
        elif event.num == 3:
            self.remove_point(x, y)
            
    def remove_point(self, x: int, y: int):
        '''Remove the start point'''
        point = self.tiles[x][y]
        if point.type == TileType.START:
            self.start_isSetted = False
            self.start_point = (-1,-1)
        elif point.type == TileType.TARGET:
            self.target_isSetted = False
            self.target_point = (-1,-1)  
        self.tiles[x][y].widget.configure(bg=self.tile_color)
        self.tiles[x][y].type = TileType.TILE 
        
    def set_point(self, x: int, y: int, type_point: TileType, color: str):
        '''Set point of interest for the maze'''
        self.tiles[x][y].widget.configure(bg=color)
        if type_point == TileType.START:
            self.start_isSetted = True
            self.start_point = self.tiles[x][y].point
        elif type_point == TileType.TARGET:
            self.target_isSetted = True
            self.target_point = self.tiles[x][y].point

    def set_obstacles(self, num_obs: int):
        '''Setting obstacles for the maze'''
        #Number should be less that the tiles
        if num_obs == 0:
            pass
        elif num_obs >= (self.grid_rows*self.grid_cols):
            raise 'Number of obstacle must be less that the number of the rows and cols'
        elif num_obs < 0:
            raise 'Number of obstacle cannot be less that zero'
        for i in range(num_obs):
            positions = [self.start_point, self.goal_point]
            num_x = random.randint(0, self.grid_rows-1)
            num_y = random.randint(0, self.grid_cols-1)
            while (num_x, num_y) in positions:
                num_x = random.randint(0, self.grid_rows-1)
                num_y = random.randint(0, self.grid_cols-1)    
            
            self.tiles[num_x][num_y].configure(bg='gray')
            positions.append((num_x,num_y))

    def create(self):
        '''Create the window'''
        self.root.mainloop()

test = Maze(10, 10,'test','green', 'yellow', 'white', 'red', 'gray')
test.create_grid()
test.create()