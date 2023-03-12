#!/usr/bin/python3
import sys
sum = 0
if __name__ == "__main__":
    no_args = len(sys.argv)
    for i in range(1, no_args):
        sum += int(sys.argv[i])
print("{result}".format(result=sum))
