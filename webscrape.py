from bs4 import BeautifulSoup
import requests

url = r'https://www.olx.co.id/?utm_source=google&utm_medium=cpc&utm_campaign=ID|MIX|B2C|PM|GP|PROS|WEB|CPC|Clicks|BrandingCampaign|NA|DefaultTab|20240515&utm_term=&utm_content=&campaign_id=21285933309&group_id=&target_id=&ad_id=&matchtype=&network=x&device=c&country=ID&territory=MIX&group=&campaign_type=PM&gad_source=1&gclid=CjwKCAjw8rW2BhAgEiwAoRO5rAoADUoSpCPF82IOShE1s8Fwl6lFflr7UWZ0D0r58MNEmAvRYhpYPxoCm3kQAvD_BwE'
response = requests.get(url)

if response.status_code != 200:
    raise ValueError("Failed to reach webpage")

print(response.content)
