import math

ax = float(input("Enter coordinate x of dot A: "))
ay = float(input("Enter coordinate y of dot A: "))

bx = float(input("Enter coordinate x of dot B: "))
by = float(input("Enter coordinate y of dot B: "))

cx = float(input("Enter coordinate x of dot C: "))
cy = float(input("Enter coordinate y of dot C: "))

# длина сторон

ab = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
ac = math.sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
bc = math.sqrt((bx - cx) ** 2 + (by - cy) ** 2)

print(f'Length of AB is : {ab}')
print(f'Length of BC is : {bc}')
print(f'Length of AC is : {ac}')


# является ли треугольник равносторонним
if math.sqrt(bc) - math.sqrt((ab + ac)) == 0:
    print("Triangle is Equilateral")
else:
    print("Triangle is not Equilateral")

# является ли треугольник равнобедренным
if ab == bc or ab == ac or bc == ab or bc == ac:
    print("Triangle is Isosceles")
else:
    print("Triangle is not Isosceles")

# является ли треугольник прямоугольным
a = (ax - ay)**2
b = (bx - by)**2
c = (cx - cy)**2

if math.sqrt(c) == math.sqrt(a) + math.sqrt(b):
    print("Triangle is Right")
else:
    print("NOT Right Triangle")

# периметр треугольника
perimeter = ab + ac + bc
print(f'Perimeter is: {perimeter}')

# все чётные числа от 0 до величины периметра треугольника включительно
print("Parity number in range from 0 to triangle perimeter: ")
for i in range(math.floor(perimeter)):
    if i % 2 == 0:
        print(i)
