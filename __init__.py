"""
516 Digital Investigation Tools
A comprehensive digital investigation and OSINT toolkit for cybersecurity professionals
"""

__version__ = "1.0.0"
__author__ = "516 Hackers"
__description__ = "Comprehensive digital investigation and OSINT toolkit for cybersecurity professionals, researchers, and ethical hackers"

# Package metadata
PACKAGE_NAME = "516-Digital-Investigation-Tools"
REPOSITORY_URL = "https://github.com/516hackers/516-Digital-Investigation-Tools"

# Import main components for easy access
try:
    from scripts import (
        Sherlock516,
        Instagram516,
        MetadataAnalyzer516,
        ImageForensics516,
        SocialMediaMapper516,
        EmailAnalyzer516,
        DomainResearch516,
        ReportGenerator516
    )
    
    from utils import (
        config,
        logger,
        ExportUtils516,
        print_banner
    )
    
except ImportError as e:
    print(f"⚠️  Some components could not be imported: {e}")

# Main entry points for the package
def show_banner():
    """Display the 516 Hackers banner"""
    from utils.helpers import print_banner
    print_banner()

def get_version():
    """Return the package version"""
    return __version__

def get_tools():
    """Return list of available tools"""
    return {
        'investigate516': 'Username investigation across social media',
        'ig516': 'Instagram profile analysis',
        'meta516': 'Image metadata analysis and cleaning',
        'image516': 'Image forensics and similarity detection',
        'social516': 'Social media presence mapping',
        'email516': 'Email validation and analysis',
        'domain516': 'Domain research and WHOIS lookup',
        'report516': 'Unified report generation'
    }

__all__ = [
    'show_banner',
    'get_version',
    'get_tools',
    'Sherlock516',
    'Instagram516',
    'MetadataAnalyzer516', 
    'ImageForensics516',
    'SocialMediaMapper516',
    'EmailAnalyzer516',
    'DomainResearch516',
    'ReportGenerator516',
    'config',
    'logger',
    'ExportUtils516',
    'print_banner'
]

# Initialize package
print(f"🎯 {PACKAGE_NAME} v{__version__} initialized")
print(f"📚 Use show_banner() to display the toolkit banner")
print(f"🔧 Use get_tools() to see available tools")
