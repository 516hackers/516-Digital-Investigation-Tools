

# Colors for styling
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color


# ASCII Art Banner
show_banner() {
    clear
    echo -e "${RED}"
    echo '╔══════════════════════════════════════════════════════════════╗'
    echo '║                                                              ║'
    echo '║                  ██████╗   ██╗  ██████╗                      ║'
    echo '║                  ██╔════╝  ██║  ██╔════╝                     ║'
    echo '║                  ███████╗  ██║  ███████╗                     ║'
    echo '║                  ╚════██║  ██║  ██╔══██║                     ║'
    echo '║                  ███████║  ██║  ╚█████╔╝                     ║'
    echo '║                                                              ║'
    echo '║           DIGITAL INVESTIGATION TOOLS v1.0.0                 ║'
    echo '║                     [ 516 HACKERS ]                          ║'
    echo '║                                                              ║'
    echo '╚══════════════════════════════════════════════════════════════╝'
    echo -e "${NC}"
    echo -e "${YELLOW}[!] Legal Disclaimer: Use responsibly with proper authorization${NC}"
    echo -e "${YELLOW}[!] For educational and authorized security research only${NC}"
    echo
}

# Simple loading function
show_loading() {
    local text="$1"
    echo -ne "${CYAN}[*] $text${NC}"
    sleep 2
    echo -e "${GREEN} ✓ DONE${NC}"
}

# Display results in terminal
display_instagram_results() {
    local username="$1"
    local output_file="outputs/instagram_${username}.json"
    
    if [[ -f "$output_file" ]]; then
        echo -e "\n${GREEN}📊 INSTAGRAM ANALYSIS RESULTS:${NC}"
        echo -e "${CYAN}================================${NC}"
        
        # Use python to parse and display JSON nicely
        python3 - <<EOF
import json
import os

try:
    with open('$output_file', 'r') as f:
        data = json.load(f)
    
    profile = data.get('profile', {})
    analysis = data.get('analysis', {})
    
    if profile:
        print("👤 Profile Information:")
        print(f"   Username: {profile.get('username', 'N/A')}")
        print(f"   Full Name: {profile.get('full_name', 'N/A')}")
        print(f"   Followers: {profile.get('followers', 'N/A'):,}")
        print(f"   Following: {profile.get('followees', 'N/A'):,}")
        print(f"   Posts: {profile.get('posts_count', 'N/A'):,}")
        print(f"   Private: {'Yes' if profile.get('is_private') else 'No'}")
        print(f"   Verified: {'Yes' if profile.get('is_verified') else 'No'}")
        print(f"   Biography: {profile.get('biography', 'N/A')[:100]}...")
        print(f"   External URL: {profile.get('external_url', 'N/A')}")
    
    if analysis:
        print("\n📈 Engagement Analysis:")
        print(f"   Follower/Following Ratio: {analysis.get('follower_to_following_ratio', 'N/A')}")
        print(f"   Posts per Follower: {analysis.get('posts_per_follower', 'N/A')}")
        print(f"   Profile Completeness: {analysis.get('profile_completeness_score', 'N/A')}%")
        
except Exception as e:
    print(f"Error reading results: {e}")
EOF
    else
        echo -e "${RED}❌ Results file not found: $output_file${NC}"
    fi
}

display_social_results() {
    local username="$1"
    local output_file=$(find outputs -name "social_map_${username}_*.json" | head -1)
    
    if [[ -f "$output_file" ]]; then
        echo -e "\n${GREEN}🌐 SOCIAL MEDIA PRESENCE RESULTS:${NC}"
        echo -e "${CYAN}==================================${NC}"
        
        python3 - <<EOF
import json
import glob

try:
    with open('$output_file', 'r') as f:
        data = json.load(f)
    
    results = data.get('results', {})
    platforms = results.get('platforms', {})
    summary = results.get('summary', {})
    
    if summary:
        print(f"📊 Summary for: {results.get('username', 'N/A')}")
        print(f"   Platforms Checked: {summary.get('total_platforms_checked', 'N/A')}")
        print(f"   Platforms Found: {summary.get('platforms_found', 'N/A')}")
        print(f"   Discovery Rate: {summary.get('discovery_rate', 'N/A')}%")
    
    print("\n🔍 Platform Details:")
    found_count = 0
    for platform, data in platforms.items():
        status = "✅ FOUND" if data.get('exists') else "❌ NOT FOUND"
        if data.get('exists'):
            found_count += 1
            print(f"   {platform.upper()}: {status} - {data.get('url')}")
        else:
            print(f"   {platform.upper()}: {status}")
    
    print(f"\n🎯 Found on {found_count} platforms")
    
except Exception as e:
    print(f"Error reading results: {e}")
EOF
    else
        echo -e "${RED}❌ Results file not found for username: $username${NC}"
    fi
}

