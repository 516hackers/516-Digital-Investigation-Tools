
# Contributing to 516 Digital Investigation Tools

We love your input! We want to make contributing to 516 Digital Investigation Tools as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## 🎯 Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## 🐛 Bug Reports

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/516hackers/516-Digital-Investigation-Tools/issues/new).

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## 💡 Feature Requests

We welcome feature requests! Please provide:

1. Use case description
2. Expected behavior
3. Proposed implementation (if you have ideas)
4. Any alternative solutions considered

## 📝 Pull Request Process

1. **Fork the Repository**
   ```bash
   git clone https://github.com/516hackers/516-Digital-Investigation-Tools.git
   cd 516-Digital-Investigation-Tools
   ```

2. **Set Up Development Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e .
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **Make Your Changes**
   - Follow our code style
   - Add tests for new functionality
   - Update documentation
   - Ensure all tests pass

5. **Test Your Changes**
   ```bash
   # Run all tests
   python -m pytest tests/
   
   # Run specific test file
   python -m pytest tests/test_metadata.py
   
   # Check code style
   flake8 scripts/ utils/ tests/
   ```

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add amazing feature"
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**

## 🏗️ Code Style Guide

### Python Code Style
- Follow PEP 8 guidelines
- Use 4 spaces for indentation
- Maximum line length: 88 characters
- Use descriptive variable names
- Add docstrings to all functions and classes

**Example:**
```python
def extract_metadata(image_path: str) -> Dict[str, Any]:
    """
    Extract EXIF metadata from image file.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary containing extracted metadata
        
    Raises:
        FileNotFoundError: If image file doesn't exist
        ValueError: If file is not a supported image format
    """
    # Your code here
```

### Documentation
- Update relevant documentation in `docs/` directory
- Add examples for new features
- Include API references for new functions

### Testing
- Write tests for new functionality
- Ensure existing tests continue to pass
- Test edge cases and error conditions

## 🎨 Project Structure

```
516-Digital-Investigation-Tools/
├── scripts/           # Main tool scripts
├── utils/            # Utility functions
├── config/           # Configuration files
├── tests/            # Test cases
├── docs/             # Documentation
├── examples/         # Usage examples
└── outputs/          # Generated outputs (gitignored)
```

## 🔧 Adding New Tools

When adding a new investigation tool:

1. **Create the script** in `scripts/` directory
2. **Follow naming convention**: `tool_name.py`
3. **Add command-line interface** using argparse
4. **Import in `scripts/__init__.py`**
5. **Update `setup.py`** with new entry point
6. **Add tests** in `tests/` directory
7. **Update documentation** in `docs/` directory
8. **Add example** in `examples/` directory

### Tool Template
```python
#!/usr/bin/env python3
"""
516 Digital Investigation Tools - [Tool Name]
[Brief description of the tool]
"""

import argparse
from typing import Dict, Any
from utils.logger import logger
from utils.export_utils import ExportUtils516

class ToolName516:
    def __init__(self, output_dir="outputs"):
        self.export_utils = ExportUtils516(output_dir)
    
    def main_functionality(self, target: str) -> Dict[str, Any]:
        """Main functionality implementation"""
        try:
            # Your code here
            results = {}
            return results
        except Exception as e:
            logger.error(f"Error processing {target}: {e}")
            return {'error': str(e)}

def main():
    parser = argparse.ArgumentParser(
        description='516 Digital Investigation Tools - [Tool Name]'
    )
    parser.add_argument('target', help='Target to investigate')
    parser.add_argument('-o', '--output', default='outputs', help='Output directory')
    
    args = parser.parse_args()
    
    # Tool execution logic
    tool = ToolName516(args.output)
    results = tool.main_functionality(args.target)
    
    # Export results
    filename = tool.export_utils.export_json(results, f"toolname_{args.target}")
    print(f"Results saved to: {filename}")

if __name__ == "__main__":
    main()
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_metadata.py

# Run with coverage
python -m pytest --cov=scripts tests/

# Run with verbose output
python -m pytest -v
```

### Writing Tests
```python
"""
Test cases for [Tool Name]
"""

import unittest
import tempfile
import os
from scripts.tool_name import ToolName516

class TestToolName516(unittest.TestCase):
    
    def setUp(self):
        self.tool = ToolName516()
    
    def test_basic_functionality(self):
        """Test basic tool functionality"""
        result = self.tool.main_functionality("test_target")
        self.assertIn('key_metric', result)
    
    def test_error_handling(self):
        """Test error handling"""
        result = self.tool.main_functionality("invalid_target")
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
```

## 📊 Reporting Issues

When reporting issues, please include:

- **OS and Python version**
- **Tool version**
- **Error messages and stack traces**
- **Steps to reproduce**
- **Expected vs actual behavior**

## 🤝 Community

- **Be respectful and inclusive**
- **Help others** when you can
- **Provide constructive feedback**
- **Follow the code of conduct**

## 🏆 Recognition

Contributors will be recognized in:
- Project README
- Release notes
- GitHub contributors page

## ❓ Questions?

- Check existing documentation in `docs/` directory
- Look at existing issues and pull requests
- Create a new issue for questions

---

<div align="center">

**Thank you for contributing to 516 Digital Investigation Tools!** 🎉

[![516 Hackers](https://img.shields.io/badge/516-Hackers-blue)](https://github.com/516hackers)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>
