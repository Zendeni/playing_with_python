# SYN Flood and Spoofed Connection Script

## Description

This Python script performs a SYN flood attack to suppress a remote server and then spoofs a connection to the target. It uses the `scapy` library to construct and send the network packets.

## Requirements

- Python 3.x
- `scapy` library

## Installation

Install `scapy` using pip:
```sh
   pip install scapy
```
## Usage

python script.py -s <syn_flood_source_ip> -S <spoofed_connection_source_ip> -t <target_ip>


python script.py -s 192.168.1.100 -S 192.168.1.101 -t 192.168.1.102
