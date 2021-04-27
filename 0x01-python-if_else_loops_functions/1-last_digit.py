#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

digit = number
great = "and is greater than 5"
zero = "and is 0"
less = "and is less than 6 and not 0"


def lastDigit(var):
    if number < 0:
        digit = (((number * -1) % 10) * -1)
    else:
        digit = number % 10
    print("Last digit of", str(number), "is", str(digit), var)


if digit > 5:
    lastDigit(great)
elif digit is 0:
    lastDigit(zero)
else:
    lastDigit(less)
