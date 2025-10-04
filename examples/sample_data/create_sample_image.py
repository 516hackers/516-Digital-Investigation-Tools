#!/usr/bin/env python3
"""
516 Hackers - Sample Image Creator
Creates a sample image with EXIF metadata for testing
"""

from PIL import Image, ImageDraw, ExifTags
from datetime import datetime
import os

def create_sample_image():
    """Create a sample image with EXIF metadata"""
    
    # Create output directory
    os.makedirs('examples/sample_data', exist_ok=True)
    
    # Create a new image
    width, height = 800, 600
    image = Image.new('RGB', (width, height), color='lightblue')
    draw = ImageDraw.Draw(image)
    
    # Add some sample content
    draw.rectangle([100, 100, 700, 500], outline='darkblue', width=5)
    draw.text((width//2 - 100, height//2 - 30), "516 Hackers", fill='darkred', font_size=40)
    draw.text((width//2 - 150, height//2 + 30), "Sample Image for Testing", fill='darkgreen', font_size=20)
    draw.text((width//2 - 200, height//2 + 80), "Created: " + datetime.now().strftime("%Y-%m-%d"), fill='black', font_size=16)
    
    # Add EXIF metadata
    exif_data = image.getexif()
    
    # Add standard EXIF tags
    exif_data[271] = "CameraBrand"  # Make
    exif_data[272] = "DSLR-5000"    # Model
    exif_data[306] = datetime.now().strftime("%Y:%m:%d %H:%M:%S")  # DateTime
    exif_data[305] = "PIL"  # Software
    exif_data[33432] = "Copyright 2024 516 Hackers"  # Copyright
    
    # Add GPS data (optional - sample coordinates for New York)
    exif_data[34853] = b''  # GPS IFD pointer
    
    # Save the image with metadata
    output_path = 'examples/sample_data/sample_image.jpg'
    image.save(output_path, 'JPEG', quality=95, exif=exif_data)
    
    print(f"✅ Sample image created: {output_path}")
    print(f"📏 Image size: {width}x{height}")
    print(f"📊 File size: {os.path.getsize(output_path)} bytes")
    
    # Display created metadata
    print("\n📋 Sample EXIF Metadata:")
    print(f"  - Make: CameraBrand")
    print(f"  - Model: DSLR-5000")
    print(f"  - DateTime: {datetime.now().strftime('%Y:%m:%d %H:%M:%S')}")
    print(f"  - Software: PIL")
    print(f"  - Copyright: Copyright 2024 516 Hackers")
    
    return output_path

def verify_image_metadata(image_path):
    """Verify the created image has metadata"""
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        if exif_data:
            print(f"\n🔍 Verifying metadata in {image_path}:")
            for tag_id, value in exif_data.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                print(f"  - {tag}: {value}")
        else:
            print("❌ No EXIF metadata found")
            
    except Exception as e:
        print(f"❌ Error reading metadata: {e}")

if __name__ == "__main__":
    print("🎯 516 Hackers - Sample Image Creator")
    print("=" * 50)
    
    # Create sample image
    image_path = create_sample_image()
    
    # Verify metadata
    verify_image_metadata(image_path)
    
    print(f"\n🎉 Sample image ready for testing metadata analysis tools!")
    print("💡 Use: python scripts/metadata_analyzer.py examples/sample_data/sample_image.jpg")
