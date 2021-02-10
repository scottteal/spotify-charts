import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv
import pandas as pd
import glob

# Use a csv file included in this repo which includes all of the desired days of data, and their respective URL path to the associated CSV file on spotifycharts.com.
# In the example file fot this repo, I am requesting the top 200 most streamed songs globally at daily granularity from 2020-01-01 to 2021-02-08.
csv_file = 'spotify_urls.csv'

# Turn the csv into a dataframe so that you will be able to loop through them.
df = pd.read_csv(csv_file, names=["url", "date"])

# Loop through the 'url' column of the dataframe to send requests to the url's in the column, downloading CSV files in the same directory
# Then save the file using the 'date' as the filename with '.csv' as the file extension
for index, row in df.iterrows():
    file = requests.get(row['url'])
    open(row['date'] + '.csv', 'wb').write(file.content)

# In order to delete an unnecessary row in every CSV, and the header row in each CSV file, create a list of the CSV files you just downloaded by matching any file ending in .csv
csv_files = glob.glob('*.csv')
for file in csv_files:
    lines = open(file).readlines()
    open(file, 'w').writelines(lines[2:])

# Combine all files in the csv_files glob into a single dataframe, while also appending the file name as a column so you know which date the data corresponds to
combined_csv = []
combined_csv = pd.concat([pd.read_csv(f).assign(charts_date=os.path.basename(f).split('.')[0]) for f in csv_files])

# Check that the dataframe looks like the combined CSV you would expect
combined_csv.head()

# Export the dataframe that combined all of the CSV's into a single CSV called "combined_csv.csv"
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
