from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/phill/Desktop/Estudo/Python/chromedriver.exe')

driver.get('https://www.goat.com/sneakers')

#getting element by XPATH
driver.find_element(By.XPATH, '//*[@id="grid-body"]/div/div[1]/div[22]/a/div[1]/div[2]/div/div/span').text

for i in range(1, 30): #mostra uma lista de no máximo 30 elementos dentro da url que queremos
    #necessário troca o valor na string pelo nosso "i" em formato de string
    price = driver.find_element(By.XPATH, '//*[@id="grid-body"]/div/div[1]/div['+str(i)+']/a/div[1]/div[2]/div/div/span').text
    print(price)

#pressing Buttons
driver.find_element(By.XPATH, 'somePath').click()

#Send Text to Input Box
driver.get('https://www.google.com/')

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('What is web scrapping') #insere o texto na box pretendida
box.send_keys(Keys.ENTER) #pressiona o enter após a pesquisa

#screenshot
driver.find_element(By.XPATH, 'somePath').screenshot('pathToSave')

#Self Scrolling
driver.get('https://www.google.com/search?q=girafa&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjS5J2a8_v8AhXI6aQKHUkiCVAQ_AUoAXoECAEQAw')
driver.execute_script('return document.body.scrollHeight') #retorna a altura da página que foi carregada, nao necessariamente inteira
driver.execute_script('window.scrollTo(0, 1000)') #zero é o incicio da página, o segundo é até onde queremos que carregue

'''while True'''  #se usarmos o while ele ficará carregando até que chegue ao fim
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)') #combinação das duas, ele carrega do inicio da pagina carregada até o próximo fim, antes de carregar mais

'''while True 2'''
while True:
    last_height = driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height


#waiting times
''' usado para esperar páginas muito lentas, para so fazer scrapping depois de cerregadas por completo'''

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

element = WebDriverWait(driver, 10).until(   #vai esperar 10seg até que o elemento seja localizado
    EC.presence_of_element_located((By.ID, 'umID')))  #se nao achar em 10 segundo gerará erro
    #só vai passar pra próxima linha se o id for encontrato

'''modo simples'''
time.sleep(3)  #vai aguadar 3 segundos antes de rodar a próxima linha de código
