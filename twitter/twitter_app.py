import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import glob
from datetime import date
from twitter_css import kpi_box_css, body_css, tweets_css
from twitter_html import kpi_box_html,  tweets_html


st.set_page_config(layout="wide")
kpi_box_css()
body_css()


@st.cache
def convert_df_to_csv(df):
  # IMPORTANT: Cache the conversion to prevent computation on every rerun
  return df.to_csv().encode('utf-8')

st.write(""" # Twitter Sentiment Analysis""")

column = st.columns([1,1,1])
keywords = glob.glob('keyword*')
keyword = column[0].selectbox('Choose keyword: ', [x.split('_')[1] for x in keywords])

df = pd.read_csv('./{}/data.csv'.format(keywords[[x.split('_')[1] for x in keywords].index(keyword)]))

df = df[df['isAds'] == 'No']
df['datetime']= pd.to_datetime(df['datetime']).dt.date
twitter_datetime = column[1].date_input('Posted date (videos):', value = (min(df['datetime']), max(df['datetime'])),key=1)
try:
    df = df[(df['datetime']>= twitter_datetime[0]) & (df['datetime']<= twitter_datetime[1])]
except:
    st.write('Please select range of date')


df = df.sort_values(by = ['numberOfLikes'], ascending = False).reset_index(drop = True)

subkeyword = column[2].text_input("Search sub-keyword")
df = df[df['tweets'].apply(lambda x: str(x).lower().find(subkeyword.lower())) != -1].reset_index(drop = True)
st.write("##### Data and videos  are scraped as of {} and based on keyword: {}".format(keywords[[x.split('_')[1] for x in keywords].index(keyword)].split('_')[2][1:-1], keyword)) 
total_tweets = len(df.tweets.unique())
total_user = len(df.username.unique())

kpi_box_html(total_tweets, total_tweets, total_user)

def convert_full_figures(x):
  x = ''.join(str(x).split(','))
  if str(x).find('K') != -1:
    x = int(float(str(x)[:-1])*1000)
  elif str(x).find('M') != -1:
    x = int(float(str(x)[:-1])*1000000)
  elif x == 'Share':
    x = 0
  else:
    try:
      x = int(x)
    except:
      x= ''
  return x
df['numberOfLikesOri'] = df['numberOfLikes']
df['numberOfViewsOri'] = df['numberOfViews']
df['numberOfRetweetsOri'] = df['numberOfRetweets']
df['numberOfCommentsOri'] = df['numberOfComments'].apply(lambda x: str(x).split('.')[0] if str(x) != 'nan'  else '')

df['numberOfLikes'] = df.numberOfLikes.apply(lambda x: convert_full_figures(x))
df['numberOfViews'] = df.numberOfViews.apply(lambda x: convert_full_figures(x))
df['numberOfRetweets'] = df.numberOfRetweets.apply(lambda x: convert_full_figures(x))
df['numberOfComments'] = df.numberOfComments.apply(lambda x: convert_full_figures(x))



columns = st.columns([13, 1, 13])
z = columns[0].slider('View comments:', 0, 100, 12)
columns[0].write('###### Top {} comments based on number of likes:'.format(z))
columns = st.columns([13, 1, 13])


x = 0

for a,b,c,d,e,f,g,h,i,j,k,l,m in list(zip(df['avatar'][:z], df['nickname'][:z], df['username'][:z], df['tweets'][:z], 
                              df['img1'][:z], df['img2'][:z], df['img3'][:z], df['img4'][:z], 
                              df['numberOfCommentsOri'][:z], df['numberOfRetweetsOri'][:z], df['numberOfLikesOri'][:z], df['numberOfViewsOri'][:z],  df['img2'][:z])):
  tweets_css(m)
  columns[2*x].markdown(tweets_html(a,b,c,d,e,f,g,h,i,j,k,l),unsafe_allow_html = True)
  x = x + 1
  if x == 2:
    x = 0
    






  