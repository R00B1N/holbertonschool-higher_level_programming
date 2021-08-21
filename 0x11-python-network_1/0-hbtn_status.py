#!/usr/bin/python3
""" a Python script that fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        print("Body response:")
        html = response.read()
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
