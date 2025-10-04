
# Usage Guide

## Quick Start

### Command Line Interface

Each tool can be used from the command line:

```bash
# Username search across social media
sherlock516 username

# Instagram profile analysis  
ig516 instagram_username

# Image metadata analysis
meta516 image.jpg

# Image comparison and forensics
img516 compare image1.jpg image2.jpg

# Social media presence mapping
social516 username

# Email validation and analysis
email516 test@example.com

# Domain research and WHOIS
domain516 example.com

# Generate unified reports
report516
```

### Python API

Import and use the tools in your Python code:

```python
from scripts import Sherlock516, Instagram516, MetadataAnalyzer516

# Username search
investigator = Sherlock516("target_user")
investigator.check_standard_sites()
results = investigator.save_results()

# Instagram analysis
ig = Instagram516()
profile_data = ig.get_profile_info("instagram_user")

# Metadata analysis
analyzer = MetadataAnalyzer516()
metadata = analyzer.extract_metadata("image.jpg")
```

## Tool Overview

### Sherlock516 - Username Search
Searches for usernames across multiple social media platforms.

**Features:**
- 50+ social media platforms
- Rate limiting protection
- JSON/CSV export
- Custom platform support

**Usage:**
```bash
sherlock516 username -o outputs/
```

### Instagram516 - Instagram Analysis
Extracts and analyzes Instagram profile data.

**Features:**
- Profile information extraction
- Engagement metrics
- Post analysis
- Follower/following statistics

**Usage:**
```bash
ig516 username --download-posts
```

### MetadataAnalyzer516 - Image Metadata
Analyzes and cleans image metadata (EXIF data).

**Features:**
- EXIF data extraction
- Metadata cleaning
- Batch processing
- Hash generation

**Usage:**
```bash
meta516 image.jpg --clean
meta516 directory/ --batch
```

## Output Formats

All tools support multiple output formats:

- **JSON**: Raw data for further processing
- **CSV**: Tabular data for spreadsheets
- **HTML**: Formatted reports
- **Excel**: Spreadsheet files

## Configuration

Customize behavior via config files in `config/` directory:

- `default_config.json`: General settings
- `social_platforms.json`: Platform configurations
- `user_agents.json`: HTTP request headers

## Best Practices

1. **Rate Limiting**: Be respectful to APIs and websites
2. **Data Privacy**: Handle output files securely
3. **Error Handling**: Check logs for issues
4. **Updates**: Keep dependencies current

## Getting Help

- Use `--help` with any command for options
- Check `examples/` directory for code samples
- Review logs in `outputs/` directory
- Create issues on GitHub for bugs
