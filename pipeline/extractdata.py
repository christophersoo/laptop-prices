from bs4 import BeautifulSoup
import requests

init_page = 1
max_page = 9

def extract_data(page):
    url = f'https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=laptop&_sacat=0&_ipg=240&_pgn={page}'

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Failed to reach webpage")

    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all('li', class_='s-item')

    for listing in listings:
        name = listing.find('div', class_='s-item__title')
        price = listing.find('span', class_='s-item__price')
        if name and price:
            print(f"Laptop: {name.text}, Price: {price.text}")

extract_data(1)
