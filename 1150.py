
x = int(input())
y = 0
temp = x
count = 1

while y <= x:
    y = int(input())

while x <= y:
    temp += 1
    x = x + temp
    count += 1

print(count)
