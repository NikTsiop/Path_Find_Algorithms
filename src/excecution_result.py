class ExcecutionResult:
    def __init__(self) -> None:
        self._searched_nodes = None
        self._solution = None
        self._total_explored = None
        self._solution_actions = None
    
    @property
    def actions(self):
        return self._solution_actions
    
    @actions.setter
    def actions(self, value):
        self._solution_actions = value
    
    @property
    def searched_nodes(self):
        return self._searched_nodes
    
    @searched_nodes.setter
    def searched_nodes(self, value):
        self._searched_nodes = value
        
    @property
    def solution(self):
        return self._solution
    
    @solution.setter
    def solution(self, value):
        self._solution = value
    
    @property
    def total_explored(self):
        return self._total_explored
    
    @total_explored.setter
    def total_explored(self, value):
        self._total_explored = value