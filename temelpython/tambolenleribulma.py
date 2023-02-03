# kullanıcıdan alınan sayıların tam bolenlerini bulan bi tane fonksiyon yazınız
def tambolenleribul(sayi):
    tambolenler=[]
    for i in range(2,sayi):
        if (sayi % i == 0):
            tambolenler.append(i)
    return tambolenler
while True:
    sayi=input("sayi:")
    if (sayi == 'q'):
        print("programdan cıkılıyor")
        break
    else:
        sayi=int(sayi)
        print("tam bolenler :",tambolenleribul(sayi))
