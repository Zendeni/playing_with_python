# Google Search Sniffer

This script is a network sniffer that captures unencrypted packets and displays Google search queries made over HTTP. It uses the Scapy library to capture packets and extracts search queries from the HTTP GET requests.

## Requirements

- Python 3.x
- Scapy
- argparse

## Installation

 Install Scapy:
    ```bash
    pip install scapy
    ```


## Usage

Run the script with the following command:

```bash
python google_sniffer.py -i <interface>
```
