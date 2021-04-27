#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if number < 0:
    number = -number
last = number % 10
if num < 0:
    last = -last
if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, last))
elif last == 0:
    print("Last digit of {} is 0 and is 0".format(num, last))
else:
    print("Last digit of %d is %d and is less than 6 and not 0" % (num, last))
