import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.capturer import PacketCapturer
from src.parser import ProtocolParser
from src.filters import PacketFilter
from src.statistics import TrafficStatistics
from src.detector import IssueDetector
from src.storage import PacketStorage
import tempfile

class TestIntegration:
    def test_complete_workflow_simulation(self):
        """Test complete capture -> parse -> filter -> analyze workflow with simulation"""
        # Capture (simulated)
        capturer = PacketCapturer(use_real_capture=False)
        capturer.start_capture(5)
        
        assert len(capturer.captured_packets) == 5
        
        # Parse
        parser = ProtocolParser()
        analyses = []
        for packet in capturer.captured_packets:
            analysis = parser.parse_packet(packet)
            analyses.append(analysis)
            assert 'protocol' in analysis
            assert 'layers' in analysis
            
        assert len(analyses) == 5
        
        # Filter
        packet_filter = PacketFilter()
        packet_filter.add_protocol_filter('TCP')
        filtered_packets = packet_filter.apply_filters(capturer.captured_packets)
        
        # Should have some TCP packets (in simulation)
        assert isinstance(filtered_packets, list)
        
        # Analyze statistics
        stats = TrafficStatistics()
        statistics = stats.generate_statistics(capturer.captured_packets)
        
        assert statistics['total_packets'] == 5
        assert 'protocol_distribution' in statistics
        
        # Detect issues
        detector = IssueDetector()
        issues = detector.analyze_packets(capturer.captured_packets)
        assert isinstance(issues, list)
        
    def test_storage_integration(self):
        """Test storage integration in workflow"""
        # Create temporary storage
        temp_dir = tempfile.mkdtemp()
        storage = PacketStorage(storage_dir=temp_dir)
        
        # Capture some packets
        capturer = PacketCapturer(use_real_capture=False)
        capturer.start_capture(3)
        
        # Save capture
        save_result = storage.save_capture(capturer.captured_packets, 'integration_test.json')
        assert save_result == True
        
        # List captures
        captures = storage.list_captures()
        assert len(captures) == 1
        
        # Load capture
        loaded_packets = storage.load_capture('integration_test.json')
        assert loaded_packets is not None
        assert len(loaded_packets) == 3
        
        # Clean up
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)