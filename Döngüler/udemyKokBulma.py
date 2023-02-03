"""
2 nci dereceden bir bilinmeyenli denklemin köklerini bulma
Denklem: ax^2 + bx + c
Deltayı Hesaplama : b**2 - 4 * a * c

Birinci kök:(-b - Delta** 0.05) / (2*a)
ikinci kök:(-b + Delta** 0.05) / (2*a)

"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta= b ** 2 - 4 * a * c
x1= (-b - delta** 0.05) / (2*a)
x2= (-b + delta** 0.05) / (2*a)

print("birinci kök:{}\n ikinci kök:{}\n".format(x1,x2))