from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import pip._vendor.requests as request
import pandas as pd
import time

#config send email
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

sender = 't@gmail.com'
receiver = 't@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'New Job on Indeed'
msg['From'] = sender
msg['To'] = ','.join(receiver)

part = MIMEBase('application', 'octet-stream')
part.set_payload(open('C:/Users/phill/Desktop/Estudo/Python/Scrapping/ScrappingProject/table_scraped.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename = "table_scraped.csv")
msg.attach(part)

s = smtplib.SMTP_SSL(host = 'smtp.mail@gmail.com', port=465)
s.login(user = 't@gmail.com', password='*******')
s.sendmail(sender, receiver, msg.as_string())
s.quit()




