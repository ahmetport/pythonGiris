
import requests
url="https://api.fixer.io/latest"


birinci_doviz=input("birinci döviz : ")
ikinci_doviz=input("ikinci döviz : ")

response=requests.get(url+birinci_doviz)
json_verisi=response.json()
print(json_verisi) # FİXER UCERTLİ oldugundan kayıt olup acces key almak lazım