display_domain_results() {
    local domain="$1"
    local output_file=$(find outputs -name "domain_research_${domain}_*.json" | head -1)
    
    if [[ -f "$output_file" ]]; then
        echo -e "\n${GREEN}🌐 DOMAIN RESEARCH RESULTS:${NC}"
        echo -e "${CYAN}=============================${NC}"
        
        python3 - <<EOF
import json

try:
    with open('$output_file', 'r') as f:
        data = json.load(f)
    
    results = data.get('results', {})
    
    print(f"🔍 Domain: {results.get('domain', 'N/A')}")
    
    # WHOIS Info
    whois_info = results.get('whois_info', {})
    if whois_info and 'error' not in whois_info:
        print("\n📋 WHOIS Information:")
        print(f"   Registrar: {whois_info.get('registrar', 'N/A')}")
        print(f"   Creation Date: {whois_info.get('creation_date', 'N/A')}")
        print(f"   Expiration Date: {whois_info.get('expiration_date', 'N/A')}")
    
    # DNS Info
    dns_info = results.get('dns_info', {})
    if dns_info:
        print("\n🔗 DNS Records:")
        for record_type, records in dns_info.items():
            if records and 'Error' not in str(records):
                print(f"   {record_type}: {len(records)} records found")
    
    # IP Info
    ip_info = results.get('ip_info', {})
    if ip_info and 'error' not in ip_info:
        print(f"\n🌍 IP Information:")
        print(f"   IP Address: {ip_info.get('ip_address', 'N/A')}")
    
    # HTTP Headers
    http_info = results.get('http_headers', {})
    if http_info and 'error' not in http_info:
        print(f"\n📡 HTTP Headers:")
        print(f"   Status Code: {http_info.get('status_code', 'N/A')}")
        print(f"   Server: {http_info.get('server', 'N/A')}")
    
except Exception as e:
    print(f"Error reading results: {e}")
EOF
    else
        echo -e "${RED}❌ Results file not found for domain: $domain${NC}"
    fi
}

# Tool functions
run_username_investigation() {
    echo -e "\n${PURPLE}[1] USERNAME INVESTIGATION${NC}"
    echo -e "${CYAN}=================================${NC}"
    read -p "Enter username to investigate: " username
    echo -e "${YELLOW}[*] Starting investigation for: $username${NC}"
    
    show_loading "Scanning 50+ social media platforms"
    investigate516 "$username"
    
    echo -e "${GREEN}[+] Investigation completed!${NC}"
    display_social_results "$username"
}

run_instagram_analysis() {
    echo -e "\n${PURPLE}[2] INSTAGRAM PROFILE ANALYSIS${NC}"
    echo -e "${CYAN}=================================${NC}"
    read -p "Enter Instagram username: " username
    echo -e "${YELLOW}[*] Analyzing Instagram profile: $username${NC}"
    
    show_loading "Extracting profile data and engagement metrics"
    ig516 "$username"
    
    echo -e "${GREEN}[+] Instagram analysis completed!${NC}"
    display_instagram_results "$username"
}

