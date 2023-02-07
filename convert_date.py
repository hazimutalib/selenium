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

df = pd.read_csv(r'C:\Users\Analyst07\Documents\Selenium\keyword_nurul izzah_(2023-02-04)\sentiment.csv')

def comment_posted_date(date):
    comment_date = date
    now = datetime.now()
    if comment_date.find('m') != -1:
        x = now - timedelta(minutes = int(comment_date.split('m')[0]))
        comment_date = '{}-{}-{}'.format(x.year,x.month,x.day)
    elif comment_date.find('h') != -1:
        x = now - timedelta(hours = int(comment_date.split('h')[0]))
        comment_date = '{}-{}-{}'.format(x.year,x.month,x.day)
    elif comment_date.find('d') != -1:
        x = now - timedelta(days = int(comment_date.split('d')[0]))
        comment_date = '{}-{}-{}'.format(x.year,x.month,x.day)
    elif comment_date.find('w') != -1:
        x = now - timedelta(weeks = int(comment_date.split('w')[0]))
        comment_date = '{}-{}-{}'.format(x.year,x.month,x.day)
    elif (len(comment_date)==4) | (len(comment_date)==5) :
        x = comment_date.split('-')
        comment_date = '{}-{}-{}'.format(now.year,'0'+x[0] if len(x[0]) == 1 else x[0], x[1])    
    else: 
        comment_date = date
    return comment_date

df['posted_date'] = df['posted_date'].apply(lambda x: comment_posted_date(x))
