def val2addr(val):
    addr = ""
    for ch in val:
        addr += ("%02x " % ch)
    addr = addr.strip().replace(" ", ":")[0:17]
    return addr

# The given binary data
binary_data = bytes.fromhex("BinaryHere")

# Convert the binary data to MAC addresses
mac_addresses = []
for i in range(0, len(binary_data), 6):
    if i + 6 <= len(binary_data):
        mac = val2addr(binary_data[i:i+6])
        mac_addresses.append(mac)

# Print the results
for mac in mac_addresses:
    print(mac)
