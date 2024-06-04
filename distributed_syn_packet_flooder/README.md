# SYN Packet Flooder (DDoS Simulation)

## Description

This script performs a simulated Distributed Denial of Service (DDoS) attack by sending a large number of TCP SYN packets from random source IP addresses to a target machine. The goal is to mimic the behavior of multiple attacking machines.


## Requirements

- Python 3.x
- Scapy library

    ```sh
    pip install scapy
    ```

## Usage

1. Clone the repository or download the script.

2. Edit the script to set the target (`tgt`) IP address and the destination port (`dport`).

3. Run the script:
    ```sh
    python ddos_syn_flood.py
    ```

## Example

```python
tgt = "192.168.1.3"
dport = 513
syn_flood(tgt, dport)
