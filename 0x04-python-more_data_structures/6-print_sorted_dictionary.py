#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if (a_dictionary is None):
        return None
    new_dic = sorted(a_dictionary.keys())
    for i in new_dic:
        print("{}: {}".format(i, a_dictionary[i]))
