#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    try:
        qv = sys.argv[1]
    except:
        qv = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': qv})
    try:
        print("[{}] {}".format(r.json()['id'], r.json()['name']))
    except ValueError:
        print("Not a valid JSON")
    except:
        print("No result")
