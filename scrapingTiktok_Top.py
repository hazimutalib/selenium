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


timenow = datetime.now()
#Buka Edge and the website
http = 'https://www.tiktok.com'
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
try:
    element = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div/form/input")
except:
    element = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/input")
                                        

element.send_keys(searchHashtag)
element.send_keys(Keys.ENTER)

time.sleep(10)

#menu Top
i=0
while i<1:
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div").click()
        i=1
    except:
        i=0
        time.sleep(5)
#Load More
ii=0
while ii<30:
    try:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        NextStory = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button")))  
        NextStory.click()
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button").click()
    except:
        ii=30

#Data html page tiktok dari beutifulsoup4
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, 'html.parser')


#Scraping data tiktok
tiktok_description, tiktok_link, username, tiktok_hashtag, tiktok_views, tiktok_views_full, posted_date_original ,posted_date, tiktok_image = [], [], [], [], [], [], [], [], []
#title
for title in soup.find_all('div', class_='tiktok-1ejylhp-DivContainer ejg0rhn0'):
    tiktok_description.append(title.text)
    
    findTitle = title.text
    # cleanedTitle = re.sub("#[A-Za-z0-9_]+","", findTitle)
    # cleanedTitle = cleanedTitle.replace("  ", "")
    # tiktok_title.append(cleanedTitle)

    newHashtag = re.findall("#([a-zA-Z0-9_]{1,50})", findTitle)
    newHashtag ='#' + ' #'.join(newHashtag)
    tiktok_hashtag.append(newHashtag)
    
#link
for link in soup.find_all('div', class_='tiktok-yz6ijl-DivWrapper e1cg0wnj1'):
    #print(link['href'])
    tiktok_link.append(link.a['href'])

#username
for user in soup.find_all('p', class_= 'tiktok-2zn17v-PUniqueId etrd4pu6'):
    username.append(user.text)

#views
for view in soup.find_all('div', class_= 'tiktok-1lbowdj-DivPlayIcon etrd4pu4'):
    tiktok_views.append(view.text)
    tiktok_views_full.append(convert_full_figures(view.text))

#posted_date
for tarikh in soup.find_all('div', class_= 'tiktok-842lvj-DivTimeTag e19c29qe14'):
    tarikh_ori = tarikh.text
    tarikh = tarikh.text
    now = datetime.now()
    if tarikh.find('h') != -1:
        x = now - timedelta(hours = int(tarikh.split('h')[0]))
        tarikh = '{}-{}-{}'.format(x.year,x.month if len(str(x.month)) == 2 else '0'+str(x.month),x.day if len(str(x.day)) == 2 else '0'+str(x.day))
    elif tarikh.find('d') != -1:
        x = now - timedelta(days = int(tarikh.split('d')[0]))
        tarikh = '{}-{}-{}'.format(x.year,x.month if len(str(x.month)) == 2 else '0'+str(x.month),x.day if len(str(x.day)) == 2 else '0'+str(x.day))
    elif tarikh.find('w') != -1:
        x = now - timedelta(weeks = int(tarikh.split('w')[0]))
        tarikh = '{}-{}-{}'.format(x.year,x.month if len(str(x.month)) == 2 else '0'+str(x.month),x.day if len(str(x.day)) == 2 else '0'+str(x.day))
    elif (len(tarikh)<=5) :
        x = tarikh.split('-')
        tarikh = '{}-{}-{}'.format(now.year,x[0] if len(x[0]) == 2 else '0'+str(x[0]), x[1] if len(x[1]) == 2 else '0'+str(x[1]))
    else:
        x = tarikh.split('-') 
        tarikh = '{}-{}-{}'.format(x[0], x[1] if len(x[1]) ==2 else '0'+str(x[1]), x[2] if len(x[2]) ==2 else '0'+str(x[2]))
    posted_date_original.append(tarikh_ori)
    posted_date.append(tarikh)

#img
for image in soup.find_all('div', class_='tiktok-1jxhpnd-DivContainer e1yey0rl0'):
    #print(link['href'])
    tiktok_image.append(image.img['src'])



#SAVE DATA
listCols = ['tiktok_link', 'tiktok_description', 'tiktok_hashtag', 'username', 'tiktok_views','tiktok_views_full', 'posted_date_original', 'posted_date', 'tiktok_image']
dict_data = dict(zip(
    listCols,(tiktok_link, tiktok_description, tiktok_hashtag , username, tiktok_views, tiktok_views_full, posted_date_original, posted_date, tiktok_image)
))

# import json
# with open('Scraping' + searchHashtag + '_top.json','w') as fp:
#     json.dump(dict_data,fp)

df = pd.DataFrame(data=dict_data)
df['extracted_date'] = date.today()
df['posted_date'] = pd.to_datetime(df['posted_date']).dt.date
df = df[df['posted_date'] >= date(year=2023,month=2,day=24)]
df = df.sort_values(by = ['tiktok_views_full'], ascending = False).reset_index(drop = True)
df.to_csv(path + '\\topVideos({})_({}).csv'.format(searchHashtag,date.today()), index=False)


for link, tarikh, views, image, caption in list(zip(df['tiktok_link'],df['posted_date'],df['tiktok_views'],df['tiktok_image'],df['tiktok_description'])):
    print(link)
    scrape_tiktok_comments(path, link, searchHashtag, tarikh, views, image, caption)

    



# time.sleep(10)
# while i < 10:
#     driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
#     time.sleep(1)
#     i = i+1

# for i in range(len(df)):
#     driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[2]/div[1]/div/div[{}]/div[1]/div/div/a/div/div[1]".format(i+3)).click()
#     driver.refresh()
#     scrape_tiktok_comments(driver,i)
#     driver.back()
#     time.sleep(10)


driver.close()