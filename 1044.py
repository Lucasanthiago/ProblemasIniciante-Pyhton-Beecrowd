value1, value2 =map(int, input().split())

if value2 % value1 == 0 or value1 % value2 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
