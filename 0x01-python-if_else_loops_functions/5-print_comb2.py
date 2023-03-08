#!/usr/bin/python3
for i in range(99):
    if i == 99:
        print("{number:02d}\n".format(number=i))
        continue
    print("{number:02d}, ".format(number=i), end='')
