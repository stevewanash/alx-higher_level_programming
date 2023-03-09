#!/usr/bin/python3
import sys
counter = 1
if __name__ == "__main__":
    no_of_arg = len(sys.argv)
    if no_of_arg == 1:
        print("{args} argument:".format(args=no_of_arg))
    elif no_of_arg == 0:
        print("{args} arguments.".format(args=no_of_arg))
    else:
        print("{args} arguments:".format(args=no_of_arg))
    if no_of_arg > 0:
        for i in range(no_of_arg):
            print("{pos}: {arg}".format(pos=counter, arg=sys.argv[i]))
            counter = +1
