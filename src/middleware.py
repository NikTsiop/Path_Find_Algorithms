import sys
import os
# Append the root directory to sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)  # Insert at the beginning of sys.path

from algorithms.dfs import DFS
from models import Tile

class Middleware:
    
    def __init__(self) -> None:
        pass
    
    def use_DFS(self, start_point, target_point, tiles: list[list[Tile]]):
        width = len(tiles[0])
        height = len(tiles)
        points = [[None for _ in range(width)] for _ in range(height)]
        for row in range(width):
            for col in range(height):
                points[row][col] = tiles[row][col].type.value
            
        dfs = DFS(start_point, target_point, points, width, height)
        result = dfs.solve()
        return result