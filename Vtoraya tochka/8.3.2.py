a = []
n = int(input())
m = int(input())

for i in range(n):
    temp = input().split()
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    a.append(temp)


for i in range(n):
    for j in range(m):
        if a[i][j] > a[0][0]:
            temp = a[0][0]
            a[0][0] = a[i][j]
            a[i][j] = temp

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()