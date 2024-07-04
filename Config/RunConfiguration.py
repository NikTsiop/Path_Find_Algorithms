from enum import Enum
from Config.BasicConfiguration import BasicConfiguration

#Section
CONFIG_SECTION = 'run_configuration'

#Options
ALGORITHM = 'algorithm'
FULLSOLUTION = 'full_solution'
STEPDELAY = 'step_delay'

#Default configuration
DEFAULT_ALGORITHM = '0'
DEFAULT_FULL_SOLUTION = 'FALSE'
DEFAULT_STEP_DELAY = '1000'

class AlgorithmsTypes(Enum):
    DFS = 0
    BFS = 1

class RunConfiguration(BasicConfiguration):
    def __init__(self) -> None:
        self.base = super()
        self.base.__init__()
        configuration = self.base.load_configuration(CONFIG_SECTION)
        if configuration is None:
            self.default_configuration = {
                ALGORITHM : DEFAULT_ALGORITHM,
                FULLSOLUTION: DEFAULT_FULL_SOLUTION,
                STEPDELAY : DEFAULT_STEP_DELAY
            }
            self.base.save_or_create_configuration(CONFIG_SECTION, self.default_configuration)
            configuration = self.base.load_configuration(CONFIG_SECTION)
            if configuration is None:
                raise "Problem with the configuration occured"
        self.run_config = configuration
    
    def update_config(self, **kwargs):
        for key, value in kwargs.items():
            self.base.save_option_configuration(CONFIG_SECTION, key, value)
        self.run_config = self.base.load_configuration(CONFIG_SECTION)
    
    @property
    def algorithm(self):
        return AlgorithmsTypes(self.run_config.getint(ALGORITHM, fallback= DEFAULT_ALGORITHM))
    
    @algorithm.setter
    def algorithm(self, value: AlgorithmsTypes):
        self.update_config(algorithm = str(value))
    
    @property
    def full_solution(self) -> bool:
        return self.run_config.getboolean(FULLSOLUTION, fallback=DEFAULT_FULL_SOLUTION)
    
    @full_solution.setter
    def full_solution(self, value):
        self.update_config(full_solution = str(value))
    
    @property
    def step_delay(self) -> int:
        return self.run_config.getint(STEPDELAY, fallback= DEFAULT_STEP_DELAY)
    
    @step_delay.setter
    def step_delay(self, value):
        self.update_config(step_delay = str(value))