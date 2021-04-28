#!/usr/bin/python3
if __name__ == "__main__":
    sum = 0
    from sys import argv
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print(sum)
