entry_qnt = int(input())
inside = 0
outside = 0

for x in range(entry_qnt):
    val = int(input())
    if 10 <= val <= 20:
        inside += 1
    else:
        outside += 1

print(inside, "in")
print(outside, "out")
