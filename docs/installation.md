
# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Installation Methods

### Method 1: Clone from GitHub (Recommended)

```bash
# Clone the repository
git clone https://github.com/516hackers/516-Digital-Investigation-Tools.git
cd 516-Digital-Investigation-Tools

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### Method 2: Install via pip (When published)

```bash
pip install 516-digital-investigation-tools
```

## Dependencies

The toolkit requires these Python packages:

- **Pillow**: Image processing and EXIF data
- **requests**: HTTP requests for web scraping
- **instaloader**: Instagram data extraction
- **imagehash**: Image similarity detection
- **pandas**: Data analysis and export
- **python-whois**: Domain WHOIS information
- **dnspython**: DNS record lookup

## Verification

Test your installation:

```bash
# Run basic tests
python -m pytest tests/

# Try the examples
python examples/basic_usage.py

# Check available commands
sherlock516 --help
```

## Troubleshooting

### Common Issues

1. **Permission Errors on Linux/macOS**
   ```bash
   pip install --user -r requirements.txt
   ```

2. **Missing Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Python Path Issues**
   ```bash
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   ```

## Next Steps

After installation, check out:
- [Usage Guide](usage.md) for how to use the tools
- [Examples](examples.md) for code examples
- [API Reference](api_reference.md) for detailed documentation
