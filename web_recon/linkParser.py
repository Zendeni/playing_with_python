import requests
from bs4 import BeautifulSoup
import os
import argparse
import re

class AnonBrowser:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    def anonymize(self):
        # Add your proxy settings here if required
        self.session.proxies = {
            'http': 'http://127.0.0.1:8080',
            'https': 'https://127.0.0.1:8080'
        }

    def open(self, url):
        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response

def print_links(url):
    ab = AnonBrowser()
    ab.anonymize()
    page = ab.open(url)
    html = page.text

    try:
        print('[+] Printing Links From Regex.')
        link_finder = re.compile(r'href="(.*?)"')
        links = link_finder.findall(html)
        for link in links:
            print(link)
    except Exception as e:
        print(f'[-] Error finding links with regex: {e}')

    try:
        print('\n[+] Printing Links From BeautifulSoup.')
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            if 'href' in link.attrs:
                print(link['href'])
    except Exception as e:
        print(f'[-] Error finding links with BeautifulSoup: {e}')

def main():
    parser = argparse.ArgumentParser(description='Web Recon with Python')
    parser.add_argument('-u', dest='tgtURL', type=str, required=True, help='Specify target URL')
    args = parser.parse_args()

    url = args.tgtURL
    if not url:
        parser.print_help()
        exit(0)
    else:
        print_links(url)

if __name__ == '__main__':
    main()
