
num = int(input())
init = 1

while num > 0:
    num -= 1

    init2 = init ** 2
    init3 = init ** 3

    print("%d %d %d" %(init, init2, init3))
    init += 1
