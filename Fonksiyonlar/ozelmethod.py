class Kitap():
    pass
kitap=Kitap() # __İNİT__ FONKSİYONU NORMALDE OTOMATİK OLARAK GELİYOR
print(kitap) # <__main__.Kitap object at 0x0000026A664770D0> str methodu çalıştı
len(kitap) # len methodu çalıştı ama hata verir
del (kitap)


class Kitap():
    def __init__(self,isim,yazar,sayfasayisi,tur): #kendi init fonksiyonumu oluşturdum yukardakini kullanmak istemiyorum
        print("init fonks calıştı")
        self.isim=isim
        self.yazar=yazar
        self.sayfasayisi=sayfasayisi
        self.tur=tur
kitap=Kitap("antephanekleri","ronaldo",600,"roman")




