#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd

secrets_df = pd.read_csv('C:/Users/Zach/OneDrive/Career/Video_Game_Data_Science_Exploration/Steam_Details/Steam_Deets.txt')

ACCESS_TOKEN=secrets_df.Twitter_API_Key
ACCESS_SECRET=secrets_df.Twitter_API_Key_Secret
CONSUMER_KEY=secrets_df.Twitter_Access_Token
CONSUMER_SECRET=secrets_df.Twitter_Access_Secret
