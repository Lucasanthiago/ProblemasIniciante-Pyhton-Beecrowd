valor = int(input())
aux = 1

for x in range(valor):
    divisor = valor % aux
    if divisor == 0:
        print(aux)
    aux += 1

