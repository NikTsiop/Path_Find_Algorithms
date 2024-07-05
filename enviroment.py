from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from Models import *
from Middleware import Middleware
from Config.GridConfiguration import GridConfiguration
from Config.RunConfiguration import RunConfiguration, AlgorithmsTypes

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
        
        self.grid_config = GridConfiguration()
        self.run_config = RunConfiguration()
        
        self.tile_width = 25
        self.tile_height = 25
        self.window_width = int((self.grid_config.rows*self.tile_width))
        self.window_height = int((self.grid_config.cols*self.tile_height))
        self.root.title(self.name)
        self.root.geometry(f'{self.window_width}x{self.window_height}')
        
        self.create_menu()
        self.create_run_config_menu()
        self.root.grid_columnconfigure(0, weight=1)
    
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

    def selection_changed(self, event):
        algorithms = event.widget
        selected_value = algorithms.get()
        self.run_config.algorithm = AlgorithmsTypes[selected_value].value

    def validation_entry(text, new_text):
        # First check that the entire content has no more than ten characters.
        if len(new_text) > 5:
            return False
        # Then make sure the text is numeric-only.
        return text.isdecimal()

    def create_run_config_menu(self):
        '''Run configuration menu'''
        run_config_menu = tk.Frame(self.root, bg="light gray")
        
        play_original_image = Image.open(r"./assets/icons/play.png")
        play_icon_image = ImageTk.PhotoImage(play_original_image.resize((16, 16)))
        play_button = ttk.Button(run_config_menu, image=play_icon_image, command= self.run_callback)
        play_button.image = play_icon_image      
        play_button.pack(side=LEFT, padx=2, pady=2)
        
        back_step_original_image = Image.open(r"./assets/icons/back_step.png")
        back_step_icon_image = ImageTk.PhotoImage(back_step_original_image.resize((16, 16)))
        back_step_button = ttk.Button(run_config_menu, image=back_step_icon_image, command= self.step_back_callback)
        back_step_button.image = back_step_icon_image      
        back_step_button.pack(side=LEFT, padx=2, pady=2)
        
        step_original_image = Image.open(r"./assets/icons/step.png")
        step_icon_image = ImageTk.PhotoImage(step_original_image.resize((16, 16)))
        step_button = ttk.Button(run_config_menu, image=step_icon_image, command= self.step_callback)
        step_button.image = step_icon_image      
        step_button.pack(side=LEFT, padx=2, pady=2)
        
        reset_original_image = Image.open(r"./assets/icons/reset.png")
        reset_icon_image = ImageTk.PhotoImage(reset_original_image.resize((16, 16)))
        reset_button = ttk.Button(run_config_menu, image=reset_icon_image, command= self.clear_steps)
        reset_button.image = reset_icon_image      
        reset_button.pack(side=LEFT, padx=2, pady=2)
        
        clear_original_image = Image.open(r"./assets/icons/clear.png")
        clear_icon_image = ImageTk.PhotoImage(clear_original_image.resize((16, 16)))
        clear_button = ttk.Button(run_config_menu, image=clear_icon_image, command= self.clear_grid)
        clear_button.image = clear_icon_image      
        clear_button.pack(side=LEFT, padx=2, pady=2)
        
        #Combobox for choosing of argolirthms
        algorithms_dropdown = ttk.Combobox(
            run_config_menu,
            state="readonly",
            values= ['DFS', 'BFS'] #TODO replace with dynamic 
        )
        algorithms_dropdown.current(self.run_config.algorithm.value)
        algorithms_dropdown.pack(side=LEFT, padx=2, pady=2)
        algorithms_dropdown.bind("<<ComboboxSelected>>", self.selection_changed)
        
        show_full_search_val = tk.BooleanVar()
        show_full_search = ttk.Checkbutton(
            run_config_menu, 
            text='Show full search', 
            variable=show_full_search_val,
            command=lambda: self.run_config.update_config(full_solution = str(show_full_search_val.get()))
        )
        show_full_search.pack(side=LEFT, padx=2, pady=2)
        
        step_delay_var = tk.StringVar()
        step_delay_var.set(self.run_config.step_delay)
        step_delay_label= ttk.Label(run_config_menu, text='Step Delay', font=('caribre', 10, 'bold'))
        step_delay_label.pack(side=LEFT, padx=2, pady=2)
        step_delay_entry = ttk.Entry(
            run_config_menu, 
            textvariable=step_delay_var, 
            font=('calibre', 10, 'normal'),
            width=5, 
            validatecommand=(run_config_menu.register(self.validation_entry), "%S", "%P")
        )
        step_delay_entry.pack(side=LEFT, padx=2, pady=2)
        step_delay_entry.bind("<Return>", lambda event: self.run_config.update_config(step_delay = step_delay_entry.get())) 
        
        run_config_menu.grid(row=0, column=0, sticky='ew')
        
    def step_callback(self):
        pass
    
    def step_back_callback(self):
        pass
    
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
        self.run(results)

    def pause_callback():
        pass
    
    def startPoint(self):
        self.start_point_clicked = True
    
    def goalPoint(self):
        self.goal_point_clicked = True
    
    def obstaclesPoints(self):
        self.obstacle_clicked = True
    
    def run(self, results):
        
        delay = self.run_config.step_delay
        increment = delay/10
        
        if results is not None:
            solution: tuple = results[0]
            full_searched_path: list = results[1]
            actions, cells, num_explored = solution
            
            enumerate_list = []
            
            if self.run_config.full_solution:
                enumerate_list = full_searched_path
            else:
                enumerate_list = cells
            
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