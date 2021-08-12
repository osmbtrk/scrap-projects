import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('SouqDataapple.csv', 'w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://jackhenry.co/collections/face'
file = open('SouqDataapple.json','w',encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['name']
for page in range(1):
    print('---', page, '---')
    r = requests.get(url)
    print(url)
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('div',{'class' : 'Grid__Cell 1/2--phone 1/3--tablet-and-up 1/4--desk'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in  ancher:
        name=pt.find('span', {'class' : 'stamped-badge-caption'})

        writer.writerow({'name': name.text.replace('                    ', '').strip('\r\n')})
        data['name'] =name.text.replace('                    ', '').strip('\r\n')

        json_data = json.dumps(data,ensure_ascii=False)
        file.write(json_data)
        file.write(",\n")             
file.write("\n]")
filecsv.close()
file.close()