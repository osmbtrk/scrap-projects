import requests
from bs4 import BeautifulSoup

url = 'https://tsacc.ca/members/?page_833f3='
for page in range(3):
    r = requests.get(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    resul = soup.find_all('div',{'class':'um-member-photo radius-1'})
    for n in resul: 
        urls = n.find_all('a')
        for x in urls:
            print(x.href)