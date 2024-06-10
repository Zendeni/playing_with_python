import argparse
from scapy.all import *
from random import randint

def ddos_test(src, dst, iface, count):
    packets = [
        IP(src=src, dst=dst)/ICMP(type=8, id=678)/Raw(load='1234'),
        IP(src=src, dst=dst)/ICMP(type=0)/Raw(load='AAAAAAAAAA'),
        IP(src=src, dst=dst)/UDP(dport=31335)/Raw(load='PONG'),
        IP(src=src, dst=dst)/ICMP(type=0, id=456)
    ]
    for pkt in packets:
        send(pkt, iface=iface, count=count)

def exploit_test(src, dst, iface, count):
    packets = [
        IP(src=src, dst=dst) / UDP(dport=518) / Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8"),
        IP(src=src, dst=dst) / UDP(dport=635) / Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    ]
    for pkt in packets:
        send(pkt, iface=iface, count=count)

def scan_test(src, dst, iface, count):
    packets = [
        IP(src=src, dst=dst) / UDP(dport=7) / Raw(load='cybercop'),
        IP(src=src, dst=dst) / UDP(dport=10080) / Raw(load='Amanda')
    ]
    for pkt in packets:
        send(pkt, iface=iface, count=count)

def main():
    parser = argparse.ArgumentParser(description='Network testing script.')
    parser.add_argument('-i', dest='iface', type=str, default='eth0', help='specify network interface')
    parser.add_argument('-s', dest='src', type=str, help='specify source address')
    parser.add_argument('-t', dest='tgt', type=str, required=True, help='specify target address')
    parser.add_argument('-c', dest='count', type=int, default=1, help='specify packet count')

    args = parser.parse_args()

    iface = args.iface
    src = args.src if args.src else '.'.join([str(randint(1, 254)) for _ in range(4)])
    dst = args.tgt
    count = args.count

    ddos_test(src, dst, iface, count)
    exploit_test(src, dst, iface, count)
    scan_test(src, dst, iface, count)

if __name__ == '__main__':
    main()
