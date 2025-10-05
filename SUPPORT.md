

## 📞 Getting Help

We're here to help you succeed with 516 Digital Investigation Tools! Here are the best ways to get support.

### 🚀 Quick Support Channels

| Channel | Best For | Response Time |
|---------|----------|---------------|
| [GitHub Issues](https://github.com/516hackers/516-Digital-Investigation-Tools/issues) | **Bug reports**, feature requests, technical issues | 1-3 business days |
| [GitHub Discussions](https://github.com/516hackers/516-Digital-Investigation-Tools/discussions) | **Questions**, usage help, community support | 1-5 business days |
| Documentation | **Self-help**, tutorials, guides | Instant |

### 🆘 Emergency Support
For **critical security issues** or **production outages**, please see our [Security Policy](SECURITY.md) for private reporting channels.

## 🔧 Before Asking for Help

To help us help you faster, please check these resources first:

### 1. Check Documentation
- [Installation Guide](docs/installation.md) - Setup and installation issues
- [Usage Guide](docs/usage.md) - How to use the tools
- [Examples](docs/examples.md) - Code examples and patterns
- [API Reference](docs/api_reference.md) - Detailed technical documentation

### 2. Search Existing Issues
- Search [existing issues](https://github.com/516hackers/516-Digital-Investigation-Tools/issues) to see if your problem has already been reported
- Check [closed issues](https://github.com/516hackers/516-Digital-Investigation-Tools/issues?q=is%3Aissue+is%3Aclosed) for solutions

### 3. Run Diagnostics
```bash
# Check installation
python -c "import scripts; print('Installation OK')"

# Run basic tests
python -m pytest tests/test_helpers.py -v

# Check tool availability
investigate516 --help
```

## 🐛 Reporting Issues

When reporting an issue, please include:

### Required Information
```markdown
## Description
[Clear description of the problem]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior
[What you expected to happen]

## Actual Behavior
[What actually happened]

## Environment
- OS: [e.g., Ubuntu 20.04, Windows 11, macOS 12]
- Python Version: [e.g., 3.8.10]
- Tool Version: [e.g., 1.0.0]
```

### Optional but Helpful
- Screenshots or error messages
- Log files from `outputs/` directory
- Configuration files (redact sensitive information)
- Network capture (if relevant)

## 🛠️ Common Solutions

### Installation Issues
```bash
# Fix Python path issues
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Reinstall in development mode
pip install -e .

# Check dependency conflicts
pip check
```

### Tool-Specific Issues

#### 🔍 Username Investigation
```bash
# Check if platforms are accessible
curl -I https://github.com/username

# Increase timeout for slow networks
investigate516 username --timeout 30
```

#### 📸 Instagram Analysis
```bash
# Handle rate limiting - add delays
ig516 username --delay 5

# Use specific Instagram instance
ig516 username --instance instagram.com
```

#### 🖼️ Image Metadata
```bash
# Check image file permissions
ls -la image.jpg

# Try different image format
meta516 image.png
```

#### 🌐 Domain Research
```bash
# Check DNS resolution
nslookup domain.com

# Verify internet connectivity
ping 8.8.8.8
```

## 🎓 Learning Resources

### Tutorials
- [Basic Usage Examples](examples/basic_usage.py)
- [Advanced Scenarios](examples/advanced_scan.py)
- [API Integration Guide](docs/api_reference.md)

### Video Guides
*[Link to video tutorials when available]*

### Community Resources
- [OSINT Framework](https://osintframework.com/)
- [Python for Security](https://github.com/topics/python-security)
- [Digital Forensics Resources](https://www.digital-forensics.org/)

## 🏗️ Development Support

### For Contributors
- [Contributing Guide](CONTRIBUTING.md) - How to contribute code
- [Code of Conduct](CODE_OF_CONDUCT.md) - Community guidelines
- [Development Setup](docs/installation.md#development-setup) - Setting up dev environment

### Building Custom Tools
```python
# Template for new investigation tools
from scripts import BaseInvestigationTool

class MyCustomTool(BaseInvestigationTool):
    def investigate(self, target):
        # Your investigation logic here
        return results
```

## 📚 Frequently Asked Questions

### Q: The tool says "command not found"
**A**: The tools may not be in your PATH. Try:
```bash
# Use Python module syntax
python -m scripts.sherlock_wrapper username

# Or reinstall the package
pip install -e .
```

### Q: Instagram analysis returns "Profile not found"
**A**: This could be due to:
- Profile is private
- Instagram rate limiting
- Network connectivity issues
Try with a public profile first.

### Q: Domain research shows WHOIS errors
**A**: Some domains restrict WHOIS access. Try:
- Different WHOIS servers
- Alternative domain research methods
- Check if domain exists via web browser

### Q: Image metadata extraction fails
**A**: Ensure:
- File is a supported image format (JPEG, PNG, TIFF)
- File is not corrupted
- You have read permissions for the file

### Q: Social media mapping shows inconsistent results
**A**: Platforms may:
- Return different status codes
- Have anti-bot measures
- Be temporarily unavailable
Try running the tool multiple times.

## ⏱️ Support Response Times

| Issue Type | Initial Response | Resolution Target |
|------------|------------------|-------------------|
| Critical Security Issue | 24 hours | 7 days |
| Bug Reports | 2 business days | 14 days |
| Feature Requests | 3 business days | 30 days |
| Usage Questions | 5 business days | N/A |


## 🤝 Community Support

### Help Each Other
- Answer questions in GitHub Discussions
- Share your use cases and solutions
- Improve documentation
- Report bugs you encounter

### Share Your Work
- Write blog posts about your experiences
- Create video tutorials
- Share on social media (tag #516Hackers)

---

<div align="center">

**We're here to help you succeed!** 🚀

[![GitHub Issues](https://img.shields.io/badge/Support-GitHub_Issues-blue)](https://github.com/516hackers/516-Digital-Investigation-Tools/issues)
[![Documentation](https://img.shields.io/badge/Docs-Read_Here-green)](docs/)
[![Community](https://img.shields.io/badge/Community-Discussions-orange)](https://github.com/516hackers/516-Digital-Investigation-Tools/discussions)

</div>
