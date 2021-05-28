from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import requests

myUrl = 'https://www.freshnlean.com/locations/#tab-section1'

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
url = 'https://www.freshnlean.com/locations/#tab-section1'
data = requests.get(url, headers={'User-Agent': user_agent})
code = BeautifulSoup(data.text, 'html.parser')

listItem = code.findAll("div",{"class":"location-list"})

city = listItem[0]

#print(city.ul.li.a)

print(city)


tmp_dict = {}
tmp_dict['city_state'] = []
tmp_dict['link'] = []
for i in city:
    for x in range(len(city.find_all('a'))):
        tmp_dict['city_state'].append(city.find_all('a')[x].text)
        tmp_dict['link'].append(city.find_all('a')[x]['href'])

#city.find_all('a')[0]['href']

print(tmp_dict)

import pandas as pd
pd.DataFrame(tmp_dict).to_csv('./links_citystate.csv')
