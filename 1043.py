values = input().split()
value1, value2, value3 = values

value1 = float(value1)
value2 = float(value2)
value3 = float(value3)

if (value1+value2) > value3 and (value1+value3) > value2 and (value2+value3) > value1:
    perimeter = value1 + value2 + value3
    print("Perimetro = %0.1f" %perimeter)
else:
    area = (value1 + value2) * value3 / 2
    print("Area = %0.1f" %area)

