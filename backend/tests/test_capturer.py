import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.capturer import PacketCapturer

class TestPacketCapturer:
    def test_initialization(self):
        """Test capturer initializes correctly"""
        capturer = PacketCapturer()
        assert capturer.captured_packets == []
        assert capturer.packet_count == 0
        assert capturer.is_capturing == False
        
    def test_initialization_with_real_capture(self):
        """Test capturer initializes with real capture enabled"""
        capturer = PacketCapturer(use_real_capture=True)
        assert capturer.use_real_capture == True
        
    def test_simulated_capture(self):
        """Test simulated packet capture"""
        capturer = PacketCapturer(use_real_capture=False)
        capturer.start_capture(3)
        
        assert len(capturer.captured_packets) == 3
        assert capturer.packet_count == 3
        assert all('protocol' in packet for packet in capturer.captured_packets)
        assert all('summary' in packet for packet in capturer.captured_packets)
        
    def test_protocol_stats_empty(self):
        """Test statistics with no packets"""
        capturer = PacketCapturer()
        # Should not crash with empty packets
        capturer.show_protocol_stats()
        
    def test_protocol_stats_with_packets(self):
        """Test statistics with captured packets"""
        capturer = PacketCapturer(use_real_capture=False)
        capturer.start_capture(2)
        
        # Should work without errors
        capturer.show_protocol_stats()
        
    def test_capture_with_timeout(self):
        """Test capture with timeout parameter"""
        capturer = PacketCapturer(use_real_capture=False)
        capturer.start_capture(2, timeout=5)
        
        assert len(capturer.captured_packets) == 2
        
    def test_scapy_availability_check(self):
        """Test Scapy availability detection"""
        capturer = PacketCapturer()
        # Should not raise an exception
        assert isinstance(capturer.scapy_available, bool)