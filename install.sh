#!/bin/bash
echo -e '\033[1;34m'
# Function to check if the script is running as root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "This script must be run as root."
        exit 1
    fi
}

# Main function for installation
install() {
    echo -e '=====================\nINSTALLING FOR KALI-LINUX\n=====================\n'
    apt install -y python3 python3-pip
    apt install aircrack-ng
    apt install mdk4
    apt install macchanger
    apt install nmap
    apt install metasploit-framework
    apt install -y php
    clear
    echo -e '=====================\nINSTALLING FOR KALI-LINUX: SUCCESS\n=====================\n'
    echo "[+] Done: pip install -r requirements.txt"
    pip install -r requirements.txt
}

# Check if the script is running as root
check_root

# Run the installation function
install
