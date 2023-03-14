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
parent_dir = "C:\\Users\\Analyst07\\Documents\\Selenium\\twitter"
path = os.path.join(parent_dir, 'keyword_{}_({})'.format(searchHashtag,date.today()))
os.mkdir(path)
element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")

element.send_keys(searchHashtag+ " since:2023-02-24")
element.send_keys(Keys.ENTER)

time.sleep(10)



# i=0
# while i<1:
#     try:
#         driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/div/span").click()
#         i=1
#     except:
#         i=1
        
# time.sleep(5)

#menu Top
n=10
i = 0 
lists = []
while i <= n:
    time.sleep(1)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    for row in soup.findAll('div',attrs = {'class':'css-1dbjc4n r-18u37iz'}):
        list = {}
        try:
            x = row.find('img', attrs = {'class':'css-9pa8cd'})['src']
        except:
            x= ''
        list['avatar'] = x
        try:
            x = row.find('span', attrs = {'class':'css-901oao css-16my406 css-1hf3ou5 r-poiln3 r-bcqeeo r-qvutc0'}).span.text
        except:
            x= ''
        list['nickname'] = x
        try:
            x = row.find('div', attrs = {'class':'css-901oao css-1hf3ou5 r-14j79pv r-18u37iz r-37j5jr r-1wvb978 r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0'}).span.text
        except:
            x= ' '
        list['username'] = x
        try:
            list['time'] = row.findNext('div', attrs = {'class':'css-1dbjc4n r-18u37iz r-1q142lx'}).a.time.text
        except:
            list['time'] = ''
        try:
            list['datetime'] = row.findNext('div', attrs = {'class':'css-1dbjc4n r-18u37iz r-1q142lx'}).a.time['datetime']
        except:
            list['datetime'] = ''
        try:
            list['tweets'] = row.find('div', attrs = {'class':'css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu'}).find('div', attrs = {'class':'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'}).text
        except:
            list['tweets'] = ''
        try:
            list['img1'] = row.findAll('img', attrs = {'class':'css-9pa8cd'})[1]['src']
        except:
            list['img1'] = ''
        try:
            list['img2'] = row.findAll('img', attrs = {'class':'css-9pa8cd'})[2]['src']
        except:
            list['img2'] = ''
        try:
            list['img3'] = row.findAll('img', attrs = {'class':'css-9pa8cd'})[3]['src']
        except:
            list['img3'] = ''
        try:
            list['img4'] = row.findAll('img', attrs = {'class':'css-9pa8cd'})[4]['src']
        except:
            list['img4'] = ''
        try:
            list['numberOfComments'] = row.find('span', attrs = {'class':'css-901oao css-16my406 r-poiln3 r-n6v787 r-1cwl3u0 r-1k6nrdp r-1e081e0 r-qvutc0'}).text
        except:
            list['numberOfComments'] = ''
        try:
            list['numberOfRetweets'] = row.findAll('span', attrs = {'class':'css-901oao css-16my406 r-poiln3 r-n6v787 r-1cwl3u0 r-1k6nrdp r-1e081e0 r-qvutc0'})[1].text
        except:
            list['numberOfRetweets'] = ''
        try:
            list['numberOfLikes'] = row.findAll('span', attrs = {'class':'css-901oao css-16my406 r-poiln3 r-n6v787 r-1cwl3u0 r-1k6nrdp r-1e081e0 r-qvutc0'})[2].text
        except:
            list['numberOfLikes'] = ''
        try:
            list['numberOfViews'] = row.findAll('span', attrs = {'class':'css-901oao css-16my406 r-poiln3 r-n6v787 r-1cwl3u0 r-1k6nrdp r-1e081e0 r-qvutc0'})[3].text
        except:
            list['numberOfViews'] = ''
        try:
            list['isAds'] = row.find('div', attrs = {'class':'css-901oao r-14j79pv r-37j5jr r-n6v787 r-16dba41 r-1cwl3u0 r-bcqeeo r-qvutc0'}).span.text
            list['isAds'] = 'Yes'
        except:
            list['isAds'] = 'No'
        

        lists.append(list)
    height = driver.execute_script("return document.body.scrollHeight")
    i = i+1
    driver.execute_script("window.scrollTo(0,{})".format(i*1500))
    time.sleep(2)
    # new_height = driver.execute_script("return document.body.scrollHeight")
    # if new_height == height:
    #     i = n + 1

    
    
df = pd.DataFrame(lists)
df = df[df['username'] != ' ']
df = df.drop_duplicates()
df.to_csv(path +'\\data.csv'.format(searchHashtag), index = False)





