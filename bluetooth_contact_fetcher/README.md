# Bluetooth Contact Fetcher

## Overview

This Python script establishes a Bluetooth connection to a specified phone and retrieves contacts using AT commands. It connects to the target phone via a Bluetooth socket and fetches contact details in a given range.

## Requirements

- Python 3.x
- PyBluez library

## Installation

1. **Install Python 3**: Ensure you have Python 3 installed on your system.

2. **Install PyBluez**: Install the PyBluez library using pip:
    ```sh
    pip install pybluez
    ```

## Usage

1. **Update the Script**: Modify the script with the appropriate target phone's Bluetooth address and the desired port.
    ```python
    TARGET_PHONE = 'AA:BB:CC:DD:EE:FF'  # Replace with your phone's Bluetooth address
    PORT = 17                           # Replace with the correct port if needed
    CONTACT_RANGE = range(1, 5)         # Adjust the contact range as required
    ```

2. **Run the Script**: Execute the script using Python 3.
    ```sh
    python fetch_contacts.py
    ```

3. **Output**: The script will print the contact details retrieved from the phone.

## Example

```sh
$ python fetch_contacts.py
[+] 1: John Doe, +1234567890
[+] 2: Jane Smith, +0987654321
[+] 3: Alice Johnson, +1122334455
[+] 4: Bob Brown, +5566778899
