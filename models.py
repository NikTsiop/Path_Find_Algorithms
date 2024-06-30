from enum import Enum
import tkinter as tk

class TileType(Enum):
    TILE = 0
    START = 1
    TARGET = 2
    OBSTACLE = 3

class Tile:
    def __init__(self, point_type: TileType, widget: tk.Frame) -> None:
        self.type: TileType = point_type
        self.widget: tk.Frame = widget
        self.isSetted = False
        self.isStepped = False
        self.isSteppable = True
        self.point = (-1, -1)