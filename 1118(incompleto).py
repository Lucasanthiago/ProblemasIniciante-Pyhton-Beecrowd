
x = 1

while x == 1:

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
    print("media = %.2f"  %(med))


    while x > 2 or x < 1 or x == 1:
        print("novo calculo (1-sim 2-nao)")
        newCalculo = int(input())
        if newCalculo == 2:
            x = 2
            break
        if newCalculo == 1:
            break
        if newCalculo > 2 or newCalculo < 1:
            continue
