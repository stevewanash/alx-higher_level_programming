#!/usr/bin/python3
import sys
counter = 1
if __name__ == "__main__":
    no_of_arg = len(sys.argv)
    if no_of_arg == 0:
        print("{pos}.".format(pos=counter))
    else:
        for i in range(no_of_arg - 1):
            print("{pos}: {arg}".format(pos=counter, arg=sys.argv[i]))
            counter = +1
