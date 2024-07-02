from Config.BasicConfiguration import BasicConfiguration

START_COLOR = 'start_color'
STEP_COLOR = 'step_color'
TILE_COLOR = 'tile_color'
TARGET_COLOR = 'target_color'
OBSTACLE_COLOR = 'obstacle_color'
ROWS = 'rows'
COLS = 'cols'

class GridConfiguration(BasicConfiguration):
    def __init__(self) -> None:
        #Defualt configuration
        if not super().load_configuration():
            self.config_dict = {
                'start_color': 'lime green',
                'step_color': 'yellow2',
                'tile_color': 'white',
                'target_color': 'brown1',
                'obstacle_color': 'dim gray',
                'rows': 10,
                'cols': 10
            }
        self.config()
    
    def config(self):
        self.start_color = self.config_dict[START_COLOR]
        self.step_color = self.config_dict[STEP_COLOR]
        self.tile_color = self.config_dict[TILE_COLOR]
        self.target_color = self.config_dict[TARGET_COLOR]
        self.obstacle_color = self.config_dict[OBSTACLE_COLOR]
        self.rows = self.config_dict[ROWS]
        self.cols = self.config_dict[COLS]

    @property
    def start_color(self):
        return self.config_dict[START_COLOR]
    
    @start_color.setter
    def start_color(self, value):
        self.config_dict[START_COLOR] = value
    
    @property
    def step_color(self):
        return self.config_dict[STEP_COLOR]
    
    @step_color.setter
    def step_color(self, value):
        self.config_dict[STEP_COLOR] = value
    
    @property
    def tile_color(self):
        return self.config_dict[TILE_COLOR]
    
    @tile_color.setter
    def tile_color(self, value):
        self.config_dict[TILE_COLOR] = value
    
    @property
    def target_color(self):
        return self.config_dict[TARGET_COLOR]
    
    @target_color.setter
    def target_color(self, value):
        self.config_dict[TARGET_COLOR] = value
    
    @property
    def obstacle_color(self):
        return self.config_dict[OBSTACLE_COLOR]
    
    @obstacle_color.setter
    def obstacle_color(self, value):
        self.config_dict[OBSTACLE_COLOR] = value
    
    @property
    def rows(self):
        return self.config_dict[ROWS]
    
    @rows.setter
    def rows(self, value):
        self.config_dict[ROWS] = value
    
    @property
    def cols(self):
        return self.config_dict[COLS]
    
    @cols.setter
    def cols(self, value):
        self.config_dict[COLS] = value