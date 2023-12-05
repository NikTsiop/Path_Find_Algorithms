#!/maze_venv/Scripts/python.exe
from tkinter import*
from models import tiel

# COLOS:
# azure1 path
# banana visited tiel
# antiquewhite3 wall
# darkgoldenrod1 start point
# emeraldgreen goal point

class maze_cofig:
    
    maze_tiels = []
    
    def __init__(self, window):
        self.window = window

    def create_maze(self, x, y):
        
        #check the size of the maze
        if x <= 1 and y <= 1:
            return None
        
        #maze dimations
        maze_canvas_x = self.window.winfo_x - 100
        maze_canvas_y = self.window.winfo_y - 70
        
        #canvas configuration
        self.maze_canvas = Canvas(self.window, maze_canvas_x, maze_canvas_y)
        self.maze_canvas.configure(bg="black", highlightthickness=1)
        self.maze_canvas.bind("<Button-1>",self.callback)
        self.maze_canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
        
    def create_square(self, canvas, x, y, size, color):
        """Create a square on the canvas."""
        x1, y1 = x, y
        x2, y2 = x + size, y + size
        new_tiel = tiel.Tiel(x2/2, y2/2, canvas.create_rectangle(x1, y1, x2, y2, fill= "azure1"))
        self.maze_tiels.append(new_tiel)
    
    def init_maze(canvas):
        """TODO: Create the maze here"""