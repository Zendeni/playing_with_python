# FTP Sniffer

## Overview

The FTP Sniffer is a Python script that listens for FTP traffic on a specified network interface and captures FTP login credentials (username and password).

## Requirements

- Python 3.x
- Scapy library


Install Scapy:
    ```sh
    pip install scapy
    ```

## Usage

Run the script with the `-i` or `--interface` option to specify the network interface to listen on.

```sh
python ftp_sniffer.py -i <interface>
```
python ftp_sniffer.py -i eth0
