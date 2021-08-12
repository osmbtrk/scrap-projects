import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
filecsv = open('com.csv', 'w',encoding='utf8')
file = open('com.json','w',encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.rehadat-adressen.de/adressen/arbeit-beschaeftigung/jobcenter-und-sgb-ii-traeger/index.html?mode=detail&filter=%28art_adr%3A%28%28%22Jobcenter%22+Jobcenter*%29%29%29+AND+doc_type%3AADR&reloaded&sort=sort_name1_adr+asc&page='
url2 ='&query=%28Jobcenter+Jobcenter*%29&listtitle=Jobcenter%20bei%20REHADAT'
file.write('[\n')
data = {}
csv_columns = ['name','price','img']
for page in range(3):
    print('---', page, '---')
    r = requests.get(url + str(page)+ url2)
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('p',{'class' : 'kontaktdaten'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in  ancher:
        name=pt.find('span',{'class':'telefon'})
        print(name)
        data['name'] = name.text
        writer.writerow({'name': name.text})
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
file.write("\n]")
filecsv.close()
file.close()