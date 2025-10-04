"""
516 Hackers - Configuration Loader
Centralized configuration management
"""

import json
import os
from typing import Dict, Any

class ConfigLoader:
    def __init__(self, config_dir="config"):
        self.config_dir = config_dir
        self.configs = {}
        self.load_all_configs()
    
    def load_all_configs(self):
        """Load all configuration files"""
        config_files = {
            'default': 'default_config.json',
            'platforms': 'social_platforms.json',
            'user_agents': 'user_agents.json'
        }
        
        for config_name, filename in config_files.items():
            filepath = os.path.join(self.config_dir, filename)
            self.configs[config_name] = self._load_json_config(filepath)
    
    def _load_json_config(self, filepath: str) -> Dict[str, Any]:
        """Load JSON configuration file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Config file not found: {filepath}")
            return {}
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing config file {filepath}: {e}")
            return {}
    
    def get(self, config_name: str, key: str = None, default=None):
        """Get configuration value"""
        config = self.configs.get(config_name, {})
        
        if key is None:
            return config
        
        # Support nested keys with dot notation
        keys = key.split('.')
        for k in keys:
            if isinstance(config, dict) and k in config:
                config = config[k]
            else:
                return default
        
        return config
    
    def get_user_agent(self) -> str:
        """Get random user agent"""
        import random
        user_agents = self.get('user_agents', 'user_agents', [])
        return random.choice(user_agents) if user_agents else "516-Hackers-OSINT-Toolkit/1.0"
    
    def get_platforms(self) -> Dict[str, Any]:
        """Get social media platforms configuration"""
        return self.get('platforms', 'platforms', {})

# Global config instance
config = ConfigLoader()
