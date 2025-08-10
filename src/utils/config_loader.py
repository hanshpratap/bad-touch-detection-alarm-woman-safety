import yaml
import os

def load_config():
    with open(os.path.join(os.path.dirname(__file__), "../../config.yaml"), "r") as f:
        return yaml.safe_load(f)
