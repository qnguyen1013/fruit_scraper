from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
trs = tbody.contents

prices = {}

#get the top 10
for table_row in trs[:10]:
    name, price = table_row.contents[2:4]
    full_name = name.p.string
    fixed_price = price.a.string
    prices[full_name] = fixed_price

print(prices)
        
        




