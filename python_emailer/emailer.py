import smtplib
from email.mime.text import MIMEText

def send_mail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            print("[+] Connecting to Mail Server.")
            smtp_server.ehlo()
            print("[+] Starting Encrypted Session.")
            smtp_server.starttls()
            smtp_server.ehlo()
            print("[+] Logging into Mail Server.")
            smtp_server.login(user, pwd)
            print("[+] Sending Mail.")
            smtp_server.sendmail(user, to, msg.as_string())
            print("[+] Mail Sent Successfully.")
    except Exception as e:
        print(f"[-] Sending Mail Failed: {e}")

if __name__ == "__main__":
    user = 'username@gmail.com'
    pwd = 'password'
    send_mail(user, pwd, 'target@tgt.tgt', 'Re: Important', 'Test Message')
