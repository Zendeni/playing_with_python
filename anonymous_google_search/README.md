# Google Search Script

This script performs a Google search using the Google Custom Search JSON API and returns the search results.\
It uses an anonymous browser to enhance privacy.

## Requirements

- Python 3.x
- `requests` library for HTTP requests
- `mechanize` for browser automation
- Google Custom Search JSON API key
- Google Custom Search Engine ID

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required modules:

```bash
pip install requests mechanize
```
Obtain a Google API key and create a Custom Search Engine (CSE) from the Google Developers Console.

## Usage

python google_search.py -k "<your_search_keyword(s)>" -a "<your_api_key>" -c "<your_cse_id>"


