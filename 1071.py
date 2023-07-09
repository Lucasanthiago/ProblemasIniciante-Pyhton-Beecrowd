valor1 = int(input())
valor2 = int(input())

maior = valor1 if valor1 > valor2 else valor2
menor = valor2 if valor2 < valor1 else valor1
menor += 1
soma = 0

while menor < maior:
    if menor % 2 != 0:
        soma += menor
    menor += 1
print(soma)
