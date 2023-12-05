#!/maze_venv/Scripts/python.exe
from tkinter import *

class WindowSettings:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Path Find Algorithms")
        self.window.geometry("500x500")
        self.window.config(bg="blanchedalmond")

    def get_window(self):
        return self.window
        