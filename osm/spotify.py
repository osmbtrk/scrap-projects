import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('spotify.csv', 'w',encoding='utf8')
file = open('spotify.json','w',encoding='utf8')
# Set the URL you want to webscrape from
allsite = ["https://www.adlibris.com/se/sok?pn=5&ps=12&filter=categoryfacet%3ab%c3%b6cker&filter=format_sv%3ae-bok"]
file.write('[\n')
data = {}
csv_columns = ['name','price']
for l in allsite:
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('div',{'class':'search-result__list-view__product__wrapper'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in  ancher:
        name=pt.find('h4',{'class':'heading--searchlist-title'})
        price=pt.find('div',{'class':'price sek'})
        print(name)
        data['name'] =name.text
        writer.writerow({'name': name.text})
        data['price'] =price.text
        writer.writerow({'price': price.text})
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
file.write("\n]")
filecsv.close()
file.close()