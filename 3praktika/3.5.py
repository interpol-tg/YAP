v = int(input())
k = int(input())

if v < k:
    print(v - k + 1)
elif k > v:
    print(k * k - v * v)
else:
    print(k * k - k)
