#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            print("{letter}".format(letter=chr(ord(i)-32)), end='')
        else:
            print("{letter}".format(letter=i), end='')
            continue
