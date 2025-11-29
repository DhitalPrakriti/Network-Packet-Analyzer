// src/components/PacketList.js
import React from 'react';

const PacketList = ({ packets, analyses }) => {
  const getAnalysisForPacket = (packetNumber) => {
    return analyses.find(analysis => analysis.packet_number === packetNumber);
  };

  return (
    <div className="packet-list">
      <h2>📦 Captured Packets ({packets.length})</h2>
      
      <div className="packets-container">
        {packets.map((packet) => {
          const analysis = getAnalysisForPacket(packet.number);
          
          return (
            <div key={packet.number} className="packet-card">
              <div className="packet-header">
                <span className="packet-number">#{packet.number}</span>
                <span className={`protocol-badge ${packet.protocol?.toLowerCase()}`}>
                  {packet.protocol}
                </span>
                <span className="packet-size">{packet.length} bytes</span>
                {packet.real_packet && (
                  <span className="real-badge">REAL</span>
                )}
              </div>
              
              <div className="packet-summary">{packet.summary}</div>
              
              {packet.src_ip && packet.dst_ip && (
                <div className="packet-ips">
                  <span>Source: {packet.src_ip}</span>
                  <span>Destination: {packet.dst_ip}</span>
                </div>
              )}
              
              {analysis && (
                <div className="packet-analysis">
                  <details>
                    <summary>🔍 View Analysis</summary>
                    <div className="analysis-details">
                      <strong>Protocol:</strong> {analysis.protocol}<br/>
                      <strong>Summary:</strong> {analysis.summary}
                      {analysis.layers && (
                        <div className="layers">
                          {Object.entries(analysis.layers).map(([layerName, layerData]) => (
                            <div key={layerName} className="layer">
                              <strong>{layerName.toUpperCase()} Layer:</strong><br/>
                              {layerData.description && (
                                <div>📝 {layerData.description}</div>
                              )}
                              {layerData.educational_note && (
                                <div>💡 {layerData.educational_note}</div>
                              )}
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  </details>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default PacketList;