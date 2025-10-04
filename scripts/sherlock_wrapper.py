#!/usr/bin/env python3
"""
516 Hackers - Enhanced Sherlock Wrapper
Extended version of Sherlock with additional features
"""

import os
import json
import asyncio
import requests
from datetime import datetime
import argparse

class Sherlock516:
    def __init__(self, username, output_dir="outputs"):
        self.username = username
        self.output_dir = output_dir
        self.results = {}
        self.found_profiles = []
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
    
    def check_standard_sites(self):
        """Check common social media platforms"""
        sites = {
            'github': f'https://github.com/{self.username}',
            'twitter': f'https://twitter.com/{self.username}',
            'instagram': f'https://instagram.com/{self.username}',
            'linkedin': f'https://linkedin.com/in/{self.username}',
            'facebook': f'https://facebook.com/{self.username}',
            'youtube': f'https://youtube.com/@{self.username}',
            'reddit': f'https://reddit.com/user/{self.username}'
        }
        
        for site, url in sites.items():
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    self.results[site] = {
                        'url': url,
                        'status': 'Found',
                        'timestamp': datetime.now().isoformat()
                    }
                    self.found_profiles.append(site)
                    print(f"✅ Found on {site}: {url}")
                else:
                    self.results[site] = {
                        'url': url,
                        'status': 'Not found',
                        'timestamp': datetime.now().isoformat()
                    }
            except Exception as e:
                self.results[site] = {
                    'url': url,
                    'status': f'Error: {str(e)}',
                    'timestamp': datetime.now().isoformat()
                }
    
    def save_results(self):
        """Save results to JSON file"""
        filename = f"{self.output_dir}/{self.username}_profiles.json"
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        return filename
    
    def generate_report(self):
        """Generate a summary report"""
        report = f"""
516 Hackers - OSINT Report
==========================
Username: {self.username}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Found Profiles: {len(self.found_profiles)}

Platforms Checked:
{chr(10).join([f'- {site}: {data["status"]}' for site, data in self.results.items()])}

Found on: {', '.join(self.found_profiles) if self.found_profiles else 'None'}
        """
        return report

def main():
    parser = argparse.ArgumentParser(description='516 Hackers - Enhanced Sherlock')
    parser.add_argument('username', help='Username to search for')
    parser.add_argument('-o', '--output', default='outputs', help='Output directory')
    
    args = parser.parse_args()
    
    investigator = Sherlock516(args.username, args.output)
    print(f"🔍 516 Hackers - Searching for username: {args.username}")
    
    investigator.check_standard_sites()
    output_file = investigator.save_results()
    report = investigator.generate_report()
    
    print(report)
    print(f"📁 Results saved to: {output_file}")

if __name__ == "__main__":
    main()
