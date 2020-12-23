import math


x = float(input("Введите значение 'x'"))
y = float(input("Введите значение 'y'"))
z = float(input("Введите значение 'z'")) #вводите не меньше 4.4

def primer1 (x, y, z):
    chislitel = 12.3 + (x - math.sqrt(z - 4.4)) * (5 / x)
    znamenatel = (8+y)**4
    return chislitel / znamenatel

print(primer1(x, y, z))