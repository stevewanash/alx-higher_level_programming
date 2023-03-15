#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_list = list(a_dictionary)
    sorted_keys = sorted(keys_list)
    for i in sorted_keys:
        print("{}: {}".format(i, a_dictionary[i]))
