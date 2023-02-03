
#1,1,2,3,5,8,13,21,34,55 ,,,,,,,fibonacci serisi
x=1
y=1
fibonacci = [x,y]

for i in range(20):
    x,y = y ,x+y
    fibonacci.append(y)
print(fibonacci)