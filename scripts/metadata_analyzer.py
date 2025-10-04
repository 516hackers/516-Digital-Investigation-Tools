
"""
516 Hackers - Metadata Analyzer & Cleaner
EXIF data analysis and cleaning tool
"""

import os
import json
from PIL import Image
from PIL.ExifTags import TAGS
import argparse
import hashlib
from datetime import datetime

class MetadataAnalyzer516:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def extract_metadata(self, image_path):
        """Extract EXIF metadata from image"""
        try:
            image = Image.open(image_path)
            exif_data = image._getexif()
            
            metadata = {
                'filename': os.path.basename(image_path),
                'file_size': os.path.getsize(image_path),
                'file_hash': self._calculate_hash(image_path),
                'image_format': image.format,
                'image_size': image.size,
                'image_mode': image.mode,
                'metadata': {}
            }
            
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    metadata['metadata'][tag] = str(value)
            
            return metadata
        except Exception as e:
            return {'error': str(e)}
    
    def clean_metadata(self, image_path, output_path):
        """Remove metadata from image"""
        try:
            image = Image.open(image_path)
            
            # Create a new image without metadata
            clean_image = Image.new(image.mode, image.size)
            clean_image.putdata(list(image.getdata()))
            
            clean_image.save(output_path, quality=95)
            return {'status': 'success', 'cleaned_file': output_path}
        except Exception as e:
            return {'error': str(e)}
    
    def _calculate_hash(self, file_path):
        """Calculate file hash"""
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def analyze_multiple(self, directory_path):
        """Analyze all images in a directory"""
        results = {}
        supported_formats = ('.jpg', '.jpeg', '.png', '.tiff', '.webp')
        
        for filename in os.listdir(directory_path):
            if filename.lower().endswith(supported_formats):
                file_path = os.path.join(directory_path, filename)
                results[filename] = self.extract_metadata(file_path)
        
        return results
    
    def save_analysis(self, metadata, filename_prefix):
        """Save metadata analysis to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_dir}/metadata_analysis_{filename_prefix}_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump({
                'analysis': metadata,
                'tool': '516 Hackers Metadata Analyzer',
                'timestamp': datetime.now().isoformat()
            }, f, indent=2)
        
        return filename

def main():
    parser = argparse.ArgumentParser(description='516 Hackers - Metadata Analyzer')
    parser.add_argument('path', help='Image file or directory path')
    parser.add_argument('-c', '--clean', action='store_true', help='Clean metadata')
    parser.add_argument('-o', '--output', default='outputs', help='Output directory')
    
    args = parser.parse_args()
    
    analyzer = MetadataAnalyzer516(args.output)
    
    if os.path.isfile(args.path):
        if args.clean:
            output_file = f"cleaned_{os.path.basename(args.path)}"
            result = analyzer.clean_metadata(args.path, output_file)
            if 'error' in result:
                print(f"❌ Error: {result['error']}")
            else:
                print(f"✅ Metadata cleaned: {result['cleaned_file']}")
        else:
            metadata = analyzer.extract_metadata(args.path)
            if 'error' in metadata:
                print(f"❌ Error: {metadata['error']}")
            else:
                filename = analyzer.save_analysis(metadata, os.path.basename(args.path))
                print(f"✅ Metadata extracted and saved to: {filename}")
                print(f"📊 Found {len(metadata.get('metadata', {}))} metadata tags")
    
    elif os.path.isdir(args.path):
        results = analyzer.analyze_multiple(args.path)
        filename = analyzer.save_analysis(results, "directory_scan")
        print(f"✅ Analyzed {len(results)} images")
        print(f"📁 Results saved to: {filename}")

if __name__ == "__main__":
    main()
