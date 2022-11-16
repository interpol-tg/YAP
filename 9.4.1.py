f = open('C:\\Users\\dimx3\\PycharmProjects\\VKparser\\Kholin_Dmitriy_vvod')
a = [line.replace("\n", "").split() for line in f]
n = int(input())
m = int(input())

for i in range(n):
    temp = input().split()
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    a.append(temp)
bestsum = - 1
sum = 0
for i in range(n):
    for j in range(m):
        sum = sum + a[i][j]
    if bestsum < sum:
        maxnumber = i
        bestsum = sum
    sum = 0

print('Наибольшая сумма элементов ', bestsum)
for i in range(m):
    print(a[maxnumber - 3][i], end=' ')
print()

minsum = 9999999
sum = 0

for i in range(n):
    for j in range(m):
        sum = sum + a[i][j]
    if minsum > sum:
        minnumber = i
        minsum = sum
file = open('C:\\Users\\dimx3\\PycharmProjects\\VKparser\\Kholin_Dmitriy_vivod', 'w')
file.write(minsum)
file.write('\n')
print('Наименьшая сумма элементов', minsum)
for i in range(m):
    file.write(' '.join(map(str, a[minnumber][i])))
