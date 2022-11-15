f = open('C:\\Users\\dimx3\\PycharmProjects\\VKparser\\Kholin_Dmitriy_vvod')
a = [line.replace("\n", "").split() for line in f]
n = 3
m = 3
for i in range(n):
    for j in range(m):
        if a[i][j] > a[0][0]:
            temp = a[0][0]
            a[0][0] = a[i][j]
            a[i][j] = temp
file = open('C:\\Users\\dimx3\\PycharmProjects\\VKparser\\Kholin_Dmitriy_vivod','w')
for i in range(n):
    file.write(' '.join(map(str, a[i])))
    file.write('\n')
file.close()