"""
516 Hackers - Utility Functions
Common helper functions for the OSINT toolkit
"""

import json
import os
from datetime import datetime
import hashlib

def create_output_dir(base_dir="outputs"):
    """Create output directory with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"{base_dir}/scan_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def save_json(data, filename):
    """Save data as JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return filename

def calculate_file_hash(filepath, algorithm='md5'):
    """Calculate file hash"""
    hasher = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def format_timestamp():
    """Get formatted timestamp"""
    return datetime.now().isoformat()

def validate_email(email):
    """Basic email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def print_banner():
    """Print 516 Hackers banner"""
    banner = """
╔══════════════════════════════════════════════╗
║                516 HACKERS                   ║
║           OSINT Toolkit v1.0                ║
║                                              ║
║    Social Media Intelligence | Forensics    ║
║        Metadata Analysis | Image OSINT      ║
╚══════════════════════════════════════════════╝
    """
    print(banner)
