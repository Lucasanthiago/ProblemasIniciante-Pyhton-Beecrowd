pares = 0
impares = 0
positivos = 0
negativos = 0


for i in range(5):
    num = int(input())

    if num > 0:
        positivos += 1
    if num < 0:
        negativos += 1
    if (num%2) == 0:
        pares += 1
    if (num%2) == 1:
        impares += 1

print(pares,"valor(es) par(es)")
print(impares,"valor(es) impar(es)")
print(positivos,"valor(es) positivo(s)")
print(negativos,"valor(es) negativo(s)")
