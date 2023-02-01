
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import plotly.express as px
import malaya
import glob
import sys

keyword = sys.argv[1]

l = []
for name in glob.glob('C:\\Users\\Analyst07\\Documents\\Selenium\\{}\\{}*'.format(keyword,keyword.split('_')[1])):
    df_temp = pd.read_csv(name)
    l.append(df_temp)
    df = pd.concat(l)

# df1 = pd.read_csv(r'C:\Users\Analyst07\Documents\Selenium\nurul izzah\nurul izzah_@jason.yew_(13h ago )_(7194059149716507930).csv')
# df2 = pd.read_csv(r'C:\Users\Analyst07\Documents\Selenium\nurul izzah\nurul izzah_@thaqibshaker_(14h ago )_(7194042940719664411).csv')
# df = pd.concat([df1,df2])

words = ''
for text in df['comment']:
    words = words + ' ' + text
words = words.lower()

model = malaya.sentiment.multinomial()

df['sentiment'] = model.predict(list(df.comment))

df.to_csv('C:\\Users\\Analyst07\\Documents\\Selenium\\{}\\sentiment.csv'.format(keyword), index = False)