#!/usr/bin/python3
"""
a script that adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
try:
    obj = load_from_json_file("add_item.json")
except:
    save_to_json_file([], "add_item.json")
obj = load_from_json_file("add_item.json")
l = []
for i in range(1, len(sys.argv)):
    l.append(sys.argv[i])
obj = obj + l
save_to_json_file(obj, "add_item.json")
