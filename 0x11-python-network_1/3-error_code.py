#!/usr/bin/python3
""" a Python script that displays the error code """
import urllib.request
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
