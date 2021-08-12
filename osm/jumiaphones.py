import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('jumiaphones.csv', 'w',encoding='utf8')
file = open('jumiaphones.json','w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.jumia.com.tn/smartphones/?page='
file.write('[\n')
data = {}
csv_columns = ['name','price','img']
for page in range(3):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('article',{'class' : 'prd _fb col c-prd'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in  ancher:
        name=pt.find('h3',{'class':'name'})
        price=pt.find('div',{'class':'prc'})
        img=pt.find('img',{'class':'img'})
        data['name'] = name.text
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