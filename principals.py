import pip._vendor.requests 
from bs4 import BeautifulSoup

'''Obtendo o HTML do Site'''

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
page = pip._vendor.requests.get(url)  #Fazemos a requisiçao para obter todo a página
soup = BeautifulSoup(page.text, 'lxml')  #usamos a framwork para fazer o parse usando "lxml" do texto retirado da página.

'''Tags'''
soup.header
soup.div

'''NavigableStrings'''
tag = soup.header.p #obtenho as tags <p> vindo do "<header>"
tag.string #apresento como string

'''Attributes'''
tag = soup.header.p
tag.attrs #obtenho um dicionário dos atributos que estao dentro desta tag
tag['role']  #posso espcificar um dos itens do dic
tag['new_att'] = 'add new attribute assim'

'''Find'''
soup.find('header') #busca na página a tag escolhida
soup.header.attrs
soup.find('div', {'class':'container test-site'}) #busca dentro das 'div' o atributo 'classe' que possua 'container test-site'
soup.find_all('h4', {'class':'someclass attr'}) #busca todos que possuem esses parametros
soup.find_all(['a', 'div', 'h4']) #busca por mais de uma tag
soup.find_all(id=True) #filtro de busca
soup.find_all(string='iphone') #busca por string no texto

import re
soup.find_all(string= re.compile('Iph')) # "re" ajuda a busca apenas utlizando partes de strings, tira a necessidade de texto literal
soup.find_all(class_= re.compile('pull')) #busca por classe
soup.find_all('a', class_= re.compile('pull', limit=3))
'---pratice---'
product_name = soup.find_all('a', class_ = 'title')
product_name
product_name_list = []
for i in product_name:  
    name = i.text #converte para string
    product_name_list.append(name) #coloca na nova lista de produtos

product_price = soup.find_all('h4', class_ = 'price')
product_price
product_price_list = []
for i in product_name:  
    price = i.text #converte para string
    product_price_list.append(price) #coloca na nova lista de preços

import pandas as pd
table = pd.DataFrame({'Product Name':product_name_list, 'Price':product_price_list}) #formato as listas ontidas em tabelas


'''Extract Data from Nasted HTML'''
#   aqui posso extrai baseado em bloco de códigos que já trazem toda a informação que preciso
#   uma tag pai, que contenha tudo
boxes = soup.find_all('div', class_ = 'uma classe pai')[6]
boxes  
boxes.find('a').text #após refinar posso extrair apenas os dados que quero
boxes.find('p', class_= 'price').text






