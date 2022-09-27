v = int(input())
k = int(input())

if v < 2 and k == 1:
    print(v - k + 1)
elif k > v:
    print(k * k + v * v)
else:
    print(k * k + v)
