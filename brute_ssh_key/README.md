# SSH Key Brute Force Script

This script attempts to brute force SSH login credentials using a directory of SSH key files. It leverages the `pexpect` library to manage SSH connections and `optparse` for command-line argument parsing. The script is multi-threaded to enhance efficiency and can manage a configurable number of simultaneous connections.

## Features

- Multi-threaded SSH brute force attack
- Handles common SSH connection issues
- Limits the number of simultaneous connections
- Exits gracefully when a key is found or too many failures occur

## Prerequisites

- Python 3.x
- `pexpect` library

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the `pexpect` library if you don't have it already:
   ```sh
   pip install pexpect


## Usage

python3 ssh_key_brute_force.py -H 192.168.1.100 -u root -d /path/to/keys
