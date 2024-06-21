# WiFi and Bluetooth Device Detector

This Python script detects WiFi MAC addresses and attempts to look up the corresponding Bluetooth device names.

## Requirements

- Python 3
- `scapy` library
- `pybluez` library

## Installation

1. Install `scapy`:
    ```sh
    pip install scapy
    ```

2. Install `pybluez`:
    ```sh
    pip install pybluez
    ```

## Usage

1. Ensure your network interface is set to monitor mode. This can usually be done with the following commands on Linux:

    ```sh
    sudo ifconfig <interface> down
    sudo iwconfig <interface> mode monitor
    sudo ifconfig <interface> up
    ```

2. Update the script to use the correct network interface (replace `'mon0'` with your interface name).

3. Run the script:
    ```sh
    python wifi_listener.py
    ```

## Script Details

### Functions

- `ret_bt_addr(addr)`: Converts a WiFi MAC address to a probable Bluetooth MAC address.
- `check_bluetooth(bt_addr)`: Checks if a Bluetooth device can be found with the given MAC address.
- `wifi_print(pkt)`: Checks packets for WiFi MAC addresses and attempts to find the corresponding Bluetooth device.

### Workflow

- The script listens for WiFi packets.
- When a WiFi MAC address is detected, it converts it to a probable Bluetooth MAC address.
- It then attempts to find and print the name of the Bluetooth device.


