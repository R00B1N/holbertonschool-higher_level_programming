#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        n = number % 10
        print("{:d}".format(n), end="")
        return n
    else:
        number = -number
        n = number % 10
        number = -number
        print("{:d}".format(n), end="")
        return n
