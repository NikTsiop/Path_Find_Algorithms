from tkinter import *
import tkinter as tk
import random
from models import *

class Maze:
    def __init__(self, name: str = "Maze"):
        self.root = Tk()
        self.name = name
        
        self.start_isSetted = False
        self.target_isSetted = False
        self.start_point = (-1, -1)
        self.target_point = (-1, -1)
        self.start_point_clicked = False
        self.goal_point_clicked = False
        self.obstacle_clicked = False
        
        #Defualt configuration
        self.config_dict = {
            'start_color': 'lime green',
            'step_color': 'yellow2',
            'tile_color': 'white',
            'target_color': 'brown1',
            'obstacle_color': 'dim gray',
            'rows': 10,
            'cols': 10
        }
        self.configure_grid()
        
        self.tile_width = 50
        self.tile_height = 50
        self.window_width = int((self.grid_rows*self.tile_width))
        self.window_height = int((self.grid_cols*self.tile_height))
        self.root.title(self.name)
        self.root.geometry(f'{self.window_width}x{self.window_height}')
        
        self.create_menu()

    def config(self, **kwargs):
        self.config_dict.update(kwargs)
        self.configure_grid()
        
    def configure_grid(self):
        '''Grid configuration'''
        self.start_color = self.config_dict.get('start_color')
        self.step_color = self.config_dict.get('step_color')
        self.tile_color = self.config_dict.get('tile_color')
        self.target_color = self.config_dict.get('target_color')
        self.obstacle_color = self.config_dict.get('obstacle_color')
        self.grid_rows = self.config_dict.get('rows')
        self.grid_cols = self.config_dict.get('cols')    

    def create_menu(self):
        '''Setting up menu'''
        menubar = tk.Menu()
        create_maze_menu = tk.Menu(menubar, tearoff=False)
        create_maze_menu.add_command(
            label= 'Set Start Point',
            accelerator= 'Ctrl+S',
            command= self.startPoint
        )
        create_maze_menu.add_command(
            label='Set Goal point',
            accelerator='Ctrl+G',
            command = self.goalPoint
        )
        create_maze_menu.add_command(
            label='Set Obstacles',
            accelerator='Ctrl+O',
            command = self.obstaclesPoints
        )
        menubar.add_cascade(menu=create_maze_menu, label='Create Maze')
        
        run_menu = tk.Menu(menubar, tearoff=False)
        run_menu.add_command(
            label= 'Run',
            accelerator= 'F5',
            command= self.run_callback
        )
        run_menu.add_command(
            label= 'Step',
            accelerator= 'F10',
            command= self.step_callback
        )
        run_menu.add_command(
            label= 'Step Back',
            accelerator= 'F11',
            command= self.step_back_callback
        )
        run_menu.add_command(
            label= 'Pause',
            accelerator= 'F12',
            command= self.pause_callback
        )
        
        self.root.bind_all("<F5>", self.run_callback)
        self.root.bind_all("<F10>", self.step_callback)
        self.root.bind_all("<F11>", self.step_back_callback)
        self.root.bind_all("<F12>", self.pause_callback)
        menubar.add_cascade(menu=run_menu, label='Run')
        
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
    
    def step_callback():
        pass
    
    def step_back_callback():
        pass
    
    def run_callback():
        pass
    
    def pause_callback():
        pass
    
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
        '''On click actions'''
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
        elif type_point == TileType.OBSTACLE:
            self.tiles[x][y].isSteppable = False

    def step(self, x: int, y:int):
        if self.tiles[x][y].type != TileType.TARGET:
            self.tiles[x][y].widget.configure(bg=self.step_color)
            self.tiles[x][y].isStepped = True
        else:
            print("Found the target") #TODO Call the function of the winning
    
    def back_step(self, x:int, y: int):
        if self.tiles[x][y].type != TileType.START:
            self.tiles[x][y].widget.configure(bg=self.tile_color)
            self.tiles[x][y].isStepped = False
        
    def take_a_step(self, x: int, y: int, back_step: bool = False):
        '''Makes the steps to the next position'''
        if back_step:
            self.back_step(x, y)
        self.step(x, y)

    def create(self):
        '''Create the window'''
        self.root.mainloop()

test = Maze()
test.create_grid()
test.create()