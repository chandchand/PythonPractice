from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=laptop'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# parser
page_soup = soup(page_html, 'html.parser')

# grab each product
containers = page_soup.findAll(
    'div', 'organic-gallery-offer-outter J-offer-wrapper')

filename = '07 alibaba/result/product.csv'
f = open(filename, 'w')

headers = 'product_name, price, shipping, min_order, country, company\n'
f.write(headers)

for container in containers:
    # product_name = container.div.div.div.div.h4.a['title']
    product_container = container.findAll(
        'a', 'elements-title-normal')
    product_name = product_container[0].text
    price = container.find('p', 'elements-offer-price-normal medium').text
    # piece = container.find('span', 'elements-offer-price-normal__unit').text
    try:
        shipping = container.find('div', 'element-shipping-price').text
    except:
        shipping = '-'
    try:
        min_order = container.find(
            'p', 'element-offer-minorder-normal medium').text
    except:
        min_order = '-'
    country_container = container.find_all(
        'div', 'organic-gallery-offer__minisite-container')
    country_div = country_container[0]
    country = country_div.span['title']
    company = container.find('a', 'organic-gallery-offer__seller-company').text

    print('product_name: ' + product_name)
    print('price: ' + price)
    print('shipping: ' + shipping)
    print('min_order: ' + min_order)
    print('country: ' + country)
    print('company: ' + company)

    f.write(product_name + ',' + price + ',' + shipping + ',' +
            min_order + ',' + country + ',' + company + '\n')
f.close()
