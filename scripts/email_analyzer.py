
"""
516 Hackers - Email Analyzer
Email validation and OSINT gathering
"""

import re
import dns.resolver
import argparse
from typing import Dict, Any
from utils.logger import logger
from utils.export_utils import ExportUtils516

class EmailAnalyzer516:
    def __init__(self):
        self.export_utils = ExportUtils516()
    
    def validate_email(self, email: str) -> Dict[str, Any]:
        """Validate email format and domain"""
        result = {
            'email': email,
            'is_valid_format': False,
            'domain': None,
            'mx_records': [],
            'syntax_analysis': {}
        }
        
        # Basic email validation regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        result['is_valid_format'] = bool(re.match(pattern, email))
        
        if result['is_valid_format']:
            result['domain'] = email.split('@')[1]
            result['mx_records'] = self._check_mx_records(result['domain'])
            
            # Syntax analysis
            result['syntax_analysis'] = {
                'local_part': email.split('@')[0],
                'domain_part': result['domain'],
                'length': len(email),
                'has_special_chars': bool(re.search(r'[._%+-]', email.split('@')[0]))
            }
        
        return result
    
    def _check_mx_records(self, domain: str) -> list:
        """Check MX records for domain"""
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            mx_records = []
            for rdata in answers:
                mx_records.append({
                    'preference': rdata.preference,
                    'exchange': str(rdata.exchange)
                })
            return mx_records
        except Exception as e:
            logger.warning(f"Could not resolve MX records for {domain}: {e}")
            return []
    
    def analyze_email_pattern(self, email: str) -> Dict[str, Any]:
        """Analyze email pattern for OSINT"""
        local_part = email.split('@')[0]
        
        analysis = {
            'possible_name_components': [],
            'possible_initial': None,
            'possible_year': None,
            'separators_used': [],
            'pattern_type': 'unknown'
        }
        
        # Check for common patterns
        if '.' in local_part:
            analysis['separators_used'].append('dot')
            parts = local_part.split('.')
            if len(parts) == 2:
                analysis['pattern_type'] = 'first.last'
                analysis['possible_name_components'] = parts
        
        if '_' in local_part:
            analysis['separators_used'].append('underscore')
        
        if '-' in local_part:
            analysis['separators_used'].append('hyphen')
        
        # Look for years
        year_match = re.search(r'(19|20)\d{2}', local_part)
        if year_match:
            analysis['possible_year'] = year_match.group()
        
        return analysis
    
    def bulk_analyze(self, emails: list) -> Dict[str, Any]:
        """Analyze multiple emails"""
        results = {
            'total_emails': len(emails),
            'valid_emails': 0,
            'invalid_emails': 0,
            'domains_found': set(),
            'analysis_results': []
        }
        
        for email in emails:
            analysis = self.validate_email(email.strip())
            results['analysis_results'].append(analysis)
            
            if analysis['is_valid_format']:
                results['valid_emails'] += 1
                results['domains_found'].add(analysis['domain'])
            else:
                results['invalid_emails'] += 1
        
        results['domains_found'] = list(results['domains_found'])
        
        return results

def main():
    parser = argparse.ArgumentParser(description='516 Hackers - Email Analyzer')
    parser.add_argument('email', nargs='?', help='Single email to analyze')
    parser.add_argument('-f', '--file', help='File containing list of emails')
    parser.add_argument('-o', '--output', default='outputs', help='Output directory')
    
    args = parser.parse_args()
    
    analyzer = EmailAnalyzer516()
    
    if args.email:
        print(f"📧 516 Hackers - Analyzing email: {args.email}")
        result = analyzer.validate_email(args.email)
        pattern_analysis = analyzer.analyze_email_pattern(args.email)
        
        combined_result = {
            'email_validation': result,
            'pattern_analysis': pattern_analysis,
            'tool': '516 Hackers Email Analyzer'
        }
        
        filename = analyzer.export_utils.export_json(combined_result, f"email_analysis_{args.email}")
        
        print(f"✅ Format Valid: {result['is_valid_format']}")
        print(f"🌐 Domain: {result['domain']}")
        print(f"📨 MX Records: {len(result['mx_records'])} found")
        print(f"📁 Results saved to: {filename}")
    
    elif args.file:
        print(f"📁 Analyzing emails from file: {args.file}")
        try:
            with open(args.file, 'r') as f:
                emails = [line.strip() for line in f if line.strip()]
            
            results = analyzer.bulk_analyze(emails)
            filename = analyzer.export_utils.export_json(results, "bulk_email_analysis")
            
            print(f"✅ Processed {results['total_emails']} emails")
            print(f"📧 Valid: {results['valid_emails']}")
            print(f"❌ Invalid: {results['invalid_emails']}")
            print(f"🌐 Unique domains: {len(results['domains_found'])}")
            print(f"📁 Results saved to: {filename}")
        
        except FileNotFoundError:
            print(f"❌ File not found: {args.file}")
    
    else:
        print("❌ Please provide an email or file with -f option")

if __name__ == "__main__":
    main()
