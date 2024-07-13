from tkinter import *
import tkinter as tk
from models import Tile, TileType
from middleware import Middleware
from config import GridConfiguration, RunConfiguration, AlgorithmsTypes
from src.excecution_result import ExcecutionResult
from src.step_execution import StepTrack
from environmentComponents import RunDropDow, SetupDropDown, RunToolbar

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
        self.isExecuted = False
        self.clean = True
        
        self.execution_result = ExcecutionResult()
        self.step_track = None
        
        self.grid_config = GridConfiguration()
        self.run_config = RunConfiguration()
        
        self.tile_width = 25
        self.tile_height = 25
        self.window_width = int((self.grid_config.rows*self.tile_width))
        self.window_height = int((self.grid_config.cols*self.tile_height))
        self.root.title(self.name)
        self.root.geometry(f'{self.window_width}x{self.window_height}')
        
        self.main_menu = tk.Menu()
        self.run_dropdown_menu = RunDropDow(self.root, self.main_menu)
        self.run_dropdown_menu.create_dropdown(self.run_callback, self.step_callback, self.step_back_callback, self.pause_callback)
        self.setup_dropdown_menu = SetupDropDown(self.root, self.main_menu)
        self.setup_dropdown_menu.create_dropdown(self.startPoint, self.goalPoint, self.obstaclesPoints)
        
        self.run_toolbar = RunToolbar(self.root, self.run_config)
        self.run_toolbar.create_run_config_menu(
            self.run_callback,
            self.step_back_callback,
            self.step_callback,
            self.clear_steps,
            self.clear_grid
        )
        
        self.root.grid_columnconfigure(0, weight=1)
    
    def startPoint(self):
        self.start_point_clicked = True
    
    def goalPoint(self):
        self.goal_point_clicked = True
    
    def obstaclesPoints(self):
        self.obstacle_clicked = True

    def step_callback(self):
        if self.isExecuted:
            self.clear_step()
            if self.step_track.next != None:
                x, y  = self.step_track.next
                
                self.take_a_step(x, y)
                self.step_track.previous = self.step_track.current
                self.step_track.current = self.step_track.next
                
                possible_index = self.step_track.track + 1
                possible_next = self.execution_result.solution[possible_index]
                
                if self.tiles[possible_next[0]][possible_next[1]].type == TileType.TARGET:
                    self.step_track.next = None
                    self.step_track.track -= 1
                else:
                    self.step_track.track += 1
                    self.step_track.next = self.execution_result.solution[self.step_track.track]
                
                #print(
                #    f"next point: {self.step_track.next} -- point type: {self.tiles[x][y].type} -- current point {self.step_track.current} -- previous point {self.step_track.previous} -- track counter {self.step_track.track}"
                #)
    
    def step_back_callback(self):
        if self.isExecuted:
            self.clear_step()
            if self.step_track.previous != None:
                x, y  = self.step_track.previous
                currentx, currenty = self.step_track.current
                self.remove_point(currentx, currenty)
                self.step_track.next = self.step_track.current
                self.step_track.current = self.step_track.previous
                self.step_track.track -= 1
                if self.step_track.track < 0 :
                    self.remove_point(self.step_track.current[0], self.step_track.current[1])
                    self.step_track.track = 0
                    self.step_track.previous = None
                    self.step_track.next = self.step_track.current
                    self.step_track.current = self.start_point
                else:
                    self.step_track.previous = self.execution_result.solution[self.step_track.track]
                #print(
                #    f"previous point: {self.step_track.previous} -- point type: {self.tiles[x][y].type} -- current point {self.step_track.current} -- next point {self.step_track.next} -- track counter {self.step_track.track}"
                #)
    
    def clear_step(self):
        if self.clean:
                self.clear_steps()
                self.clean = False
    
    def clear_steps(self):
        for row in range(self.grid_config.rows):
            for col in range(self.grid_config.cols):
                if self.tiles[row][col].isStepped:
                    self.remove_point(row, col)
    
    def clear_grid(self):
        for row in range(self.grid_config.rows):
            for col in range(self.grid_config.cols):
                self.remove_point(row, col)
    
    def run_callback(self):
        middleware = Middleware()
        results  = None
        self.clear_steps()       
        if self.run_config.algorithm == AlgorithmsTypes.DFS:
            results = middleware.use_DFS(self.start_point, self.target_point, self.tiles)
            self.isExecuted = True
            self.clean = True
        self.run(results)

    def pause_callback():
        pass
    
    def run(self, results):
        
        delay = self.run_config.step_delay
        increment = delay/10
        
        if results is not None:
            self.execution_result.actions = results[0][0][0]
            self.execution_result.solution = results[0][0][1]
            self.execution_result.searched_nodes = results[1]
            self.execution_result.total_explored = results[0][1]
            
            self.step_track = StepTrack(None, self.start_point, self.execution_result.solution[0])
            
            enumerate_list = []
            
            if self.run_config.full_solution:
                enumerate_list = self.execution_result.searched_nodes
            else:
                enumerate_list = self.execution_result.solution
            
            for i, coor in enumerate(enumerate_list):
                x, y = coor
                self.take_a_step(x, y, delay=delay + i*increment)
    
    def create_grid(self):
        '''Configure the maze grid'''
        parent_frame = tk.Frame(self.root, bg='light gray')
        parent_frame.grid(row=1, column=0, sticky='ew')
        rows = self.grid_config.rows
        cols = self.grid_config.cols
        self.tiles: list[list[Tile]] = [[None for _ in range(rows)] for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                tile = tk.Frame(parent_frame, width=self.tile_width, height=self.tile_height, bg=self.grid_config.tile_color)
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
                self.set_point(x, y, TileType.START, self.grid_config.start_color)
            elif self.goal_point_clicked and not self.target_isSetted:
                self.set_point(x, y, TileType.TARGET, self.grid_config.target_color)
            elif self.obstacle_clicked:
                self.set_point(x, y, TileType.OBSTACLE, self.grid_config.obstacle_color)
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
        if point.isStepped:
            point.isStepped = False  
        self.tiles[x][y].widget.configure(bg=self.grid_config.tile_color)
        self.tiles[x][y].type = TileType.TILE 
        
    def set_point(self, x: int, y: int, type_point: TileType, color: str):
        '''Set point of interest for the maze'''
        self.tiles[x][y].widget.configure(bg=color)
        self.tiles[x][y].type = type_point
        if type_point == TileType.START:
            self.start_isSetted = True
            self.start_point = self.tiles[x][y].point
        elif type_point == TileType.TARGET:
            self.target_isSetted = True
            self.target_point = self.tiles[x][y].point
        elif type_point == TileType.OBSTACLE:
            self.tiles[x][y].isSteppable = False

    def step(self, x: int, y:int, delay = 0):
        if self.tiles[x][y].type != TileType.TARGET and self.tiles[x][y].type != TileType.START:
            self.tiles[x][y].widget.after(int(delay), lambda: self.tiles[x][y].widget.configure(bg=self.grid_config.step_color))
            self.tiles[x][y].isStepped = True
    
    def back_step(self, x:int, y: int, delay = 0):
        if self.tiles[x][y].type != TileType.START:
            self.tiles[x][y].widget.after(delay, lambda: self.tiles[x][y].widget.configure(bg=self.grid_config.tile_color))
            self.tiles[x][y].isStepped = False
        
    def take_a_step(self, x: int, y: int, back_step: bool = False, delay = 0):
        '''Makes the steps to the next position'''
        if back_step:
            self.back_step(x, y, delay)
        self.step(x, y, delay)

    def create(self):
        '''Create the window'''
        self.root.mainloop()

test = Maze()
test.create_grid()
test.create()