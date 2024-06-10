# Network Testing Script

Script performs several types of network tests including DDoS, exploit, and scan tests.

## Requirements

- Python 3.x
- Scapy library

You can install Scapy using pip:
```sh
pip install scapy
```
## Usage

python3 network_test.py -i <iface> -s <src> -t <target> -c <count>

python3 network_test.py -i eth0 -t 192.168.1.1 -c 10
