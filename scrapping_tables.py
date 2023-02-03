from bs4 import BeautifulSoup
import pip._vendor.requests as request
import pandas as pd

#Scrapping from page
url = 'https://www.worldometers.info/world-population/'
page = request.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_="table table-striped table-bordered table-hover table-condensed table-list")

# Columns Table
table.find_all('th')
headers = []

for i in table.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns=headers)

# Rows Table
for j in table.find_all('tr')[1:]:  #inicia da segunda linha pois a primeira são os headers
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    df.loc[length] = row

#export CSV

df.to_csv('C:/Users/phill/Desktop/Estudo/Python/Scrapping/ScrappingProject/table_scraped.csv')