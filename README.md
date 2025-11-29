# 🕵️‍♂️ Packet Analyzer - Professional Network Analysis Tool

A comprehensive, educational network packet analyzer built with Python. Capture, analyze, and understand network traffic with real-time parsing and professional-grade visualization.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-green)
![React](https://img.shields.io/badge/react-18%2B-blue)

## ✨ Features

### 🔍 Core Capabilities
- **Real & Simulated Packet Capture** - Real network traffic or safe simulation
- **Protocol Parsing** - Deep analysis of Ethernet, IP, TCP, UDP, ICMP
- **Smart Filtering** - Filter by protocol, IP, port, and more
- **Traffic Statistics** - Comprehensive analytics and visualization
- **Issue Detection** - Automatic network problem detection
- **Data Persistence** - Save/load captures in JSON or Pickle format

### 🎯 Educational Focus
- **Layer-by-Layer Analysis** - Understand OSI model in practice
- **Protocol Explanations** - Learn how each protocol works
- **Security Insights** - Detect suspicious network activity
- **Real-time Learning** - See networking concepts in action

PacketAnalyzer/
├── backend/ # Python Flask API & Core Engine
├── frontend/ # React Web Interface
└── src/ # Python CLI & Library


## 🚀 Quick Start

### Backend 
```bash
# Clone repository
git clone https://github.com/DhitalPrakriti/Packet-Analyzer.git
cd Packet-Analyzer

# Install backend dependencies
pip install -r requirements.txt
pip install -e .

cd frontend
npm install
npm start
# Frontend: http://localhost:3000

# Run comprehensive demo
packetanalyzer --demo

# Capture packets
packetanalyzer --capture --count 10 --stats

cd backend/api
python app.py
# API: http://localhost:5000

🛠️ Tech Stack
Backend: Python, Flask, Scapy, Click
Frontend: React, Axios, CSS3
CLI: Python Click

