import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.statistics import TrafficStatistics

class TestTrafficStatistics:
    def setup_method(self):
        self.stats = TrafficStatistics()
        self.sample_packets = [
            {'protocol': 'TCP', 'length': 100, 'timestamp': 1000, 'summary': 'TCP packet 1'},
            {'protocol': 'UDP', 'length': 50, 'timestamp': 1001, 'summary': 'UDP packet 1'},
            {'protocol': 'TCP', 'length': 150, 'timestamp': 1002, 'summary': 'TCP packet 2'},
            {'protocol': 'ICMP', 'length': 80, 'timestamp': 1003, 'summary': 'ICMP packet 1'},
            {'protocol': 'TCP', 'length': 200, 'timestamp': 1004, 'summary': 'TCP packet 3'}
        ]
    
    def test_initialization(self):
        """Test statistics analyzer initializes correctly"""
        assert self.stats is not None
        
    def test_generate_statistics(self):
        """Test statistics generation"""
        result = self.stats.generate_statistics(self.sample_packets)
        
        assert result['total_packets'] == 5
        assert result['total_bytes'] == 580  # 100+50+150+80+200
        assert result['capture_duration'] == 4.0  # 1004-1000
        
        # Check protocol distribution
        assert 'TCP' in result['protocol_distribution']
        assert 'UDP' in result['protocol_distribution']
        assert 'ICMP' in result['protocol_distribution']
        assert result['protocol_distribution']['TCP']['count'] == 3
        assert result['protocol_distribution']['TCP']['percentage'] == 60.0
        
        # Check packet size distribution
        size_data = result['packet_size_distribution']
        assert size_data['small'] >= 0
        assert size_data['medium'] >= 0
        assert size_data['large'] >= 0
        assert size_data['average_size'] == 116.0  # 580/5
        
    def test_empty_packets(self):
        """Test statistics with empty packet list"""
        result = self.stats.generate_statistics([])
        
        assert result['total_packets'] == 0
        assert result['total_bytes'] == 0
        assert result['capture_duration'] == 0
        
    def test_single_packet(self):
        """Test statistics with single packet"""
        single_packet = [{'protocol': 'TCP', 'length': 100, 'timestamp': 1000}]
        result = self.stats.generate_statistics(single_packet)
        
        assert result['total_packets'] == 1
        assert result['total_bytes'] == 100
        assert result['capture_duration'] == 0  # Single packet has no duration
        
    def test_display_statistics(self):
        """Test statistics display method"""
        result = self.stats.generate_statistics(self.sample_packets)
        # Should not raise an exception
        self.stats.display_statistics(result)
        
    def test_display_empty_statistics(self):
        """Test displaying empty statistics"""
        result = self.stats.generate_statistics([])
        # Should not raise an exception
        self.stats.display_statistics(result)