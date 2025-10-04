
"""
516 Hackers - Image Forensics & Similarity Detection
Image analysis and comparison tool
"""

import os
import imagehash
from PIL import Image
import argparse
import json
from datetime import datetime

class ImageForensics516:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def calculate_hashes(self, image_path):
        """Calculate multiple perceptual hashes for an image"""
        try:
            with Image.open(image_path) as img:
                return {
                    'average_hash': str(imagehash.average_hash(img)),
                    'phash': str(imagehash.phash(img)),
                    'dhash': str(imagehash.dhash(img)),
                    'whash': str(imagehash.whash(img)),
                    'color_hash': str(imagehash.colorhash(img))
                }
        except Exception as e:
            return {'error': str(e)}
    
    def compare_images(self, image1_path, image2_path, threshold=10):
        """Compare two images and return similarity score"""
        try:
            with Image.open(image1_path) as img1, Image.open(image2_path) as img2:
                hash1 = imagehash.average_hash(img1)
                hash2 = imagehash.average_hash(img2)
                
                difference = hash1 - hash2
                similarity = max(0, 100 - (difference / 64) * 100)
                
                return {
                    'image1': image1_path,
                    'image2': image2_path,
                    'hash_difference': int(difference),
                    'similarity_percentage': round(similarity, 2),
                    'is_similar': difference <= threshold
                }
        except Exception as e:
            return {'error': str(e)}
    
    def find_similar_images(self, directory_path, threshold=10):
        """Find similar images in a directory"""
        image_hashes = {}
        supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
        
        # Calculate hashes for all images
        for filename in os.listdir(directory_path):
            if filename.lower().endswith(supported_formats):
                file_path = os.path.join(directory_path, filename)
                hashes = self.calculate_hashes(file_path)
                if 'error' not in hashes:
                    image_hashes[filename] = hashes['average_hash']
        
        # Find similar images
        similar_pairs = []
        processed = set()
        
        for img1, hash1 in image_hashes.items():
            for img2, hash2 in image_hashes.items():
                if img1 != img2 and (img2, img1) not in processed:
                    difference = imagehash.hex_to_hash(hash1) - imagehash.hex_to_hash(hash2)
                    if difference <= threshold:
                        similar_pairs.append({
                            'image1': img1,
                            'image2': img2,
                            'similarity_score': 100 - (difference / 64) * 100,
                            'hash_difference': int(difference)
                        })
                    processed.add((img1, img2))
        
        return similar_pairs
    
    def analyze_image_characteristics(self, image_path):
        """Analyze basic image characteristics"""
        try:
            with Image.open(image_path) as img:
                return {
                    'format': img.format,
                    'size': img.size,
                    'mode': img.mode,
                    'info': dict(img.info) if img.info else {},
                    'is_animated': getattr(img, "is_animated", False),
                    'frames': getattr(img, "n_frames", 1)
                }
        except Exception as e:
            return {'error': str(e)}
    
    def save_analysis(self, data, analysis_type):
        """Save analysis results"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_dir}/image_analysis_{analysis_type}_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump({
                'analysis': data,
                'tool': '516 Hackers Image Forensics',
                'timestamp': datetime.now().isoformat()
            }, f, indent=2)
        
        return filename

def main():
    parser = argparse.ArgumentParser(description='516 Hackers - Image Forensics')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Hash command
    hash_parser = subparsers.add_parser('hash', help='Calculate image hashes')
    hash_parser.add_argument('image', help='Image file path')
    
    # Compare command
    compare_parser = subparsers.add_parser('compare', help='Compare two images')
    compare_parser.add_argument('image1', help='First image file path')
    compare_parser.add_argument('image2', help='Second image file path')
    compare_parser.add_argument('-t', '--threshold', type=int, default=10, help='Similarity threshold')
    
    # Find similar command
    similar_parser = subparsers.add_parser('find-similar', help='Find similar images in directory')
    similar_parser.add_argument('directory', help='Directory to scan')
    similar_parser.add_argument('-t', '--threshold', type=int, default=10, help='Similarity threshold')
    
    args = parser.parse_args()
    
    forensics = ImageForensics516()
    
    if args.command == 'hash':
        hashes = forensics.calculate_hashes(args.image)
        if 'error' in hashes:
            print(f"❌ Error: {hashes['error']}")
        else:
            filename = forensics.save_analysis(hashes, 'hashes')
            print(f"✅ Image hashes calculated:")
            for hash_type, hash_value in hashes.items():
                print(f"   {hash_type}: {hash_value}")
            print(f"📁 Saved to: {filename}")
    
    elif args.command == 'compare':
        comparison = forensics.compare_images(args.image1, args.image2, args.threshold)
        if 'error' in comparison:
            print(f"❌ Error: {comparison['error']}")
        else:
            filename = forensics.save_analysis(comparison, 'comparison')
            status = "✅ SIMILAR" if comparison['is_similar'] else "❌ DIFFERENT"
            print(f"{status} - Similarity: {comparison['similarity_percentage']}%")
            print(f"📁 Saved to: {filename}")
    
    elif args.command == 'find-similar':
        similar_images = forensics.find_similar_images(args.directory, args.threshold)
        filename = forensics.save_analysis(similar_images, 'similar_images')
        print(f"✅ Found {len(similar_images)} similar image pairs")
        for pair in similar_images:
            print(f"   📸 {pair['image1']} ↔ {pair['image2']} ({pair['similarity_score']:.1f}%)")
        print(f"📁 Saved to: {filename}")

if __name__ == "__main__":
    main()
