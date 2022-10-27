a = []
n = int(input())

for i in range(n):
    temp = input().split()
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    a.append(temp)
flag = 1
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i][j] != a[j][i]:
            flag = 0

if flag == 1:
    print('Thats OK')
else:
    print('Not OK')
