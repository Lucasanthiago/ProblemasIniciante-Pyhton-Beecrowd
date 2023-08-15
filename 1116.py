

num = int(input())

while num > 0:

    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)

    if x2 == 0:
        div = "divisao impossivel"
    else:
        div = x1 / x2

    num = num - 1

    print(div)
