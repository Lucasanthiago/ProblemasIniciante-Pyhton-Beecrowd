values = input().split()
a, b, c = values

a = int(a)
b = int(b)
c = int(c)

def bigger(a,b):
    maior = (a+b+abs(a-b))/2
    return maior

bigger_1 = bigger(a,b)
bigger_2 = bigger(bigger_1,c)

print("%i eh o maior" %bigger_2)