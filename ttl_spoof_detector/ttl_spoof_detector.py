import time
import argparse
from scapy.all import *
from IPy import IP as IPTEST

ttlValues = {}
THRESH = 5

def checkTTL(ipsrc, ttl):
    if IPTEST(ipsrc).iptype() == 'PRIVATE':
        return
    if ipsrc not in ttlValues:
        pkt = sr1(IP(dst=ipsrc) / ICMP(), retry=0, timeout=1, verbose=0)
        ttlValues[ipsrc] = pkt.ttl
    if abs(int(ttl) - int(ttlValues[ipsrc])) > THRESH:
        print(f'\n[!] Detected Possible Spoofed Packet From: {ipsrc}')
        print(f'[!] TTL: {ttl}, Actual TTL: {ttlValues[ipsrc]}')

def testTTL(pkt):
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            checkTTL(ipsrc, ttl)
    except Exception as e:
        pass

def main():
    parser = argparse.ArgumentParser(description="Detect possible spoofed packets based on TTL values.")
    parser.add_argument('-i', '--iface', type=str, help='Specify network interface')
    parser.add_argument('-t', '--thresh', type=int, help='Specify threshold count')
    args = parser.parse_args()

    if args.iface:
        conf.iface = args.iface
    else:
        conf.iface = 'eth0'

    global THRESH
    if args.thresh:
        THRESH = args.thresh

    sniff(prn=testTTL, store=0)

if __name__ == '__main__':
    main()
