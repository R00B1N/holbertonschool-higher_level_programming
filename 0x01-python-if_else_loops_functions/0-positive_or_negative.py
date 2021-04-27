#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print('{:d}'.format(number), "is positive")
elif number is 0:
    print('{:d}'.format(number), "is zero")
else:
    print('{:d}'.format(number), "is negative")
