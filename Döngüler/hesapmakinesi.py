print("""**********************************
Hesap Makinesi Programı

işlemler:

1.toplama işlemi
2.çıkarma işlemi
3.çarpma işlemi
4.bölme işlemi
*************************************************
""")

a = int(input("birinci sayi: "))
b = int(input("ikinci sayi: "))
islem = input("işlemi giriniz: ")

if islem == "1":
    print("{} ile {} in toplamı {} dir".format(a,b, a+b))
elif islem == "2":
    print("{} ile {} in farkı {} dir".format(a,b, a-b))
elif islem == "3":
    print("{} ile {} nın çarpımı {} dir".format(a,b, a*b))
elif islem == "4":
    print("{} ile {} in bölümü {} dir".format(a,b, a/b))
else:
    print("gecersiz işlem......")