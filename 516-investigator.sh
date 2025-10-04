#!/bin/bash

# 516 Digital Investigation Tools - Hacker Interface
# Stylish menu-driven interface for all investigation tools

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
    echo -e "${CYAN}"
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


# Animation function
typewriter() {
    local text="$1"
    for ((i=0; i<${#text}; i++)); do
        echo -n "${text:$i:1}"
        sleep 0.03
    done
    echo
}

# Loading animation
show_loading() {
    local pid=$1
    local text="$2"
    echo -ne "${CYAN}[*] $text${NC}"
    while kill -0 $pid 2>/dev/null; do
        for X in '-' '/' '|' '\'; do
            echo -ne "${CYAN}\b$X${NC}"
            sleep 0.1
        done
    done
    echo -e "${GREEN} ✓ DONE${NC}"
}

# Tool functions
run_username_investigation() {
    echo -e "\n${PURPLE}[1] USERNAME INVESTIGATION${NC}"
    echo -e "${CYAN}=================================${NC}"
    read -p "Enter username to investigate: " username
    echo -e "${YELLOW}[*] Starting investigation for: $username${NC}"
    
    (investigate516 "$username" > /dev/null 2>&1) &
    show_loading $! "Scanning 50+ social media platforms"
    
    echo -e "${GREEN}[+] Investigation completed!${NC}"
    echo -e "${BLUE}[i] Results saved to: outputs/${username}_profiles.json${NC}"
}

run_instagram_analysis() {
    echo -e "\n${PURPLE}[2] INSTAGRAM PROFILE ANALYSIS${NC}"
    echo -e "${CYAN}=================================${NC}"
    read -p "Enter Instagram username: " username
    echo -e "${YELLOW}[*] Analyzing Instagram profile: $username${NC}"
    
    (ig516 "$username" > /dev/null 2>&1) &
    show_loading $! "Extracting profile data and engagement metrics"
    
    echo -e "${GREEN}[+] Instagram analysis completed!${NC}"
    echo -e "${BLUE}[i] Results saved to: outputs/instagram_${username}.json${NC}"
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
    
    (meta516 "$image_path" > /dev/null 2>&1) &
    show_loading $! "Extracting EXIF and metadata"
    
    echo -e "${GREEN}[+] Metadata analysis completed!${NC}"
    echo -e "${BLUE}[i] Results saved to: outputs/metadata_analysis_*.json${NC}"
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
            (image516 compare "$img1" "$img2" > /dev/null 2>&1) &
            show_loading $! "Comparing images using perceptual hashing"
            ;;
        2)
            read -p "Enter directory path: " dir_path
            (image516 find-similar "$dir_path" > /dev/null 2>&1) &
            show_loading $! "Finding similar images in directory"
            ;;
        3)
            read -p "Enter image path: " img_path
            (image516 hash "$img_path" > /dev/null 2>&1) &
            show_loading $! "Calculating image hashes"
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
    
    (social516 "$username" > /dev/null 2>&1) &
    show_loading $! "Checking 8 major social platforms"
    
    echo -e "${GREEN}[+] Social media mapping completed!${NC}"
    echo -e "${BLUE}[i] Results saved to: outputs/social_map_${username}_*.json${NC}"
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
            (email516 "$email" > /dev/null 2>&1) &
            show_loading $! "Validating email and analyzing patterns"
            ;;
        2)
            read -p "Enter file path with emails: " file_path
            (email516 -f "$file_path" > /dev/null 2>&1) &
            show_loading $! "Processing bulk email analysis"
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
    
    (domain516 "$domain" > /dev/null 2>&1) &
    show_loading $! "Gathering WHOIS, DNS, and HTTP data"
    
    echo -e "${GREEN}[+] Domain research completed!${NC}"
    echo -e "${BLUE}[i] Results saved to: outputs/domain_research_${domain}_*.json${NC}"
}

run_report_generator() {
    echo -e "\n${PURPLE}[8] UNIFIED REPORT GENERATION${NC}"
    echo -e "${CYAN}=================================${NC}"
    echo -e "${YELLOW}[*] Generating comprehensive report from all scans${NC}"
    
    (report516 > /dev/null 2>&1) &
    show_loading $! "Compiling data and generating reports"
    
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
    
    (python examples/advanced_scan.py "$target" ${email:+-e "$email"} ${domain:+-d "$domain"} > /dev/null 2>&1) &
    show_loading $! "Running multi-tool comprehensive investigation"
    
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
