f = open('C:\\Users\\dimx3\\PycharmProjects\\VKparser\\Kholin_Dmitriy_vvod')
a = [line.replace("\n", "").split() for line in f]
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
file = open('C:\\Users\\dimx3\\PycharmProjects\\VKparser\\Kholin_Dmitriy_vivod', 'w')
file.write(*[a[i][x] if x <= i else '' for x in range(len(a[i]))], '')
