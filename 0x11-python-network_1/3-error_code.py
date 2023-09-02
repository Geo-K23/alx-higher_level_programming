#!/usr/bin/python3
"""
This Python script takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
e.g.: ./3-error_code.py <URL>
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
