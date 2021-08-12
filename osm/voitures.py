import requests
from bs4 import BeautifulSoup
url ='https://www.tayara.tn/c/v%C3%A9hicules'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
results = soup.find_all('div',{'class':'card__body'})
for result in results:
    names=result.find_all('h2')
    for name in names:
        nm=name.text
        print(nm)