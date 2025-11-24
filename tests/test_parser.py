import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.parser import ProtocolParser

class TestProtocolParser:
    def setup_method(self):
        self.parser = ProtocolParser()

    def test_initialization(self):
        """Test parser initialization"""
        assert self.parser is not None

    def test_parse_simulated_packet(self):
        """Test parsing simulated packet"""
        packet_info = {
            'number': 1,
            'protocol': 'TCP',
            'src_ip': '192.168.1.1',
            'dst_ip': '192.168.1.2',
            'length': 64,
            'real_packet': False
        }
        analysis = self.parser.parse_packet(packet_info)
        assert analysis['packet_number'] == 1
        assert analysis['protocol'] == 'TCP'
        assert 'simulated' in analysis['layers']

    def test_parse_packet_with_missing_fields(self):
        """Test parsing packet with missing optional fields"""
        packet_info = {
            'number': 1,
            'protocol': 'UDP',
            'real_packet': False
            # Missing src_ip, dst_ip, etc.
        }
        analysis = self.parser.parse_packet(packet_info)
        assert analysis['packet_number'] == 1
        assert analysis['protocol'] == 'UDP'
        assert analysis['layers']['simulated']['source'] == 'N/A'

    def test_tcp_flags_parsing(self):
        """Test TCP flags parsing directly"""
        # Test the internal _parse_tcp_flags method
        flags = ['S', 'A']  # SYN-ACK
        result = self.parser._parse_tcp_flags(flags)
        assert len(result) == 2
        assert any('SYN' in flag for flag in result)
        assert any('ACK' in flag for flag in result)

    def test_parse_empty_packet(self):
        """Test parsing empty packet info"""
        packet_info = {}
        analysis = self.parser.parse_packet(packet_info)
        assert analysis['packet_number'] == 0
        assert analysis['protocol'] == 'Unknown'
        assert 'error' in analysis['layers']