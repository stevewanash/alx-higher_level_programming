#!/usr/bin/python3
import sys
counter = 1
index = 0
if __name__ == "__main__":
    for i in sys.argv:
        print("{pos}: {arg}".format(pos=counter, arg=sys.argv[index]))
        counter = +1
        index = +1
    if i == 1:
        print("{pos}.".format(pos=counter))
