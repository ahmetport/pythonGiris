class ayew(object):
    age = 20
    salary = 500
    def agesalary(self):
        a=self.age/self.salary
        print(a)

ayew1=ayew()
ayew1.agesalary() # 0.04 bu class içinde method oluşturdum

#---------------------------------------------------------------------
# fonksiyon

def agesalary1(age,salary):
    a= age/salary
    print(a)

agesalary1(20,400) # burdada fonksiyon oluşturdum