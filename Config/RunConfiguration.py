from enum import Enum
from Config.BasicConfiguration import BasicConfiguration

ALGORITHM = 'algorithm'
FULLSOLUTION = 'full_solution'
STEPDELAY = 'step_delay'

class AlgorithmsTypes(Enum):
    DFS = 0
    BFS = 1

class RunConfiguration(BasicConfiguration):
    def __init__(self) -> None:
        if not super().load_configuration():
            self.run_config = {
                'algorithm' : AlgorithmsTypes.DFS.value,
                'full_solution': False,
                'step_delay' : 1000
            }
        self.config()
    
    def update_config(self, **kwargs):
        self.run_config.update(kwargs)
        self.config()
    
    def config(self):
        self.algorithm = AlgorithmsTypes(self.run_config[ALGORITHM])
        self.full_solution = self.run_config[FULLSOLUTION]
        self.step_delay = self.run_config[STEPDELAY] 
    
    @property
    def algorithm(self):
        return AlgorithmsTypes(self.run_config[ALGORITHM])
    
    @algorithm.setter
    def algorithm(self, value: AlgorithmsTypes):
        self.run_config[ALGORITHM] = value.value
    
    @property
    def full_solution(self):
        return self.run_config[FULLSOLUTION]
    
    @full_solution.setter
    def full_solution(self, value):
        self.run_config[FULLSOLUTION] = value
    
    @property
    def step_delay(self):
        return int(self.run_config[STEPDELAY])
    
    @step_delay.setter
    def step_delay(self, value):
        self.run_config[STEPDELAY] = value