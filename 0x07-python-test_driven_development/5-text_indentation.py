#!/usr/bin/python3
"""
This module contains one function:
text_indentation(text)
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
        return
    for i in range(0, len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i], end="")
            print("\n")
        elif text[i] == " ":
            for x in range(i, 0, -1):
                if text[x] == " ":
                    continue
                elif text[x] in [".", "?", ":"]:
                    break
                else:
                    print(text[i], end="")
                    break
        else:
            print(text[i], end="")
