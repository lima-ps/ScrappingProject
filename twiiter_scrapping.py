from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pip._vendor.requests as request
import pandas as pd
import time

#config
driver = webdriver.Chrome('C:/Users/phill/Desktop/Estudo/Python/chromedriver.exe')
driver.get('https://twitter.com/i/flow/login')
time.sleep(2)

#login
login = driver.find_element(By.XPATH, '/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input') #localiza o input do email
login.send_keys('umteste@gmail.com') #preenche o email
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]').click() #press next to go to password

password = driver.find_element(By.XPATH, '/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input') #acha o campo de input
password.send_keys('*********') #preenche a pass
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div').click() #button login
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]').click() #accept buttom terms 

#search
celebrity = 'The Rock'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')))
search = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input') #caixa de pesquisa
search.send_keys(celebrity) #insere pesquisa
search.send_keys(Keys.ENTER) #click enter
time.sleep(2)
people_div = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]').click()
time.sleep(2)
chosen_profile = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span').click()
time.sleep(2)

#scrappin celebrity chosen page
soup = BeautifulSoup(driver.page_source, 'lxml')
posts = soup.find_all('div', class_="css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0")

'''ao fazer scrowdown, twitter descarta os tuites que ficaram pra cima, ele nao apenas carrega os novos'''
'''solução: scrowdown um pouco e scraping todos e assim repetir isso'''
tweets = []
while True:
    for post in posts:
        tweets.append(post.text)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)') #carrega a pagina ate a altura definida
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    posts = soup.find_all('div', class_="css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0")
    unique_tweets = list(set(tweets)) #remove os possiveis tweets duplicados
    if len(unique_tweets) > 200: #para quando chegar no 200
        break
