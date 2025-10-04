"""
516 Hackers OSINT Toolkit
Configuration package
"""

__version__ = "1.0.0"
__author__ = "516 Hackers"

import os
import json

def get_config_path():
    """Get the absolute path to the config directory"""
    return os.path.dirname(os.path.abspath(__file__))

def load_config(filename):
    """Load a configuration file from the config directory"""
    config_path = os.path.join(get_config_path(), filename)
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️  Config file not found: {filename}")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing config file {filename}: {e}")
        return {}

# Pre-load common configs for easy access
try:
    default_config = load_config('default_config.json')
    social_platforms = load_config('social_platforms.json')
    user_agents = load_config('user_agents.json')
except Exception as e:
    print(f"❌ Error loading configs: {e}")
    default_config = {}
    social_platforms = {}
    user_agents = {}

__all__ = [
    'get_config_path',
    'load_config', 
    'default_config',
    'social_platforms',
    'user_agents'
]
