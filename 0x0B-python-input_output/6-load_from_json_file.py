#!/usr/bin/python3
"""
This module contains one function
"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)
