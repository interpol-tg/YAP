a = int(input())
b = int(input())

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    while a >= b:
        print(a)
        a = a - 1