from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import requests

myUrl = 'https://www.freshnlean.com/locations/#tab-section1'

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
url = 'https://www.freshnlean.com/locations/#tab-section1'
data = requests.get(url, headers={'User-Agent': user_agent})
code = BeautifulSoup(data.text, 'html.parser')
print(code.h1)