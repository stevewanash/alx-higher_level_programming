#!/usr/bin/python3
import sys
counter = 1
if __name__ == "__main__":
    no_of_arg = len(sys.argv)
    if no_of_arg == 2:
        print("{args} argument:".format(args=no_of_arg))
    elif no_of_arg == 1:
        print("{args} arguments.".format(args=no_of_arg))
    else:
        print("{args} arguments:".format(args=no_of_arg))
    if no_of_arg > 2:
        for i in range(1, no_of_arg):
            print("{pos}: {arg}".format(pos=counter, arg=sys.argv[i]))
            counter = +1
    elif no_of_arg == 2:
        print("{pos}: {arg}".format(pos=counter, arg=sys.argv[1]))
