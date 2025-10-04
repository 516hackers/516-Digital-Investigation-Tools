"""
516 Hackers OSINT Toolkit
Test package for unit and integration tests
"""

import os
import sys

# Add the parent directory to Python path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

__version__ = "1.0.0"
__author__ = "516 Hackers"

# Test configuration
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')

def create_test_data_dir():
    """Create test data directory if it doesn't exist"""
    os.makedirs(TEST_DATA_DIR, exist_ok=True)

__all__ = [
    'TEST_DATA_DIR',
    'create_test_data_dir'
]
