valor = int(input())
medias = []

for x in range(valor):
    val1, val2, val3 = input().split()
    val1 = float(val1)
    val2 = float(val2)
    val3 = float(val3)

    medias.append((val1*2 + val2*3 + val3*5) / 10)

for x in range(len(medias)):
    print("%.1f" % (medias[x]))
