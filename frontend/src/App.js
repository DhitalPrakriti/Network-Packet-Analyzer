// src/App.js
import React, { useState, useEffect } from 'react';
import { checkBackendHealth } from './services/api';
import CapturePanel from './components/CapturePanel';
import PacketList from './components/PacketList';
import StatisticsPanel from './components/StatisticsPanel';
import IssuesPanel from './components/IssuesPanel';
import FilterPanel from './components/FilterPanel';
import StoragePanel from './components/StoragePanel';
import './App.css';

function App() {
  const [packets, setPackets] = useState([]);
  const [analyses, setAnalyses] = useState([]);
  const [statistics, setStatistics] = useState(null);
  const [issues, setIssues] = useState([]);
  const [activeTab, setActiveTab] = useState('capture');
  const [loading, setLoading] = useState(false);
  const [backendStatus, setBackendStatus] = useState('unknown');

  // Auto-check backend connection on app start
  useEffect(() => {
    handleTestConnection();
  }, []);

  // Auto-refresh connection status periodically
  useEffect(() => {
    const interval = setInterval(() => {
      if (backendStatus === 'connected') {
        handleTestConnection();
      }
    }, 30000); // Check every 30 seconds

    return () => clearInterval(interval);
  }, [backendStatus]);

  const handleTestConnection = async () => {
    setLoading(true);
    const result = await checkBackendHealth();
    
    if (result.success) {
      setBackendStatus('connected');
    } else {
      setBackendStatus('error');
    }
    
    setLoading(false);
  };

  const handleCaptureComplete = (data) => {
    setPackets(data.packets);
    setAnalyses(data.analyses);
    setStatistics(data.statistics);
    setIssues(data.issues);
    setActiveTab('packets');
  };

  const handleFilteredPackets = (filteredPackets) => {
    setPackets(filteredPackets);
  };

  const getConnectionStatusText = () => {
    switch (backendStatus) {
      case 'connected': return 'Connected';
      case 'error': return '❌ Connection Failed';
      case 'unknown': return '🔍 Check Connection';
      default: return 'Test Connection';
    }
  };

  const getStatusColor = () => {
    switch (backendStatus) {
      case 'connected': return '#2ecc71';
      case 'error': return '#e74c3c';
      case 'unknown': return '#f39c12';
      default: return '#95a5a6';
    }
  };

  const tabs = [
    { id: 'capture', label: '📡 Capture', disabled: false },
    { id: 'packets', label: `📦 Packets (${packets.length})`, disabled: packets.length === 0 },
    { id: 'statistics', label: '📊 Statistics', disabled: !statistics },
    { id: 'issues', label: `🚨 Issues (${issues.length})`, disabled: issues.length === 0 },
    { id: 'storage', label: '💾 Storage', disabled: false },
  ];

  // Welcome state for empty application
  if (packets.length === 0 && activeTab !== 'capture' && activeTab !== 'storage') {
    return (
      <div className="App">
        <header className="app-header">
          <h1>🔍 Packet Analyzer</h1>
          <p>Professional Network Traffic Analysis</p>
          <div className="connection-status">
            <span 
              className="status-dot" 
              style={{ backgroundColor: getStatusColor() }}
            ></span>
            <button 
              onClick={handleTestConnection} 
              disabled={loading}
              className="connection-test-btn"
            >
              {loading ? '🔄 Testing...' : getConnectionStatusText()}
            </button>
          </div>
        </header>

        <div className="welcome-state">
          <div className="welcome-content">
            <h2>Welcome to Packet Analyzer! 🚀</h2>
            <p>Start exploring network traffic by capturing your first packets.</p>
            
            <div className="feature-grid">
              <div className="feature-card">
                <h3>📡 Capture</h3>
                <p>Capture real network traffic or use simulation mode</p>
              </div>
              <div className="feature-card">
                <h3>🔍 Analyze</h3>
                <p>Deep protocol analysis with educational insights</p>
              </div>
              <div className="feature-card">
                <h3>📊 Statistics</h3>
                <p>Comprehensive traffic analytics and visualization</p>
              </div>
              <div className="feature-card">
                <h3>🚨 Detect</h3>
                <p>Automatic network issue and security detection</p>
              </div>
            </div>

            <button 
              onClick={() => setActiveTab('capture')} 
              className="btn-primary start-capture-btn"
            >
              📡 Start Your First Capture
            </button>

            {backendStatus === 'error' && (
              <div className="connection-help">
                <h4>⚠️ Backend Connection Required</h4>
                <p>Make sure your Flask backend is running:</p>
                <code>cd backend/api && python app.py</code>
                <p>The backend should be available at: <strong>http://localhost:5000</strong></p>
              </div>
            )}
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="app-header">
        <h1>🔍 Packet Analyzer</h1>
        <p>Professional Network Traffic Analysis</p>
        <div className="connection-status">
          <span 
            className="status-dot" 
            style={{ backgroundColor: getStatusColor() }}
          ></span>
          <button 
            onClick={handleTestConnection} 
            disabled={loading}
            className="connection-test-btn"
          >
            {loading ? '🔄 Testing...' : getConnectionStatusText()}
          </button>
        </div>
      </header>

      <nav className="tabs">
        {tabs.map(tab => (
          <button
            key={tab.id}
            className={`tab ${activeTab === tab.id ? 'active' : ''} ${tab.disabled ? 'disabled' : ''}`}
            onClick={() => !tab.disabled && setActiveTab(tab.id)}
            disabled={tab.disabled}
          >
            {tab.label}
          </button>
        ))}
      </nav>

      <main className="app-main">
        {activeTab === 'capture' && (
          <CapturePanel 
            onCaptureComplete={handleCaptureComplete}
            loading={loading}
            setLoading={setLoading}
          />
        )}

        {activeTab === 'packets' && packets.length > 0 && (
          <>
            <FilterPanel packets={packets} onFiltered={handleFilteredPackets} />
            <PacketList packets={packets} analyses={analyses} />
          </>
        )}

        {activeTab === 'statistics' && statistics && (
          <StatisticsPanel statistics={statistics} />
        )}

        {activeTab === 'issues' && issues.length > 0 && (
          <IssuesPanel issues={issues} />
        )}

        {activeTab === 'storage' && (
          <StoragePanel packets={packets} onLoad={handleCaptureComplete} />
        )}
      </main>

      {/* Global loading overlay */}
      {loading && (
        <div className="loading-overlay">
          <div className="loading-spinner"></div>
          <p>Processing...</p>
        </div>
      )}
    </div>
  );
}

export default App;