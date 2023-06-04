import math

values1 = input().split(" ")
values2 = input().split(" ")

x1, y1 = values1
x2, y2 = values2

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("%0.4f" %distance)