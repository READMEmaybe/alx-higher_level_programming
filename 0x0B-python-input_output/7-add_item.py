#!/usr/bin/python3
"""
This script adds command-line arguments to a list and
saves it to a JSON file.
"""
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    n_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    n_list = []
for arg in argv[1:]:
    n_list.append(arg)

save_to_json_file(n_list, "add_item.json")
