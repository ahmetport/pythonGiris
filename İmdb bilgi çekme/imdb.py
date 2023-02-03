import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top"

response = requests.get(url)
html_icerigi=response.content
soup=BeautifulSoup(html_icerigi,"html.parser")
a=float(input("film rating giriniz :  "))

basliklar=soup.find_all("td",{"class":"titleColumn"})
ratingler=soup.find_all("td",{"class":"ratingColumn imdbRating"})

for basliklar,ratingler in zip(basliklar,ratingler):
    basliklar=basliklar.text
    ratingler=ratingler.text

    basliklar=basliklar.strip()
    basliklar=basliklar.replace("\n","")

    ratingler=ratingler.strip()
    ratingler=ratingler.replace("\n","")

    if (float(ratingler) >a):
        print("film ismi : {} film ratingi:{}".format(basliklar,ratingler))

    #print("basliklar",basliklar.text) #film başlıkları geldi sadece tyazılar
    #print("ratingler",ratingler.text) # film ratingleri geldi

#print(response) # eger 200 donerse bilgilere ulaşabiliyor demek <Response [200]>




