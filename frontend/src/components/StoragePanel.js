// src/components/StoragePanel.js
import React, { useState, useEffect } from 'react';
import { saveCapture, loadCapture, listCaptures, deleteCapture } from '../services/api';

const StoragePanel = ({ packets, onLoad }) => {
  const [filename, setFilename] = useState('my_capture');
  const [savedCaptures, setSavedCaptures] = useState([]);
  const [loading, setLoading] = useState(false);
  const [saveFormat, setSaveFormat] = useState('json');

  // Load saved captures list on component mount
  useEffect(() => {
    loadSavedCaptures();
  }, []);

  const loadSavedCaptures = async () => {
    try {
      const result = await listCaptures();
      if (result.success) {
        setSavedCaptures(result.data.captures || []);
      }
    } catch (error) {
      console.error('Failed to load captures:', error);
    }
  };

  const handleSave = async () => {
    if (packets.length === 0) {
      alert('No packets to save');
      return;
    }

    if (!filename.trim()) {
      alert('Please enter a filename');
      return;
    }

    setLoading(true);
    try {
      const result = await saveCapture(packets, filename, saveFormat);
      if (result.success) {
        alert(`✅ Capture saved as ${filename}.${saveFormat}`);
        loadSavedCaptures(); // Refresh the list
        setFilename(''); // Clear filename
      } else {
        alert(`❌ Save failed: ${result.error}`);
      }
    } catch (error) {
      alert(`❌ Error saving: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleLoad = async (captureFilename) => {
    setLoading(true);
    try {
      const result = await loadCapture(captureFilename);
      if (result.success) {
        onLoad({
          packets: result.data.packets,
          analyses: [],
          statistics: null,
          issues: [],
          mode: 'loaded'
        });
        alert(`✅ Loaded ${result.data.packets.length} packets from ${captureFilename}`);
      } else {
        alert(`❌ Load failed: ${result.error}`);
      }
    } catch (error) {
      alert(`❌ Error loading: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (captureFilename) => {
    if (window.confirm(`Are you sure you want to delete ${captureFilename}?`)) {
      try {
        const result = await deleteCapture(captureFilename);
        if (result.success) {
          alert(`✅ Deleted ${captureFilename}`);
          loadSavedCaptures();
        } else {
          alert(`❌ Delete failed: ${result.error}`);
        }
      } catch (error) {
        alert(`❌ Error deleting: ${error.message}`);
      }
    }
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString() + ' ' + 
           new Date(dateString).toLocaleTimeString();
  };

  return (
    <div className="storage-panel">
      <h2>💾 Capture Storage</h2>
      
      <div className="storage-controls">
        {/* Save Section */}
        <div className="save-section">
          <h3>💾 Save Current Capture</h3>
          <div className="save-controls">
            <div className="input-group">
              <label>Filename:</label>
              <input
                type="text"
                placeholder="Enter filename (without extension)"
                value={filename}
                onChange={(e) => setFilename(e.target.value)}
              />
            </div>
            
            <div className="input-group">
              <label>Format:</label>
              <select 
                value={saveFormat} 
                onChange={(e) => setSaveFormat(e.target.value)}
              >
                <option value="json">JSON (Human-readable)</option>
                <option value="pkl">Pickle (Python objects)</option>
              </select>
            </div>
            
            <button 
              onClick={handleSave} 
              disabled={packets.length === 0 || loading || !filename.trim()}
              className="btn-primary save-btn"
            >
              {loading ? '💾 Saving...' : '💾 Save to Server'}
            </button>
          </div>
          <p className="packet-count">Current capture: {packets.length} packets</p>
        </div>

        {/* Saved Captures Section */}
        <div className="saved-captures">
          <h3>📁 Saved Captures</h3>
          
          <div className="refresh-section">
            <button onClick={loadSavedCaptures} className="btn-secondary">
              🔄 Refresh List
            </button>
            <span>{savedCaptures.length} capture(s) found</span>
          </div>

          {savedCaptures.length === 0 ? (
            <div className="no-captures">
              <p>No saved captures found on server</p>
              <p>Save a capture to see it here!</p>
            </div>
          ) : (
            <div className="captures-list">
              {savedCaptures.map((capture, index) => (
                <div key={index} className="capture-item">
                  <div className="capture-info">
                    <div className="capture-name">
                      <strong>{capture.filename}</strong>
                    </div>
                    <div className="capture-details">
                      <span className="capture-size">📏 {formatFileSize(capture.size)}</span>
                      <span className="capture-date">⏰ {formatDate(capture.modified)}</span>
                    </div>
                  </div>
                  <div className="capture-actions">
                    <button 
                      onClick={() => handleLoad(capture.filename)}
                      disabled={loading}
                      className="btn-load"
                    >
                      📂 Load
                    </button>
                    <button 
                      onClick={() => handleDelete(capture.filename)}
                      className="btn-delete"
                    >
                      🗑️ Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default StoragePanel;