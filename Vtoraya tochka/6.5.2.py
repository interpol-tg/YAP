a = []
b = []

for i in range(0, 10):
    a.append(int(input()))

a.sort()
b.append(a[0])
for i in range(1, 10):
    if a[i] == a[i - 1]:
        continue
    else:
        b.append(a[i])
print(b)
