import re
import argparse
from scapy.all import sniff, IP

cookie_table = {}

def detect_cookie_conflict(pkt, pattern):
    raw = pkt.sprintf('%Raw.load%')
    matches = re.findall(pattern, raw)
    if matches and 'Set' not in raw:
        cookie = matches[0]
        ip_src = pkt.getlayer(IP).src
        if cookie not in cookie_table:
            cookie_table[cookie] = ip_src
            print('[+] Detected and indexed cookie.')
        elif cookie_table[cookie] != ip_src:
            print('[*] Detected Conflict for ' + cookie)
            print('Victim = ' + cookie_table[cookie])
            print('Attacker = ' + ip_src)

def main():
    parser = argparse.ArgumentParser(description="Packet sniffer to detect conflicts in cookies.")
    parser.add_argument('-i', '--interface', required=True, help='Specify interface to listen on')
    parser.add_argument('-p', '--pattern', required=True, help='Specify the regex pattern to match cookies')
    args = parser.parse_args()

    conf.iface = args.interface
    try:
        sniff(filter='tcp port 80', prn=lambda x: detect_cookie_conflict(x, args.pattern))
    except KeyboardInterrupt:
        print("\n[!] Sniffing interrupted by user. Exiting...")
        exit(0)

if __name__ == '__main__':
    main()
