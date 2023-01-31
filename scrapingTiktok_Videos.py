import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 
import re

#Buka Edge dan Situs
alamatSitus = 'https://www.tiktok.com'
pathEdge = '\Selenium\Firefox\geckodriver.exe'

#customize chrome display
browser_options = Options()
browser_options.add_argument('--no-sanbox')

#chrome options argument('--headless')
browser_options.add_argument('disable-notificatioon')
browser_options.add_argument('--disable-infobars')
browser_options.add_argument("--start-maximized")

driver = webdriver.Firefox(executable_path=pathEdge, options=browser_options)
driver.get(alamatSitus)

#Search Berdasar Tagar
tagarSearch = '#catfunny'
element = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div/form/input")
element.send_keys(tagarSearch)
element.send_keys(Keys.ENTER)

time.sleep(5)

#menu video
ii=0
while ii<1:
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[3]").click()
        ii=1
    except:
        ii=0
        time.sleep(5)

time.sleep(5)
#Load More
i=0
while i<30:
    try:
        NextStory = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button")))
        NextStory.click()
        time.sleep(2)
    except:
        i=30

#Data html page tiktok dari beutifulsoup4
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, 'html.parser')

#Scraping data tiktok
#Scraping data tiktok
deskripsi_tiktok, link_tiktok, username, judul_tiktok, tagar_tiktok=[], [], [], [], []
#Judul
for judul in soup.find_all('div', class_='tiktok-1ejylhp-DivContainer ejg0rhn0'):
    deskripsi_tiktok.append(judul.text)
    
    cariJudul = judul.text
    judulBersih = re.sub("#[A-Za-z0-9_]+","", cariJudul)
    judulBersih = judulBersih.replace("  ", "")
    judul_tiktok.append(judulBersih)

    newTagar = re.findall("#([a-zA-Z0-9_]{1,50})", cariJudul)
    newTagar ='#' + ' #'.join(newTagar)
    tagar_tiktok.append(newTagar)
    
#link
for link in soup.find_all('div', class_='tiktok-yz6ijl-DivWrapper e1cg0wnj1'):
    #print(link['href'])
    link_tiktok.append(link.a['href'])

#username
for user in soup.find_all('p', class_= 'tiktok-2zn17v-PUniqueId etrd4pu6'):
    username.append(user.text)


#SAVE DATA
listCols = ['link_tiktok', 'deskripsi_tiktok', 'judul_tiktok', 'tagar_tiktok', 'Username']
dict_data = dict(zip(
    listCols,(link_tiktok, deskripsi_tiktok, judul_tiktok, tagar_tiktok , username)
))

import json
with open('Scraping' + tagarSearch + '_videos.json','w') as fp:
    json.dump(dict_data,fp)

df = pd.DataFrame(data=dict_data)
#df.head()

df.to_csv('scraping_' + tagarSearch + '_videos.csv', index=False)

driver.close()
