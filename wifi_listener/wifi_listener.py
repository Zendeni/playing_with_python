from scapy.all import *
from bluetooth import *

def ret_bt_addr(addr):
    bt_addr = str(hex(int(addr.replace(':', ''), 16) + 1))[2:]
    bt_addr = ':'.join([bt_addr[i:i+2] for i in range(0, 12, 2)])
    return bt_addr

def check_bluetooth(bt_addr):
    bt_name = lookup_name(bt_addr)
    if bt_name:
        print(f'[+] Detected Bluetooth Device: {bt_name}')
    else:
        print('[-] Failed to Detect Bluetooth Device.')

def wifi_print(pkt):
    if pkt.haslayer(Dot11):
        wifi_mac = pkt.getlayer(Dot11).addr2
        if wifi_mac:
            print(f'[*] Detected WiFi MAC: {wifi_mac}')
            bt_addr = ret_bt_addr(wifi_mac)
            print(f'[+] Testing Bluetooth MAC: {bt_addr}')
            check_bluetooth(bt_addr)

if __name__ == "__main__":
    conf.iface = 'mon0'
    sniff(prn=wifi_print)
