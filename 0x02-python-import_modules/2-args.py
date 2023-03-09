#!/usr/bin/python3
import sys
counter = 1
if __name__ == "__main__":
    for i in sys.argv:
        print("{position}: {argument}".format(position=counter, argument=i))
        counter = +1
    if i == 1:
        print("{position}.".format(position=counter))
