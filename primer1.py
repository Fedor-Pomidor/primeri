import math
print("y должно быть юольше x")


x = float(input("Введите значение 'x'"))
y = float(input("Введите значение 'y'"))
z = float(input("Введите значение 'z'"))
def primer1 (x, y, z):
    chislitel1 = float(y+x)
    znamenatel1 = float(189*y)
    chislitel2 = float(-50.3)
    znamenatel2 = float(math.sqrt((z**2+x)/(y-x)))
    print(float((y+chislitel1/znamenatel1-4)*(chislitel2/znamenatel2)))
    return
if y > x:
    primer1(x, y, z)