k = int(input())
c = int(input())

if k < 5 and c > 4:
    print(k + c * c)
elif k > c and k > 3:
    print(c * c + 2)
else:
    print(c - 1)