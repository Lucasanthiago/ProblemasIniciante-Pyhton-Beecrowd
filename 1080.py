num = 0
refe = 0

for x in range(100):
    val = int(input())
    if val > num:
        num = val
        refe = x + 1

print(num)
print(refe)
