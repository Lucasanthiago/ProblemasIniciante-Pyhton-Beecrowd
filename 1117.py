
nota_1 = -1
nota_2 = -1

while (nota_1 and nota_2 < 0):
    nota_temp = (float(input()))


    if nota_temp >= 0 and nota_temp <= 10:
        if nota_1 < 0:
            nota_1 = nota_temp
            continue
        if nota_1 > 0:
            nota_2 = nota_temp
            continue
        continue
    else:
        print("nota invalida")
        continue

med = (nota_1 + nota_2) / 2
print("media =", med)
