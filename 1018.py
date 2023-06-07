value = int(input())
valor = value

nota100 = value/100
value = value % 100

nota50 = value/50
value = value % 50

nota20 = value/20
value = value % 20

nota10 = value/10
value = value % 10

nota5 = value/5
value = value % 5

nota2 = value/2
value = value % 2

print(valor)
print("%i nota(s) de R$ 100,00" %nota100)
print("%i nota(s) de R$ 50,00" %nota50)
print("%i nota(s) de R$ 20,00" %nota20)
print("%i nota(s) de R$ 10,00" %nota10)
print("%i nota(s) de R$ 5,00" %nota5)
print("%i nota(s) de R$ 2,00" %nota2)
print("%i nota(s) de R$ 1,00" %value)
