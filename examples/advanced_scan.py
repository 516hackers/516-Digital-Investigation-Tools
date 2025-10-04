
"""
516 Hackers - Advanced OSINT Scan
Comprehensive digital investigation with multiple tools
"""

import os
import json
from datetime import datetime
from utils.helpers import print_banner, create_output_dir
from scripts.sherlock_wrapper import Sherlock516
from scripts.social_media_mapper import SocialMediaMapper516
from scripts.email_analyzer import EmailAnalyzer516
from scripts.domain_research import DomainResearch516
from scripts.report_generator import ReportGenerator516
from utils.logger import logger

class AdvancedScan516:
    def __init__(self, target, output_base="outputs"):
        self.target = target
        self.scan_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = create_output_dir(output_base)
        self.results = {
            'target': target,
            'scan_id': self.scan_id,
            'start_time': datetime.now().isoformat(),
            'tools_used': [],
            'findings': {}
        }
        
        logger.info(f"Advanced scan initialized for target: {target}")
        logger.info(f"Output directory: {self.output_dir}")
    
    def run_username_investigation(self):
        """Comprehensive username analysis"""
        logger.info("Starting username investigation...")
        
        # Social media presence mapping
        mapper = SocialMediaMapper516(self.output_dir)
        social_results = mapper.map_presence(self.target)
        
        # Detailed username search
        sherlock = Sherlock516(self.target, self.output_dir)
        sherlock.check_standard_sites()
        sherlock_results = sherlock.save_results()
        
        self.results['findings']['social_media'] = social_results
        self.results['findings']['username_search'] = sherlock_results
        self.results['tools_used'].extend(['SocialMediaMapper516', 'Sherlock516'])
        
        logger.info(f"Username investigation completed - Found on {social_results['summary']['platforms_found']} platforms")
    
    def run_email_analysis(self, email=None):
        """Email analysis and pattern recognition"""
        if not email:
            # Generate potential email patterns
            email = f"{self.target}@example.com"
        
        logger.info(f"Starting email analysis for: {email}")
        
        analyzer = EmailAnalyzer516()
        email_results = analyzer.validate_email(email)
        pattern_analysis = analyzer.analyze_email_pattern(email)
        
        self.results['findings']['email_analysis'] = {
            'validation': email_results,
            'pattern_analysis': pattern_analysis
        }
        self.results['tools_used'].append('EmailAnalyzer516')
        
        logger.info(f"Email analysis completed - Valid: {email_results['is_valid_format']}")
    
    def run_domain_research(self, domain=None):
        """Domain and web presence research"""
        if not domain:
            domain = f"{self.target}.com"
        
        logger.info(f"Starting domain research for: {domain}")
        
        researcher = DomainResearch516()
        domain_results = researcher.comprehensive_analysis(domain)
        
        self.results['findings']['domain_research'] = domain_results
        self.results['tools_used'].append('DomainResearch516')
        
        logger.info(f"Domain research completed - WHOIS: {'Available' if 'error' not in domain_results['whois_info'] else 'Failed'}")
    
    def generate_comprehensive_report(self):
        """Generate unified comprehensive report"""
        logger.info("Generating comprehensive report...")
        
        generator = ReportGenerator516()
        unified_report = generator.generate_unified_report(
            self.results['findings'],
            f"Advanced OSINT Scan Report - {self.target}"
        )
        
        # Add scan metadata
        unified_report['scan_metadata'] = {
            'target': self.target,
            'scan_id': self.scan_id,
            'duration': self._calculate_duration(),
            'tools_executed': len(self.results['tools_used'])
        }
        
        # Save comprehensive report
        from utils.export_utils import ExportUtils516
        exporter = ExportUtils516(self.output_dir)
        
        export_files = exporter.export_multiple_formats(
            unified_report,
            f"advanced_scan_{self.target}_{self.scan_id}"
        )
        
        logger.info(f"Comprehensive report generated: {export_files}")
        return export_files
    
    def _calculate_duration(self):
        """Calculate scan duration"""
        start_time = datetime.fromisoformat(self.results['start_time'])
        end_time = datetime.now()
        duration = end_time - start_time
        return str(duration)
    
    def run_complete_scan(self, email=None, domain=None):
        """Run complete OSINT scan"""
        print(f"🎯 516 Hackers - Advanced OSINT Scan")
        print(f"🔍 Target: {self.target}")
        print(f"📁 Output: {self.output_dir}")
        print("=" * 50)
        
        try:
            # Run all investigation modules
            self.run_username_investigation()
            self.run_email_analysis(email)
            self.run_domain_research(domain)
            
            # Generate final report
            report_files = self.generate_comprehensive_report()
            
            # Update completion time
            self.results['end_time'] = datetime.now().isoformat()
            self.results['status'] = 'completed'
            
            # Save raw results
            results_file = os.path.join(self.output_dir, f"raw_results_{self.scan_id}.json")
            with open(results_file, 'w') as f:
                json.dump(self.results, f, indent=2, default=str)
            
            print(f"✅ Scan completed successfully!")
            print(f"📊 Tools executed: {len(self.results['tools_used'])}")
            print(f"📁 Report files:")
            for format_name, filepath in report_files.items():
                print(f"   • {format_name.upper()}: {filepath}")
            
            return self.results
            
        except Exception as e:
            logger.error(f"Scan failed: {e}")
            self.results['status'] = 'failed'
            self.results['error'] = str(e)
            raise

def main():
    """Command line interface for advanced scan"""
    import argparse
    
    parser = argparse.ArgumentParser(description='516 Hackers - Advanced OSINT Scan')
    parser.add_argument('target', help='Target username or identifier')
    parser.add_argument('-e', '--email', help='Target email address')
    parser.add_argument('-d', '--domain', help='Target domain')
    parser.add_argument('-o', '--output', default='outputs', help='Output directory')
    
    args = parser.parse_args()
    
    # Display banner
    print_banner()
    
    # Run advanced scan
    scanner = AdvancedScan516(args.target, args.output)
    scanner.run_complete_scan(args.email, args.domain)

if __name__ == "__main__":
    main()
