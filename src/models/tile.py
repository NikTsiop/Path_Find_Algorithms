from models import TileType
import tkinter as tk
class Tile:
    def __init__(self, point_type: TileType, widget: tk.Frame) -> None:
        self.type: TileType = point_type
        self.widget: tk.Frame = widget
        self.isSetted = False
        self.isStepped = False
        self.isSteppable = True
        self.point = (-1, -1)