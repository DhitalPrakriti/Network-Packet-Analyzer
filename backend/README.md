# 🔧 Packet Analyzer - Backend

Python backend for the Packet Analyzer project, providing packet capture, analysis, and REST API functionality.

## 🏗️ Architecture
backend/
├── api/
│ └── app.py # Flask REST API server
└── (linked to src/) # Core analyzer engine

text

## 📦 Core Modules

### `src/capturer.py`
- Real and simulated packet capture
- Scapy integration for network traffic
- Protocol detection and classification

### `src/parser.py` 
- Deep protocol analysis (Ethernet, IP, TCP, UDP, ICMP)
- Layer-by-layer packet dissection
- Educational protocol explanations

### `src/statistics.py`
- Traffic analytics and metrics
- Protocol distribution analysis
- Packet size statistics

### `src/detector.py`
- Network issue detection
- Security anomaly identification
- Performance problem analysis

### `src/filters.py`
- Custom packet filtering
- Protocol, IP, and port-based filters
- Real-time traffic filtering

### `src/storage.py`
- Capture persistence (JSON/Pickle)
- File management and organization
- Data export/import functionality

### `src/cli.py`
- Command-line interface
- Interactive packet analysis
- Batch processing capabilities

## 🚀 Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
📡 API Endpoints
Health & Status
GET /api/health - Service health check

Packet Operations
POST /api/capture - Capture packets

POST /api/analyze - Analyze packet protocols

POST /api/statistics - Generate traffic statistics

POST /api/detect-issues - Detect network issues

Storage Operations
POST /api/storage/save - Save capture to file

GET /api/storage/load/<filename> - Load capture from file

GET /api/storage/captures - List saved captures

DELETE /api/storage/delete/<filename> - Delete capture file

💻 CLI Usage
bash
# Comprehensive demo
packetanalyzer --demo

# Basic capture
packetanalyzer --capture --count 10

# Capture with analysis
packetanalyzer --capture --analyze --stats --detect-issues

# Filter specific traffic
packetanalyzer --capture --filter-protocol TCP --filter-dst-ip 8.8.8.8

# Load and analyze saved capture
packetanalyzer --load capture_20231201_143022.json --stats
🛠️ Development
Dependencies
txt
scapy>=2.4.5      # Packet manipulation and capture
Flask>=2.3.0      # Web framework and REST API
flask-cors>=4.0.0 # Cross-origin resource sharing
click>=8.0.0      # Command-line interface
Running the API
bash
cd backend/api
python app.py
# Server starts on http://localhost:5000
Testing
bash
# Run comprehensive demo
packetanalyzer --demo

# Test specific functionality
packetanalyzer --capture --count 5 --stats
🔧 Configuration
Network Permissions
Real packet capture requires administrative privileges:

bash
# Linux/macOS
sudo packetanalyzer --capture

# Windows: Run as Administrator
Storage Directory
Captures are saved to ./captures/ directory by default.

🐛 Troubleshooting
Common Issues
Permission denied for packet capture

Run with sudo (Linux/macOS) or as Administrator (Windows)

Scapy installation issues

bash
pip install --upgrade scapy
Port 5000 

📚 API Examples
Capture Packets
bash
curl -X POST http://localhost:5000/api/capture \
  -H "Content-Type: application/json" \
  -d '{"count": 10, "realCapture": true}'
Get Statistics
bash
curl -X POST http://localhost:5000/api/statistics \
  -H "Content-Type: application/json" \
  -d '{"packets": [...]}'
text

