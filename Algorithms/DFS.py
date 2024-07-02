from Algorithms.Node import Node
from Algorithms.Helpers import StackFrontier

class DFS:
    def __init__(self, start_point, target_point, points: list[tuple], width, height) -> None:
        self.start_point = start_point
        self.target_point = target_point
        self.points = points
        self.width = width
        self.height = height
        self.solution = None
    
    def neighbors(self, state) -> list[tuple]:
        row, col = state
        candidates= [
            ("up", (row-1, col)),
            ("down", (row+1, col)),
            ("left", (row, col-1)),
            ("right", (row,col+1)) 
        ]
        
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width:
                if self.points[r][c] == 3:
                    continue
                result.append((action, (r, c)))
        return result
    
    def solve(self) -> tuple:
        
        self.num_explored = 0
        
        start = Node(state= self.start_point, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)
        
        self.explored = set()
        full_searched_path = list()
        
        while True:
            
            if frontier.empty():
                return (self.solution, full_searched_path)
            
            node = frontier.remove()
            self.num_explored +=1
            
            full_searched_path.append(node.state)
            
            if node.state == self.target_point:
                actions = []
                cells = []
                
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells, self.num_explored)
                return (self.solution, full_searched_path)
            
            self.explored.add(node.state)
            
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)