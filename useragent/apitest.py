import requests
from bs4 import BeautifulSoup

#url="https://www.naukri.com/jobs-in-andhra-pradesh"
url1="https://www.glassdoor.com/Explore/top-companies-birmingham_IL.14,24_IM93.htm"
# glassdoor sitesi için user-agent kullandık bunu sitenin headerından aldık yoksa 403 hatası veriyor

header={
    "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

get=requests.get(url1)
print(get.status_code)# 200 naukri sitesine giriş izni olmadan veri alabildik
content=get.content # içerigini göstermek içim mesela burda html
soup=BeautifulSoup(content,"html.parser") # ben bu html kodunu parçalamak için yaptım
titles=soup.find_all("span",{"class":"align-items-center mb-xsm"}) # locater

for i in titles:
    i=i.text # sadece yazıları getir başlıkları
    print(i)
