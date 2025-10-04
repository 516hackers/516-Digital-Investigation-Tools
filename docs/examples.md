
## Basic Usage Examples

### 1. Username Search
```python
from scripts.sherlock_wrapper import Sherlock516

# Search for username across social media
investigator = Sherlock516("john_doe", "outputs/")
investigator.check_standard_sites()
results = investigator.save_results()
report = investigator.generate_report()
print(report)
```

### 2. Instagram Profile Analysis
```python
from scripts.enhanced_instaloader import Instagram516

# Analyze Instagram profile
ig = Instagram516("outputs/")
profile_data = ig.get_profile_info("instagram_user")
analysis = ig.analyze_engagement(profile_data)
filename = ig.save_data("instagram_user", profile_data, analysis)

print(f"Followers: {profile_data['followers']}")
print(f"Engagement Score: {analysis['profile_completeness_score']}")
```

### 3. Image Metadata Analysis
```python
from scripts.metadata_analyzer import MetadataAnalyzer516

# Extract metadata from image
analyzer = MetadataAnalyzer516("outputs/")
metadata = analyzer.extract_metadata("photo.jpg")
print(f"Found {len(metadata.get('metadata', {}))} metadata tags")

# Clean metadata from image
clean_result = analyzer.clean_metadata("photo.jpg", "cleaned_photo.jpg")
```

## Advanced Examples

### 4. Bulk Social Media Mapping
```python
from scripts.social_media_mapper import SocialMediaMapper516

# Map multiple usernames
usernames = ["user1", "user2", "user3"]
mapper = SocialMediaMapper516("outputs/")

for username in usernames:
    results = mapper.map_presence(username)
    report = mapper.generate_report(results)
    filename = mapper.save_results(results, username)
    print(f"Completed: {username}")
```

### 5. Email Analysis Batch Processing
```python
from scripts.email_analyzer import EmailAnalyzer516

# Analyze multiple emails from file
analyzer = EmailAnalyzer516()

with open("emails.txt", "r") as f:
    emails = [line.strip() for line in f]

results = analyzer.bulk_analyze(emails)
print(f"Valid emails: {results['valid_emails']}")
print(f"Unique domains: {len(results['domains_found'])}")
```

### 6. Comprehensive Domain Research
```python
from scripts.domain_research import DomainResearch516

# Full domain analysis
researcher = DomainResearch516()
domain_info = researcher.comprehensive_analysis("example.com")

print(f"Domain: {domain_info['domain']}")
print(f"IP Address: {domain_info['ip_info']['ip_address']}")
print(f"MX Records: {len(domain_info['dns_info']['MX'])}")
```

## Integration Examples

### 7. Combined OSINT Investigation
```python
from scripts.sherlock_wrapper import Sherlock516
from scripts.email_analyzer import EmailAnalyzer516
from scripts.report_generator import ReportGenerator516

# Multi-source investigation
target = "target_username"
email = "target@example.com"

# Gather data from multiple sources
username_results = Sherlock516(target).check_standard_sites()
email_results = EmailAnalyzer516().validate_email(email)

# Generate unified report
generator = ReportGenerator516()
combined_data = {
    'username_search': username_results,
    'email_analysis': email_results
}

unified_report = generator.generate_unified_report(
    combined_data, 
    f"OSINT Report for {target}"
)
```

### 8. Automated Image Forensics
```python
from scripts.image_forensics import ImageForensics516

# Find similar images in directory
forensics = ImageForensics516("outputs/")
similar_pairs = forensics.find_similar_images("images/", threshold=5)

for pair in similar_pairs:
    print(f"Similar: {pair['image1']} ↔ {pair['image2']}")
```

## Command Line Examples

### 9. Basic CLI Usage
```bash
# Single username search
sherlock516 johndoe

# Instagram profile with custom output
ig516 instagram_user -o /custom/output/path

# Metadata analysis with cleaning
meta516 photo.jpg --clean

# Compare two images
img516 compare image1.jpg image2.jpg -t 10

# Bulk email analysis
email516 -f emails.txt

# Domain research
domain516 example.com

# Generate report from existing data
report516 -d outputs/
```

### 10. Advanced CLI Usage
```bash
# Batch process multiple images
for image in *.jpg; do
    meta516 "$image"
done

# Chain multiple tools
sherlock516 username && \
ig516 username && \
social516 username && \
report516
```

## Output Examples

### Sample JSON Output
```json
{
  "tool": "516 Hackers OSINT Toolkit",
  "timestamp": "2024-01-15T10:30:00",
  "results": {
    "username": "johndoe",
    "platforms_found": ["github", "twitter", "instagram"],
    "analysis": {
      "discovery_rate": "60%",
      "risk_level": "medium"
    }
  }
}
```

## Best Practices

1. **Error Handling**: Always wrap in try-catch blocks
2. **Rate Limiting**: Add delays between API calls
3. **Data Validation**: Validate inputs before processing
4. **Secure Storage**: Encrypt sensitive output files
