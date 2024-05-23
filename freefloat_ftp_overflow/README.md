# Freefloat FTP 1.0 Buffer Overflow Exploit

## Description

This script exploits a buffer overflow vulnerability in Freefloat FTP 1.0 by sending a specially crafted command that triggers a buffer overflow, allowing the execution of arbitrary code. The script uses a hardcoded shellcode to open a shell on the target system.

## Usage

```sh
python3 exploit.py 192.168.1.10 PWND

