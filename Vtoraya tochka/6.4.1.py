a = []
n = int(input())

for i in range(0, n):
    a.append(int(input()))

max = a[0]
for i in range(1, n):
    if a[i] > max:
        max = a[i]

print(a.index(max))
