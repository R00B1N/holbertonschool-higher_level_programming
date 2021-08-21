#!/usr/bin/python3
""" a Python script that requests an url and displays
the value of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == '__main__':
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
