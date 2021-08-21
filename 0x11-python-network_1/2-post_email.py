#!/usr/bin/python3
""" a Python script that sends an email in a POST request to a URL"""
import urllib.request
import sys


if __name__ == '__main__':
    data = "email=" + sys.argv[2]
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
