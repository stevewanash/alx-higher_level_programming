#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j < i or j == i:
            continue
        if i+1 == 9 and j+1 == 10:
            print("{first}{last}".format(first=i, last=j))
            continue
        print("{first}{last}, ".format(first=i, last=j), end='')
