class Calisan():
    def __init__(self,isim,maas,departman):
        print("calisan sinifin init fonksiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgilerigoster(self):
        print("calisan sinifin bilgileri")
        print("isim :{}\nmaas :{}\ndepartman :{}\n" .format(self.isim,self.maas,self.departman))
    def departman_ekle(self,yeni_departman):
        self.departman=yeni_departman
 # yukarda oluşturdugum benim ana classım ve iki tane method şimdi bunları inheritance kullanarak cagıracagım

class Yonetici(Calisan): #calısan classının butun özelliklerini kullanabilirim
    pass #blogu sonra kullanacagımı pass fonksiyonu ile belirtiyorum

yonetici=Yonetici("ahmet portakal",5000,"tester")
yonetici.bilgilerigoster()
yonetici.departman_ekle("devops")
yonetici.bilgilerigoster()

class Yonetici(Calisan):# yeni bir method ekledik maasa zam yaptık
    def zam_yap(self,zam_miktari):
        self.maas += zam_miktari
yonetici=Yonetici("GULSAH PORTAKAL",3500,"BİLİŞİMCİ")
yonetici.zam_yap(500)
yonetici.bilgilerigoster()
yonetici.zam_yap(2000)
yonetici.bilgilerigoster()


