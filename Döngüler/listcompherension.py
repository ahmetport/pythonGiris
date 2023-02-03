liste= [2,3,4,5]
liste1 = [i * 2 for i in liste]
print(liste1)


liste2= [(1,2),(3,4),(5,6)]
liste3= [i*j  for i,j in liste2]
print(liste3)
#listcomprehensionsuz hali
liste4=[[1,2,3],[4,5,6,7,8,9],[10,11,12,13,14,15]]
liste5=list()
for i in liste4:
    for x in i:
        liste5.append(x)
print(liste5)

#daha pratik
liste4=[[1,2,3],[4,5,6,7,8,9],[10,11,12,13,14,15]]
liste5=[x for i in liste4 for x in i]  #listcomprehension lu hali
print(liste5)
