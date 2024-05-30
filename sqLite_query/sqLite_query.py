import sqlite3
import argparse
import os

def query_table(db_path, table, columns):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    columns_str = ', '.join(columns)
    query = f"SELECT {columns_str} FROM {table};"
    c.execute(query)
    print(f'\n[*] -- Data from {table} --')
    for row in c:
        print('[+] ' + ' | '.join(f"{col}: {val}" for col, val in zip(columns, row)))
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="Query a SQLite database.")
    parser.add_argument('-p', '--path', required=True, help='Specify the database path')
    parser.add_argument('-t', '--table', required=True, help='Specify the table name to query')
    parser.add_argument('-c', '--columns', nargs='+', required=True, help='Specify the columns to query')
    args = parser.parse_args()
    db_path = args.path
    table = args.table
    columns = args.columns

    if not os.path.isdir(db_path):
        print('[!] Path Does Not Exist: ' + db_path)
        exit(1)

    db_file = os.path.join(db_path, 'main.db')
    if os.path.isfile(db_file):
        query_table(db_file, table, columns)
    else:
        print('[!] Database does not exist: ' + db_file)
        exit(1)

if __name__ == '__main__':
    main()
