# SSH Brute Force Script

This script attempts to brute force SSH login credentials using a list of passwords. It utilizes the `pxssh` module from `pexpect` to handle SSH connections and the `optparse` module for command-line argument parsing. The script is multi-threaded to improve efficiency and can handle a configurable number of simultaneous connections.

## Features

- Multi-threaded brute force attack
- Handles common SSH connection issues
- Limits the number of simultaneous connections
- Exits gracefully when a password is found or too many failures occur

## Prerequisites

- Python 3.x
- `pexpect` library

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the `pexpect` library if you don't have it already:
   ```sh
   pip install pexpect


## Usage

python3 ssh_brute_force.py -H 192.168.1.100 -u root -F passwords.txt
