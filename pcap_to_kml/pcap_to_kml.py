import dpkt
import socket
import pygeoip
import argparse

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def retKML(ip):
    rec = gi.record_by_name(ip)
    try:
        longitude = rec['longitude']
        latitude = rec['latitude']
        kml = (
            '<Placemark>\n'
            '<name>{}</name>\n'
            '<Point>\n'
            '<coordinates>{}, {}</coordinates>\n'
            '</Point>\n'
            '</Placemark>\n'
        ).format(ip, longitude, latitude)
        return kml
    except:
        return ''

def plotIPs(pcap):
    kmlPts = ''
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            if not isinstance(ip, dpkt.ip.IP):
                continue
            src = socket.inet_ntoa(ip.src)
            srcKML = retKML(src)
            dst = socket.inet_ntoa(ip.dst)
            dstKML = retKML(dst)
            kmlPts += srcKML + dstKML
        except:
            pass
    return kmlPts

def main():
    parser = argparse.ArgumentParser(description='Process a pcap file to generate KML data.')
    parser.add_argument('-p', '--pcapfile', type=str, required=True, help='Specify pcap filename')
    args = parser.parse_args()

    pcapFile = args.pcapfile
    with open(pcapFile, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'
        kmlfooter = '</Document>\n</kml>\n'
        kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
        print(kmldoc)

if __name__ == '__main__':
    main()
