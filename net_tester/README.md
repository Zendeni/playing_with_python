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


## Options
-i <iface>: (Optional) Specify the network interface to use. The default is eth0.\
Example: -i wlan0\
-s <src>: (Optional) Specify the source IP address. If not provided, a random IP address will be generated.\
Example: -s 192.168.1.100\
-t <target>: (Required) Specify the target IP address.\
Example: -t 192.168.1.1\
-c <count>: (Optional) Specify the number of packets to send for each test. The default is 1.\
Example: -c 10\
