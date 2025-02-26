# config/load_config.py
import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "platform_config.yaml")
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)