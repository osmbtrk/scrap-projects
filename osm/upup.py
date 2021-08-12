import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('work1.csv', 'w',encoding='utf8')
file = open('work1.json','w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.nordstrom.ca/browse/women/clothing?breadcrumb=Home%2FWomen%2FClothing&origin=topnav&page='
file.write('[\n')
data = {}
csv_columns = ['name','price','img']
for page in range(3):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('article',{'class' : '_1AOd3 QIjwE'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in  ancher:
        print(pt)
        name=pt.find('a',{'class':'_5lXiG _1sMDh _2PDR1'})
        price=pt.find('span',{'class':'_3wu-9'})
        img=pt.find('img',{'class':'TDd9E'})
        data['name'] = name.text
        print(name.text)
        writer.writerow({'name': name.text})
        data['price'] = price.text.replace(',', '')
        writer.writerow({'price': price.text})
        data['img'] = img.get('src')
        writer.writerow({'img': img.text})
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
file.write("\n]")
filecsv.close()
file.close()