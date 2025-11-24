# Setup Guide - Windows

## 🚀 Quick Installation

### Step 1: Prerequisites
- **Python 3.8 or higher** 
- **Windows 10/11** with Administrator access
- **Npcap** (replaces WinPcap for packet capture)

### Step 2: Install Npcap (Required for Packet Capture)
1. Download Npcap from: https://npcap.com/#download
2. Run the installer **as Administrator**
3. **Important**: Choose these options during installation:
   - ✅ "Install Npcap in WinPcap API-compatible mode"
   - ✅ "Restrict Npcap driver's access to Administrators only"

### Step 3: Install Python Dependencies
```cmd
# Open Command Prompt as Administrator
pip install scapy rich