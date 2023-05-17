#!/usr/bin/python3
"""uses json for input and output
"""
import sys
import os
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

name = "add_item.json"
new_list = []
if not os.stat(name).st_size == 0:
    new_list = load_from_json(name)
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        new_list.append(sys.argv[i])
save_to_json(new_list, name)
