import math
x = float(input("Введите значение x"))
y = float(input("Введите значение y"))
z = float(input("Введите значение z"))
if y > 1.2:
    def primer(x,y,z):
        chislitel = 3.14*(10*x+4)-(24.8*z*y)/(x**2+z)
        znamenatel = 10*math.sqrt(4+y-5.2)
        return chislitel/znamenatel
print(primer(x,y,z))