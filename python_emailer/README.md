## Python Emailer Script
This script sends an email using a Gmail SMTP server. It uses the smtplib and email.mime.text libraries.


## Requirements
Python 3\
Gmail account for sending emails

## Installation
Clone the repository or download the script.\
Ensure you have Python 3 installed on your system.

## Usage
Replace username@gmail.com and password in the script with your Gmail username and password.\
Replace target@tgt.tgt with the recipient's email address.\
Customize the email subject and body in the script as needed.


## Running the Script
Run the script using the following command:
```
python3 emailer.py
```

## Example
The script is designed to be run directly. It will send an email from the specified Gmail account to the specified recipient with the given subject and body text.

```
if __name__ == "__main__":
    user = 'username@gmail.com'
    pwd = 'password'
    send_mail(user, pwd, 'target@tgt.tgt', 'Re: Important', 'Test Message')
```


## Notes
Ensure that 'Less secure app access' is enabled on your Gmail account, or use an App Password if you have 2-Step Verification enabled.\
Handle your credentials securely and avoid hardcoding them in your script. Consider using environment variables or a configuration file.
