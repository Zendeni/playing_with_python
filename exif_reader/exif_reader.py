import urllib.request
import argparse
from urllib.parse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

def find_images(url):
    try:
        print(f'[+] Finding images on {url}')
        url_content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(url_content, 'html.parser')
        img_tags = soup.findAll('img')
        print(f'[+] Found {len(img_tags)} images')
        return img_tags
    except Exception as e:
        print(f'[-] Error finding images: {e}')
        return []

def download_image(img_tag):
    try:
        print('[+] Downloading image...')
        img_src = img_tag.get('src')
        if not img_src:
            print('[-] No src attribute found')
            return ''
        img_content = urllib.request.urlopen(img_src).read()
        img_file_name = basename(urlsplit(img_src)[2])
        with open(img_file_name, 'wb') as img_file:
            img_file.write(img_content)
        print(f'[+] Downloaded image: {img_file_name}')
        return img_file_name
    except Exception as e:
        print(f'[-] Failed to download image: {e}')
        return ''

def test_for_exif(img_file_name):
    try:
        exif_data = {}
        img_file = Image.open(img_file_name)
        info = img_file._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value
            exif_gps = exif_data.get('GPSInfo')
            if exif_gps:
                print(f'[*] {img_file_name} contains GPS MetaData')
            else:
                print(f'[-] No GPS MetaData found in {img_file_name}')
        else:
            print(f'[-] No EXIF data found in {img_file_name}')
    except Exception as e:
        print(f'[-] Failed to extract EXIF data: {e}')

def main():
    parser = argparse.ArgumentParser(description='Download images from a URL and check for EXIF data.')
    parser.add_argument('-u', '--url', type=str, required=True, help='Specify URL address')
    args = parser.parse_args()
    url = args.url

    print(f'[+] Processing URL: {url}')
    img_tags = find_images(url)
    for img_tag in img_tags:
        img_file_name = download_image(img_tag)
        if img_file_name:
            test_for_exif(img_file_name)

if __name__ == '__main__':
    main()
