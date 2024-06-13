import re
import argparse
from scapy.all import sniff, Raw, conf

def find_google(pkt):
    if pkt.haslayer(Raw):
        payload = pkt[Raw].load.decode('utf-8', errors='ignore')
        if 'GET' in payload and 'google' in payload:
            r = re.findall(r'(?i)\&q=(.*?)\&', payload)
            if r:
                search = r[0].split('&')[0]
                search = search.replace('q=', '').replace('+', ' ').replace('%20', ' ')
                print(f'[+] Searched For: {search}')

def main():
    parser = argparse.ArgumentParser(description='Google search sniffer')
    parser.add_argument('-i', '--interface', type=str, required=True, help='specify interface to listen on')
    args = parser.parse_args()

    conf.iface = args.interface
    print('[*] Starting Google Sniffer.')
    try:
        sniff(filter='tcp port 80', prn=find_google)
    except KeyboardInterrupt:
        print("\n[*] Stopping Google Sniffer.")
        exit(0)

if __name__ == '__main__':
    main()
