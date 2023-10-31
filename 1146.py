
x = 1

while x != 0:
    x = int(input())
    if x == 0:
        break
    lits = []

    for i in range(x):
        lits.append(i+1)

    print(' '.join(map(str, lits)))
