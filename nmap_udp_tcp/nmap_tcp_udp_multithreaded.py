import argparse
import nmap  # Ensure this is python-nmap
from concurrent.futures import ThreadPoolExecutor, as_completed

def nmap_scan(tgt_host, tgt_ports, scan_type='tcp'):
    try:
        nm_scan = nmap.PortScanner()
        port_range = ','.join(map(str, tgt_ports))
        nm_scan.scan(tgt_host, port_range, arguments=f'-T4 -s{scan_type[0].upper()}')
        for port in nm_scan[tgt_host][scan_type]:
            state = nm_scan[tgt_host][scan_type][port]['state']
            service = nm_scan[tgt_host][scan_type][port]['name']
            version = nm_scan[tgt_host][scan_type][port].get('version', 'unknown')
            print(f"[*] {tgt_host} {scan_type}/{port} {state} {service} {version}")
    except KeyError as e:
        print(f"An error occurred: {e}")
    except nmap.PortScannerError as e:
        print(f"Nmap scan error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def full_scan(tgt_host, scan_type='tcp'):
    try:
        nm_scan = nmap.PortScanner()
        nm_scan.scan(tgt_host, '1-65535', arguments=f'-T4 -s{scan_type[0].upper()}')
        for port in nm_scan[tgt_host][scan_type]:
            state = nm_scan[tgt_host][scan_type][port]['state']
            service = nm_scan[tgt_host][scan_type][port]['name']
            version = nm_scan[tgt_host][scan_type][port].get('version', 'unknown')
            print(f"[*] {tgt_host} {scan_type}/{port} {state} {service} {version}")
    except KeyError as e:
        print(f"An error occurred: {e}")
    except nmap.PortScannerError as e:
        print(f"Nmap scan error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def parallel_scan(tgt_host, ports, scan_type):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(nmap_scan, tgt_host, [port], scan_type): port for port in ports}
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error scanning port {futures[future]}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Usage: %prog -H <target host> [-p <target port(s)> | --full-scan] [--udp | --tcp] [--both]")
    parser.add_argument("-H", dest="tgt_host", type=str, required=True, help="specify target host")
    parser.add_argument("-p", dest="tgt_ports", type=str, help="specify target port(s), separated by commas if multiple")
    parser.add_argument("--full-scan", dest="full_scan", action="store_true", help="scan all ports and services")
    parser.add_argument("--udp", dest="udp_scan", action="store_true", help="perform a UDP scan")
    parser.add_argument("--tcp", dest="tcp_scan", action="store_true", help="perform a TCP scan")
    parser.add_argument("--both", dest="both_scan", action="store_true", help="perform both TCP and UDP scans")

    args = parser.parse_args()
    tgt_host = args.tgt_host

    if args.both_scan:
        scan_types = ['tcp', 'udp']
    else:
        scan_types = []
        if args.tcp_scan:
            scan_types.append('tcp')
        if args.udp_scan:
            scan_types.append('udp')

    if args.full_scan:
        for scan_type in scan_types:
            full_scan(tgt_host, scan_type)
    elif args.tgt_ports:
        tgt_ports = args.tgt_ports.split(',')
        valid_ports = [int(port) for port in tgt_ports if port.isdigit()]
        for scan_type in scan_types:
            parallel_scan(tgt_host, valid_ports, scan_type)
    else:
        print("Please specify either -p for target ports or --full-scan for a full scan, and at least one of --tcp, --udp, or --both")

if __name__ == "__main__":
    main()
