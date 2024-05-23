# Freefloat FTP 1.0 Buffer Overflow Exploit

## Description

This script exploits a buffer overflow vulnerability in Freefloat FTP 1.0 by sending a specially crafted command that triggers a buffer overflow, allowing the execution of arbitrary code. The script uses a hardcoded shellcode to open a shell on the target system.

## Usage

```sh
python3 exploit.py 192.168.1.10 PWND
```

## Supported Commands

AUTH (Authentication/Security Mechanism):

1. The AUTH command is used to specify an authentication mechanism to the server. This command is part of the FTP authentication and security extensions and allows for more secure methods of authenticating than plain text username and password.
APPE (Append):

2. The APPE command is used to append data to an existing file on the FTP server. If the file does not exist, the server might create it, depending on the server's implementation.
ALLO (Allocate):

3. The ALLO command is used to allocate sufficient storage space to accommodate the file being transferred. It’s more of an advisory command and is rarely required or enforced by modern FTP servers.
ACCT (Account):

4. The ACCT command is used to send account information to the FTP server. Some servers require an additional account parameter after the initial login to grant specific permissions or access to certain resources.
