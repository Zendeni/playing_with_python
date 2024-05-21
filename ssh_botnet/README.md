# SSH Botnet Command Execution Script

This script allows you to execute commands on multiple SSH-connected machines (a botnet) using the `pxssh` module from `pexpect`.

## Features

- Connect to multiple SSH hosts.
- Execute commands on all connected hosts.
- Display output from each host.

## Prerequisites

- Python 3.x
- `pexpect` library

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the `pexpect` library if you don't have it already:
   ```sh
   pip install pexpect

## Usage

To use the script, you need to define the SSH hosts and credentials, and then execute the desired commands.

## Example

Add clients (SSH hosts) with their credentials.
Execute commands on all connected hosts.

## Running the Script

python3 ssh_botnet.py
