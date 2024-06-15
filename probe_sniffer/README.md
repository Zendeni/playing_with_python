# Probe Sniffer

This Python script uses `scapy` to sniff probe requests on a specified wireless interface in monitor mode (`mon0` by default). It detects and prints new probe requests along with their SSID.

## Requirements

- Python 3.x
- scapy library

Install scapy using pip:
```sh
pip install scapy
```

## Usage

Use tools like airmon-ng to set your wireless interface to monitor mode. Example:

sudo airmon-ng start wlan0

Run script
sudo python3 probe_sniffer.py
