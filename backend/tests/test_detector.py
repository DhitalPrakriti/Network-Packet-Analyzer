import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.detector import IssueDetector

class TestIssueDetector:
    def setup_method(self):
        self.detector = IssueDetector()
        self.normal_packets = [
            {'protocol': 'TCP', 'length': 100, 'summary': 'Normal TCP packet'},
            {'protocol': 'UDP', 'length': 150, 'summary': 'Normal UDP packet'}
        ]
        
    def test_initialization(self):
        """Test detector initializes correctly"""
        assert self.detector.detected_issues == []
        
    def test_analyze_empty_packets(self):
        """Test analysis with empty packet list"""
        issues = self.detector.analyze_packets([])
        assert issues == []
        
    def test_analyze_normal_packets(self):
        """Test analysis with normal packets"""
        issues = self.detector.analyze_packets(self.normal_packets)
        # Normal packets might not trigger any issues
        assert isinstance(issues, list)
        
    def test_display_issues_empty(self):
        """Test displaying no issues"""
        self.detector.analyze_packets(self.normal_packets)
        # Should not raise an exception
        self.detector.display_issues()
        
    def test_issue_structure(self):
        """Test that issues have correct structure when detected"""
        # Create packets that might trigger issues
        small_packets = [
            {'protocol': 'TCP', 'length': 54, 'summary': 'Small TCP packet'},
            {'protocol': 'TCP', 'length': 55, 'summary': 'Another small TCP packet'}
        ]
        
        issues = self.detector.analyze_packets(small_packets)
        
        # If issues are detected, check their structure
        if issues:
            for issue in issues:
                assert 'type' in issue
                assert 'severity' in issue
                assert 'description' in issue
                assert 'details' in issue
                assert 'educational_note' in issue