a = []

for i in range(0, 10):
    a = int(input())

for i in range(0, 10):
    if a[i] < 0 and a[i + 1] < 0:
        print(a[i], a[i + 1])
