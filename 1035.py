values = input().split()
a, b, c, d = values
a = int(a)
b = int(b)
c = int(c)
d = int(d)

cd = c + d
ab = a + b

if b > c:
    if d > a:
        if cd > ab:
            if c and d > 0:
                if a % 2 == 0:
                    print("Valores aceitos")
                else:
                    print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")