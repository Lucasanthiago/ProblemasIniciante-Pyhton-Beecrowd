

while True:
    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)

    if x1 > x2:
        print("Decrescente")
    if x1 < x2:
        print("Crescente")
    if x1 == x2:
        break
