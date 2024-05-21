# Zip File Password Cracker

This script attempts to crack the password of a zip file using a dictionary attack. It uses multiple threads to speed up the process by testing each password from the provided dictionary file.

## Features

- Multithreaded password cracking for efficiency.
- Uses a dictionary attack to test a list of passwords.
- Outputs the found password if successful.

## Prerequisites

- Python 3.x

## Installation

1. Ensure you have Python 3 installed on your system.

## Usage

Run the script with the following command-line arguments:

- `-f` or `--file`: Specify the zip file to crack.
- `-d` or `--dictionary`: Specify the dictionary file containing the list of passwords.

### Example

python3 zip_cracker.py -f protected.zip -d dictionary.txt
