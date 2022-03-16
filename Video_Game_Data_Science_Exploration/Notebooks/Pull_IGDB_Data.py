# Author: Zach Shaw
# Purpose: Perform API Calls to IGDB to create Games, Company, Engine, and Franchise datasets
    # Then output them to csv files.

import pandas as pd
import keyring
import requests
import json
from io import StringIO

data_output = 'C:/Users/Zach/source/repos/Video_Game_DS_Hype_Predict/Video_Game_Data_Science_Exploration/Data/Output/'

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

df.reset_index()
company_df = df.copy()


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
df.reset_index()
franchise_df = df.copy()

## Create the Game Engines Data Set
url = 'https://api.igdb.com/v4/game_engines'
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
df.reset_index()
engine_df = df.copy()

## Create the Games Data Set
url = 'https://api.igdb.com/v4/games'
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
df.reset_index()
games_df = df.copy()



engine_df.to_csv(data_output+'engine_data.csv')
franchise_df.to_csv(data_output+'franchise_data.csv')
company_df.to_csv(data_output+'company_data.csv')
games_df.to_csv(data_output+'game_data.csv')