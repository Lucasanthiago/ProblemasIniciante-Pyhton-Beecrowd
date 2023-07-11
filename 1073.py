valor = int(input())

for i in range(valor):
    x = i+1
    if x % 2 == 0:
        print("{}^2 = {}".format(x,x**2))
