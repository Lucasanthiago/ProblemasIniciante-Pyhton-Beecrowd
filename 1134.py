Alcool = 0
Gasolina = 0
Diesel = 0
x = 0

while x != 4:
    x = int(input())

    if x == 1:
        Alcool = Alcool + 1
    if x == 2:
        Gasolina = Gasolina + 1
    if x == 3:
        Diesel = Diesel + 1

print("MUITO OBRIGADO\n"
      "Alcool: %d\n"
      "Gasolina: %d\n"
      "Diesel: %d" % (Alcool,Gasolina,Diesel))

