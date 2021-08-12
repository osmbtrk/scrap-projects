import requests
from bs4 import BeautifulSoup

url = 'https://www.jumia.com.tn/accessoires-de-sport-et-de-plage/?page='
for page in range(2):
    r = requests.get(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    results = soup.find_all('article',{'class':'prd _fb col c-prd'})
    for result in results:
        name = result.find('h3',{'class':'name'})
        price = result.find('div',{'class':'prc'})
        nm = name.text
        prc = price.text
        print(nm)
        print(prc)
