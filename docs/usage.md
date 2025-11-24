# Usage Guide

## Quick Start Examples

### Basic Capture & Analysis
```bash
# Capture 10 packets with statistics
python src/cli.py --capture --count 10 --stats

# Educational protocol analysis
python src/cli.py --capture --count 8 --analyze

# Run complete demo
python src/cli.py --demo


# Capture and save for later
python src/cli.py --capture --count 15 --save network_baseline --stats

# List all saved captures
python src/cli.py --list-captures

# Load and analyze saved data
python src/cli.py --load network_baseline.json --detect-issues --parse-all

# Capture and save for later
python src/cli.py --capture --count 15 --save network_baseline --stats

# List all saved captures
python src/cli.py --list-captures

# Load and analyze saved data
python src/cli.py --load network_baseline.json --detect-issues --parse-all

# Monitor network traffic with full analysis
python src/cli.py --capture --count 25 --stats --detect-issues --analyze

# Analyze only TCP traffic
python src/cli.py --capture --count 12 --filter-protocol TCP --analyze

# Study DNS queries (UDP traffic)
python src/cli.py --capture --count 8 --filter-protocol UDP --analyze

# Capture and analyze TCP connections
python src/cli.py --capture --filter-protocol TCP --analyze --count 10

# See detailed breakdown of each protocol layer
python src/cli.py --capture --count 5 --analyze

# Detect potential network issues
python src/cli.py --capture --count 30 --detect-issues --stats

# Capture large dataset and save
python src/cli.py --capture --count 50 --save daily_traffic --stats

# Later, perform detailed analysis
python src/cli.py --load daily_traffic.json --detect-issues --parse-all --analyze