"""
516 Digital Investigation Tools
Scripts package for all digital investigation and OSINT tools
"""

__version__ = "1.0.0"
__author__ = "516 Hackers"
__description__ = "Comprehensive digital investigation and OSINT toolkit"

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
print(f"🔍 516 Digital Investigation Tools v{__version__} loaded")
