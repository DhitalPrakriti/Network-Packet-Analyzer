import pytest
import sys
import os
import tempfile
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.storage import PacketStorage

class TestPacketStorage:
    def setup_method(self):
        # Create temporary directory for tests
        self.temp_dir = tempfile.mkdtemp()
        self.storage = PacketStorage(storage_dir=self.temp_dir)
        self.sample_packets = [
            {'number': 1, 'protocol': 'TCP', 'length': 100, 'summary': 'Test packet 1'},
            {'number': 2, 'protocol': 'UDP', 'length': 150, 'summary': 'Test packet 2'}
        ]
    
    def teardown_method(self):
        # Clean up temporary directory
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_initialization(self):
        """Test storage initializes correctly"""
        assert self.storage.storage_dir == self.temp_dir
        assert os.path.exists(self.temp_dir)
        
    def test_save_capture_json(self):
        """Test saving capture as JSON"""
        result = self.storage.save_capture(self.sample_packets, 'test_capture.json', 'json')
        assert result == True
        
        # Check file was created
        filepath = os.path.join(self.temp_dir, 'test_capture.json')
        assert os.path.exists(filepath)
        
    def test_save_capture_empty(self):
        """Test saving empty capture"""
        result = self.storage.save_capture([], 'empty_capture.json')
        assert result == False  # Should fail with empty packets
        
    def test_load_capture(self):
        """Test loading saved capture"""
        # First save a capture
        self.storage.save_capture(self.sample_packets, 'test_load.json')
        
        # Then load it
        loaded_packets = self.storage.load_capture('test_load.json')
        assert loaded_packets is not None
        assert len(loaded_packets) == len(self.sample_packets)
        
    def test_load_nonexistent_file(self):
        """Test loading non-existent file"""
        loaded_packets = self.storage.load_capture('nonexistent.json')
        assert loaded_packets is None
        
    def test_list_captures(self):
        """Test listing capture files"""
        # Save a couple of captures
        self.storage.save_capture(self.sample_packets, 'capture1.json')
        self.storage.save_capture(self.sample_packets, 'capture2.json')
        
        captures = self.storage.list_captures()
        assert len(captures) == 2
        
    def test_list_captures_empty(self):
        """Test listing captures when directory is empty"""
        empty_storage = PacketStorage(storage_dir=tempfile.mkdtemp())
        captures = empty_storage.list_captures()
        assert captures == []
        
    def test_delete_capture(self):
        """Test deleting capture file"""
        # First save a capture
        self.storage.save_capture(self.sample_packets, 'to_delete.json')
        
        # Then delete it
        result = self.storage.delete_capture('to_delete.json')
        assert result == True
        
        # Verify file is gone
        filepath = os.path.join(self.temp_dir, 'to_delete.json')
        assert not os.path.exists(filepath)
        
    def test_delete_nonexistent_capture(self):
        """Test deleting non-existent file"""
        result = self.storage.delete_capture('nonexistent.json')
        assert result == False