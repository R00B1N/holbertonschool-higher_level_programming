#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        number = 0
        for number in range(x):
            print(my_list[number], end="")
            number += 1
    except IndexError:
        None
    print()
    return number
