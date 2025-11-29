# src/statistics.py
import time
from collections import Counter

class TrafficStatistics:
    """
    Generates traffic statistics and analysis
    Educational tool for understanding network traffic patterns
    """
    
    def __init__(self):
        print("📊 TrafficStatistics initialized!")
    
    def generate_statistics(self, packets):
        """Generate comprehensive traffic statistics with proper data handling"""
        if not packets:
            print("No packets to analyze")
            return self._create_empty_stats()
        
        # Calculate basic metrics with proper error handling
        total_packets = len(packets)
        total_bytes = self._calculate_total_bytes(packets)
        duration = self._calculate_duration(packets)
        
        # Calculate traffic rate (avoid division by zero)
        traffic_rate = total_packets / duration if duration > 0 else total_packets
        
        stats = {
            'total_packets': total_packets,
            'total_bytes': total_bytes,
            'total_data': total_bytes,  # Alias for frontend compatibility
            'capture_duration': duration,
            'traffic_rate': round(traffic_rate, 2),
            'protocol_distribution': self._protocol_distribution(packets),
            'packet_size_distribution': self._packet_size_distribution(packets),
            'average_packet_size': self._calculate_average_size(packets),
            'traffic_timeline': self._traffic_timeline(packets),
            'top_conversations': self._top_conversations(packets)
        }
        
        return stats
    
    def _create_empty_stats(self):
        """Return empty statistics structure"""
        return {
            'total_packets': 0,
            'total_bytes': 0,
            'total_data': 0,
            'capture_duration': 0,
            'traffic_rate': 0,
            'protocol_distribution': {},
            'packet_size_distribution': {
                'small': 0, 'medium': 0, 'large': 0,
                'average_size': 0, 'min_size': 0, 'max_size': 0
            },
            'average_packet_size': 0,
            'traffic_timeline': {},
            'top_conversations': []
        }
    
    def _calculate_total_bytes(self, packets):
        """Calculate total bytes with proper handling of missing lengths"""
        total = 0
        for packet in packets:
            length = packet.get('length', 0)
            if length > 0:
                total += length
            else:
                # Estimate length for packets with missing data
                total += self._estimate_packet_length(packet)
        return total
    
    def _estimate_packet_length(self, packet):
        """Estimate packet length when not provided"""
        protocol = packet.get('protocol', '').lower()
        summary = packet.get('summary', '')
        
        # Try to extract length from summary first
        if 'len=' in summary:
            import re
            match = re.search(r'len=(\d+)', summary)
            if match:
                return int(match.group(1))
        
        # Typical packet sizes by protocol
        size_estimates = {
            'tcp': 1500,    # Typical TCP packet with data
            'udp': 512,     # Typical UDP packet
            'dns': 128,     # DNS query/response
            'http': 1400,   # HTTP data
            'icmp': 84,     # ICMP packet
            'icmpv6': 84,   # ICMPv6 packet
            'ip': 576,      # Typical IP packet
            'ipv6': 1280,   # IPv6 packet
        }
        
        return size_estimates.get(protocol, 256)  # Default fallback
    
    def _calculate_duration(self, packets):
        """Calculate capture duration with proper timestamp handling"""
        if len(packets) < 2:
            return 1.0  # Default to 1 second if not enough packets
        
        # Get all valid timestamps
        timestamps = [p.get('timestamp', 0) for p in packets if p.get('timestamp', 0) > 0]
        
        if len(timestamps) < 2:
            return 1.0  # Fallback duration
        
        # Calculate actual duration
        duration = max(timestamps) - min(timestamps)
        
        # Ensure minimum duration to avoid division by zero
        return max(duration, 0.1)  # At least 0.1 seconds
    
    def _calculate_average_size(self, packets):
        """Calculate average packet size"""
        if not packets:
            return 0
        
        total_bytes = self._calculate_total_bytes(packets)
        return round(total_bytes / len(packets), 2)
    
    def _protocol_distribution(self, packets):
        """Calculate protocol distribution"""
        protocols = [p.get('protocol', 'Unknown') for p in packets]
        distribution = Counter(protocols)
        
        # Add percentages
        total = len(packets)
        result = {}
        for protocol, count in distribution.items():
            percentage = (count / total) * 100
            result[protocol] = {
                'count': count,
                'percentage': round(percentage, 1)
            }
        
        return result
    
    def _traffic_timeline(self, packets):
        """Create traffic timeline (packets per second)"""
        if not packets:
            return {}
        
        timeline = {}
        for packet in packets:
            timestamp = packet.get('timestamp', 0)
            second = int(timestamp)
            timeline[second] = timeline.get(second, 0) + 1
        
        return timeline
    
    def _packet_size_distribution(self, packets):
        """Analyze packet size distribution"""
        sizes = []
        for packet in packets:
            length = packet.get('length', 0)
            if length == 0:
                length = self._estimate_packet_length(packet)
            sizes.append(length)
        
        if not sizes:
            return {
                'small': 0, 'medium': 0, 'large': 0,
                'average_size': 0, 'min_size': 0, 'max_size': 0
            }
        
        return {
            'small': len([s for s in sizes if s < 100]),
            'medium': len([s for s in sizes if 100 <= s < 1000]),
            'large': len([s for s in sizes if s >= 1000]),
            'average_size': round(sum(sizes) / len(sizes), 2),
            'min_size': min(sizes),
            'max_size': max(sizes)
        }
    
    def _top_conversations(self, packets):
        """Identify top conversations (source-destination pairs)"""
        conversations = []
        
        for packet in packets:
            summary = packet.get('summary', '')
            # Extract conversation info from summary
            if '>' in summary:
                parts = summary.split('>')
                if len(parts) == 2:
                    src = parts[0].strip()
                    dst = parts[1].split('/')[0].strip() if '/' in parts[1] else parts[1].strip()
                    conversations.append(f"{src} → {dst}")
        
        return Counter(conversations).most_common(5)
    
    def display_statistics(self, stats):
        """Display statistics in educational format"""
        print("\n" + "="*60)
        print("📊 NETWORK TRAFFIC STATISTICS & ANALYSIS")
        print("="*60)
        
        print(f"\n📈 CAPTURE OVERVIEW:")
        print(f"   Total Packets: {stats['total_packets']}")
        print(f"   Total Data: {stats['total_bytes']:,} bytes")
        print(f"   Duration: {stats['capture_duration']:.2f} seconds")
        print(f"   Traffic Rate: {stats['traffic_rate']:.1f} packets/second")
        
        print(f"\n🔍 PROTOCOL DISTRIBUTION:")
        for protocol, data in stats['protocol_distribution'].items():
            print(f"   {protocol}: {data['count']} packets ({data['percentage']}%)")
        
        print(f"\n📦 PACKET SIZE ANALYSIS:")
        size_data = stats['packet_size_distribution']
        print(f"   Small packets (<100B): {size_data['small']}")
        print(f"   Medium packets (100B-1KB): {size_data['medium']}")
        print(f"   Large packets (≥1KB): {size_data['large']}")
        print(f"   Average size: {size_data['average_size']:.1f} bytes")
        print(f"   Size range: {size_data['min_size']}-{size_data['max_size']} bytes")
        
        print(f"\n💬 TOP CONVERSATIONS:")
        for i, (conversation, count) in enumerate(stats['top_conversations'], 1):
            print(f"   {i}. {conversation} ({count} packets)")
        
        print(f"\n⏰ TRAFFIC TIMELINE:")
        timeline = stats['traffic_timeline']
        if timeline:
            busiest_second = max(timeline.items(), key=lambda x: x[1])
            print(f"   Busiest second: {busiest_second[1]} packets at timestamp {busiest_second[0]}")
        else:
            print("   No timeline data available")
        
        print("\n" + "="*60)