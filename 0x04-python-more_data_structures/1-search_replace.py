#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(replace if my_list[i] == search else my_list[i])
    return (new_list)
