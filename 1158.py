
N = int(input())

for x in range(N):
    aux = 0
    lista = []
    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)

    if x1 % 2 == 0:
        x1 += 1

    while aux < x2:
        lista.append(x1)
        aux += 1
        x1 += 2
    print(sum(lista))
