#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or len(list(a_dictionary)) == 0):
        return None
    key = -999999999999999999999
    res = ""
    for i in a_dictionary:
        v = a_dictionary[i]
        v = (v, -v)[v < 0]
        if (v > key):
            key = v
            res = i
    return res
