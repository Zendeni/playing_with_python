import winreg

def val2addr(val):
    addr = ''
    for ch in val:
        addr += f'{ch:02x} '
    addr = addr.strip().replace(' ', ':')[0:17]
    return addr

def printNets():
    net = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, net)
    print('\n[*] Networks You Have Joined.')

    for i in range(100):
        try:
            guid = winreg.EnumKey(key, i)
            netKey = winreg.OpenKey(key, str(guid))
            addr = winreg.EnumValue(netKey, 5)[1]
            name = winreg.EnumValue(netKey, 4)[1]
            macAddr = val2addr(addr)
            netName = str(name)
            print(f'[+] {netName} {macAddr}')
            winreg.CloseKey(netKey)
        except OSError:
            break

def main():
    printNets()

if __name__ == "__main__":
    main()
