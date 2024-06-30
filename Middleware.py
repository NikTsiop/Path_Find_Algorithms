from Algorithms.DFS import DFS
from Models import Tile, TileType

class Middleware:
    
    def __init__(self) -> None:
        pass
    
    def use_DFS(self, start_point, target_point, tiles: list[list[Tile]]):
        points = []
        for row in tiles:
            for tile in row:
                points.append((tile.point, tile.type.value))
            
        dfs = DFS(start_point, target_point, points, len(tiles[0]), len(tiles))
        result = dfs.solve()
        return result