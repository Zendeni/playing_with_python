from scapy.all import *

interface = 'mon0'
probe_reqs = []

def sniff_probe(packet):
    if packet.haslayer(Dot11ProbeReq):
        net_name = packet.info.decode('utf-8')
        if net_name not in probe_reqs:
            probe_reqs.append(net_name)
            print(f'[+] Detected New Probe Request: {net_name}')

def start_sniffer(interface):
    print(f'Starting sniffer on interface {interface}')
    sniff(iface=interface, prn=sniff_probe, store=0)

if __name__ == "__main__":
    start_sniffer(interface)
