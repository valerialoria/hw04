import requests
from bs4 import BeautifulSoup

keyword='essential+oils'
page_number = '5'
results = []

for i in range(1,11):
    #r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword)
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i))
    print('r.status_code',r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')

    '''
    items = soup.select('.s-item__link')
    for item in items:
        print('item=',item.text)

    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=',price.text)

    '''
    
    boxes = soup.select('.clearfix.s-item__wrapper')
    for box in boxes:
        #print('--------')
        result = {}
        names = box.select('.s-item__link')
        for name in names:
            #print('name=',name.text)
            result['name'] = name.text
        prices = box.select('.s-item__price')
        for price in prices:
           # print('price=',price.text)
            result['price'] = price.text
        statuses = box.select('.SECONDARY_INFO')
        for status in statuses:
           # print('status=',status.text)
            result['status'] = status.text
       # print('result=',result)
        results.append(result)
    print('len(results)=',len(results))

import json
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
