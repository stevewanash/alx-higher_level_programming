#!/usr/bin/python3
"""input and output JSON
"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
loadd = __import__('6-load_from_json_file').load_from_json_file
name = "./add_item.json"

with open(name, '+a', encoding='utf-8') as file:
    new_list = loadd(name)
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            new_list.append(sys.argv[i])

    save(new_list, name)
