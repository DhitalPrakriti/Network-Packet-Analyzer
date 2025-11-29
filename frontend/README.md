# 🎨 Packet Analyzer - Frontend

React frontend for the Packet Analyzer project, providing a modern web interface for network traffic analysis.

## 🏗️ Project Structure
frontend/
├── public/
│ ├── index.html
│ └── favicon.ico
├── src/
│ ├── components/
│ │ ├── CapturePanel.js # Packet capture interface
│ │ ├── PacketList.js # Packet display and analysis
│ │ ├── StatisticsPanel.js # Traffic statistics visualization
│ │ ├── IssuesPanel.js # Network issues display
│ │ ├── FilterPanel.js # Packet filtering interface
│ │ └── StoragePanel.js # Capture storage management
│ ├── services/
│ │ └── api.js # Backend API integration
│ ├── App.js # Main application component
│ ├── App.css # Styling and themes
│ └── index.js # Application entry point
├── package.json
└── README.md

text

## 🚀 Installation

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start

# Application will open at http://localhost:3000
📦 Available Scripts
npm start - Runs the app in development mode

npm build - Builds the app for production

npm test - Launches the test runner

npm run eject - Ejects from Create React App (one-way operation)

🎯 Components
CapturePanel
Packet capture controls and settings

Real/simulation mode toggle

Capture count and duration configuration

PacketList
Display captured packets in card format

Protocol-specific styling and badges

Expandable packet analysis details

Layer-by-layer protocol information

StatisticsPanel
Traffic overview and metrics

Protocol distribution charts

Packet size analysis

Traffic rate visualization

IssuesPanel
Network issue detection display

Severity-based color coding

Security anomaly alerts

Performance problem identification

FilterPanel
Real-time packet filtering

Protocol, IP, and port-based filters

Multiple filter combination support

StoragePanel
Capture save/load functionality

File management interface

Export/import capabilities

🔌 API Integration
Services
The services/api.js file handles all backend communication:

javascript
// API endpoints
- capturePackets(count, realCapture)
- analyzePackets(packets)
- getStatistics(packets) 
- detectIssues(packets)
- saveCapture(packets, filename, format)
- loadCapture(filename)
- listCaptures()
- deleteCapture(filename)
Example Usage
javascript
import { capturePackets, analyzePackets } from './services/api';

// Capture packets
const result = await capturePackets(10, true);
if (result.success) {
  const packets = result.data.packets;
  // Process packets...
}
🎨 Styling & Themes
CSS Features
Modern gradient backgrounds

Responsive design for all screen sizes

Protocol-specific color coding

Smooth animations and transitions

Professional card-based layout

Color Scheme
Primary: Purple gradient (#667eea to #764ba2)

Success: Green gradient for TCP

Warning: Orange gradient for UDP

Danger: Red gradient for issues

Dark: #2d3748 for code backgrounds

🛠️ Development
Dependencies
json
{
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "axios": "^1.6.0"
}
Environment Setup
Ensure backend API is running on http://localhost:5000

Start frontend development server

Open http://localhost:3000 in your browser

Adding New Components
Create component in src/components/

Import necessary services from src/services/

Add component to App.js as needed

Update routing if necessary

🔧 Configuration
Backend URL
Update API base URL in src/services/api.js:

javascript
const API_BASE = 'http://localhost:5000/api';
CORS
Ensure backend has CORS enabled for frontend domain.

📱 Responsive Design
The application is fully responsive and works on:

Desktop computers (1200px+)

Tablets (768px - 1199px)

Mobile devices (< 768px)

🐛 Troubleshooting
Common Issues
Backend connection failed

Ensure Flask server is running on port 5000

Check CORS configuration in backend

Verify network connectivity

Empty statistics

Check if packets have valid length data

Verify backend statistics calculation

Filter not working

Check filter logic in FilterPanel

Verify packet data structure

🚀 Deployment
Production Build
bash
npm run build
Serving Built App
The build folder contains optimized production files that can be served by any static hosting service.

Environment Variables
Create .env file for configuration:

env
REACT_APP_API_BASE=http://localhost:5000/api
REACT_APP_VERSION=1.0.0
📚 Component Examples
Using CapturePanel
javascript
<CapturePanel 
  onCaptureComplete={handleCaptureComplete}
  loading={loading}
  setLoading={setLoading}
/>
Using FilterPanel
javascript
<FilterPanel 
  packets={packets}
  onFiltered={setFilteredPackets}
/>
text

## **How to Use These Files:**

1. **Main README.md** - Place in project root
2. **Backend README.md** - Place in `backend/` folder  
3. **Frontend README.md** - Place in `frontend/` folder

## **File Structure:**
PacketAnalyzer/
├── README.md # Main documentation
├── backend/
│ └── README.md # Backend-specific docs
├── frontend/
│ └── README.md # Frontend-specific docs
└── ...other files

text

Now you have **comprehensive documentation** for your entire project! 🎉







