n = int(input())

a = []
sum = 0

for i in range(0, n):
    a.append(int(input()))
    sum += a[i]
sr = sum / len(a)

for i in range(0, n):
    if a[i] == 0:
        a[i] = sr

print(a)
