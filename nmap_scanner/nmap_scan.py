import argparse
import nmap  # Ensure this is python-nmap

def nmap_scan(tgt_host, tgt_port):
    try:
        nm_scan = nmap.PortScanner()
        nm_scan.scan(tgt_host, tgt_port)
        state = nm_scan[tgt_host]['tcp'][int(tgt_port)]['state']
        print(f"[*] {tgt_host} tcp/{tgt_port} {state}")
    except KeyError as e:
        print(f"An error occurred: {e}")
    except nmap.PortScannerError as e:
        print(f"Nmap scan error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Usage: %prog -H <target host> -p <target port>")
    parser.add_argument("-H", dest="tgt_host", type=str, required=True, help="specify target host")
    parser.add_argument("-p", dest="tgt_ports", type=str, required=True, help="specify target port(s), separated by commas if multiple")
    
    args = parser.parse_args()
    tgt_host = args.tgt_host
    tgt_ports = args.tgt_ports.split(',')

    for tgt_port in tgt_ports:
        if tgt_port.isdigit():
            nmap_scan(tgt_host, tgt_port)
        else:
            print(f"Invalid port number: {tgt_port}")

if __name__ == "__main__":
    main()
