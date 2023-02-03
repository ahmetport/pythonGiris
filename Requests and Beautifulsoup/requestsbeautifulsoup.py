import requests
from bs4 import BeautifulSoup
url ="https://www.amazon.com.tr/b?ie=UTF8&node=20467303031"
response= requests.get(url)
print(response)  # <Response [200]> bilgileri çekebiliriz

html_icerigi = response.content
soup=BeautifulSoup(html_icerigi ,"html.parser") # sayfanın kaynak kodlarını getirir
#print(soup.prettify())

#for i in soup.find_all("a"):# a ile başlayan butun taglar geldı
 #   print(i)
print("*****************************************************")

for i in soup.find_all("a"):
    print(i.text) # sayfanın içindeki tum yazıları getirir




