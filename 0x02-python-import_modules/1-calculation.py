#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
    print("{n1} + {n2} = {n3}".format(n1=a, n2=b, n3=add(a, b)))
    print("{n1} - {n2} = {n3}".format(n1=a, n2=b, n3=sub(a, b)))
    print("{n1} * {n2} = {n3}".format(n1=a, n2=b, n3=mul(a, b)))
    print("{n1} / {n2} = {n3}".format(n1=a, n2=b, n3=div(a, b)))
