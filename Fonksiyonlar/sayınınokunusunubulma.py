#Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

birler = ["","bir","iki","üc","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def okunus(sayi):
    birinci = sayi%10
    ikinci=sayi//10
    return onlar[ikinci] + "" + birler[birinci]

sayi=int(input("sayi:"))
print(okunus(sayi))
