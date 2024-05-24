import PyPDF2
import argparse

def print_meta(file_name):
    with open(file_name, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        doc_info = pdf_reader.metadata
        print(f'[*] PDF MetaData For: {file_name}')
        for meta_item, value in doc_info.items():
            print(f'[+] {meta_item}: {value}')

def main():
    parser = argparse.ArgumentParser(description='Extract metadata from a PDF file.')
    parser.add_argument('-F', '--file', dest='file_name', type=str, required=True,
                        help='Specify PDF file name')
    args = parser.parse_args()
    print_meta(args.file_name)

if __name__ == '__main__':
    main()
