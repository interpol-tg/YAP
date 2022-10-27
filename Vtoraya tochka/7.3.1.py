import math


def gip(a, b):
    c = (a * a + b * b) ** (1 / 2)
    return c


a = int(input())
b = int(input())
c1 = gip(a, b)
a = int(input())
b = int(input())
c2 = gip(a, b)
if c1 > c2:
    print('Первая гипотенуза больше', c1)
elif c2 > c1:
    print('Вторая гипотенуза больше', c2)
else:
    print('Гипотенузы равны')
