from bs4 import BeautifulSoup
import requests
import psycopg2

url = r''

conn = {
        'dbname': '',
        'user': '',
        'password': '',
        'host': '',
        'port': ''
        }

response = requests.get(url)

if response.status_code != 200:
    raise ValueError("Failed to reach webpage")

print(response.content)
