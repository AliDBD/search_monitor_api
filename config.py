import yaml

def load_config(config_path='config.yml'):
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise Exception(f"配置文件加载失败: {e}") 