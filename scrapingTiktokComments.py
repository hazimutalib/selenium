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

def convert_full_figures(x):
  if str(x).find('K') != -1:
    x = int(float(str(x)[:-1])*1000)
  elif str(x).find('M') != -1:
    x = int(float(str(x)[:-1])*1000000)
  elif x == 'Share':
    x = 0
  else:
    x = int(x)
  return x

def scrape_tiktok_comments(path,link,keyword,tarikh,video_views,video_image_link, video_caption):
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
    try:
        video_likes = soupTemp.find_all('strong', attrs = {'class':'tiktok-wxn977-StrongText edu4zum2'})[0].text
    except:
        video_likes = soupTemp.find_all('strong', attrs = {'class':'tiktok-1asxc6s-StrongText edu4zum2'})[0].text
    try:                                                           
        noOfComments= int(convert_full_figures(soupTemp.find_all('strong', attrs = {'class':'tiktok-wxn977-StrongText edu4zum2'})[1].text))
    except:
        noOfComments= int(convert_full_figures(soupTemp.find_all('strong', attrs = {'class':'tiktok-1asxc6s-StrongText edu4zum2'})[1].text))
    try:    
        video_shared = soupTemp.find_all('strong', attrs = {'class':'tiktok-wxn977-StrongText edu4zum2'})[2].text
    except:
        video_shared = soupTemp.find_all('strong', attrs = {'class':'tiktok-1asxc6s-StrongText edu4zum2'})[2].text
        
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
            comment_date = row.find('p', attrs = {'class':'tiktok-1wmf4bu-PCommentSubContent e1g2efjf8'}).span.text
            now = datetime.now()
            if comment_date.find('m') != -1:
                x = now - timedelta(minutes = int(comment_date.split('m')[0]))
                comment_date = '{}-{}-{}'.format(x.year,x.month if len(str(x.month)) == 2 else '0'+str(x.month),x.day if len(str(x.day)) == 2 else '0'+str(x.day))
            elif comment_date.find('h') != -1:
                x = now - timedelta(hours = int(comment_date.split('h')[0]))
                comment_date = '{}-{}-{}'.format(x.year,x.month if len(str(x.month)) == 2 else '0'+str(x.month),x.day if len(str(x.day)) == 2 else '0'+str(x.day))
            elif comment_date.find('d') != -1:
                x = now - timedelta(days = int(comment_date.split('d')[0]))
                comment_date = '{}-{}-{}'.format(x.year,x.month if len(str(x.month)) == 2 else '0'+str(x.month),x.day if len(str(x.day)) == 2 else '0'+str(x.day))
            elif comment_date.find('w') != -1:
                x = now - timedelta(weeks = int(comment_date.split('w')[0]))
                comment_date = '{}-{}-{}'.format(x.year,x.month if len(str(x.month)) == 2 else '0'+str(x.month),x.day if len(str(x.day)) == 2 else '0'+str(x.day))
            elif len(comment_date)<=5 :
                x = comment_date.split('-')
                comment_date = '{}-{}-{}'.format(now.year, x[0] if len(x[0]) ==2 else '0'+str(x[0]), x[1] if len(x[1]) ==2 else '0'+str(x[1]))
            else: 
                x = comment_date.split('-')
                comment_date = '{}-{}-{}'.format(x[0], x[1] if len(x[1]) ==2 else '0'+str(x[1]), x[2] if len(x[2]) ==2 else '0'+str(x[2]))
            try:
                avatar = row.find('span', attrs = {'class':'tiktok-tuohvl-SpanAvatarContainer e1e9er4e0'}).img['src']
            except:
                avatar = ' '
            list['avatar'] = avatar
            list['posted_date'] =  comment_date
            list['extracted_date'] = date.today()
            list['video_link'] = link
            list['video_likes'] = video_likes
            list['video_comments'] = noOfComments
            list['video_shared'] = video_shared
            list['video_posted_date'] = tarikh
            list['video_views'] = video_views
            list['video_image_link'] = video_image_link
            list['video_caption'] = video_caption
            lists.append(list)

        driver.close()
        df = pd.DataFrame(lists)
        df.to_csv(path +'\\{}_{}_({})_({}).csv'.format(keyword,link.split('/')[3],tarikh,link.split('/')[-1]),index = False)
    else:
        df = print('No comments found')
    return df

    

# scrape_tiktok_comments('https://www.tiktok.com/@triviamy.com/video/7186874504407174426','kwsp','')