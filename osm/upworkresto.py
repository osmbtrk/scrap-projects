import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('resto.csv', 'w',encoding='utf8')
file = open('resto.json','w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.caionline.org/pages/credentials-directory.aspx#k='
file.write('[\n')
data = {}
csv_columns = ['name','price','img']
for page in range(4):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('div',{'class' : 'ms-srch-item'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in  ancher:
        name=pt.find('td',{'class':'credentialColumn'})
        data['name'] = name.text
        writer.writerow({'name': name.text})
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
        print(name.text)
file.write("\n]")
filecsv.close()
file.close()