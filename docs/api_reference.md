

## Core Classes

### Sherlock516
Username search across social media platforms.

**Constructor:**
```python
Sherlock516(username: str, output_dir: str = "outputs")
```

**Methods:**
- `check_standard_sites()`: Check common social media platforms
- `save_results()`: Save results to JSON file
- `generate_report()`: Generate summary report

**Example:**
```python
from scripts.sherlock_wrapper import Sherlock516

investigator = Sherlock516("target_user")
investigator.check_standard_sites()
filename = investigator.save_results()
report = investigator.generate_report()
```

### Instagram516
Instagram profile analysis and data extraction.

**Constructor:**
```python
Instagram516(output_dir: str = "outputs")
```

**Methods:**
- `get_profile_info(username)`: Get profile data
- `analyze_engagement(profile_data)`: Calculate engagement metrics
- `save_data(username, profile_data, analysis)`: Save to files

**Example:**
```python
from scripts.enhanced_instaloader import Instagram516

ig = Instagram516()
profile = ig.get_profile_info("instagram_user")
analysis = ig.analyze_engagement(profile)
ig.save_data("instagram_user", profile, analysis)
```

### MetadataAnalyzer516
Image metadata analysis and cleaning.

**Constructor:**
```python
MetadataAnalyzer516(output_dir: str = "outputs")
```

**Methods:**
- `extract_metadata(image_path)`: Extract EXIF metadata
- `clean_metadata(image_path, output_path)`: Remove metadata
- `analyze_multiple(directory_path)`: Batch process images

**Example:**
```python
from scripts.metadata_analyzer import MetadataAnalyzer516

analyzer = MetadataAnalyzer516()
metadata = analyzer.extract_metadata("photo.jpg")
clean_result = analyzer.clean_metadata("photo.jpg", "clean.jpg")
```

## Utility Classes

### ConfigLoader
Configuration management.

**Usage:**
```python
from utils.config_loader import config

# Get configuration values
timeout = config.get('default', 'settings.request_timeout')
platforms = config.get_platforms()
user_agent = config.get_user_agent()
```

### Logger516
Centralized logging.

**Usage:**
```python
from utils.logger import logger

logger.info("Processing started")
logger.warning("Rate limit approaching")
logger.error("API request failed")
```

### ExportUtils516
Data export utilities.

**Usage:**
```python
from utils.export_utils import ExportUtils516

exporter = ExportUtils516()
exporter.export_json(data, "report")
exporter.export_csv(data, "data")
exporter.generate_html_report(data, "My Report")
```

## Function Reference

### Helper Functions
```python
from utils.helpers import *

# Directory management
output_dir = create_output_dir()

# File operations
save_json(data, "file.json")

# Security
file_hash = calculate_file_hash("file.jpg")

# Validation
is_valid = validate_email("test@example.com")

# Display
print_banner()
```

## Data Structures

### Profile Data Structure
```python
{
    "username": "johndoe",
    "full_name": "John Doe",
    "followers": 1500,
    "followees": 300,
    "posts_count": 45,
    "is_private": False,
    "biography": "Sample bio",
    "external_url": "https://example.com",
    "scraped_at": "2024-01-15T10:30:00"
}
```

### Metadata Structure
```python
{
    "filename": "image.jpg",
    "file_size": 1024000,
    "file_hash": "md5_hash",
    "image_format": "JPEG",
    "image_size": [1920, 1080],
    "metadata": {
        "Make": "Camera Maker",
        "Model": "Camera Model",
        "DateTime": "2024:01:15 10:30:00"
    }
}
```

## Error Handling

All methods return dictionaries that may contain error keys:

```python
result = ig.get_profile_info("invalid_user")
if 'error' in result:
    print(f"Error: {result['error']}")
else:
    # Process successful result
    process_profile(result)
```

## Configuration Reference

See `config/default_config.json` for all available settings.

