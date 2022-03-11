#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import keyring
import requests
import json
from io import StringIO

# IGDB KEY
#igdb_key = 'la70dhayt9crzxlfqxazqfnr958j60'
#igdb_secret = 'mi1m1udu3ax1kwatqlm3u5iqq7zu6m'
#keyring.set_password('igdb_api','key', igdb_key)
#keyring.set_password('igdb_api','secret',igdb_secret)
#print(keyring.get_password('igdb_api','key'),keyring.get_password('igdb_api','secret'))

# Create URL to get Bearer token
url = 'https://id.twitch.tv/oauth2/token?client_id=%s&client_secret=%s&grant_type=client_credentials'%(keyring.get_password('igdb_api','key'),keyring.get_password('igdb_api','secret'))

response = requests.post(url)
auth_results = json.loads(response.text.split('\n')[0])
authorization = 'Bearer ' + auth_results['access_token']
client_id = keyring.get_password('igdb_api','key')

# Create Companies dataset
url = 'https://api.igdb.com/v4/companies'
headers = {'Client-ID': client_id, 'Authorization': authorization, 'Accept': 'application/json'}
body = {'Data-Raw': 'fields name;'}
response = requests.post(url = url, headers = headers, data = 'fields *;limit 500;')


test_df = pd.read_json(StringIO(response.text))
df = pd.DataFrame()
while test_df.shape[0] != 0:
    df = df.append(test_df)   
    current_ids = list(df.id.values.astype(str))
    current_ids = '('+', '.join(current_ids)+')'
    response = requests.post(url = url, headers=headers, data= 'fields *; where id != %s; limit 500;'%current_ids)
    test_df = pd.read_json(StringIO(response.text))

company_df = df.reset_index()


# Create the Franchises Data Set
url = 'https://api.igdb.com/v4/franchises'
headers = {'Client-ID': client_id, 'Authorization': authorization, 'Accept': 'application/json'}
response = requests.post(url = url, headers = headers, data = r'fields *;limit 500;')
test_df = pd.read_json(StringIO(response.text))
df = pd.DataFrame()
while test_df.shape[0] != 0:
    df = df.append(test_df)   
    current_ids = list(df.id.values.astype(str))
    current_ids = '('+', '.join(current_ids)+')'
    response = requests.post(url = url, headers=headers, data= r'fields *; where id != %s; limit 500;'%current_ids)
    test_df = pd.read_json(StringIO(response.text))
franchise_df = df.reset_index

## Create the Game Engines Data Set
url = 'https://api.igdb.com/v4/game_engines'
headers = {'Client-ID': client_id, 'Authorization': authorization, 'Accept': 'application/json'}
response = requests.post(url = url, headers = headers, data = r'fields *;limit 500;')
test_df = pd.read_json(response.text)
df = pd.DataFrame()
while test_df.shape[0] != 0:
    df = df.append(test_df)   
    current_ids = list(df.id.values.astype(str))
    current_ids = '('+', '.join(current_ids)+')'
    response = requests.post(url = url, headers=headers, data= r'fields *; where id != %s; limit 500;'%current_ids)
    test_df = pd.read_json(response.text)
engine_df = df.reset_index()