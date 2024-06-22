from bluetooth import find_service

def sdp_browse(addr):
    """Browse and print available Bluetooth services for a given address."""
    services = find_service(address=addr)
    if not services:
        print(f'[-] No services found on {addr}')
        return
    
    for service in services:
        name = service.get('name', 'Unknown')
        proto = service.get('protocol', 'Unknown')
        port = str(service.get('port', 'Unknown'))
        print(f'[+] Found {name} on {proto}:{port}')

if __name__ == "__main__":
    device_address = '00:16:38:DE:AD:11'
    sdp_browse(device_address)
