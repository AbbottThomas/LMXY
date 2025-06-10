# 环境感知配置加载代码
import os
import logging.config
from pathlib import Path
import yaml
# from typing import Dict, Any,List

def setup_logging(env: str|None=None) -> None:
    """根据环境变量加载对应的YAML配置"""
    env = env or os.getenv("APP_ENV", "dev").lower()
    config_path = f"./configs/logging_{env}.yaml"
  
    LOG_DIR = Path("logs")
    LOG_DIR.mkdir(exist_ok=True)
    
    try:
        with open(config_path, 'rt', encoding='utf-8') as f:
            config_str = f.read().replace("{{LOG_PATH}}", str(LOG_DIR))
            config = yaml.safe_load(config_str)
            logging.config.dictConfig(config)
    except Exception as e:
        logging.basicConfig(level=logging.INFO)
        logging.error(f"Failed to load logging config: {e}")


