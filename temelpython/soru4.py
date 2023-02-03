"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi
dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi ,
 dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı ,
eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
 Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

"""
sekil= input("hangi şekil istiyorsun : ")
if (sekil == "dörtgen"):
    print("kenarları sırasıyla gırınız")
    a=int(input("kenar-1:"))
    b=int(input("kenar-2:"))
    c=int(input("kenar-3:"))
    d=int(input("kenar-4:"))
    if (a == b and a == c and a == d):
        print("kare")
    elif (a == c and b == d):
        print("dikdörgen")
    else:
        print("dörtgen")

elif (sekil == "ücgen"):
    print("kenarları sırasıyla giriniz")
    a = int(input("kenar-1:"))
    b = int(input("kenar-2:"))
    c = int(input("kenar-3:"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

else:
    print("Geçersiz Şekil...")







