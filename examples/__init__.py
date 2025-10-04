"""
516 Hackers OSINT Toolkit
Examples package - demonstration scripts and sample data
"""

__version__ = "1.0.0"
__author__ = "516 Hackers"

import os

# Example data directory
EXAMPLE_DATA_DIR = os.path.join(os.path.dirname(__file__), 'sample_data')

def get_example_data_path(filename):
    """Get path to example data file"""
    return os.path.join(EXAMPLE_DATA_DIR, filename)

__all__ = [
    'EXAMPLE_DATA_DIR',
    'get_example_data_path'
]
