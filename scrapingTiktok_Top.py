import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 
from datetime import date
import re
import sys
from scrapingTiktokComments import scrape_tiktok_comments
import os



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
path = os.path.join(parent_dir, searchHashtag)
os.mkdir(path)
element = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/form/input")

element.send_keys(searchHashtag)
element.send_keys(Keys.ENTER)

time.sleep(10)

#menu Top
ii=0
while ii<1:
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div").click()
        ii=1
    except:
        ii=0
        time.sleep(5)

#Load More
i=0
while i<30:
    try:
        NextStory = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[2]/div[2]/button")))
        NextStory.click()
        time.sleep(2)
    except:
        i=30

#Data html page tiktok dari beutifulsoup4
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, 'html.parser')


#Scraping data tiktok
tiktok_description, tiktok_link, username, tiktok_hashtag, tiktok_views, posted_date = [], [], [], [], [], []
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

#posted_date
for tarikh in soup.find_all('div', class_= 'tiktok-842lvj-DivTimeTag e19c29qe14'):
    posted_date.append(tarikh.text)



#SAVE DATA
listCols = ['tiktok_link', 'tiktok_description', 'tiktok_hashtag', 'Username', 'Views', 'posted_date']
dict_data = dict(zip(
    listCols,(tiktok_link, tiktok_description, tiktok_hashtag , username, tiktok_views, posted_date)
))

# import json
# with open('Scraping' + searchHashtag + '_top.json','w') as fp:
#     json.dump(dict_data,fp)

df = pd.DataFrame(data=dict_data)
df['extracted_date'] = date.today()

df.to_csv(path + '\\topVideos({}).csv'.format(searchHashtag), index=False)


for link, tarikh in zip(df['tiktok_link'][:10],df['posted_date'][:10]):
    scrape_tiktok_comments(path, link, searchHashtag, tarikh)

    



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