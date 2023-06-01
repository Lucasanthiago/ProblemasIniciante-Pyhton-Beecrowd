values = input().split(" ")

a, b, c = values
pi = 3.14159

a = float(a)
b = float(b)
c = float(c)

area_triangle = (a*c)/2
area_circle = pi*(c*c)
area_trapeze = ((a+b)*c)/2
area_square = b*b
area_rectangle = a*b

print("TRIANGULO: %0.3f" %area_triangle)
print("CIRCULO: %0.3f" %area_circle)
print("TRAPEZIO: %0.3f" %area_trapeze)
print("QUADRADO: %0.3f" %area_square)
print("RETANGULO: %0.3f" %area_rectangle)


