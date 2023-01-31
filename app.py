import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

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


df = pd.read_csv('./nurul izzah/sentiment.csv')

col1, col2= st.columns(2)
video_posted_date = col1.multiselect('Video posted date', df['video_posted_date'].sort_values( ascending = False).unique(),
df['video_posted_date'].sort_values( ascending = True).unique(), key = 1 )
# sentiment = col2.multiselect('Sentiment', df['sentiment'].unique(),df['sentiment'].unique(), key =2 )

df = df[df['video_posted_date'].isin(video_posted_date) ]


stopwords = pd.read_csv('stopwords-ms.csv')
mask = np.array(Image.open('tiktok.jpg'))
# image = Image.open(r"C:\Users\Analyst07\Documents\Selenium\tiktok.jpg")
# st.image(image)
stop = []
for text in stopwords.stopwords:
    stop.append(text)

words = ''
for text in df['comment']:
    words = words + ' ' + text
words = words.lower()

# model = malaya.sentiment.multinomial()

df = df[['sentiment', 'comment', 'username', 'nickname', 'likes', 'noOfRepliedComments', 'posted_date',	'extracted_date', 'video_link',
	'video_likes', 'video_comments', 'video_shared', 'video_posted_date']]

st.write("\n \n \n")
df = df.sort_values(by = ['likes'], ascending = False)
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
col = st.columns(4)
keyword = col[0].text_input("Search keyword")

df1 = df[df['comment'].apply(lambda x: str(x).lower().find(keyword)) != -1]

st.write(df1)

st.download_button(
  label="Download data as CSV",
  data=convert_df_to_csv(df1),
  file_name='test_{}.csv'.format(keyword),
  mime='text/csv',
)
