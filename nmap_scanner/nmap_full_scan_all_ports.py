import argparse
import nmap  # Ensure this is python-nmap

def nmap_scan(tgt_host, tgt_ports):
    try:
        nm_scan = nmap.PortScanner()
        nm_scan.scan(tgt_host, tgt_ports)
        for port in nm_scan[tgt_host]['tcp']:
            state = nm_scan[tgt_host]['tcp'][port]['state']
            service = nm_scan[tgt_host]['tcp'][port]['name']
            version = nm_scan[tgt_host]['tcp'][port]['version']
            print(f"[*] {tgt_host} tcp/{port} {state} {service} {version}")
    except KeyError as e:
        print(f"An error occurred: {e}")
    except nmap.PortScannerError as e:
        print(f"Nmap scan error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def full_scan(tgt_host):
    try:
        nm_scan = nmap.PortScanner()
        nm_scan.scan(tgt_host, '1-65535')
        for port in nm_scan[tgt_host]['tcp']:
            state = nm_scan[tgt_host]['tcp'][port]['state']
            service = nm_scan[tgt_host]['tcp'][port]['name']
            version = nm_scan[tgt_host]['tcp'][port]['version']
            print(f"[*] {tgt_host} tcp/{port} {state} {service} {version}")
    except KeyError as e:
        print(f"An error occurred: {e}")
    except nmap.PortScannerError as e:
        print(f"Nmap scan error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Usage: %prog -H <target host> [-p <target port(s)> | --full-scan]")
    parser.add_argument("-H", dest="tgt_host", type=str, required=True, help="specify target host")
    parser.add_argument("-p", dest="tgt_ports", type=str, help="specify target port(s), separated by commas if multiple")
    parser.add_argument("--full-scan", dest="full_scan", action="store_true", help="scan all ports and services")

    args = parser.parse_args()
    tgt_host = args.tgt_host

    if args.full_scan:
        full_scan(tgt_host)
    elif args.tgt_ports:
        tgt_ports = args.tgt_ports.split(',')
        for tgt_port in tgt_ports:
            if tgt_port.isdigit():
                nmap_scan(tgt_host, tgt_port)
            else:
                print(f"Invalid port number: {tgt_port}")
    else:
        print("Please specify either -p for target ports or --full-scan for a full scan")

if __name__ == "__main__":
    main()
