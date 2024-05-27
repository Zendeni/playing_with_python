# TTL Spoof Detection

## Description

This Python script detects possible spoofed packets by analyzing the Time-to-Live (TTL) values of incoming packets. 
If the TTL value of a packet deviates significantly from the expected TTL value for a given IP address, it is flagged as a possible spoofed packet.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `scapy` library: For packet manipulation and sniffing
- `IPy` library: For IP address type checking

## Installation

You can install the required libraries using pip:

```bash
pip install scapy IPy
```

## USage

python3 ttl_spoof_detector.py -i <interface> -t <threshold>

## Example

python3 ttl_spoof_detector.py -i eth0 -t 5

