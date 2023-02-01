import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import glob
from datetime import date

@st.cache
def convert_df_to_csv(df):
  # IMPORTANT: Cache the conversion to prevent computation on every rerun
  return df.to_csv().encode('utf-8')


st.set_page_config(layout="wide")

st.markdown(""" 
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open Sans">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <style>
  h1,h2,h3,h4,h5,h6 {font-family: "Oswald"}
  </style>
  """, unsafe_allow_html=True,)

st.write(""" # TikTok Sentiment Analysis""")

column= st.columns([2, 2, 2, 6])
keywords = glob.glob('keyword*')
keyword = column[0].selectbox('Choose keyword: ', [x.split('_')[1] for x in keywords])



df = pd.read_csv('./{}/sentiment.csv'.format(keywords[[x.split('_')[1] for x in keywords].index(keyword)]))

st.write("##### Data scraped from {} videos as of {} and based on keyword: {}".format(len(df.video_link.unique()), keywords[[x.split('_')[1] for x in keywords].index(keyword)].split('_')[2][1:-1], keyword)) 

df['video_posted_date'] = pd.to_datetime(df['video_posted_date']).dt.date

video_date_posted = column[1].date_input('Date of the videos being posted:', value = (min(df['video_posted_date']), max(df['video_posted_date'])),key=1)
try:
    df = df[(df['video_posted_date']>= video_date_posted[0]) & (df['video_posted_date']<= video_date_posted[1])]
except:
    st.write('Please select range of date')

mask = np.array(Image.open('tiktok.jpg'))
# image = Image.open(r"C:\Users\Analyst07\Documents\Selenium\tiktok.jpg")
# st.image(image)
stop = ['tu', 'dia', 'nak', 'yg' , 'la', 'dah', 'nk', 'ni', 'je', 'di', 'ko', 'ok', 'ini', 'pun' , 'dgn', 'utk', 'kat', 'kt', 'aku', 'kau', 'kita'
        'kan', 'lg', 'dlm', 'pon', 'tau', 'jer', 'itu', 'dan', 'saya', 'sy', 'sbb', 'nya']


df = df[['sentiment', 'comment', 'username', 'nickname', 'likes', 'noOfRepliedComments', 'posted_date',	'extracted_date', 'video_link',
	'video_likes', 'video_comments', 'video_shared', 'video_posted_date']]

st.write("\n \n \n")
df = df.sort_values(by = ['likes'], ascending = False).reset_index(drop = True)

subkeyword = column[2].text_input("Search sub-keyword")
df = df[df['comment'].apply(lambda x: str(x).lower().find(subkeyword.lower())) != -1].reset_index(drop = True)
st.write(df)


st.download_button(
  label="Download data as CSV",
  data=convert_df_to_csv(df),
  file_name='sentiment.csv',
  mime='text/csv',
)

st.write("\n")
st.write("\n")
st.write("\n")
st.write("##### Based on {} comments:".format(len(df))) 

# p1 =  ax[1].bar(np.arange(3),pd.DataFrame(pd.DataFrame(model.predict(list(df.comment)))[0].value_counts())[0],color = ['#f02800', '#1f0cf0', '#0cf0f0'])
# ax[1].bar_label(p1)
# ax[1].set_xticks(np.arange(3))
# ax[1].set_xticklabels(labels=pd.DataFrame(pd.DataFrame(model.predict(list(df.comment)))[0].value_counts())[0].index)
# ax[1].yaxis.set_visible(False)
# ax[1].spines['right'].set_visible(False)
# ax[1].spines['left'].set_visible(False)
# ax[1].spines['top'].set_visible(False)
# ax[1].set_title(label = 'Sentiment', loc = 'left',pad = pad, fontsize = 6)

x1, padding, x2 = st.columns([6,3,9])

words = ''
for text in df['comment']:
    words = words + ' ' + text
words = words.lower()

wordcloud = WordCloud(stopwords = stop, max_font_size=50, max_words=100, background_color="white",mask = mask).generate(words)
fig1, ax1 = plt.subplots()
ax1.imshow(wordcloud, interpolation="bilinear")
ax1.axis('off')
ax1.get_xaxis().set_visible(False)
x1.write('### Wordcloud \n \n') 
x1.write('\n')
x1.pyplot(fig1)


sizes =  pd.DataFrame(df['sentiment'].value_counts())['sentiment']
fig2, ax2 = plt.subplots()
donut, text = ax2.pie(sizes, colors=['#f02800', '#1f0cf0', '#0cf0f0'],startangle=90, frame=True,
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

st.write('\n')
st.write('\n')


# col = st.columns(4)
# subkeyword = col[0].text_input("Search keyword")



# st.write(df1)

# st.download_button(
#   label="Download data as CSV",
#   data=convert_df_to_csv(df1),
#   file_name='test_{}.csv'.format(keyword),
#   mime='text/csv',
# )
