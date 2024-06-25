# AnonBrowser

AnonBrowser is a Python script that provides a customized web browser for anonymous web browsing.\
It leverages the `mechanize` library for browsing capabilities and `http.cookiejar` for cookie management.\
The browser can randomly change user agents and proxies to help maintain anonymity.

## Features

- Clear cookies
- Change user agent randomly
- Change proxy randomly
- Optional sleep for delayed requests

## Requirements

- Python 3.x
- `mechanize` library
- `http.cookiejar` library

## Installation

Install the required libraries using pip:

```bash
pip install mechanize
```

## Usage: import it in your script

```python
import time
from anon_browser import AnonBrowser

# Define your proxies and user agents
proxies = ['proxy1:port', 'proxy2:port']
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
]

# Create an instance of AnonBrowser
browser = AnonBrowser(proxies=proxies, user_agents=user_agents)

# Open a URL
response = browser.open('http://example.com')
print(response.read())

# Anonymize the browser (clear cookies, change user agent and proxy)
browser.anonymize(sleep=True)  # sleep=True will wait for 60 seconds

```
