from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import requests

myUrl = 'https://www.freshnlean.com/locations/#tab-section1'

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
url = 'https://www.freshnlean.com/locations/#tab-section1'
data = requests.get(url, headers={'User-Agent': user_agent})
code = BeautifulSoup(data.text, 'html.parser')

Object = code.findAll("div",{"class":"location-list"})

list = Object[0]

tmp_dict = {}
tmp_dict['city_state'] = []
tmp_dict['link'] = []

for x in range(len(list.find_all('a'))):
    tmp_dict['city_state'].append(list.find_all('a')[x].text)
    tmp_dict['link'].append(list.find_all('a')[x]['href'])

print(tmp_dict)

import pandas as pd
pd.DataFrame(tmp_dict).to_csv('./links_citystate.csv')
