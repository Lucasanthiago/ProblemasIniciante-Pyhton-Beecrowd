
num = int(input())
fatorial = num
aux = 0

for i in range(num-1):
    aux = aux - 1
    fatorial = fatorial * abs(aux)

print(fatorial)
