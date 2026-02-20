import yaml
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / "configs" / "config.yaml"

def get_config():
    with open(config_path) as file:
        config = yaml.safe_load(file)
        return config
    
config = get_config()
SERVER_CONFIG = config["server"]
DATABASE_CONFIG = config["database"]