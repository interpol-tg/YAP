f = int(input())
k = int(input())

if f < k:
    print(f + k * k - 1)
elif k < 2 and f == 3:
    print(k * k)
else:
    print(f - 1)