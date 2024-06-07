# DDoS Test Script

This Python script uses Scapy to simulate a DDoS attack by sending a series of ICMP and UDP packets to a specified target.

## Requirements

- Python 3.x
- Scapy library

## Installation
 Install Scapy using pip:
    ```sh
    pip install scapy
    ```

## Usage

    ```sh
    python ddos_test.py
    ```

    The script contains default values for the source IP, destination IP, network interface, and the number of times to send each packet. Modify these values directly in the script or update the `if __name__ == "__main__":` section to accept command-line arguments for more flexibility.

## Parameters

- `src`: Source IP address (default is `"1.3.3.7"`)
- `dst`: Destination IP address (default is `"192.168.1.106"`)
- `iface`: Network interface to send packets through (default is `"eth0"`)
- `count`: Number of times to send each packet (default is `1`)

## Example

```python
if __name__ == "__main__":
    src = "1.3.3.7"
    dst = "192.168.1.106"
    iface = "eth0"
    count = 1
    ddos_test(src, dst, iface, count)
