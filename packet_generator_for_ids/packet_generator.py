from scapy.all import *

def ddos_test(src, dst, iface, count):
    packets = [
        IP(src=src, dst=dst)/ICMP(type=8, id=678)/Raw(load='1234'),
        IP(src=src, dst=dst)/ICMP(type=0)/Raw(load='AAAAAAAAAA'),
        IP(src=src, dst=dst)/UDP(dport=31335)/Raw(load='PONG'),
        IP(src=src, dst=dst)/ICMP(type=0, id=456)
    ]
    
    for pkt in packets:
        send(pkt, iface=iface, count=count)

if __name__ == "__main__":
    src = "1.3.3.7"
    dst = "192.168.1.106"
    iface = "eth0"
    count = 1
    ddos_test(src, dst, iface, count)
