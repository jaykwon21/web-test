import requests
from bs4 import BeautifulSoup

import time

import csv

# Every class __str__(self):
#               return "dongmae babo"
#str(): priority (1) : user-defined (overwritten) function
#                (2) : built-in function

class Product:
    def __init__(self, name, price, description): 
        self.name = name
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return str(self.name) + ", " + str(self.price) + ", " + str(self.description) + "\n"


subpages =[ '106',
           '107',
           'dongmae-necklace',
           '108']
        #    '108',
        #    '109',
        #    '110',
        #    '111',
        #    'alice-2mm',
        #    'alice-3mm',
        #    'alice-bundle',
        #    'aria-emerald',
        #    'aria-pink',
        #    'avery-earrings',
        #    'bold-chain-aria-bundle',
        #    'bold-chain-adjustable-ring',
        #    'dual-pearl-necklace',
        #    'gold-beaded-cuffs',
        #    'dongmae-necklace',
        #    'copy-of-silver-bean-earrings',
        #    'gold-bold-chain-necklace',
        #    'gold-crescent-large-hoops',
        #    'medium-gold-hoops-202']



headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'text/html; charset=utf-8'
        }


product_list = []
for i in subpages:
    response = requests.get("https://dmaari.com/products/{}".format(i), headers=headers)
    
    content = BeautifulSoup(response.content, 'html.parser')
    
    name_containers = content.find('div', {'class': 'product__title'})
    price_containers = content.find('span', {'class': 'price-item price-item--regular'})
    desc_containers = content.find('div', {'class': 'product__description rte quick-add-hidden'})

    try:
        temp_name = name_containers.text
        split_name = temp_name.split(" ")[0]
        split_name = split_name.replace('\n', '')
        print(split_name)
        # homework: post-processing: cut temp_name unnecessary parts

        temp_price = price_containers.text
        split_price = temp_price.replace("$", "")
        split_price2 = split_price.split(".", 1)[0]
        int_price = int(split_price2)
        print(int_price)
        # homework: post-processing : text (temp_price) >integer

        temp_desc = desc_containers.text
        replaced_desc = temp_desc.replace(",", " ")
        replaced_desc = replaced_desc.replace("\n", "")
        print(replaced_desc)
        # homeworkk: post-processing : covert any comma in description -> white_space

        time.sleep(1)

        temp_product = Product(split_name, int_price, replaced_desc)
        product_list.append(temp_product)
    except AttributeError:
        print(i + " crashes!!")
        continue

with open("products.csv", 'w') as csvfile:
    for item in product_list:
        csvfile.write(str(item))

    # data type of "item" : temp_product -> instance(Product) str X int X float X

csvfile.close()

