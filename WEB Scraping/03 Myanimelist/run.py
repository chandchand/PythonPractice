import requests
from bs4 import BeautifulSoup
# import urllib2
import csv

key = '2020'
url = 'https://myanimelist.net/search/all?cat=all&q={}'.format(key)
# page = urllib2.urlopen(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54'
}
datas = []
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")
items = soup.findAll('div', 'list di-t w100')

for item in items:
    try: title = item.find('a', 'hoverinfo_trigger fw-b fl-l').text
    except : title = item.find('a', 'hoverinfo_trigger fw-b').text
    try: info = item.find('div', 'pt8 fs10 lh14 fn-grey4').text
    except: info = item.find('div', 'pt4 fs10 lh14 fn-grey4')
    datas.append([title, info])

head = ['Title', 'Info']
writer = csv.writer(open('result/myanimelist_{}.csv'.format(key), 'w', newline= ''))
writer.writerows(head)
for d in datas:writer.writerows(d)