import math


x = float(input("Введите значение 'x'"))
y = float(input("Введите значение 'y'"))
z = float(input("Введите значение 'z'")) #вводите не меньше 4.4
if z >= 4.4:
    def primer1 (x, y, z):
        chislitel = math.sqrt(25 * ((x * y * math.sqrt(z - 4.4)) ** 2 + 5))
        znamenatel = 8 + y
        return chislitel / znamenatel

print(primer1(x, y, z))