# Bluetooth Service Discovery Script

## Description

This Python script performs a Bluetooth Service Discovery Protocol (SDP) browse on a specified Bluetooth device address. It discovers and prints the available services on the device.

## Requirements

- Python 3.x
- PyBluez library
- A Bluetooth adapter and stack configured on your system

## Installation

1. Ensure you have Python 3 installed on your machine.

2. Install the PyBluez library if you don't have it already. You can install it using pip:

    ```bash
    pip install pybluez
    ```

3. On Linux, ensure you have `bluez` installed and running. You can typically install it using your package manager. For example, on Ubuntu:

    ```bash
    sudo apt-get install bluez
    ```

## Usage

1. Save the script to a file, e.g., `sdp_browse.py`.

2. Run the script using Python. You might need to use `sudo` to run the script with the necessary permissions:

    ```bash
    sudo python sdp_browse.py
    ```

    Ensure you replace `'00:16:38:DE:AD:11'` in the script with the Bluetooth address of the device you want to browse.

## Example

The script will output the services found on the specified Bluetooth device, for example:\

[+] Found OBEX Object Push on RFCOMM:9
[+] Found Voice Gateway on RFCOMM:4
[+] Found Serial Port on RFCOMM:1

