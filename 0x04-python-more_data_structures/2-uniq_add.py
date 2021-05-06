#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    val = 0
    for i in range(len(my_list)):
        if (new_list.count(my_list[i]) == 0):
            new_list.append(my_list[i])
    for i in new_list:
        val += i
    return (val)
