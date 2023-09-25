
x,y = input().split()

x = int(x)
backup_x = x
y = int(y)
num = 0
inter = (y/x)

while inter > 0:
    lista = []
    while x > 0:
        num += 1
        lista.append(num)
        x -= 1
    lst_new = [str(a) for a in lista]
    print(" ".join(lst_new))
    x = backup_x
    inter -= 1
