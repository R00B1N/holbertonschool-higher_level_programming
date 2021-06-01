#!/usr/bin/python3
"""
This module contains one function
"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file and prints its content """
    with open(filename) as f:
        c = 0
        l = -1
        while (nb_lines <= 0 and l != 0) or c < nb_lines:
            c += 1
            line = f.readline()
            l = len(line)
            print(line, end="")
