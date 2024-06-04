# SYN Packet Flooder

## Description

This script performs a SYN flood attack, a type of Denial of Service (DoS) attack. It sends a large number of TCP SYN packets to a target machine, potentially overwhelming its resources and causing it to become unresponsive.

## Requirements

- Python 3.x
- Scapy library

    ```sh
    pip install scapy
    ```

## Usage

1. Clone the repository or download the script.

2. Edit the script to set the source (`src`) and target (`tgt`) IP addresses.

3. Run the script:
    ```sh
    python syn_flood.py
    ```

## Example

```python
src = "10.1.1.2"
tgt = "192.168.1.3"
syn_flood(src, tgt)
