
vet = []

num = int(input())

for i in range(10):
    vet.append(num)
    num = num*2

for j in range(10):
    print("N[%d] = %d" %(j, vet[j]))
