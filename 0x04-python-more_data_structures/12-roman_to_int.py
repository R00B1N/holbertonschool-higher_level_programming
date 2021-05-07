#!/usr/bin/python3
def roman_to_int(roman_string):
    if(type(roman_string) != str or roman_string is None):
        return (0)
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    v = ""
    u = 0
    res = 0
    for i in range(len(roman_string)):
        v = roman_string[i]
        if (len(roman_string) != i + 1 and my_dict[roman_string[i + 1]] >
           my_dict[v]):
            u = my_dict[v]
        res += my_dict[v]
        res -= u
    return (res)
