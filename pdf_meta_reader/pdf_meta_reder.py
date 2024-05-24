import PyPDF2
import argparse

def print_meta(file_name):
    with open(file_name, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        doc_info = pdf_reader.getDocumentInfo()
        print(f'[*] PDF MetaData For: {file_name}')
        for meta_item in doc_info:
            print(f'[+] {meta_item}: {doc_info[meta_item]}')

def main():
    parser = argparse.ArgumentParser(description='Extract metadata from a PDF file.')
    parser.add_argument('-F', '--file', dest='file_name', type=str, required=True,
                        help='Specify PDF file name')
    args = parser.parse_args()
    print_meta(args.file_name)

if __name__ == '__main__':
    main()
