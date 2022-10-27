a = []
n = int(input())

for i in range(n):
    temp = input().split()
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    a.append(temp)

for i in range(n):
    for j in range(n):
        if a[i][j] > 0:
            a[i][j] = 1
        elif a[i][j] < 0:
            a[i][j] = 0

print(*[a[i][x] if x <= i else '' for x in range(len(a[i]))], '')
