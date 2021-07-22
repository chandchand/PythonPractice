from os import replace
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.com/p/pl?d=graphic+card'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, 'html.parser')

# grabs each product
containers = page_soup.find_all('div', 'item-cell')

filename = "06 NewEgg.com/result/product.csv"
f = open(filename, 'w')

headers = 'brand, product_name, shipping\n'
f.write(headers)

for container in containers:
    try:
        brand = container.div.div.img['title']
    except:
        brand = ''

    title_container = container.findAll('a', 'item-title')
    try:
        product_name = title_container[0].text
    except:
        product_name = ''

    ship_price = container.findAll('li', 'price-ship')
    try:
        shipping = ship_price[0].text.strip()
    except:
        shipping = ''

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + ',' + product_name.replace(',', '|') + ',' + shipping + '\n')
f.close()
