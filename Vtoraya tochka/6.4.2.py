a = []
b = []
n = int(input('Введите количество элементов массива'))
for i in range(0, n):
    a.append(int(input()))
    if a[i] % 2 == 1:
        b.append(a[i])
b.sort()
dl = len(b)
for i in range(dl - 1, -1, -1):
    print(b[i])