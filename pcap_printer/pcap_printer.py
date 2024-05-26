import dpkt
import socket
import pygeoip
import argparse

# Initialize GeoIP database
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city:
            geoLoc = f"{city}, {country}"
        else:
            geoLoc = country
        return geoLoc
    except Exception as e:
        return 'Unregistered'

def printPcap(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if not isinstance(eth.data, dpkt.ip.IP):
                continue  # Not an IP packet
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print(f'[+] Src: {src} --> Dst: {dst}')
            print(f'[+] Src: {retGeoStr(src)} --> Dst: {retGeoStr(dst)}')
        except Exception as e:
            print(f"Error processing packet: {e}")

def main():
    parser = argparse.ArgumentParser(description='Packet Sniffer Tool')
    parser.add_argument('-p', '--pcapfile', type=str, required=True, help='specify pcap filename')
    args = parser.parse_args()
    
    pcapFile = args.pcapfile
    with open(pcapFile, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        printPcap(pcap)

if __name__ == '__main__':
    main()
