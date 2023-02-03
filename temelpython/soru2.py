"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

if a >= b and a >= c:
    print("en buyuk sayı:" ,a)
elif b >= a and b >= c:
    print("en buyuk sayı:" ,b)
elif c >= a and c >= b:
    print("en buyuk sayı:" ,c)
