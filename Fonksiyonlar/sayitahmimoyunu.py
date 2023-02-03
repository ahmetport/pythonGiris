import random
import time

print("""************************************************

sayı tahmın oyunumuza hosgeldiniz

""")
rastgele_sayi=random.randint(1,100)
tahmin_hakki=5
while True:

    tahmin=int(input("tahmininiz :"))

    if (tahmin < rastgele_sayi):
        print("bilgiler sorgulanıyor....")
        time.sleep(1)
        print("daha yuksek sayı soyleyin......")

        tahmin_hakki -= 1
    elif (tahmin > rastgele_sayi):
        print("bilgiler sorgulanıyor....")
        time.sleep(1)
        print("daha dusuk sayı soyleyin......")

        tahmin_hakki -= 1
    else:
        print("bilgiler sorgulanıyor......")
        time.sleep(1)
        print("tebrikler!!! sayımız:" , rastgele_sayi)
        break

    if (tahmin_hakki == 0):
        print("tahmin hakkınız bitti....")
        print("sayımız:" , rastgele_sayi)
        break








