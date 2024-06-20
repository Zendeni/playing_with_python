# Cookie Conflict Detector

This Python script uses Scapy to sniff network traffic on a specified interface and detect conflicts in cookies based on a given regex pattern.\
It identifies when a session cookie appears from different IP addresses, which might indicate a session hijacking attempt.

## Requirements

- Python 3.x
- Scapy

## Installation

1. **Clone the repository or download the script.**

2. **Install Scapy:**

    ```sh
    pip install scapy
    ```

## Usage

Run the script with the desired network interface and cookie regex pattern as arguments.

```sh
python cookie_detector.py -i <interface> -p <pattern>
