#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv
import pandas as pd
import glob


# In[2]:


csv_file = 'spotify_urls.csv'


# In[3]:


df = pd.read_csv(csv_file, names=["url", "date"])


# In[4]:


df.head()


# In[5]:


for index, row in df.iterrows():
    file = requests.get(row['url'])
    open(row['date'] + '.csv', 'wb').write(file.content)


# In[9]:


csv_files = glob.glob('*.csv')
for file in csv_files:
    lines = open(file).readlines()
    open(file, 'w').writelines(lines[2:])


# In[20]:


csv_out = "spotify-sample-data.csv"
csv_header = 'Position','Track Name','Artist','Streams','URL'
with open(csv_out,"a") as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)


# In[27]:


li = []

for filename in csv_files:
    df = pd.read_csv(filename, index_col=None)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

