// frontend/src/services/api.js
import axios from 'axios';

const API_BASE = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE,
  timeout: 15000, // Increased timeout for packet capture
});

// Health check endpoint
export const checkBackendHealth = async () => {
  try {
    const response = await api.get('/health');
    return { success: true, data: response.data };
  } catch (error) {
    return { 
      success: false, 
      error: error.message,
      details: 'Make sure Flask backend is running on port 5000'
    };
  }
};

// Capture packets
export const capturePackets = async (count, realCapture) => {
  try {
    const response = await api.post('/capture', { 
      count, 
      realCapture 
    });
    return { success: true, data: response.data };
  } catch (error) {
    return { 
      success: false, 
      error: error.response?.data?.error || error.message 
    };
  }
};

// Analyze packets
export const analyzePackets = async (packets) => {
  try {
    const response = await api.post('/analyze', { packets });
    return { success: true, data: response.data };
  } catch (error) {
    return { 
      success: false, 
      error: error.response?.data?.error || error.message 
    };
  }
};

// Get statistics
export const getStatistics = async (packets) => {
  try {
    const response = await api.post('/statistics', { packets });
    return { success: true, data: response.data };
  } catch (error) {
    return { 
      success: false, 
      error: error.response?.data?.error || error.message 
    };
  }
};

// Detect issues
export const detectIssues = async (packets) => {
  try {
    const response = await api.post('/detect-issues', { packets });
    return { success: true, data: response.data };
  } catch (error) {
    return { 
      success: false, 
      error: error.response?.data?.error || error.message 
    };
  }
};

// ========== STORAGE ENDPOINTS ========== //

// Save capture to server
export const saveCapture = async (packets, filename, format = 'json') => {
  try {
    const response = await api.post('/storage/save', { 
      packets, 
      filename, 
      format 
    });
    return { success: true, data: response.data };
  } catch (error) {
    return { 
      success: false, 
      error: error.response?.data?.error || error.message 
    };
  }
};

// Load capture from server
export const loadCapture = async (filename) => {
  try {
    const response = await api.get(`/storage/load/${filename}`);
    return { success: true, data: response.data };
  } catch (error) {
    return { 
      success: false, 
      error: error.response?.data?.error || error.message 
    };
  }
};

// List all saved captures
export const listCaptures = async () => {
  try {
    const response = await api.get('/storage/captures');
    return { success: true, data: response.data };
  } catch (error) {
    return { 
      success: false, 
      error: error.response?.data?.error || error.message 
    };
  }
};

// Delete a capture
export const deleteCapture = async (filename) => {
  try {
    const response = await api.delete(`/storage/delete/${filename}`);
    return { success: true, data: response.data };
  } catch (error) {
    return { 
      success: false, 
      error: error.response?.data?.error || error.message 
    };
  }
};

export default api;