from Algorithms.DFS import DFS
from Models import Tile, TileType

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