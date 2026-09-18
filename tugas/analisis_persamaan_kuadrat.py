import math

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

diskriminan = b**2 - 4*a*c

if diskriminan > 0:
    x1 = (-b + math.sqrt(diskriminan)) / (2*a)
    x2 = (-b - math.sqrt(diskriminan)) / (2*a)

    print("Persamaan memiliki dua akar real.")
    print("x1 =", x1)
    print("x2 =", x2)

elif diskriminan == 0:
    x = -b / (2*a)

    print("Persamaan memiliki satu akar real kembar.")
    print("x =", x)

else:
    print("Persamaan tidak memiliki akar real.")