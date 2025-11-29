# backend/api/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

# Add the src directory to path (it's in the parent folder)
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import your EXISTING PacketAnalyzer modules
from src.capturer import PacketCapturer
from src.parser import ProtocolParser
from src.statistics import TrafficStatistics
from src.detector import IssueDetector
from src.filters import PacketFilter
from src.storage import PacketStorage

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy', 
        'message': 'Packet Analyzer API is running',
        'version': '1.0.0'
    })

@app.route('/api/capture', methods=['POST'])
def capture_packets():
    """Capture packets using your existing PacketCapturer"""
    try:
        data = request.get_json()
        count = data.get('count', 10)
        use_real = data.get('realCapture', False)
        
        # Use your EXISTING PacketCapturer
        capturer = PacketCapturer(use_real_capture=use_real)
        capturer.start_capture(count)
        
        # Convert to JSON-serializable format
        serializable_packets = []
        for packet in capturer.captured_packets:
            serializable_packet = {
                'number': packet.get('number'),
                'timestamp': packet.get('timestamp'),
                'protocol': packet.get('protocol'),
                'summary': packet.get('summary'),
                'length': packet.get('length'),
                'src_ip': packet.get('src_ip'),
                'dst_ip': packet.get('dst_ip'),
                'real_packet': packet.get('real_packet', False)
            }
            serializable_packets.append(serializable_packet)
        
        return jsonify({
            'success': True,
            'packets': serializable_packets,
            'total': len(serializable_packets),
            'mode': 'real' if use_real else 'simulation'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analyze', methods=['POST'])
def analyze_packets():
    """Analyze packets using your existing ProtocolParser"""
    try:
        data = request.get_json()
        packets = data.get('packets', [])
        
        # Use your EXISTING ProtocolParser
        parser = ProtocolParser()
        analyses = [parser.parse_packet(packet) for packet in packets]
        
        return jsonify({
            'success': True,
            'analyses': analyses
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/statistics', methods=['POST'])
def get_statistics():
    """Generate statistics using your existing TrafficStatistics"""
    try:
        data = request.get_json()
        packets = data.get('packets', [])
        
        # Use your EXISTING TrafficStatistics
        stats = TrafficStatistics()
        statistics = stats.generate_statistics(packets)
        
        return jsonify({
            'success': True,
            'statistics': statistics
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/detect-issues', methods=['POST'])
def detect_issues():
    """Detect issues using your existing IssueDetector"""
    try:
        data = request.get_json()
        packets = data.get('packets', [])
        
        # Use your EXISTING IssueDetector
        detector = IssueDetector()
        issues = detector.analyze_packets(packets)
        
        return jsonify({
            'success': True,
            'issues': issues
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
        
       
@app.route('/api/storage/save', methods=['POST'])
def save_capture():
    """Save capture to file"""
    try:
        data = request.get_json()
        packets = data.get('packets', [])
        filename = data.get('filename')
        format = data.get('format', 'json')
        
        storage = PacketStorage()
        success = storage.save_capture(packets, filename, format)
        
        return jsonify({
            'success': success,
            'message': 'Capture saved successfully' if success else 'Failed to save capture'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/storage/load/<filename>', methods=['GET'])
def load_capture_file(filename):
    """Load capture from file"""
    try:
        storage = PacketStorage()
        packets = storage.load_capture(filename)
        
        if packets:
            return jsonify({
                'success': True,
                'packets': packets
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to load capture'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/storage/captures', methods=['GET'])
def list_saved_captures():
    """List all saved captures"""
    try:
        storage = PacketStorage()
        captures = storage.list_captures()
        
        return jsonify({
            'success': True,
            'captures': captures
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/storage/delete/<filename>', methods=['DELETE'])
def delete_capture_file(filename):
    """Delete a capture file"""
    try:
        storage = PacketStorage()
        success = storage.delete_capture(filename)
        
        return jsonify({
            'success': success,
            'message': 'Capture deleted successfully' if success else 'Failed to delete capture'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
        

if __name__ == '__main__':
    print("🚀 Packet Analyzer API Starting...")
    print("📡 Using your existing src/ modules")
    print("🌐 API: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)