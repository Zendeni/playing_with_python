#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
import argparse
from email.mime.text import MIMEText

def send_mail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            print("[+] Connecting To Mail Server.")
            smtp_server.ehlo()
            print("[+] Starting Encrypted Session.")
            smtp_server.starttls()
            smtp_server.ehlo()
            print("[+] Logging Into Mail Server.")
            smtp_server.login(user, pwd)
            print("[+] Sending Mail.")
            smtp_server.sendmail(user, to, msg.as_string())
            print("[+] Mail Sent Successfully.")
    except Exception as e:
        print(f"[-] Sending Mail Failed. Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Send an email with a predefined message')
    parser.add_argument('-t', dest='tgt', type=str, required=True, help='specify target email')
    parser.add_argument('-l', dest='user', type=str, required=True, help='specify gmail login')
    parser.add_argument('-p', dest='pwd', type=str, required=True, help='specify gmail password')
    
    args = parser.parse_args()
    
    tgt = args.tgt
    user = args.user
    pwd = args.pwd
    
    spam_msg = f"Dear {tgt},\n\nThis is a predefined message.\n\nBest regards,\nYour Name"
    
    print(f"[+] Sending Msg: {spam_msg}")
    send_mail(user, pwd, tgt, 'Re: Important', spam_msg)

if __name__ == '__main__':
    main()
