class Bankaccount(object):

    def __init__(self,name,money,adress):
        self.name=name
        self.__money=money #variable iki alt çizgi ile private yaptım
        self.adress=adress

# get and set
    def getmoney(self):
        return self.__money
        print("get method :", )
    def setmoney(self,amount):
        self.__money= amount
    def __zaaam(self): # methoduda private yaptık
        self.__money += 500

p1 = Bankaccount("messi", 1000, "barcelona")
p2 = Bankaccount("neymar", 2000, "paris")


print("get method :",p1.getmoney()) # private olanı çagırdım get methodu ile
#p1.__zaaam() böyle hata verir methodu private yaptıgım için
#print("zamdan sonraki para :",p1.getmoney())





