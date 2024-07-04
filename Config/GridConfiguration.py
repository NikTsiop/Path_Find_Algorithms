from Config.BasicConfiguration import BasicConfiguration

#Section
CONFIG_SECTION = 'grid_configuration'

#Options
START_COLOR = 'start_color'
STEP_COLOR = 'step_color'
TILE_COLOR = 'tile_color'
TARGET_COLOR = 'target_color'
OBSTACLE_COLOR = 'obstacle_color'
ROWS = 'rows'
COLS = 'cols'

#Default config
DEFAULT_START_COLOR = 'lime green'
DEFAULT_STEP_COLOR = 'yellow2'
DEFAULT_TILE_COLOR  = 'white'
DEFAULT_TARGET_COLOR = 'brown1'
DEFAULT_OBSTACLE_COLOR = 'dim gray'
DEFAULT_ROWS = '10'
DEFAULT_COLS = '10'

class GridConfiguration(BasicConfiguration):
    def __init__(self) -> None:
        self.base = super()
        self.base.__init__()
        configuration = self.base.load_configuration(CONFIG_SECTION)
        if configuration is None:
            self.default_configuration = {
                START_COLOR: DEFAULT_START_COLOR,
                STEP_COLOR: DEFAULT_STEP_COLOR,
                TILE_COLOR: DEFAULT_TILE_COLOR,
                TARGET_COLOR: DEFAULT_TARGET_COLOR,
                OBSTACLE_COLOR: DEFAULT_OBSTACLE_COLOR,
                ROWS: DEFAULT_ROWS,
                COLS: DEFAULT_COLS
            }
            self.base.save_or_create_configuration(CONFIG_SECTION, self.default_configuration)
            configuration = self.base.load_configuration(CONFIG_SECTION)
            if configuration is None:
                raise "Problem with the configuration occured"
        self.config_dict = configuration

    def update_config(self, **kwargs):
        for key, value in kwargs.items():
            self.base.save_option_configuration(CONFIG_SECTION, key, value)
        self.run_config = self.base.load_configuration(CONFIG_SECTION)

    @property
    def start_color(self):
        return self.config_dict.get(START_COLOR, fallback= DEFAULT_START_COLOR )
    
    @start_color.setter
    def start_color(self, value):
        self.config_dict[START_COLOR] = value
    
    @property
    def step_color(self):
        return self.config_dict.get(STEP_COLOR, fallback= DEFAULT_STEP_COLOR)
    
    @step_color.setter
    def step_color(self, value):
        self.config_dict[STEP_COLOR] = value
    
    @property
    def tile_color(self):
        return self.config_dict.get(TILE_COLOR, fallback= DEFAULT_TILE_COLOR)
    
    @tile_color.setter
    def tile_color(self, value):
        self.config_dict[TILE_COLOR] = value
    
    @property
    def target_color(self):
        return self.config_dict.get( TARGET_COLOR, fallback= DEFAULT_TARGET_COLOR)
    
    @target_color.setter
    def target_color(self, value):
        self.config_dict[TARGET_COLOR] = value
    
    @property
    def obstacle_color(self):
        return self.config_dict.get(OBSTACLE_COLOR, fallback= DEFAULT_OBSTACLE_COLOR)
    
    @obstacle_color.setter
    def obstacle_color(self, value):
        self.config_dict[OBSTACLE_COLOR] = value
    
    @property
    def rows(self):
        return self.config_dict.getint(ROWS, fallback= DEFAULT_ROWS)
    
    @rows.setter
    def rows(self, value):
        self.config_dict[ROWS] = str(value)
    
    @property
    def cols(self) -> int:
        return self.config_dict.getint(COLS, fallback= DEFAULT_COLS)
       
    @cols.setter
    def cols(self, value):
        self.config_dict[COLS] = str(value)