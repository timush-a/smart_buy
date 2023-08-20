import json
import logging


class ConfigException(Exception):
    def __init__(self, *args):
        super().__init__(args)


def load_config(path_to_json: str) -> dict:
    with open(path_to_json, 'r') as f:
        data = f.read()
    if data:
        return json.loads(data)
    raise ConfigException(f'Config file {path_to_json} is empty.')


def get_logger(name: str = "app", level=logging.INFO) -> logging.Logger:
    pass
