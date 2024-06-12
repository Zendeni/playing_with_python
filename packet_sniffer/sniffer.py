import re
import argparse
from scapy.all import sniff, conf

def find_data(pkt, patterns):
    raw = pkt.sprintf('%Raw.load%')
    results = {}
    for key, pattern in patterns.items():
        match = re.findall(pattern, raw)
        if match:
            results[key] = match[0]
    if results:
        print(f'[+] Found data: {results}')

def main():
    parser = argparse.ArgumentParser(description='Packet Sniffer')
    parser.add_argument('-i', '--interface', type=str, required=True, help='Specify interface to listen on')
    parser.add_argument('-p', '--patterns', type=str, nargs='+', required=True, 
                        help='Specify patterns in the form key=pattern.')
    args = parser.parse_args()

    conf.iface = args.interface
    patterns = {p.split('=')[0]: p.split('=')[1] for p in args.patterns}

    print('[*] Starting Packet Sniffer.')
    try:
        sniff(filter='tcp', prn=lambda pkt: find_data(pkt, patterns), store=0)
    except KeyboardInterrupt:
        print('\n[*] Stopping Packet Sniffer.')
        exit(0)

if __name__ == '__main__':
    main()
