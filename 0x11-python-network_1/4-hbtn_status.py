#!/usr/bin/python3
"""
This Python script fetches https://alx-intranet.hbtn.io/status
It uses the package requests
"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
