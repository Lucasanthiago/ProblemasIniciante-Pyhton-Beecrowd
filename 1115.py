
while True:
    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)

    if x1 > 0:
        if x2 > 0:
            print("primeiro")
            continue
        if x2 < 0:
            print("quarto")
            continue

    if x1 < 0:
        if x2 > 0:
            print("segundo")
            continue
        if x2 < 0:
            print("terceiro")
            continue


