from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
url = 'https://www.amazon.com/s?k=laptop&ref=nb_sb_noss_2'

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def getnextpage(soup):
    page = soup.find('ul', 'a-pagination')
    if not page.find('li', {'class': 'a-last'}):
        url = 'http://www.amazon.com' + str(page.find('li', 'a-last').find('a')['href'])
        return url
    else:
        return
while True:
    soup = getdata(url)
    url = getnextpage(soup)
    if not url:
        break
    print(url)