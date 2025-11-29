// src/components/IssuesPanel.js
import React from 'react';

const IssuesPanel = ({ issues }) => {
  if (!issues || issues.length === 0) {
    return (
      <div className="issues-panel">
        <h2>🚨 Network Issues</h2>
        <div className="no-issues">
          <p>✅ No network issues detected</p>
          <p>All packets appear to be normal</p>
        </div>
      </div>
    );
  }

  const getSeverityColor = (severity) => {
    switch (severity?.toLowerCase()) {
      case 'high': return '#e74c3c';
      case 'medium': return '#f39c12';
      case 'low': return '#3498db';
      default: return '#95a5a6';
    }
  };

  return (
    <div className="issues-panel">
      <h2>🚨 Network Issues Detected ({issues.length})</h2>
      
      <div className="issues-list">
        {issues.map((issue, index) => (
          <div key={index} className="issue-card">
            <div className="issue-header">
              <span className="issue-type">{issue.type}</span>
              <span 
                className="severity-badge"
                style={{ backgroundColor: getSeverityColor(issue.severity) }}
              >
                {issue.severity}
              </span>
            </div>
            
            <div className="issue-description">{issue.description}</div>
            
            {issue.details && (
              <div className="issue-details">
                <strong>Details:</strong> {issue.details}
              </div>
            )}
            
            {issue.suggestion && (
              <div className="issue-suggestion">
                <strong>💡 Suggestion:</strong> {issue.suggestion}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default IssuesPanel;