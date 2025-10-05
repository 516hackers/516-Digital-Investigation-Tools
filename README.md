
# 🔍 516 Digital Investigation Tools

![516 Hackers](https://img.shields.io/badge/516-Hackers-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)
![OSINT](https://img.shields.io/badge/OSINT-Tools-red)
![Forensics](https://img.shields.io/badge/Digital-Forensics-purple)

A comprehensive digital investigation and OSINT toolkit designed for cybersecurity professionals, researchers, and ethical hackers. Perform advanced digital investigations with our all-in-one command-line interface and Python API.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/516hackers/516-Digital-Investigation-Tools.git
cd 516-Digital-Investigation-Tools

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Verify Installation
```bash
# Test installation
python -m pytest tests/

# Run basic examples
python examples/basic_usage.py
```

## 🛠️ Available Tools

| Tool | Command | Description |
|------|---------|-------------|
| 🔍 Username Investigation | `investigate516` | Search across 50+ social media platforms |
| 📸 Instagram Analysis | `ig516` | Extract and analyze Instagram profile data |
| 🖼️ Image Metadata Analysis | `meta516` | Analyze and clean image EXIF metadata |
| 🔬 Image Forensics | `image516` | Image similarity detection and comparison |
| 🌐 Social Media Mapping | `social516` | Cross-platform social media presence mapping |
| 📧 Email Intelligence | `email516` | Email validation and pattern analysis |
| 🌍 Domain Research | `domain516` | WHOIS lookup, DNS analysis, and HTTP inspection |
| 📊 Report Generator | `report516` | Unified report generation in multiple formats |

## 🎯 Usage Guide

### Method 1: Interactive Hacker Interface (Recommended)
```bash
# Run the interactive menu
chmod +x 516-investigator.sh
./516-investigator.sh
```

<img width="547" height="535" alt="image" src="https://github.com/user-attachments/assets/c9ea014f-6a81-4e6f-b196-0295fcf8880d" />


### Method 2: Command Line Tools
```bash
# Username investigation
investigate516 username

# Instagram profile analysis
ig516 instagram_username

# Image metadata analysis
meta516 image.jpg

# Domain research
domain516 example.com

# Email analysis
email516 test@example.com

# Generate reports
report516
```

### Method 3: Python API
```python
from scripts import Sherlock516, Instagram516, MetadataAnalyzer516

# Username investigation
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

## 📖 Detailed Tool Documentation

### 🔍 Username Investigation (`investigate516`)
Search for usernames across multiple social media platforms.

**Features:**
- 50+ social media platforms
- Rate limiting protection
- JSON/CSV export
- Custom platform support

**Usage:**
```bash
investigate516 username -o outputs/
```

**Output:**
- `username_profiles.json` - Detailed platform results
- Summary report in terminal

### 📸 Instagram Analysis (`ig516`)
Extract and analyze Instagram profile data.

**Features:**
- Profile information extraction
- Engagement metrics calculation
- Follower/following analysis
- Post statistics

**Usage:**
```bash
ig516 username --download-posts
```

**Output:**
- `instagram_username.json` - Profile data and analysis
- `instagram_username.csv` - Tabular data export

### 🖼️ Image Metadata Analysis (`meta516`)
Analyze and clean image metadata (EXIF data).

**Features:**
- EXIF data extraction
- Metadata cleaning
- Batch processing
- Hash generation

**Usage:**
```bash
# Single image analysis
meta516 image.jpg

# Clean metadata
meta516 image.jpg --clean

# Batch process directory
meta516 directory/ --batch
```

**Output:**
- `metadata_analysis_*.json` - Extracted metadata
- Cleaned image files (with `--clean`)

### 🔬 Image Forensics (`image516`)
Image similarity detection and forensic analysis.

**Features:**
- Perceptual hashing
- Image comparison
- Duplicate detection
- Hash-based similarity

**Usage:**
```bash
# Compare two images
image516 compare image1.jpg image2.jpg

# Find similar images in directory
image516 find-similar images/ -t 5

# Calculate image hashes
image516 hash image.jpg
```

**Output:**
- Similarity scores and comparison results
- Hash values for images

### 🌐 Social Media Mapping (`social516`)
Map social media presence across platforms.

**Features:**
- 8 major social platforms
- Response time tracking
- Discovery rate calculation
- Comprehensive reporting

**Usage:**
```bash
social516 username
```

**Output:**
- `social_map_username_*.json` - Platform presence data
- Summary with discovery rate

### 📧 Email Intelligence (`email516`)
Email validation and intelligence gathering.

**Features:**
- Email format validation
- Domain MX record checking
- Pattern analysis
- Bulk processing

**Usage:**
```bash
# Single email analysis
email516 test@example.com

# Bulk analysis from file
email516 -f emails.txt
```

**Output:**
- Validation results
- Pattern analysis
- Domain information

### 🌍 Domain Research (`domain516`)
Comprehensive domain investigation.

**Features:**
- WHOIS information lookup
- DNS record analysis
- HTTP header inspection
- IP information

**Usage:**
```bash
domain516 example.com
```

**Output:**
- `domain_research_*.json` - Complete domain analysis
- WHOIS, DNS, and HTTP data

### 📊 Report Generator (`report516`)
Generate unified reports from multiple investigations.

**Features:**
- Combine results from all tools
- Multiple export formats (JSON, CSV, HTML, Excel)
- Executive summaries
- Risk assessment

**Usage:**
```bash
report516 -d outputs/
```

**Output:**
- Unified reports in multiple formats
- Executive summaries
- Risk assessments

## 🏗️ Project Structure

```
516-Digital-Investigation-Tools/
├── scripts/              # Main investigation tools
│   ├── sherlock_wrapper.py      # Username investigation
│   ├── enhanced_instaloader.py  # Instagram analysis
│   ├── metadata_analyzer.py     # Image metadata
│   ├── image_forensics.py       # Image comparison
│   ├── social_media_mapper.py   # Social media mapping
│   ├── email_analyzer.py        # Email intelligence
│   ├── domain_research.py       # Domain research
│   └── report_generator.py      # Report generation
├── utils/               # Utility functions
│   ├── helpers.py              # Common utilities
│   ├── config_loader.py        # Configuration management
│   ├── logger.py               # Logging utilities
│   └── export_utils.py         # Data export functions
├── config/              # Configuration files
│   ├── default_config.json     # Main configuration
│   ├── social_platforms.json   # Social media platforms
│   └── user_agents.json        # HTTP user agents
├── outputs/             # Analysis results and reports
├── docs/                # Documentation
│   ├── installation.md         # Installation guide
│   ├── usage.md               # Usage instructions
│   ├── examples.md            # Code examples
│   └── api_reference.md       # API documentation
├── tests/               # Test cases
├── examples/            # Usage examples
└── 516-investigator.sh # Interactive hacker interface
```

## 🔧 Configuration

### Customizing Settings
Edit `config/default_config.json` to customize tool behavior:

```json
{
    "settings": {
        "output_directory": "outputs",
        "request_timeout": 10,
        "max_workers": 5,
        "log_level": "INFO"
    },
    "social_media": {
        "enable_instagram": true,
        "enable_twitter": true,
        "enable_github": true
    }
}
```

### Adding Social Media Platforms
Edit `config/social_platforms.json` to add custom platforms:

```json
{
    "custom_platform": {
        "name": "Custom Platform",
        "url": "https://custom.com/{}",
        "check_type": "http_status"
    }
}
```

## 🐛 Troubleshooting

### Common Issues

**Installation Errors:**
```bash
# Fix permission issues
pip install --user -r requirements.txt

# Upgrade pip
pip install --upgrade pip

# Set Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**Tool-Specific Issues:**
- **Instagram Rate Limiting**: Tools include built-in rate limiting
- **WHOIS Lookup Failures**: Some domains may restrict WHOIS access
- **Image Processing**: Ensure Pillow supports your image format

### Getting Help
1. Check the logs in `outputs/` directory
2. Use `--help` with any command for options
3. Review examples in `examples/` directory
4. Check existing issues on GitHub

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Set up development environment
git clone https://github.com/516hackers/516-Digital-Investigation-Tools.git
cd 516-Digital-Investigation-Tools
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
pip install -e .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```text
MIT License

Copyright (c) 2024 516 Hackers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## ⚠️ Legal Disclaimer

**This toolkit is intended for:**

- ✅ Legal digital investigations
- ✅ Authorized penetration testing
- ✅ Cybersecurity research
- ✅ Educational purposes
- ✅ Ethical hacking with proper authorization

**Prohibited Uses:**

- ❌ Unauthorized access to systems
- ❌ Illegal surveillance
- ❌ Harassment or stalking
- ❌ Any unlawful activities

**Users are responsible for:**
- Ensuring they have proper authorization before conducting investigations
- Complying with local laws and regulations
- Using the tools ethically and responsibly

## 🛡️ Security Best Practices

1. **Authorization**: Always obtain proper authorization before investigations
2. **Data Handling**: Securely store and handle investigation results
3. **Rate Limiting**: Respect API rate limits and terms of service
4. **Legal Compliance**: Ensure compliance with relevant laws and regulations
5. **Ethical Use**: Use tools for legitimate security research and investigations

## 🌟 Features Highlights

- **🔍 Comprehensive OSINT**: Multiple investigation techniques in one toolkit
- **🎯 User-Friendly**: Both CLI and interactive menu interfaces
- **📊 Multiple Formats**: JSON, CSV, HTML, and Excel exports
- **⚡ Fast & Efficient**: Optimized for performance with rate limiting
- **🔧 Extensible**: Easy to add new platforms and tools
- **📝 Well-Documented**: Comprehensive guides and examples

## 📞 Support

- **Documentation**: Check the `docs/` directory for detailed guides
- **Issues**: Create an issue on GitHub for bugs and feature requests
- **Examples**: Review the `examples/` directory for usage patterns

---

<div align="center">

**Made with ❤️ by 516 Hackers**

[![516 Hackers](https://img.shields.io/badge/516-Hackers-blue)](https://github.com/516hackers)
[![Follow](https://img.shields.io/badge/Follow-516_Hackers-green)](https://github.com/516hackers)

*For educational and authorized security research purposes only*

</div>
