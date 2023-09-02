#!/usr/bin/python3
"""
This Python script takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter,
and finally displays the body of the response.
e.g. ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    response = requests.post(url, data=value)
    print(response.text)
