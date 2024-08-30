from bs4 import BeautifulSoup
import requests

url = r'https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p3711649.m570.l1313&_nkw=laptop&_sacat=0'

response = requests.get(url)

if response.status_code != 200:
    raise ValueError("Failed to reach webpage")

soup = BeautifulSoup()
