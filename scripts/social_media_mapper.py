
"""
516 Hackers - Social Media Presence Mapper
Cross-platform social media analysis
"""

import json
import requests
from datetime import datetime
import argparse
import os

class SocialMediaMapper516:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        self.platforms = {
            'github': {
                'url': 'https://github.com/{}',
                'check': self._check_github
            },
            'twitter': {
                'url': 'https://twitter.com/{}',
                'check': self._check_twitter
            },
            'instagram': {
                'url': 'https://instagram.com/{}',
                'check': self._check_instagram
            },
            'linkedin': {
                'url': 'https://linkedin.com/in/{}',
                'check': self._check_linkedin
            },
            'reddit': {
                'url': 'https://reddit.com/user/{}',
                'check': self._check_reddit
            },
            'youtube': {
                'url': 'https://youtube.com/@{}/',
                'check': self._check_youtube
            }
        }
    
    def map_presence(self, username):
        """Map social media presence for a username"""
        results = {
            'username': username,
            'timestamp': datetime.now().isoformat(),
            'platforms': {}
        }
        
        found_count = 0
        
        for platform, info in self.platforms.items():
            print(f"🔍 Checking {platform}...")
            platform_result = info['check'](username, info['url'])
            results['platforms'][platform] = platform_result
            
            if platform_result['exists']:
                found_count += 1
                print(f"   ✅ Found on {platform}")
            else:
                print(f"   ❌ Not found on {platform}")
        
        results['summary'] = {
            'total_platforms_checked': len(self.platforms),
            'platforms_found': found_count,
            'discovery_rate': round((found_count / len(self.platforms)) * 100, 2)
        }
        
        return results
    
    def _check_github(self, username, url_pattern):
        """Check GitHub presence"""
        try:
            url = url_pattern.format(username)
            response = requests.get(url, timeout=10)
            return {
                'url': url,
                'exists': response.status_code == 200,
                'response_time': response.elapsed.total_seconds()
            }
        except:
            return {'url': url_pattern.format(username), 'exists': False, 'error': 'Request failed'}
    
    def _check_twitter(self, username, url_pattern):
        """Check Twitter presence"""
        try:
            url = url_pattern.format(username)
            response = requests.get(url, timeout=10)
            return {
                'url': url,
                'exists': response.status_code == 200,
                'response_time': response.elapsed.total_seconds()
            }
        except:
            return {'url': url_pattern.format(username), 'exists': False, 'error': 'Request failed'}
    
    def _check_instagram(self, username, url_pattern):
        """Check Instagram presence"""
        try:
            url = url_pattern.format(username)
            response = requests.get(url, timeout=10)
            return {
                'url': url,
                'exists': response.status_code == 200,
                'response_time': response.elapsed.total_seconds()
            }
        except:
            return {'url': url_pattern.format(username), 'exists': False, 'error': 'Request failed'}
    
    def _check_linkedin(self, username, url_pattern):
        """Check LinkedIn presence"""
        try:
            url = url_pattern.format(username)
            response = requests.get(url, timeout=10)
            # LinkedIn might return 999 for some cases
            return {
                'url': url,
                'exists': response.status_code in [200, 999],
                'response_time': response.elapsed.total_seconds()
            }
        except:
            return {'url': url_pattern.format(username), 'exists': False, 'error': 'Request failed'}
    
    def _check_reddit(self, username, url_pattern):
        """Check Reddit presence"""
        try:
            url = url_pattern.format(username)
            response = requests.get(url, timeout=10)
            return {
                'url': url,
                'exists': response.status_code == 200,
                'response_time': response.elapsed.total_seconds()
            }
        except:
            return {'url': url_pattern.format(username), 'exists': False, 'error': 'Request failed'}
    
    def _check_youtube(self, username, url_pattern):
        """Check YouTube presence"""
        try:
            url = url_pattern.format(username)
            response = requests.get(url, timeout=10)
            return {
                'url': url,
                'exists': response.status_code == 200,
                'response_time': response.elapsed.total_seconds()
            }
        except:
            return {'url': url_pattern.format(username), 'exists': False, 'error': 'Request failed'}
    
    def generate_report(self, results):
        """Generate a comprehensive report"""
        report = f"""
516 Hackers - Social Media Presence Report
===========================================

Target Username: {results['username']}
Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Summary:
--------
• Platforms Checked: {results['summary']['total_platforms_checked']}
• Platforms Found: {results['summary']['platforms_found']}
• Discovery Rate: {results['summary']['discovery_rate']}%

Detailed Results:
----------------
"""
        for platform, data in results['platforms'].items():
            status = "✅ FOUND" if data['exists'] else "❌ NOT FOUND"
            report += f"• {platform.upper()}: {status}\n"
            report += f"  URL: {data['url']}\n"
            if 'response_time' in data:
                report += f"  Response Time: {data['response_time']:.2f}s\n"
            report += "\n"
        
        return report
    
    def save_results(self, results, filename_prefix):
        """Save results to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_dir}/social_map_{filename_prefix}_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump({
                'results': results,
                'tool': '516 Hackers Social Media Mapper',
                'timestamp': datetime.now().isoformat()
            }, f, indent=2)
        
        return filename

def main():
    parser = argparse.ArgumentParser(description='516 Hackers - Social Media Mapper')
    parser.add_argument('username', help='Username to search across social media')
    parser.add_argument('-o', '--output', default='outputs', help='Output directory')
    
    args = parser.parse_args()
    
    print(f"🌐 516 Hackers - Mapping social media presence for: {args.username}")
    print("=" * 60)
    
    mapper = SocialMediaMapper516(args.output)
    results = mapper.map_presence(args.username)
    
    report = mapper.generate_report(results)
    filename = mapper.save_results(results, args.username)
    
    print(report)
    print(f"📁 Full results saved to: {filename}")

if __name__ == "__main__":
    main()
