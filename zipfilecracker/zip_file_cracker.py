import zipfile
import argparse
from threading import Thread

def extract_file(zfile, password):
    try:
        zfile.extractall(pwd=password.encode('utf-8'))
        print(f'[+] Found Password: {password}\n')
    except (RuntimeError, zipfile.BadZipFile):
        pass

def process_passwords(zfile, dictionary_file):
    with open(dictionary_file, 'r') as pass_file:
        for line in pass_file:
            password = line.strip()
            t = Thread(target=extract_file, args=(zfile, password))
            t.start()
            t.join()  # Ensures each thread completes before starting a new one

def main():
    parser = argparse.ArgumentParser(description='Zip file password cracker using a dictionary attack')
    parser.add_argument('-f', '--file', dest='zfile', type=str, required=True, help='Specify zip file')
    parser.add_argument('-d', '--dictionary', dest='dfile', type=str, required=True, help='Specify dictionary file')
    args = parser.parse_args()

    try:
        with zipfile.ZipFile(args.zfile) as zfile:
            process_passwords(zfile, args.dfile)
    except FileNotFoundError:
        print(f'Error: File {args.zfile} or {args.dfile} not found.')
    except zipfile.BadZipFile:
        print(f'Error: File {args.zfile} is not a valid zip file.')

if __name__ == '__main__':
    main()
