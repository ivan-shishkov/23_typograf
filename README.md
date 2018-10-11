# Typograf Service

This service is intended to process Russian texts with according to following rules:
* remove redundant spaces and line breaks
* replace quotes ' and " with french quotes
* replace hyphen with m-dash
* replace hyphen with n-dash in phone numbers
* bind numbers with next words using a non-breaking space
* bind words of 1-2 characters with next words using a non-breaking space

# Quickstart

For service launch need to install Python 3.5 and then install all dependencies:

```bash

$ pip install -r requirements.txt

```

Usage:

```bash

$ python3 server.py

```

Then open page [localhost:5000](http://localhost:5000) in browser.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
