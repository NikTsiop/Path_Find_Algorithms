import configparser

CONFIG_PATH = './Config/config.ini'

class BasicConfiguration:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        
    def save_or_create_configuration(self, section_name: str, config: dict):
        self.config[section_name] = config
        with open(CONFIG_PATH, 'w') as configfile:
            self.config.write(configfile)
    
    def save_option_configuration(self, section_name: str, option_name: str, value):
        self.config.set(section_name, option_name, str(value))
        with open(CONFIG_PATH, 'w') as configfile:
            self.config.write(configfile)
    
    def load_configuration(self, section_name: str):
        self.config.read(CONFIG_PATH)
        if section_name in self.config:
            return self.config[section_name]
        return None