from bs4 import BeautifulSoup
import pip._vendor.requests as request
import pandas as pd

#scrapping from page
url = 'https://www.airbnb.com/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Honolulu%2C%20HI&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2023-02-27&checkout=2023-03-09&source=structured_search_input_header&search_type=autocomplete_click'
page = request.get(url)
soup = BeautifulSoup(page.text, 'lxml')

#find next page and loop for all pages to scrap

df = pd.DataFrame({'Links':[''], 'Title':[''], 'Price':[''], 'Rating':['']})
while True:
    
    postings = soup.find_all('div', class_="cy5jw6o")
    for post in postings:

        try:
            link = post.find('a', class_='bn2bl2p').get('href')
            link_full = 'https://www.airbnb.com'+link
            title = post.find('span', class_='t6mzqp7').text
            price = post.find('span', class_='_14y1gc').text[:4]
            rating = post.find('span', class_='r1dxllyb').text
            
            df = df.append({'Links':link_full, 'Title':title, 'Price':price, 'Rating':rating}, ignore_index = True)
        except:
            pass

    next_page = soup.find('a', {'aria-label':'Next'}).get('href') #busca em forma de dicionário utilizando o atributo da "a" tag. Depois chama o link associado a este atributo.
    next_page_full = 'https://www.airbnb.com'+next_page  #o href que pegamos acima, nao traz a url inteira por isso add o restante
    url = next_page_full
    page = request.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

df.to_csv('C:/Users/phill/Desktop/Estudo/Python/Scrapping/ScrappingProject/multipages_scraped.csv')