// src/components/CapturePanel.js
import React, { useState } from 'react';
import { capturePackets, analyzePackets, getStatistics, detectIssues } from '../services/api';

const CapturePanel = ({ onCaptureComplete, loading, setLoading }) => {
  const [packetCount, setPacketCount] = useState(10);
  const [realCapture, setRealCapture] = useState(false);

  const handleCapture = async () => {
    setLoading(true);
    
    try {
      // Capture packets
      const captureResult = await capturePackets(packetCount, realCapture);
      
      if (captureResult.success) {
        // Analyze packets
        const analysisResult = await analyzePackets(captureResult.data.packets);
        
        // Get statistics
        const statsResult = await getStatistics(captureResult.data.packets);
        
        // Detect issues
        const issuesResult = await detectIssues(captureResult.data.packets);

        onCaptureComplete({
          packets: captureResult.data.packets,
          analyses: analysisResult.success ? analysisResult.data.analyses : [],
          statistics: statsResult.success ? statsResult.data.statistics : null,
          issues: issuesResult.success ? issuesResult.data.issues : [],
          mode: captureResult.data.mode
        });
      } else {
        alert(`Capture failed: ${captureResult.error}`);
      }
    } catch (error) {
      alert(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="capture-panel">
      <h2>📡 Packet Capture</h2>
      
      <div className="controls">
        <div className="control-group">
          <label>Packet Count:</label>
          <input
            type="number"
            value={packetCount}
            onChange={(e) => setPacketCount(parseInt(e.target.value))}
            min="1"
            max="50"
          />
        </div>
        
        <div className="control-group">
          <label>
            <input
              type="checkbox"
              checked={realCapture}
              onChange={(e) => setRealCapture(e.target.checked)}
            />
            Real Network Capture
          </label>
        </div>
        
        <button 
          onClick={handleCapture} 
          disabled={loading}
          className="capture-button"
        >
          {loading ? '🔄 Capturing...' : '📡 Start Capture'}
        </button>
      </div>
      
      {realCapture && (
        <div className="warning">
          ⚠️ Real capture requires backend to run with administrator privileges
        </div>
      )}
    </div>
  );
};

export default CapturePanel;