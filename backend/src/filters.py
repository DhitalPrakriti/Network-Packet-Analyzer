# src/filters.py
class PacketFilter:
    """
    Custom filtering system for network packets
    Educational tool for understanding packet filtering concepts
    """
    
    def __init__(self):
        self.filters = []
        self.protocol_filters = []  # Special handling for protocol filters
        print("🔍 PacketFilter initialized!")
    
    def add_protocol_filter(self, protocol):
        """Filter by protocol type (TCP, UDP, ICMP, etc.)"""
        self.protocol_filters.append(protocol.upper())
        print(f"✅ Added protocol filter: {protocol}")
    
    def add_ip_filter(self, src_ip=None, dst_ip=None):
        """Filter by source and/or destination IP"""
        def ip_filter(packet_info):
            packet_src_ip = packet_info.get('src_ip')
            packet_dst_ip = packet_info.get('dst_ip')
            summary = packet_info.get('summary', '')
            
            # Try to extract IPs from summary if direct fields are not available
            if not packet_src_ip or not packet_dst_ip:
                # Simple IP extraction from summary
                import re
                ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                ips_in_summary = re.findall(ip_pattern, summary)
                
                if not packet_src_ip and ips_in_summary:
                    packet_src_ip = ips_in_summary[0]
                if not packet_dst_ip and len(ips_in_summary) > 1:
                    packet_dst_ip = ips_in_summary[1]
            
            # Apply filters
            if src_ip and packet_src_ip != src_ip:
                return False
            if dst_ip and packet_dst_ip != dst_ip:
                return False
            
            return True
        
        self.filters.append(ip_filter)
        filter_desc = []
        if src_ip:
            filter_desc.append(f"Source: {src_ip}")
        if dst_ip:
            filter_desc.append(f"Destination: {dst_ip}")
        print(f"✅ Added IP filter - {', '.join(filter_desc)}")
    
    def add_port_filter(self, port=None, src_port=None, dst_port=None):
        """Filter by port numbers"""
        def port_filter(packet_info):
            summary = packet_info.get('summary', '').lower()
            
            # Look for port patterns in the summary
            if port:
                port_str = str(port)
                if f":{port_str} " not in summary and f">{port_str}" not in summary:
                    return False
            
            if src_port:
                src_port_str = str(src_port)
                if f":{src_port_str} >" not in summary:
                    return False
            
            if dst_port:
                dst_port_str = str(dst_port)
                if f">{dst_port_str}" not in summary:
                    return False
            
            return True
        
        self.filters.append(port_filter)
        print(f"✅ Added port filter - Port: {port}, Src: {src_port}, Dst: {dst_port}")
    
    def apply_filters(self, packets):
        """Apply all filters to a list of packets"""
        if not packets:
            return []
        
        filtered_packets = packets
        
        # Apply protocol filters (OR logic for multiple protocols)
        if self.protocol_filters:
            filtered_packets = [
                p for p in filtered_packets 
                if p.get('protocol', '').upper() in self.protocol_filters
            ]
        
        # Apply other filters (AND logic)
        for filter_func in self.filters:
            filtered_packets = [p for p in filtered_packets if filter_func(p)]
        
        print(f"📊 Filters applied: {len(packets)} → {len(filtered_packets)} packets")
        return filtered_packets
    
    def clear_filters(self):
        """Clear all filters"""
        self.filters = []
        self.protocol_filters = []
        print("🧹 All filters cleared")
    
    def show_active_filters(self):
        """Display currently active filters"""
        if not self.filters and not self.protocol_filters:
            print("No active filters")
            return
        
        print("🔍 Active Filters:")
        for i, protocol in enumerate(self.protocol_filters):
            print(f"  {i+1}. Protocol: {protocol}")
        
        for i, filter_func in enumerate(self.filters, start=len(self.protocol_filters) + 1):
            print(f"  {i}. {filter_func.__name__}")