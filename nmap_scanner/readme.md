# Nmap Scan Script

This Python script utilizes the `nmap` library to scan specified ports or all ports on a target host. It provides real-time feedback on the scan progress and allows you to monitor the scan interactively by pressing the spacebar to see the percentage of completion and current scan details.

## Features

- Scan specified ports on a target host.
- Perform a full scan of all ports on a target host.
- Display real-time progress and details of the current scan.
- Interactive monitoring by pressing the spacebar.

## Requirements

- Python 3.x
- `python-nmap` library

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the `python-nmap` library:

```bash
pip install python-nmap keyboard
```
## Examples
Scan specific ports:
python nmap_scan.py -H 192.168.1.1 -p 22,80,443

Perform a full scan:
python nmap_scan.py -H 192.168.1.1 --full-scan

Perform a range scan for ports 1-100:
python nmap_scan.py -H 192.168.1.1 --range-scan


![image](https://github.com/Zendeni/playing_with_python/assets/53412927/5eb96546-a932-4abf-8196-42f1c94cf98c)
