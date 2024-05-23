# Nmap Scanner Script

This Python script uses the `nmap` library to perform TCP and UDP port scans on a specified target host. The script allows for scanning specific ports or conducting a full scan of all ports. It supports both TCP and UDP scans.

## Requirements

- Python 3.x
- `python-nmap` library

You can install the required library using pip:

```sh
pip install python-nmap
```

Command-line Arguments
-H: Specify the target host (required)
-p: Specify the target port(s), separated by commas if multiple
--full-scan: Perform a scan of all ports and services
--udp: Perform a UDP scan instead of the default TCP scan

## Examples

python nmap_scanner.py -H <target_host> -p 80,443,8080

python nmap_scanner.py -H <target_host> --full-scan

python nmap_scanner.py -H <target_host> -p 53,67,123 --udp

python nmap_scanner.py -H <target_host> --full-scan --udp


## Example Output

[*] 192.168.1.1 tcp/80 open http Apache 2.4.41
[*] 192.168.1.1 tcp/443 open https OpenSSL 1.1.1f

