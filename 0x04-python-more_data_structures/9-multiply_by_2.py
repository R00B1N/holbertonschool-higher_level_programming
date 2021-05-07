#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i, v in a_dictionary.items():
        new_dictionary[i] = v * 2
    return (new_dictionary)
