# Hidden SSID Detector

This script detects hidden SSIDs by sniffing 802.11 probe response and beacon frames. When a hidden SSID is decloaked, the script prints the SSID along with the MAC address of the access point.

## Prerequisites

- Python 3.x
- Scapy

## Installation

1. **Install Scapy:**

    ```bash
    pip install scapy
    ```

2. **Ensure you have the necessary permissions:**

    Sniffing network traffic typically requires root privileges. You may need to run the script with `sudo`.

3. **Set up your network interface:**

    Ensure your network interface is in monitor mode. For example, to set `wlan0` to monitor mode using `airmon-ng`:

    ```bash
    sudo airmon-ng start wlan0
    ```

    This will typically rename the interface to something like `wlan0mon`.

## Usage

1. **Edit the interface variable in the script:**

    Change the `interface` variable in `hidden_ssid_detector.py` to match your network interface in monitor mode (e.g., `wlan0mon`).

2. **Run the script:**

    ```bash
    sudo python3 hidden_ssid_detector.py
    ```

## How it Works

- **Dot11Beacon frames:** These frames are sent periodically by access points to announce the presence of a wireless network. If the SSID field is empty, it indicates a hidden SSID.

- **Dot11ProbeResp frames:** These frames are sent by access points in response to probe request frames from clients. If a client probes for a specific SSID, the access point responds with the SSID, even if it is hidden.

The script identifies hidden SSIDs by analyzing these frames and printing the SSID and MAC address once the hidden SSID is decloaked.

