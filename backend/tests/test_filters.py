import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.filters import PacketFilter

class TestPacketFilter:
    def setup_method(self):
        self.filter = PacketFilter()
        self.sample_packets = [
            {
                'protocol': 'TCP', 
                'summary': 'TCP 192.168.1.1:80 > 10.0.0.2:54321 SYN',
                'src_ip': '192.168.1.1',
                'dst_ip': '10.0.0.2'
            },
            {
                'protocol': 'UDP',
                'summary': 'UDP 192.168.1.1:53 > 10.0.0.2:49152',
                'src_ip': '192.168.1.1', 
                'dst_ip': '10.0.0.2'
            },
            {
                'protocol': 'TCP',
                'summary': 'TCP 10.0.0.2:54321 > 192.168.1.1:80 ACK',
                'src_ip': '10.0.0.2',
                'dst_ip': '192.168.1.1'
            }
        ]
    
    def test_initialization(self):
        """Test filter initializes correctly"""
        assert self.filter.filters == []
        
    def test_protocol_filter(self):
        """Test filtering by protocol"""
        self.filter.add_protocol_filter('TCP')
        filtered = self.filter.apply_filters(self.sample_packets)
        
        assert len(filtered) == 2
        assert all(p['protocol'] == 'TCP' for p in filtered)
        
    def test_multiple_protocol_filters(self):
        """Test multiple protocol filters"""
        self.filter.add_protocol_filter('TCP')
        self.filter.add_protocol_filter('UDP')
        filtered = self.filter.apply_filters(self.sample_packets)
        
        # Should return all packets since both protocols are included
        assert len(filtered) == 3
        
    def test_ip_filter_source(self):
        """Test filtering by source IP"""
        self.filter.add_ip_filter(src_ip='192.168.1.1')
        filtered = self.filter.apply_filters(self.sample_packets)
        
        assert len(filtered) == 2
        assert all('192.168.1.1' in p['summary'] for p in filtered)
        
    def test_ip_filter_destination(self):
        """Test filtering by destination IP"""
        self.filter.add_ip_filter(dst_ip='10.0.0.2')
        filtered = self.filter.apply_filters(self.sample_packets)
        
        assert len(filtered) == 2
        assert all('10.0.0.2' in p['summary'] for p in filtered)
        
    def test_ip_filter_both(self):
        """Test filtering by both source and destination IP"""
        self.filter.add_ip_filter(src_ip='192.168.1.1', dst_ip='10.0.0.2')
        filtered = self.filter.apply_filters(self.sample_packets)
        
        assert len(filtered) == 2
        
    def test_empty_filters(self):
        """Test applying no filters returns all packets"""
        filtered = self.filter.apply_filters(self.sample_packets)
        assert len(filtered) == len(self.sample_packets)
        
    def test_clear_filters(self):
        """Test clearing all filters"""
        self.filter.add_protocol_filter('TCP')
        assert len(self.filter.filters) == 1
        
        self.filter.clear_filters()
        assert len(self.filter.filters) == 0
        
    def test_show_active_filters(self):
        """Test displaying active filters"""
        self.filter.add_protocol_filter('TCP')
        # Should not raise an exception
        self.filter.show_active_filters()