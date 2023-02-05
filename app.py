import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import glob
from datetime import date
from custom import body_css, kpi_box_css, tiktok_video_css, kpi_box, tiktok_video

st.set_page_config(layout="wide")

body_css()
kpi_box_css()
tiktok_video_css()

@st.cache
def convert_df_to_csv(df):
  # IMPORTANT: Cache the conversion to prevent computation on every rerun
  return df.to_csv().encode('utf-8')

st.write(""" # TikTok Sentiment Analysis""")

column = st.columns([1,1,1])
keywords = glob.glob('keyword*')
keyword = column[0].selectbox('Choose keyword: ', [x.split('_')[1] for x in keywords])

df = pd.read_csv('./{}/sentiment.csv'.format(keywords[[x.split('_')[1] for x in keywords].index(keyword)]))
df['video_posted_date'] = pd.to_datetime(df['video_posted_date']).dt.date
video_date_posted = column[1].date_input('Date of the videos being posted:', value = (min(df['video_posted_date']), max(df['video_posted_date'])),key=1)
try:
    df = df[(df['video_posted_date']>= video_date_posted[0]) & (df['video_posted_date']<= video_date_posted[1])]
except:
    st.write('Please select range of date')

mask = np.array(Image.open('tiktok.jpg'))
stop = ['tu', 'dia', 'nak', 'yg' , 'la', 'dah', 'nk', 'ni', 'je', 'di', 'ko', 'ok', 'ini', 'pun' , 'dgn', 'utk', 'kat', 'kt', 'aku', 'kau', 'kita'
        'kan', 'lg', 'dlm', 'pon', 'tau', 'jer', 'itu', 'dan', 'saya', 'sy', 'sbb', 'nya', 'ke', 'kan', 'tak', 'ada', 'apa',
        'kita', 'lah', 'lagi', 'jgn', 'klu', 'org', 'x', 'blh', 'tp', 'dia', 'mcm', 'dh', 'yang', 'jadi', 'ckp', 'skrg', 'bkn',
        'dpt', 'untuk', 'lain', 'macam', 'mmg', 'kn', 'tk', 'lebih', 'n', 'byk', 'dari', 'hahaha', 'jd', 'akan', 'mana', 'juga',
        'pulak', 'ja', 'pa','die', 'i', 'nie', 'ka', 'atau', 'kami', 'dalam', 'bg', 'tidak', 'bro', 'bila']

df = df.sort_values(by = ['likes'], ascending = False).reset_index(drop = True)

subkeyword = column[2].text_input("Search sub-keyword")
df = df[df['comment'].apply(lambda x: str(x).lower().find(subkeyword.lower())) != -1].reset_index(drop = True)
st.write("##### Data scraped as of {} and based on keyword: {}".format(keywords[[x.split('_')[1] for x in keywords].index(keyword)].split('_')[2][1:-1], keyword)) 
total_videos = len(df.video_link.unique())
total_comments = len(df)
total_user = len(df.username.unique())

st.sidebar.write("#### Scraped videos")
df1 = df.groupby(['video_link', 'video_image_link', 'video_caption', 'video_posted_date', 'video_views','video_likes'])[['video_link', 'video_image_link', 'video_caption', 'video_posted_date', 'video_views','video_likes']].max()
for a,b,c,d,e,f,g in list(zip(list(df1['video_link']),list(df1['video_image_link']), list(df1['video_caption']),list(df1['video_link'].apply(lambda x: x.split('/')[3])) , list(df1['video_posted_date']), list(df1['video_views']),list(df1['video_likes']))):
  tiktok_video(a,b,c,d,e,f,g)

df = df[['sentiment', 'comment', 'username', 'nickname', 'likes', 'noOfRepliedComments', 'posted_date', 'video_link']]

kpi_box(total_videos, total_comments, total_user)

st.write(df)

st.download_button(
  label="Download data as CSV",
  data=convert_df_to_csv(df),
  file_name='sentiment.csv',
  mime='text/csv',
)

st.write("##### Based on {} comments:".format(len(df))) 
x1, padding, x2 = st.columns([6,3,9])

def wordcloud():
  words = ''
  for text in df['comment']:
      words = words + ' ' + text
  words = words.lower()

  wordcloud = WordCloud(stopwords = stop, max_font_size=50, max_words=100, colormap = 'CMRmap', background_color="white",mask = mask).generate(words)
  fig1, ax1 = plt.subplots()
  ax1.imshow(wordcloud, interpolation="bilinear")
  ax1.axis('off')
  ax1.get_xaxis().set_visible(False)
  x1.write('### Wordcloud \n \n') 
  x1.write('\n')
  x1.pyplot(fig1)


def donut_chart():
  sizes =  pd.DataFrame(df['sentiment'].value_counts())['sentiment']
  fig2, ax2 = plt.subplots()
  donut, text = ax2.pie(sizes, colors=['#01213d', '#004e92', '#0cf0f0'],startangle=90, frame=True,
      pctdistance =0.85,counterclock=False, wedgeprops={"edgecolor":"black",'linewidth': 0.5, 'linestyle': 'solid', 'antialiased': True})
  ax2.add_patch(plt.Circle((0, 0), radius=0.6,color='black', linewidth=1))
  ax2.add_patch(plt.Circle((0, 0), radius=0.6,color='white', linewidth=0))
  ax2.yaxis.set_visible(False)
  ax2.xaxis.set_visible(False)
  ax2.spines['right'].set_visible(False)
  ax2.spines['left'].set_visible(False)
  ax2.spines['top'].set_visible(False)
  ax2.spines['bottom'].set_visible(False)


  recipe = ['negative \n {} ({:.2f}%)'.format(sizes[0],(sizes[0]/sizes.sum())*100), 
              'positive \n {} ({:.2f}%)'.format(sizes[1], (sizes[1]/sizes.sum())*100), 'neutral \n {} ({:.2f}%)'.format(sizes[2], (sizes[2]/sizes.sum())*100),]
  bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.0)
  kw = dict(arrowprops=dict(arrowstyle="<|-", ls = "dashed"),
              bbox=bbox_props, zorder=0, va="center")

  for i, p in enumerate(donut):
      ang = (p.theta2 - p.theta1)/2. + p.theta1
      y = np.sin(np.deg2rad(ang))
      x = np.cos(np.deg2rad(ang))
      horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
      connectionstyle = "angle,angleA=0,angleB={}".format(ang)
      kw["arrowprops"].update({"connectionstyle": connectionstyle})
      ax2.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),horizontalalignment=horizontalalignment, fontsize=8, **kw)
  x2.write('### Sentiment')    
  x2.write('\n')    
  x2.pyplot(fig2)

wordcloud()
donut_chart()