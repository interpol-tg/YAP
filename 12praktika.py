import math

print('Задача 12.1, блок А')
x = int(input())
n = int(input())


def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


x = pow(x, n)
print(x / factorial(n))

print('Задача 12.1, блок Б')


def function():
    a = int(input())
    while a != 0:
        if a == 0:
            return 0
        else:
            return max(n, function())


print(function())

print('Program end')