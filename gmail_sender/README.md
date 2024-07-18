# Email Sender Script

This script sends an email with a predefined message using Gmail's SMTP server.

## Requirements

- Python 3.x
- `smtplib` (comes with Python)
- `email` (comes with Python)
- `argparse` (comes with Python)

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone the repository or download the script file to your local machine.

## Usage

Run the script with the following arguments:

```bash
./email_sender.py -t <target_email> -l <gmail_login> -p <gmail_password>
```

-t : Target email to send the email to.
-l : Gmail login email.
-p : Gmail password.

