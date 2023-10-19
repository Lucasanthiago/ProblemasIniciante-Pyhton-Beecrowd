vet = []


for x in range(10):
    num = int(input())
    vet.append(num)

for i in range(10):
    if vet[i] < 1:
        vet[i] = 1

for j in range(10):
    print("X[%d] = %d" %(j, vet[j]))
