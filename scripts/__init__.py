"""
516 Hackers OSINT Toolkit
Scripts package for all OSINT and media analysis tools
"""

__version__ = "1.0.0"
__author__ = "516 Hackers"
__description__ = "Comprehensive OSINT and media analysis toolkit"

# Import main classes for easy access
from .sherlock_wrapper import Sherlock516
from .enhanced_instaloader import Instagram516
from .metadata_analyzer import MetadataAnalyzer516
from .image_forensics import ImageForensics516
from .social_media_mapper import SocialMediaMapper516
from .email_analyzer import EmailAnalyzer516
from .domain_research import DomainResearch516
from .report_generator import ReportGenerator516

# Define what gets imported with "from scripts import *"
__all__ = [
    'Sherlock516',
    'Instagram516', 
    'MetadataAnalyzer516',
    'ImageForensics516',
    'SocialMediaMapper516',
    'EmailAnalyzer516',
    'DomainResearch516',
    'ReportGenerator516'
]

# Package initialization
print(f"🔍 516 Hackers OSINT Toolkit v{__version__} loaded")
