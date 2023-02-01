import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 
from datetime import date,datetime
import re
import sys
import os

def scrape_tiktok_comments(path,link,keyword,tarikh):
    #open Edge and the website
    http = link
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
    driver.execute_script('videos = document.querySelectorAll("video"); for(video of videos) {video.pause()}')
    htmlTemp = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soupTemp = BeautifulSoup(htmlTemp, 'html.parser')
    video_likes = soupTemp.find_all('strong', attrs = {'class':'tiktok-wxn977-StrongText edu4zum2'})[0].text
    noOfComments= int(soupTemp.find_all('strong', attrs = {'class':'tiktok-wxn977-StrongText edu4zum2'})[1].text)
    video_shared = soupTemp.find_all('strong', attrs = {'class':'tiktok-wxn977-StrongText edu4zum2'})[2].text
    time.sleep(20)
  

    if noOfComments <= 500:
        noOfClicks = int(noOfComments/20+1)
    elif noOfComments > 500 and noOfComments <= 1000: 
        noOfClicks = int(noOfComments/25+1)
    elif noOfComments > 1000 and noOfComments <= 2000: 
        noOfClicks = int(noOfComments/30+1)
    elif noOfComments > 2000 and noOfComments <= 3000: 
        noOfClicks = int(noOfComments/40+1)
    elif noOfComments > 3000 and noOfComments <= 5000: 
        noOfClicks = int(noOfComments/50+1)
    else:
        noOfClicks = int(noOfComments/60+1)
     
    if noOfComments > 0:
        i = 0
        while i < noOfClicks:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
            i = i+1
            


        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, 'html.parser')

        lists = []

        table = soup.find('div', attrs = {'class':'tiktok-xzzes5-DivCommentListContainer ekjxngi0'})

        for row in table.findAll('div',attrs = {'class':'tiktok-16r0vzi-DivCommentItemContainer eo72wou0'}):
            list = {}
            list['comment'] = row.p.text
            list['username'] = row.a['href'][1:]
            list['nickname'] = row.find('span', attrs = {'class':'tiktok-mfqbp1-SpanUserNameText e1g2efjf3'}).text
            list['likes'] = row.find('div', attrs = {'class':'tiktok-1e3qwdr-DivLikeWrapper-StyledLikeWrapper ezxoskx1'}).span.text
            try:
                list['noOfRepliedComments'] = row.find('p', attrs = {'class':'tiktok-1qqecn-PReplyActionText eo72wou4'}).text.split(' ')[3][1:-1]
            except:
                list['noOfRepliedComments'] = 0
            list['posted_date'] = row.find('p', attrs = {'class':'tiktok-1wmf4bu-PCommentSubContent e1g2efjf8'}).span.text 
            list['extracted_date'] = date.today()
            list['video_link'] = link
            list['video_likes'] = video_likes
            list['video_comments'] = noOfComments
            list['video_shared'] = video_shared
            list['video_posted_date'] = tarikh
            lists.append(list)

        driver.close()
        df = pd.DataFrame(lists)
        df.to_csv(path +'\\{}_{}_({})_({}).csv'.format(keyword,link.split('/')[3],tarikh,link.split('/')[-1]),index = False)
    else:
        df = print('No comments found')
    return df

    

# scrape_tiktok_comments('https://www.tiktok.com/@triviamy.com/video/7186874504407174426','kwsp','')