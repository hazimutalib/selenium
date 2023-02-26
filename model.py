
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
files = glob.glob('C:\\Users\\Analyst07\\Documents\\Selenium\\{}\\{}*'.format(keyword,keyword.split('_')[1]))
print(files)
for name in files:
    print(name)
    df_temp = pd.read_csv(name)
    l.append(df_temp)
    df = pd.concat(l)


model = malaya.sentiment.multinomial()

df['sentiment'] = model.predict(list(df.comment))

df.to_csv('C:\\Users\\Analyst07\\Documents\\Selenium\\{}\\sentiment.csv'.format(keyword), index = False)