#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for i in set_2:
        for b in set_1:
            if (i == b):
                new_list.append(i)
    return new_list
