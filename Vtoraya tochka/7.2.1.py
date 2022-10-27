import math

a = int(input())


def pl(a):
    s = (a * a * (3 ** (1 / 2))) / 4
    return s


print(pl(a) * 6)