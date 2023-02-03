class Animal: # burası parent class
    def __init__(self):
        print("animal is created")
    def tostring(self):
        print("animal")
    def walk(self):
        print("animal walk...")
#CHILD
class Monkey(Animal):
     def __init__(self):
         super().__init__()  # parent class daki init alıyorum ilk once extend gibi
         print("monkey is created")
     def tostring(self):
         print("monkey")
     def climb(self):
         print("monkey can climb") # biz burda parent classına extends edip genişletiyoruz
class Birds(Animal): # buraya Monkey yazarsak bird monkeyın child class olur ve climb methoduda çalıişr
    def __init__(self):
        super().__init__()
        print("bird is created")
    def fly(self):
        print("birds can fly")


b1=Birds()
b1.__init__()
b1.fly()
# b1.climb() Birds animalın chıld oldugundan monkeydeki method sadece monkey içinde çalışır


m1 = Monkey() #animal is created , monkey is created

m1.tostring() # monkey
m1.walk() # animal walk...
