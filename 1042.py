values = input().split()
val1, val2, val3 = values

val1 = int(val1)
val2 = int(val2)
val3 = int(val3)

maior = 0
medio = 0
menor = 0

#maior
if val1 > val2:
    maior = val1
else:
    maior = val2

if maior < val3:
    maior = val3

#menor
if val1 < val2:
    menor = val1
else:
    menor = val2

if menor > val3:
    menor = val3

#medio
if maior != val1:
    if menor != val1:
        medio = val1

if maior != val2:
    if menor != val2:
        medio = val2

if maior != val3:
    if menor != val3:
        medio = val3


print(menor)
print(medio)
print("%i\n"%maior)
print(val1)
print(val2)
print(val3)
