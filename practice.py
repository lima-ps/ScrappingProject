#Fazer 'scrapping' de mercado da apple, buscando "preço, preço fechado,
#o preço em uma janela de 52 semanas e o rating"

# configurando
from bs4 import BeautifulSoup
import pip._vendor.requests

url = 'https://www.marketwatch.com/investing/stock/aapl'
page = pip._vendor.requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup

# Price

price = soup.find('bg-quote', class_='value').text
price

#Closing Price
closing_price = soup.find('td', class_="table__cell u-semi").text
closing_price

#52 Week Range (lower, upper)

'''como existiam muitas classes span primary, foi necessário começas
    o scrapping pela tag pai e depois filtrar as tags spans que queriamos'''

nested = soup.find('mw-rangebar', class_="element element--range range--yearly") 
nested

lower = nested.find_all('span', class_="primary")[0].text
lower

upper = nested.find_all('span', class_="primary")[1].text
upper

# Rating
rating = soup.find('li', class_="analyst__option active").text
rating