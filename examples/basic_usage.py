
"""
516 Hackers - Basic Usage Examples
Demonstrate how to use the toolkit
"""

from scripts.sherlock_wrapper import Sherlock516
from scripts.metadata_analyzer import MetadataAnalyzer516
from scripts.email_analyzer import EmailAnalyzer516
from utils.helpers import print_banner

def demonstrate_sherlock():
    """Demonstrate username search"""
    print("🔍 Demonstrating Username Search...")
    investigator = Sherlock516("outputs/examples")
    investigator.check_standard_sites()
    results = investigator.save_results()
    print(f"✅ Username search completed. Results: {results}")

def demonstrate_metadata_analysis():
    """Demonstrate metadata analysis"""
    print("\n📊 Demonstrating Metadata Analysis...")
    analyzer = MetadataAnalyzer516("outputs/examples")
    
    # Note: You would need an actual image file for this
    print("⚠️  Add an image file to test metadata analysis")
    # metadata = analyzer.extract_metadata("path/to/image.jpg")
    # print(f"✅ Metadata extracted: {len(metadata.get('metadata', {}))} tags")

def demonstrate_email_analysis():
    """Demonstrate email analysis"""
    print("\n📧 Demonstrating Email Analysis...")
    analyzer = EmailAnalyzer516()
    result = analyzer.validate_email("test@example.com")
    print(f"✅ Email validation: {result['is_valid_format']}")

def main():
    print_banner()
    print("516 Hackers OSINT Toolkit - Basic Usage Examples")
    print("=" * 50)
    
    demonstrate_sherlock()
    demonstrate_metadata_analysis() 
    demonstrate_email_analysis()
    
    print("\n🎯 Examples completed! Check the 'outputs/examples' directory for results.")

if __name__ == "__main__":
    main()
