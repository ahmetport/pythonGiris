# kullanıcıdan aldıgınız 3 sayıyı çarparak ekrana yazdırınız format yontemini kullanınız

x = int(input("a:"))
y= int(input("b:"))
z = int(input("c:"))
carpim = x * y * z
print("{} * {} * {} = {} dir." .format(x , y, z, carpim))

# kullanıcıdan aldıgınız boy ve kilo degerlerine gore vki bulunuz

boy=float(input("x:"))
kilo=int(input("y:"))
print("vucut kitle endexi:", kilo/(boy**2))

# bir aracın km basina ne kadar yaktıgını alın, kaç km yol yaptıgını alın,surucunun toplam ne kadar odeme yapöması gerek

km_yakan_miktar=float(input("x:"))
yapilan_km=int(input("y:"))
print("tutar: {} tl".format(km_yakan_miktar * yapilan_km))

# kullanıcıdan ad soyad numara bilgisi alın ve alt alta yazdırın

ad = input("adiniz:")
soyad = input("soyadiniz")
numara= input("telefonunuz")

print("\nBilgiler...\n")
print("{}\n{}\n{}".format(ad,soyad,numara))

# kullanıcıdan iki sayı isteyin ve degerlerini bir birleriyle degiştirin

a = input("a:")
b = input("b:")
5
print("Değiştirilmeden Önce Değerler\na: {} b: {}\n".format(a,b))

a,b = b,a

print("Değiştirildikten Sonraki Değerler\na: {} b: {}\n".format(a,b))

# Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
# Hipotenüs Formülü: a^2 + b^2 = c^2
a=int(input("x:"))
b=int(input("y:"))
c=(a ** 2 + b ** 2) ** 0.5
print("hipotenus:" , c)







