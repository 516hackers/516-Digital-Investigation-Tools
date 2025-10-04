#!/usr/bin/env python3
"""
516 Hackers - Unified Report Generator
Combine results from multiple tools into comprehensive reports
"""

import json
import os
from datetime import datetime
from utils.export_utils import ExportUtils516
from utils.logger import logger

class ReportGenerator516:
    def __init__(self):
        self.export_utils = ExportUtils516()
    
    def generate_unified_report(self, data_sources: dict, title: str = "516 Hackers OSINT Report") -> str:
        """Generate unified report from multiple data sources"""
        
        report = {
            'metadata': {
                'title': title,
                'generated_by': '516 Hackers OSINT Toolkit',
                'timestamp': datetime.now().isoformat(),
                'version': '1.0.0'
            },
            'executive_summary': self._generate_executive_summary(data_sources),
            'detailed_findings': data_sources,
            'recommendations': self._generate_recommendations(data_sources)
        }
        
        return report
    
    def _generate_executive_summary(self, data_sources: dict) -> dict:
        """Generate executive summary"""
        summary = {
            'total_data_sources': len(data_sources),
            'tools_used': list(data_sources.keys()),
            'key_findings': [],
            'risk_assessment': 'Low'  # Default, can be enhanced
        }
        
        # Analyze findings
        for tool, data in data_sources.items():
            if 'social_media' in tool.lower():
                if 'platforms_found' in str(data):
                    summary['key_findings'].append(f"Social media presence detected")
            
            if 'email' in tool.lower():
                if 'valid_emails' in str(data):
                    summary['key_findings'].append(f"Email analysis completed")
            
            if 'domain' in tool.lower():
                if 'whois_info' in str(data):
                    summary['key_findings'].append(f"Domain research completed")
        
        return summary
    
    def _generate_recommendations(self, data_sources: dict) -> list:
        """Generate recommendations based on findings"""
        recommendations = []
        
        # Social media recommendations
        if any('social' in tool.lower() for tool in data_sources.keys()):
            recommendations.extend([
                "Review social media privacy settings",
                "Consider removing or limiting publicly available personal information",
                "Monitor for impersonation accounts"
            ])
        
        # Email recommendations
        if any('email' in tool.lower() for tool in data_sources.keys()):
            recommendations.extend([
                "Use email aliases for different services",
                "Enable two-factor authentication",
                "Monitor for data breaches involving your email"
            ])
        
        # Domain recommendations  
        if any('domain' in tool.lower() for tool in data_sources.keys()):
            recommendations.extend([
                "Ensure domain registration information is accurate",
                "Implement proper security headers on websites",
                "Regularly update DNS records"
            ])
        
        return recommendations
    
    def load_results_from_directory(self, directory: str) -> dict:
        """Load previous results from output directory"""
        results = {}
        
        for filename in os.listdir(directory):
            if filename.endswith('.json') and '516' in filename:
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                        tool_name = data.get('tool', 'Unknown Tool')
                        results[tool_name] = data
                except Exception as e:
                    logger.warning(f"Could not load {filename}: {e}")
        
        return results

def main():
    parser = argparse.ArgumentParser(description='516 Hackers - Report Generator')
    parser.add_argument('-d', '--directory', default='outputs', help='Directory containing result files')
    parser.add_argument('-t', '--title', default='516 Hackers OSINT Report', help='Report title')
    
    args = parser.parse_args()
    
    generator = ReportGenerator516()
    
    print(f"📊 516 Hackers - Generating Unified Report")
    print("=" * 50)
    
    # Load existing results
    results = generator.load_results_from_directory(args.directory)
    
    if not results:
        print("❌ No result files found in directory")
        return
    
    # Generate unified report
    unified_report = generator.generate_unified_report(results, args.title)
    
    # Export in multiple formats
    export_results = generator.export_utils.export_multiple_formats(
        unified_report, 
        "unified_osint_report"
    )
    
    print(f"✅ Generated unified report from {len(results)} data sources")
    for format_name, filename in export_results.items():
        print(f"   📁 {format_name.upper()}: {filename}")
    
    print(f"📋 Executive Summary:")
    summary = unified_report['executive_summary']
    print(f"   • Tools Used: {', '.join(summary['tools_used'])}")
    print(f"   • Key Findings: {len(summary['key_findings'])}")
    print(f"   • Risk Assessment: {summary['risk_assessment']}")

if __name__ == "__main__":
    main()
