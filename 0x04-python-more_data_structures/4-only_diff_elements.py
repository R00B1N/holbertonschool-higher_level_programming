#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    for i in (set_1):
        if (list(set_1).count(i) == 1 and list(set_2).count(i) == 0):
            new_list.append(i)
    for b in (set_2):
        if (list(set_2).count(b) == 1 and list(set_1).count(b) == 0):
            new_list.append(b)
    return new_list
