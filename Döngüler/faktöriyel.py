print("""***********************

faktöriyel hesaplama formulu
çıkmak için q basınız
*******************************
""")
while True:
    sayı = input("sayı: ")
    if (sayı == "q"):
        print("program sonlandırılıyor")
        break
    else:
        sayı = int(sayı)
        faktöriyel = 1
        for i in range(2,sayı+1):
            faktöriyel *= i
        print("faktöriyel :" , faktöriyel)