run_metadata_analysis() {
    echo -e "\n${PURPLE}[3] IMAGE METADATA ANALYSIS${NC}"
    echo -e "${CYAN}=================================${NC}"
    read -p "Enter image file path: " image_path
    echo -e "${YELLOW}[*] Analyzing metadata for: $image_path${NC}"
    
    if [[ ! -f "$image_path" ]]; then
        echo -e "${RED}[!] Error: File not found: $image_path${NC}"
        return
    fi
    
    show_loading "Extracting EXIF and metadata"
    meta516 "$image_path"
    
    echo -e "${GREEN}[+] Metadata analysis completed!${NC}"
    
    # Show metadata results
    local output_file=$(find outputs -name "metadata_analysis_*.json" | head -1)
    if [[ -f "$output_file" ]]; then
        echo -e "\n${GREEN}📸 METADATA ANALYSIS RESULTS:${NC}"
        echo -e "${CYAN}==============================${NC}"
        python3 -c "
import json
file = '$output_file'
with open(file, 'r') as f:
    data = json.load(f)
analysis = data.get('analysis', {})
print(f'📁 File: {analysis.get(\"filename\", \"N/A\")}')
print(f'📊 Size: {analysis.get(\"file_size\", \"N/A\")} bytes')
print(f'🔢 Hash: {analysis.get(\"file_hash\", \"N/A\")}')
print(f'🖼️ Format: {analysis.get(\"image_format\", \"N/A\")}')
print(f'📏 Dimensions: {analysis.get(\"image_size\", \"N/A\")}')
metadata = analysis.get('metadata', {})
print(f'📋 Metadata Tags: {len(metadata)}')
if metadata:
    print('\n🔍 Key Metadata:')
    for key in list(metadata.keys())[:5]:
        print(f'   {key}: {metadata[key][:50]}...')
"
    fi
}

run_image_forensics() {
    echo -e "\n${PURPLE}[4] IMAGE FORENSICS & SIMILARITY${NC}"
    echo -e "${CYAN}=================================${NC}"
    echo -e "${YELLOW}Select option:${NC}"
    echo "1) Compare two images"
    echo "2) Find similar images in directory"
    echo "3) Calculate image hashes"
    read -p "Choice [1-3]: " choice
    
    case $choice in
        1)
            read -p "Enter first image path: " img1
            read -p "Enter second image path: " img2
            show_loading "Comparing images using perceptual hashing"
            image516 compare "$img1" "$img2"
            ;;
        2)
            read -p "Enter directory path: " dir_path
            show_loading "Finding similar images in directory"
            image516 find-similar "$dir_path"
            ;;
        3)
            read -p "Enter image path: " img_path
            show_loading "Calculating image hashes"
            image516 hash "$img_path"
            ;;
        *)
            echo -e "${RED}[!] Invalid choice${NC}"
            return
            ;;
    esac
    
    echo -e "${GREEN}[+] Image forensics completed!${NC}"
}

run_social_mapping() {
    echo -e "\n${PURPLE}[5] SOCIAL MEDIA PRESENCE MAPPING${NC}"
    echo -e "${CYAN}=================================${NC}"
    read -p "Enter username to map: " username
    echo -e "${YELLOW}[*] Mapping social media presence for: $username${NC}"
    
    show_loading "Checking 8 major social platforms"
    social516 "$username"
    
    echo -e "${GREEN}[+] Social media mapping completed!${NC}"
    display_social_results "$username"
}

run_email_analysis() {
    echo -e "\n${PURPLE}[6] EMAIL INTELLIGENCE${NC}"
    echo -e "${CYAN}=================================${NC}"
    echo -e "${YELLOW}Select option:${NC}"
    echo "1) Single email analysis"
    echo "2) Bulk email analysis from file"
    read -p "Choice [1-2]: " choice
    
    case $choice in
        1)
            read -p "Enter email address: " email
            show_loading "Validating email and analyzing patterns"
            email516 "$email"
            ;;
        2)
            read -p "Enter file path with emails: " file_path
            show_loading "Processing bulk email analysis"
            email516 -f "$file_path"
            ;;
        *)
            echo -e "${RED}[!] Invalid choice${NC}"
            return
            ;;
    esac
    
    echo -e "${GREEN}[+] Email analysis completed!${NC}"
}

run_domain_research() {
    echo -e "\n${PURPLE}[7] DOMAIN RESEARCH & OSINT${NC}"
    echo -e "${CYAN}=================================${NC}"
    read -p "Enter domain to research: " domain
    echo -e "${YELLOW}[*] Researching domain: $domain${NC}"
    
    show_loading "Gathering WHOIS, DNS, and HTTP data"
    domain516 "$domain"
    
    echo -e "${GREEN}[+] Domain research completed!${NC}"
    display_domain_results "$domain"
}

