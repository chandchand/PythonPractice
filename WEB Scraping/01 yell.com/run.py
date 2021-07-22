import requests
from bs4 import BeautifulSoup
import csv

key = input('Please Insert the term:')
location = input('Please Insert the location:')
url = 'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1091695012&keywords={}&location={}&pageNum='.format(key, location)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54'
}

datas = []
count_pages = 0
for page in range(1, 11):
    count_pages+=1
    print('Scraping Page :',count_pages)
    req = requests.get(url+str(page), headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    items = soup.findAll('div', 'row businessCapsule--mainRow')

    for it in items:
        name = it.find('h2', 'businessCapsule--name text-h2').text
        try : address = ''.join(it.find('span', {'itemprop':'address'}).text.strip().split('\n'))
        except : address = ''
        try : web = it.find('a', {'rel':'nofollow noopener'})['href'].replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0]
        except : web = ''
        try : telp = it.find('span', {'itemprop':'telephone'}).text
        except : telp = ''
        img = it.find('div','col-sm-4 col-md-4 col-lg-5 businessCapsule--leftSide').find('img')['data-original']
        if 'http' not in img: img = 'https://www.yell.com{}'.format(img)
        datas.append([name, address, web, telp, img])

    head = ['Name', 'Address', 'Website', 'Phone', 'Image Url']
    writer = csv.writer(open('result/{}_{}.csv'.format(key, location), 'w', newline= ''))
    writer.writerow(head)
    for d in datas: writer.writerow(d)