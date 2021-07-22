import requests
from bs4 import BeautifulSoup
import csv

# key = 'laptop'
url = 'https://shopee.co.id/api/v4/pages/is_short_url/?path=search'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54'
}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
items = soup.findAll('div', 'fBhek2 _2xt0JJ')
print(items)
# for it in items:
#     name = it.find('h2', 'a-size-mini a-spacing-none a-color-base s-line-clamp-2').text
#     print(name)