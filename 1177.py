


var = int(input())

x = 0
num = 0

while x < 1000:

    while num < var:
        print("N[%d] = %d" %(x, num))
        num += 1
        x += 1
        if x == 1000:
            break

    num = 0
