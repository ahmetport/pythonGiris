"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazd

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

x= float(input("boy:"))
y = int(input("kilo:"))
vki = y / (x**2)
print(vki)

if vki < 18.5:
    print("zayif")
elif vki > 18.5 and vki <= 25:
    print("normal")
elif vki < 25 and vki <= 30:
    print("fazla kilolu")
else:
    print("obez")
