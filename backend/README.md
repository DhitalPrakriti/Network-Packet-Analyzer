**🕵️‍♂️ Packet Analyzer - Professional Network Analysis Tool**
A comprehensive, educational network packet analyzer built with Python. Capture, analyze, and understand network traffic with real-time parsing and professional-grade visualization.

🔍 Core Capabilities
Real & Simulated Packet Capture - Real network traffic or safe simulation
Protocol Parsing - Deep analysis of Ethernet, IP, TCP, UDP, ICMP
Smart Filtering - Filter by protocol, IP, port, and more
Traffic Statistics - Comprehensive analytics and visualization
Issue Detection - Automatic network problem detection
Data Persistence - Save/load captures in JSON or Pickle format

🎯 Educational Focus
Layer-by-Layer Analysis - Understand OSI model in practice
Protocol Explanations - Learn how each protocol works
Security Insights - Detect suspicious network activity
Real-time Learning - See networking concepts in action

🚀 Quick Start
Prerequisites
Python 3.8 or higher
Administrative privileges (for real packet capture)

Installation
Clone or download this project

Open in VS Code

bash
code PacketAnalyzer
Install dependencies

bash
pip install -r requirements.txt
Install in development mode

bash
pip install -e .
💻 Usage
Command Line Interface (CLI)
bash
# Run comprehensive demo
packetanalyzer --demo

# Capture 10 real packets
packetanalyzer --capture --count 10

# Capture and show statistics
packetanalyzer --capture --stats

# Full analysis with issue detection
packetanalyzer --capture --analyze --detect-issues

# Filter specific traffic
packetanalyzer --capture --filter-protocol TCP --filter-dst-ip 8.8.8.8

# Load and analyze saved capture
packetanalyzer --load capture_20231201_143022.json --stats --detect-issues
Web API (Flask)
bash
# Start the API server
cd backend/api
python app.py

# API will be available at: http://localhost:5000
API Endpoints
GET /api/health - Health check

POST /api/capture - Capture packets

POST /api/analyze - Analyze packets

POST /api/statistics - Get traffic statistics

POST /api/detect-issues - Detect network issues

🏗️ Project Structure
text
PacketAnalyzer/
├── src/                          # Core analyzer engine
│   ├── capturer.py              # Packet capture (real/simulated)
│   ├── parser.py                # Protocol parsing & analysis
│   ├── filters.py               # Custom packet filtering
│   ├── statistics.py            # Traffic analytics
│   ├── storage.py               # Save/load captures
│   ├── detector.py              # Issue detection
│   └── cli.py                   # Command-line interface
├── backend/api/
│   └── app.py                   # Flask REST API
├── tests/                       # Test suite
├── docs/                        # Documentation
├── examples/                    # Usage examples
├── setup.py                     # Package configuration
├── requirements.txt             # Dependencies
└── README.md                    # This file
🛠️ VS Code Setup
Recommended Extensions
Add these to your VS Code for the best experience:

json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "ms-python.flake8",
        "ms-python.isort"
    ]
}
VS Code Settings
Create .vscode/settings.json:

json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.analysis.extraPaths": ["./src"],
    "python.formatting.provider": "black",
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
    "editor.formatOnSave": true
}
Debugging Configuration
Create .vscode/launch.json:

json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Packet Analyzer CLI",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/cli.py",
            "args": ["--demo"],
            "console": "integratedTerminal"
        },
        {
            "name": "Packet Analyzer API",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/backend/api/app.py",
            "console": "integratedTerminal"
        }
    ]
}
📚 Learning Resources
Understanding the Code
Start with: src/capturer.py - Basic packet capture

Then explore: src/parser.py - Protocol analysis

Advanced: src/detector.py - Network security

Networking Concepts
OSI Model Layers

TCP/IP Protocol Suite

Packet Headers & Structure

Network Security Fundamentals

🐛 Troubleshooting
Common Issues
"Permission denied" for packet capture

bash
# On Linux/macOS
sudo packetanalyzer --capture

# Or run VS Code as administrator (Windows)
Scapy not installed

bash
pip install scapy
Import errors in VS Code

Set Python interpreter: Ctrl+Shift+P → "Python: Select Interpreter"

Mark src as source root: Right-click src → "Mark Directory as" → "Sources Root"

🤝 Contributing
Fork the project

Create a feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Built with Scapy for packet manipulation

Educational focus for networking students

Professional-grade architecture patterns

Happy Analyzing! 🎯

For questions or support, please open an issue in the project repository.


