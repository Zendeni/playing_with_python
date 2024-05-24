import os
import argparse
from winreg import *

def sid2user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,
                      r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" + '\\' + sid)
        value, regtype = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except OSError:
        return sid

def return_dir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for recycle_dir in dirs:
        if os.path.isdir(recycle_dir):
            return recycle_dir
    return None

def find_recycled(recycle_dir):
    if recycle_dir is None:
        print("No recycle bin directory found.")
        return

    dir_list = os.listdir(recycle_dir)
    for sid in dir_list:
        sid_path = os.path.join(recycle_dir, sid)
        if os.path.isdir(sid_path):
            try:
                files = os.listdir(sid_path)
                user = sid2user(sid)
                print(f'\n[*] Listing Files For User: {user}')
                for file in files:
                    print(f'[+] Found File: {file}')
            except PermissionError:
                print(f"[!] Permission denied accessing {sid_path}")

def main():
    parser = argparse.ArgumentParser(description="Recycle Bin file lister for Windows")
    args = parser.parse_args()

    recycled_dir = return_dir()
    find_recycled(recycled_dir)

if __name__ == '__main__':
    main()
