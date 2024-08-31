from bs4 import BeautifulSoup
import pandas as pd
from transform_etl import transform
from load_etl import load
import requests

def extract_data(page):
    url = f'https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=laptop&_sacat=0&_ipg=240&_pgn={page}'

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Failed to reach webpage")

    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all('li', class_='s-item')

    mdict = {"name": [], "price": []}

    for listing in listings:
        name = listing.find('div', class_='s-item__title')
        price = listing.find('span', class_='s-item__price')
        if name and price:
            mdict["name"].append(name.text)
            mdict["price"].append(price.text)

    df_raw = pd.DataFrame(mdict)
    load(df_raw, "raw_laptop_data")
    
for i in range(1, 20):
    extract_data(i)
