
"""
516 Hackers - Instagram Data Collector
Enhanced Instaloader wrapper with analytics
"""

import instaloader
import json
import pandas as pd
from datetime import datetime
import argparse
import os

class Instagram516:
    def __init__(self, output_dir="outputs"):
        self.loader = instaloader.Instaloader()
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def get_profile_info(self, username):
        """Get comprehensive profile information"""
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)
            
            profile_data = {
                'username': profile.username,
                'userid': profile.userid,
                'full_name': profile.full_name,
                'biography': profile.biography,
                'followers': profile.followers,
                'followees': profile.followees,
                'posts_count': profile.mediacount,
                'is_private': profile.is_private,
                'is_verified': profile.is_verified,
                'profile_pic_url': profile.profile_pic_url,
                'external_url': profile.external_url,
                'scraped_at': datetime.now().isoformat()
            }
            
            return profile_data
        except Exception as e:
            return {'error': str(e)}
    
    def analyze_engagement(self, profile_data):
        """Basic engagement analysis"""
        if 'error' in profile_data:
            return {'error': 'Cannot analyze - profile data missing'}
        
        # Simple engagement metrics
        analysis = {
            'follower_to_following_ratio': round(profile_data['followers'] / profile_data['followees'], 2) if profile_data['followees'] > 0 else 0,
            'posts_per_follower': round(profile_data['posts_count'] / profile_data['followers'], 4) if profile_data['followers'] > 0 else 0,
            'profile_completeness_score': self._calculate_completeness(profile_data)
        }
        
        return analysis
    
    def _calculate_completeness(self, profile_data):
        """Calculate profile completeness score"""
        score = 0
        if profile_data['full_name']: score += 25
        if profile_data['biography']: score += 25
        if profile_data['external_url']: score += 25
        if profile_data['posts_count'] > 0: score += 25
        return score
    
    def save_data(self, username, profile_data, analysis):
        """Save data to files"""
        base_filename = f"{self.output_dir}/instagram_{username}"
        
        # Save JSON
        with open(f"{base_filename}.json", 'w') as f:
            json.dump({
                'profile': profile_data,
                'analysis': analysis,
                'metadata': {
                    'tool': '516 Hackers Instagram Analyzer',
                    'timestamp': datetime.now().isoformat()
                }
            }, f, indent=2)
        
        # Save CSV
        df = pd.DataFrame([profile_data])
        df.to_csv(f"{base_filename}.csv", index=False)
        
        return base_filename

def main():
    parser = argparse.ArgumentParser(description='516 Hackers - Instagram Analyzer')
    parser.add_argument('username', help='Instagram username to analyze')
    parser.add_argument('-o', '--output', default='outputs', help='Output directory')
    
    args = parser.parse_args()
    
    print(f"📸 516 Hackers - Analyzing Instagram profile: {args.username}")
    
    ig = Instagram516(args.output)
    profile_data = ig.get_profile_info(args.username)
    
    if 'error' in profile_data:
        print(f"❌ Error: {profile_data['error']}")
        return
    
    analysis = ig.analyze_engagement(profile_data)
    filename = ig.save_data(args.username, profile_data, analysis)
    
    print(f"✅ Profile analysis complete!")
    print(f"👤 {profile_data['full_name']}")
    print(f"📊 Followers: {profile_data['followers']:,}")
    print(f"📈 Following: {profile_data['followees']:,}")
    print(f"📷 Posts: {profile_data['posts_count']}")
    print(f"💼 External URL: {profile_data['external_url'] or 'None'}")
    print(f"📁 Data saved to: {filename}.json & {filename}.csv")

if __name__ == "__main__":
    main()
