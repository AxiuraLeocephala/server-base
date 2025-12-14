from typing import Dict
import pathlib
import yaml 

BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent

config_path = BASE_DIR / "config.yml"

def get_config():
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config()

SERVER_CONFIG: Dict = config["server"]
DATABASE_CONFIG_MYSQL: Dict = config["database_mysql"]