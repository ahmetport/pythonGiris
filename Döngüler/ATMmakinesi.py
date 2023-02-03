print("""**********************************************
 ******** Hoşgeldiniz*********
 1.bakiye
 2.para yatırma
 3.para çekme
 
 programdan cıkmak için q basınız
 *******************************************************
""")
bakiye = 5000
while True:
    islem = input("işlemi seciniz: ")
    if (islem == 'q'):
        print("yine bekleriz gule gule")
        break
    elif (islem == "1"):
        print("bakiyeniz {} tl dir" .format(bakiye))
    elif (islem == "2"):
        miktar=int(input("yatırılacak miktarı giriniz"))
        bakiye += miktar
    elif(islem == "3"):
        miktar = int(input("çekilecek miktarı giriniz"))
        if (bakiye - miktar < 0):
            print("bakiye yetersiz")
            continue
        bakiye -= miktar
    else:
        print("gecersiz işlem.......")




