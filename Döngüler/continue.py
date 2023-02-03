liste = list(range(10))
print(liste)

for i in liste:
    if (i==3 or i== 5):
        continue #alttaki işlemleri yapmaz dongunun başına gıder yani 3 ve 5 aşagıda yazdırmaz
    print("i :",i)

i=0 #bu kodda sonsuz donguye girmemesi için iki defa +1 yaptık continue kullanırken buna dikkat
while (i < 10):
    if (i==2):
        i += 1 #sonsuz donguye girmemesi için sadece 2 yi almadı eger bunu eklemezsek 0,1 alır sonsuz donguye girer
        continue
    print("i :",i)
    i += 1
