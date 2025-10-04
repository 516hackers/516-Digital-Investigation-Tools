
"""
516 Hackers - Domain Research Tool
Domain information and reputation analysis
"""

import whois
import requests
import socket
import argparse
from datetime import datetime
from utils.logger import logger
from utils.export_utils import ExportUtils516

class DomainResearch516:
    def __init__(self):
        self.export_utils = ExportUtils516()
    
    def get_whois_info(self, domain: str) -> Dict[str, Any]:
        """Get WHOIS information for domain"""
        try:
            whois_data = whois.whois(domain)
            
            # Convert to serializable format
            result = {}
            for key, value in whois_data.items():
                if hasattr(value, '__dict__'):
                    result[key] = str(value)
                else:
                    result[key] = value
            
            return result
        except Exception as e:
            logger.error(f"WHOIS lookup failed for {domain}: {e}")
            return {'error': str(e)}
    
    def get_dns_info(self, domain: str) -> Dict[str, Any]:
        """Get DNS information"""
        import dns.resolver
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
        dns_results = {}
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                dns_results[record_type] = [str(rdata) for rdata in answers]
            except Exception as e:
                dns_results[record_type] = f"Error: {e}"
        
        return dns_results
    
    def check_http_headers(self, domain: str) -> Dict[str, Any]:
        """Analyze HTTP headers"""
        try:
            response = requests.get(f"http://{domain}", timeout=10, allow_redirects=True)
            headers_analysis = {
                'status_code': response.status_code,
                'final_url': response.url,
                'headers': dict(response.headers),
                'server': response.headers.get('Server', 'Unknown'),
                'content_type': response.headers.get('Content-Type', 'Unknown'),
                'security_headers': {}
            }
            
            # Check security headers
            security_headers = [
                'Strict-Transport-Security',
                'Content-Security-Policy', 
                'X-Frame-Options',
                'X-Content-Type-Options',
                'X-XSS-Protection'
            ]
            
            for header in security_headers:
                headers_analysis['security_headers'][header] = response.headers.get(header, 'Not Present')
            
            return headers_analysis
        except Exception as e:
            return {'error': str(e)}
    
    def get_ip_info(self, domain: str) -> Dict[str, Any]:
        """Get IP address information"""
        try:
            ip_address = socket.gethostbyname(domain)
            
            # Basic IP information
            ip_info = {
                'ip_address': ip_address,
                'hostname': domain,
                'resolved_at': datetime.now().isoformat()
            }
            
            # Optional: Reverse DNS lookup
            try:
                hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip_address)
                ip_info['reverse_dns'] = {
                    'hostname': hostname,
                    'aliases': aliaslist,
                    'ip_addresses': ipaddrlist
                }
            except socket.herror:
                ip_info['reverse_dns'] = 'Not available'
            
            return ip_info
        except Exception as e:
            return {'error': str(e)}
    
    def comprehensive_analysis(self, domain: str) -> Dict[str, Any]:
        """Perform comprehensive domain analysis"""
        print(f"🔍 Analyzing domain: {domain}")
        
        results = {
            'domain': domain,
            'analysis_date': datetime.now().isoformat(),
            'whois_info': self.get_whois_info(domain),
            'dns_info': self.get_dns_info(domain),
            'http_headers': self.check_http_headers(domain),
            'ip_info': self.get_ip_info(domain),
            'tool': '516 Hackers Domain Research'
        }
        
        return results

def main():
    parser = argparse.ArgumentParser(description='516 Hackers - Domain Research')
    parser.add_argument('domain', help='Domain to research')
    parser.add_argument('-o', '--output', default='outputs', help='Output directory')
    
    args = parser.parse_args()
    
    researcher = DomainResearch516()
    
    print(f"🌐 516 Hackers - Domain Research: {args.domain}")
    print("=" * 50)
    
    results = researcher.comprehensive_analysis(args.domain)
    
    # Export results
    filename = researcher.export_utils.export_json(results, f"domain_research_{args.domain}")
    
    # Print summary
    print(f"✅ WHOIS Info: {'Available' if 'error' not in results['whois_info'] else 'Error'}")
    print(f"✅ DNS Records: {len(results['dns_info'])} types found")
    print(f"✅ HTTP Headers: {'Available' if 'error' not in results['http_headers'] else 'Error'}")
    print(f"✅ IP Information: {'Available' if 'error' not in results['ip_info'] else 'Error'}")
    print(f"📁 Full report saved to: {filename}")

if __name__ == "__main__":
    main()
