import argparse
import nmap
import threading
import sys
import time

progress = 0
nm_scan = nmap.PortScanner()
scan_details = ""
scan_in_progress = False

def nmap_scan(tgt_host, tgt_ports):
    global progress, nm_scan, scan_details, scan_in_progress
    scan_in_progress = True
    try:
        nm_scan.scan(tgt_host, ','.join(tgt_ports))
        total_ports = len(tgt_ports)
        for i, port in enumerate(tgt_ports):
            port = int(port)
            state = nm_scan[tgt_host]['tcp'][port]['state']
            service = nm_scan[tgt_host]['tcp'][port]['name']
            version = nm_scan[tgt_host]['tcp'][port]['version']
            scan_details = f"Scanning port {port}: {service} {version} ({state})"
            print(f"[*] {tgt_host} tcp/{port} {state} {service} {version}")
            progress = int(((i + 1) / total_ports) * 100)
    except KeyError as e:
        print(f"An error occurred: {e}")
    except nmap.PortScannerError as e:
        print(f"Nmap scan error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    scan_in_progress = False

def full_scan(tgt_host):
    global progress, nm_scan, scan_details, scan_in_progress
    scan_in_progress = True
    try:
        nm_scan.scan(tgt_host, '1-65535')
        total_ports = 65535
        for i, port in enumerate(nm_scan[tgt_host]['tcp']):
            state = nm_scan[tgt_host]['tcp'][port]['state']
            service = nm_scan[tgt_host]['tcp'][port]['name']
            version = nm_scan[tgt_host]['tcp'][port]['version']
            scan_details = f"Scanning port {port}: {service} {version} ({state})"
            print(f"[*] {tgt_host} tcp/{port} {state} {service} {version}")
            progress = int(((i + 1) / total_ports) * 100)
    except KeyError as e:
        print(f"An error occurred: {e}")
    except nmap.PortScannerError as e:
        print(f"Nmap scan error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    scan_in_progress = False

def check_spacebar():
    global scan_in_progress
    while scan_in_progress:
        if sys.stdin.read(1) == ' ':
            print(f"\nProgress: {progress}%\nDetails: {scan_details}\n")
        time.sleep(0.1)

def main():
    global scan_in_progress
    parser = argparse.ArgumentParser(description="Usage: %prog -H <target host> [-p <target port(s)> | --full-scan]")
    parser.add_argument("-H", dest="tgt_host", type=str, required=True, help="specify target host")
    parser.add_argument("-p", dest="tgt_ports", type=str, help="specify target port(s), separated by commas if multiple")
    parser.add_argument("--full-scan", dest="full_scan", action="store_true", help="scan all ports and services")

    args = parser.parse_args()
    tgt_host = args.tgt_host

    scan_thread = None

    if args.full_scan:
        scan_thread = threading.Thread(target=full_scan, args=(tgt_host,))
    elif args.tgt_ports:
        tgt_ports = args.tgt_ports.split(',')
        scan_thread = threading.Thread(target=nmap_scan, args=(tgt_host, tgt_ports))
    else:
        print("Please specify either -p for target ports or --full-scan for a full scan")
        sys.exit(1)

    scan_in_progress = True
    scan_thread.start()

    print("Press spacebar to see progress...")
    check_spacebar_thread = threading.Thread(target=check_spacebar)
    check_spacebar_thread.start()

    scan_thread.join()
    scan_in_progress = False
    check_spacebar_thread.join()
    print("Scan completed.")

if __name__ == "__main__":
    main()
