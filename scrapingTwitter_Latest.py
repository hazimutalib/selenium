import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 
from datetime import date, datetime, timedelta
import re
import sys
from scrapingTiktokComments import scrape_tiktok_comments
import os
import re


timenow = datetime.now()
#Buka Edge and the website
http = 'https://twitter.com/'
pathEdge = r'C:\Users\Analyst07\Documents\Selenium\Edge\msedgedriver.exe'

#customize chrome display
browser_options = Options()
browser_options.add_argument('--no-sanbox')
browser_options.add_experimental_option('excludeSwitches', ['enable-logging'])

#chrome options argument('--headless')
browser_options.add_argument('disable-notificatioon')
browser_options.add_argument('--disable-infobars')
browser_options.add_argument("--start-maximized")

driver = webdriver.Edge(executable_path=pathEdge, options=browser_options)
driver.get(http)
time.sleep(5)

#Search Based on Hashtag
searchHashtag = sys.argv[1]
parent_dir = "C:\\Users\\Analyst07\\Documents\\Selenium"
path = os.path.join(parent_dir, 'keyword_{}_({})'.format(searchHashtag,date.today()))
os.mkdir(path)
element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")

element.send_keys(searchHashtag)
element.send_keys(Keys.ENTER)

time.sleep(10)



i=0
while i<1:
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/div/span").click()
        i=1
    except:
        i=0
        time.sleep(5)


#menu Top
n=1
i = 0 
while i < n:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    i = i+1

time.sleep(5)


#Data html page tiktok dari beutifulsoup4
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, 'html.parser')

lists = []

for row in soup.findAll('div',attrs = {'class':'css-1dbjc4n r-18u37iz'}):
    list = {}
    try:
        x = row.find('span', attrs = {'class':'css-901oao css-16my406 css-1hf3ou5 r-poiln3 r-bcqeeo r-qvutc0'}).span.text
    except:
        x= ' '
    list['nickname'] = x
    try:
        x = row.find('div', attrs = {'class':'css-901oao css-1hf3ou5 r-14j79pv r-18u37iz r-37j5jr r-1wvb978 r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0'}).span.text
    except:
        x= ' '
    list['username'] = x

    lists.append(list)


driver.close()
df = pd.DataFrame(lists)
df = df[df['username'] != ' ']
df.to_csv(path +'\\{}.csv'.format(searchHashtag), index = False)





