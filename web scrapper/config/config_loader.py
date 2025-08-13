import json
import os
from core.logger import get_logger

logger = get_logger(__name__)

def load_config(config_file: str = "config/scraper_config.json") -> dict:
    """Load configuration from JSON file or create default one."""
    default_config = {...}  # Paste default_config dict from your original code here
    
    if not os.path.exists(config_file):
        save_config(default_config, config_file)
        logger.info(f"Config file created at {config_file}")
    
    with open(config_file, 'r', encoding='utf-8') as f:
        user_config = json.load(f)
        default_config.update(user_config)
    
    return default_config

def save_config(config: dict, config_file: str):
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
