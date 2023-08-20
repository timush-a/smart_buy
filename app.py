from argparse import ArgumentParser
from src.common.utils import get_logger, load_config


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", type=str, help="Path to configuration file")
    args = parser.parse_args()
    config_path = args.config
    logger = get_logger()
    config = load_config(config_path)
