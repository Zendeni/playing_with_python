# Nmap Scanner Script

This script is a simple wrapper around the `nmap` tool, allowing you to scan specified ports on a target host. It uses the `python-nmap` library and `argparse` for command-line argument parsing.

## Requirements

- Python 3.x
- `nmap` installed on your system
- `python-nmap` library

## Installation

1. Install `nmap` on your system. Instructions can be found [here](https://nmap.org/download.html).

2. Install the `python-nmap` library:

    ```sh
    pip install python-nmap
    ```

## Usage

Run the script from the command line with the following options:

- `-H`: Specify the target host
- `-p`: Specify the target port(s), separated by commas if multiple

### Example

To scan port 80 on the target host `192.168.1.1`:

```sh
python script.py -H 192.168.1.1 -p 80
