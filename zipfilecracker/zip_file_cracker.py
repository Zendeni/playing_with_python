import zipfile
import argparse
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password.encode('utf-8'))
        print('[+] Found Password: ' + password + '\n')
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description='Zip file password cracker using a dictionary attack')
    parser.add_argument('-f', dest='zFile', type=str, required=True, help='specify zip file')
    parser.add_argument('-d', dest='dFile', type=str, required=True, help='specify dictionary file')
    args = parser.parse_args()

    zFile = zipfile.ZipFile(args.zFile)
    passFile = open(args.dFile, 'r')

    for line in passFile.readlines():
        password = line.strip()
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()
