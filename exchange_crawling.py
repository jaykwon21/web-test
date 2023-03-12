import requests
from bs4 import BeautifulSoup  

def get_exchange_rate(target1):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response =  requests.get("https://dmaari.com/products/{}".format(target1), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'class': 'price-item price-item--regular'})
    # print(containers)
    print(containers.text)

for i in range(4):
    id = i + 106
    get_exchange_rate(str(id))