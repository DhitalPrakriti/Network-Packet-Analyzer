// src/components/FilterPanel.js
import React, { useState } from 'react';

const FilterPanel = ({ packets, onFiltered }) => {
  const [protocolFilter, setProtocolFilter] = useState('');
  const [srcIpFilter, setSrcIpFilter] = useState('');
  const [dstIpFilter, setDstIpFilter] = useState('');

  const applyFilters = () => {
    let filtered = packets;

    if (protocolFilter) {
      filtered = filtered.filter(packet => 
        packet.protocol?.toLowerCase().includes(protocolFilter.toLowerCase())
      );
    }

    if (srcIpFilter) {
      filtered = filtered.filter(packet => 
        packet.src_ip?.includes(srcIpFilter)
      );
    }

    if (dstIpFilter) {
      filtered = filtered.filter(packet => 
        packet.dst_ip?.includes(dstIpFilter)
      );
    }

    onFiltered(filtered);
  };

  const clearFilters = () => {
    setProtocolFilter('');
    setSrcIpFilter('');
    setDstIpFilter('');
    onFiltered(packets);
  };

  // Get unique protocols for dropdown
  const uniqueProtocols = [...new Set(packets.map(p => p.protocol))].filter(Boolean);

  return (
    <div className="filter-panel">
      <h3>🔍 Filter Packets</h3>
      
      <div className="filter-controls">
        <div className="filter-group">
          <label>Protocol:</label>
          <select 
            value={protocolFilter} 
            onChange={(e) => setProtocolFilter(e.target.value)}
          >
            <option value="">All Protocols</option>
            {uniqueProtocols.map(protocol => (
              <option key={protocol} value={protocol}>{protocol}</option>
            ))}
          </select>
        </div>

        <div className="filter-group">
          <label>Source IP:</label>
          <input
            type="text"
            placeholder="Filter by source IP..."
            value={srcIpFilter}
            onChange={(e) => setSrcIpFilter(e.target.value)}
          />
        </div>

        <div className="filter-group">
          <label>Destination IP:</label>
          <input
            type="text"
            placeholder="Filter by destination IP..."
            value={dstIpFilter}
            onChange={(e) => setDstIpFilter(e.target.value)}
          />
        </div>

        <div className="filter-actions">
          <button onClick={applyFilters} className="btn-primary">
            Apply Filters
          </button>
          <button onClick={clearFilters} className="btn-secondary">
            Clear Filters
          </button>
        </div>
      </div>
    </div>
  );
};

export default FilterPanel;