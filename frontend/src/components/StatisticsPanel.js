// src/components/StatisticsPanel.js
import React from 'react';

const StatisticsPanel = ({ statistics }) => {
  if (!statistics) {
    return (
      <div className="statistics-panel">
        <h2>📊 Traffic Statistics</h2>
        <p>No statistics available. Capture some packets first.</p>
      </div>
    );
  }

  // Helper function to safely render protocol distribution
  const renderProtocolDistribution = () => {
    if (!statistics.protocol_distribution) {
      return <p>No protocol data available</p>;
    }

    return Object.entries(statistics.protocol_distribution).map(([protocol, data]) => {
      // Handle both object format {count: X, percentage: Y} and simple number format
      const count = typeof data === 'object' ? data.count : data;
      const percentage = typeof data === 'object' ? data.percentage : null;
      
      return (
        <div key={protocol} className="stat-item">
          <span className="label">{protocol}:</span>
          <span className="value">
            {count} packets
            {percentage && ` (${percentage}%)`}
          </span>
        </div>
      );
    });
  };

  // Helper function to safely render packet size analysis
  const renderPacketSizeAnalysis = () => {
    if (!statistics.packet_size_analysis) {
      return null;
    }

    // Handle both object and simple number formats
    const small = typeof statistics.packet_size_analysis.small === 'object' 
      ? statistics.packet_size_analysis.small.count 
      : statistics.packet_size_analysis.small;
    
    const medium = typeof statistics.packet_size_analysis.medium === 'object'
      ? statistics.packet_size_analysis.medium.count
      : statistics.packet_size_analysis.medium;
    
    const large = typeof statistics.packet_size_analysis.large === 'object'
      ? statistics.packet_size_analysis.large.count
      : statistics.packet_size_analysis.large;

    return (
      <>
        <div className="stat-item">
          <span className="label">Small (&lt;100B):</span>
          <span className="value">{small || 0}</span>
        </div>
        <div className="stat-item">
          <span className="label">Medium (100B-1KB):</span>
          <span className="value">{medium || 0}</span>
        </div>
        <div className="stat-item">
          <span className="label">Large (≥1KB):</span>
          <span className="value">{large || 0}</span>
        </div>
      </>
    );
  };

  return (
    <div className="statistics-panel">
      <h2>📊 Traffic Statistics</h2>
      
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Overview</h3>
          <div className="stat-item">
            <span className="label">Total Packets:</span>
            <span className="value">{statistics.total_packets || 0}</span>
          </div>
          <div className="stat-item">
            <span className="label">Total Data:</span>
            <span className="value">{statistics.total_data || 0} bytes</span>
          </div>
          <div className="stat-item">
            <span className="label">Traffic Rate:</span>
            <span className="value">
              {typeof statistics.traffic_rate === 'number' 
                ? statistics.traffic_rate.toFixed(2) 
                : '0.00'} packets/sec
            </span>
          </div>
        </div>
        
        <div className="stat-card">
          <h3>Protocol Distribution</h3>
          {renderProtocolDistribution()}
        </div>
        
        <div className="stat-card">
          <h3>Packet Sizes</h3>
          {renderPacketSizeAnalysis()}
          <div className="stat-item">
            <span className="label">Average Size:</span>
            <span className="value">
              {typeof statistics.average_packet_size === 'number'
                ? statistics.average_packet_size.toFixed(2)
                : '0.00'} bytes
            </span>
          </div>
        </div>
      </div>

      {/* Debug section - you can remove this later */}
      <details style={{ marginTop: '2rem', background: '#f8f9fa', padding: '1rem', borderRadius: '5px' }}>
        <summary>🔧 Debug Data (Raw Statistics)</summary>
        <pre style={{ background: '#2d3748', color: 'white', padding: '1rem', borderRadius: '5px', overflow: 'auto' }}>
          {JSON.stringify(statistics, null, 2)}
        </pre>
      </details>
    </div>
  );
};

export default StatisticsPanel;