# lesson 3, classwork
print('Введите интервал')
inter1 = int(input())
inter2 = int(input())
if inter1 > inter2:
    print('Введите 3 числа')
    a = int(input())
    b = int(input())
    c = int(input())

    if a >= inter2 and a <= inter1:
        print(a)
    if b >= inter2 and b <= inter1:
        print(b)
    if c >= inter2 and c <= inter1:
        print(c)
else:
    print('Введите 3 числа')
    a = int(input())
    b = int(input())
    c = int(input())
    if a >= inter1 and a <= inter2:
        print(a)
    if b >= inter1 and b <= inter2:
        print(b)
    if c >= inter1 and c <= inter2:
        print(c)
