import zipfile
import optparse
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('[+] Found Password ' + password + '\n')
    except:
        pass
def main():
    parser = optparse.OptionParser("usage="%prog "+\" -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zFile', type='string', help='specify zip file')
    parser.add_option('-d', dest='dFile', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zFile == None) | (options.dFile == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zFile
        dname = options.dFile
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
