import sys
counter = 1
if __name__ == "__main__":
    no_of_arg = len(sys.argv)
    if no_of_arg - 1 == 1:
        print("{args} argument:".format(args=no_of_arg - 1))
    elif no_of_arg - 1 == 0:
        print("{args} arguments.".format(args=no_of_arg - 1))
    else:
        print("{args} arguments:".format(args=no_of_arg - 1))
    if no_of_arg - 1 > 1:
        for i in range(1, no_of_arg):
            if counter == no_of_arg - 1:
                print("{po}: {ar}".format(po=counter, ar=sys.argv[i]), end='')
                counter = counter + 1
            else:
                print("{pos}: {arg}".format(pos=counter, arg=sys.argv[i]))
                counter = counter + 1
    elif no_of_arg - 1 == 1:
        print("{pos}: {arg}".format(pos=counter, arg=sys.argv[1]), end='')
