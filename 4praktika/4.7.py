n = int(input())
f = 1
sum = 0

for i in range(1, n + 1):
    f = f * i
    sum = sum + f

print(sum)