run_report_generator() {
    echo -e "\n${PURPLE}[8] UNIFIED REPORT GENERATION${NC}"
    echo -e "${CYAN}=================================${NC}"
    echo -e "${YELLOW}[*] Generating comprehensive report from all scans${NC}"
    
    show_loading "Compiling data and generating reports"
    report516
    
    echo -e "${GREEN}[+] Unified report generated!${NC}"
    echo -e "${BLUE}[i] Reports saved in multiple formats (JSON, CSV, HTML, Excel)${NC}"
}

run_advanced_scan() {
    echo -e "\n${PURPLE}[9] ADVANCED COMPREHENSIVE SCAN${NC}"
    echo -e "${CYAN}=================================${NC}"
    read -p "Enter target (username/identifier): " target
    read -p "Enter email (optional): " email
    read -p "Enter domain (optional): " domain
    
    echo -e "${YELLOW}[*] Starting comprehensive scan for: $target${NC}"
    
    show_loading "Running multi-tool comprehensive investigation"
    python examples/advanced_scan.py "$target" ${email:+-e "$email"} ${domain:+-d "$domain"}
    
    echo -e "${GREEN}[+] Advanced scan completed!${NC}"
    echo -e "${BLUE}[i] Complete report generated with all findings${NC}"
}

# Main menu
show_menu() {
    echo -e "\n${WHITE}╔══════════════════════════════════════════════╗${NC}"
    echo -e "${WHITE}║           INVESTIGATION TOOLS MENU           ║${NC}"
    echo -e "${WHITE}╠══════════════════════════════════════════════╣${NC}"
    echo -e "${WHITE}║ ${GREEN}1${NC}) Username Investigation               ${WHITE}║${NC}"
    echo -e "${WHITE}║ ${GREEN}2${NC}) Instagram Profile Analysis           ${WHITE}║${NC}"
    echo -e "${WHITE}║ ${GREEN}3${NC}) Image Metadata Analysis              ${WHITE}║${NC}"
    echo -e "${WHITE}║ ${GREEN}4${NC}) Image Forensics & Similarity         ${WHITE}║${NC}"
    echo -e "${WHITE}║ ${GREEN}5${NC}) Social Media Presence Mapping        ${WHITE}║${NC}"
    echo -e "${WHITE}║ ${GREEN}6${NC}) Email Intelligence                   ${WHITE}║${NC}"
    echo -e "${WHITE}║ ${GREEN}7${NC}) Domain Research & OSINT              ${WHITE}║${NC}"
    echo -e "${WHITE}║ ${GREEN}8${NC}) Unified Report Generation            ${WHITE}║${NC}"
    echo -e "${WHITE}║ ${GREEN}9${NC}) Advanced Comprehensive Scan          ${WHITE}║${NC}"
    echo -e "${WHITE}║ ${RED}0${NC}) Exit                                ${WHITE}║${NC}"
    echo -e "${WHITE}╚══════════════════════════════════════════════╝${NC}"
    echo
}

# Main function
main() {
    show_banner
    
    while true; do
        show_menu
        read -p "$(echo -e ${CYAN}"Select tool [0-9]: "${NC})" choice
        
        case $choice in
            1) run_username_investigation ;;
            2) run_instagram_analysis ;;
            3) run_metadata_analysis ;;
            4) run_image_forensics ;;
            5) run_social_mapping ;;
            6) run_email_analysis ;;
            7) run_domain_research ;;
            8) run_report_generator ;;
            9) run_advanced_scan ;;
            0)
                echo -e "\n${RED}[!] Exiting 516 Digital Investigation Tools${NC}"
                echo -e "${YELLOW}[*] Remember to use responsibly!${NC}"
                exit 0
                ;;
            *)
                echo -e "${RED}[!] Invalid selection. Please choose 0-9${NC}"
                ;;
        esac
        
        echo
        read -p "$(echo -e ${YELLOW}"Press Enter to continue..."${NC})" -r
        clear
        show_banner
    done
}

# Check if tools are installed
check_dependencies() {
    local missing_tools=()
    
    for tool in investigate516 ig516 meta516 image516 social516 email516 domain516 report516; do
        if ! command -v $tool &> /dev/null; then
            missing_tools+=("$tool")
        fi
    done
    
    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        echo -e "${RED}[!] Missing tools: ${missing_tools[*]}${NC}"
        echo -e "${YELLOW}[*] Please install the toolkit first:${NC}"
        echo -e "${BLUE}    pip install -e .${NC}"
        exit 1
    fi
}

# Initialize
check_dependencies
main
