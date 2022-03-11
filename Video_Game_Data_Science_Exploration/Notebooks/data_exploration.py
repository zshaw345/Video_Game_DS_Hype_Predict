#!/usr/bin/env python
# coding: utf-8

# In[1]:


# standard library imports
import csv
import datetime as dt
import json
import os
import statistics
import time

# third-party imports
import numpy as np
import pandas as pd
import requests


import random
import time

from lxml.html import fromstring
import nltk
nltk.download('punkt')
from twitter import OAuth, Twitter

secrets_df = pd.read_csv('C:/Users/Zach/OneDrive/Career/Video_Game_Data_Science_Exploration/Steam_Details/Steam_Deets.txt')

ACCESS_TOKEN=secrets_df.Twitter_API_Key
ACCESS_SECRET=secrets_df.Twitter_API_Key_Secret
CONSUMER_KEY=secrets_df.Twitter_Access_Token
CONSUMER_SECRET=secrets_df.Twitter_Access_Secret

# customisations - ensure tables show all columns
pd.set_option("max_columns", 100)


# In[212]:


def expand_methods(current_row,expanded_df):
    title = current_row[0]
    for current_method in current_row.methods:
        expanded_methods = {my_key:[my_values] for my_key,my_values in zip(current_method.keys(),current_method.values())}
        expanded_methods['api_name'] = title
        expanded_df = expanded_df.append(pd.DataFrame(expanded_methods),ignore_index=True)
    return expanded_df


# In[227]:


url = 'http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key=526E083FB4A22BE11CD40E88A45C0AE0'
response = requests.get(url=url, params=parameters)
api_metadata = response.json()


# In[228]:


api_metadata_df = pd.DataFrame.from_dict(api_metadata['apilist']['interfaces'])
expanded_df = pd.DataFrame()


# In[229]:


for row in api_metadata_df.iterrows():
    expanded_df = expand_methods(row[1],expanded_df)
ordered_columns = ['api_name','method_name','description','version','httpmethod','parameters']
expanded_df.columns = ['method_name', 'version', 'httpmethod', 'parameters', 'api_name','description']
expanded_df = expanded_df.reindex(columns = ordered_columns)


# In[230]:


expanded_df


# In[232]:


expanded_df.to_csv('../Data/Output/Accessible_API.csv',index=False)


# In[ ]:





# In[45]:


url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=526E083FB4A22BE11CD40E88A45C0AE0&steamid=76561198132877289&format=json"
parameters = {"request": "all"}
response = requests.get(url=url, params=parameters)
print(response)
# request 'all' from steam spy and parse into dataframe
# json_data = get_request(url, parameters=parameters)
steam_spy_all = pd.DataFrame(json_data['response']['games'])


# In[233]:


from bs4 import BeautifulSoup


# In[237]:


# Making a GET request
useragent = "SteamDB-Educational-Access;"
url = 'https://steamdb.info/search/?a=app&q=star+wars'
headers = {"user-agent": useragent}
r = requests.get(url,headers=headers)


print(r)

# Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())


# In[ ]:
oauth = OAuth(
        ACCESS_TOKEN,
        ACCESS_SECRET,
        CONSUMER_KEY,
        CONSUMER_SECRET
    )
t = Twitter(auth=oauth)



#%%
def scrape_website():
    
