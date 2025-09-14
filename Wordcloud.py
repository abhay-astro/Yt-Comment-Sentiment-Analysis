import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets

import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

from subprocess import check_output


def cloud(result,comments):
    sentiment=[]
    for tuple in result:
        sentiment.append(tuple[0])

    dataDict={'text':comments,'sentiment':sentiment}
    data = pd.DataFrame(data=dataDict)
    # data = pd.read_csv('Sentiment.csv')
    # Keeping only the neccessary columns
    # data = data[['text','sentiment']]
# my end goal is to get a data array in pandas suhc as this
    # Splitting the dataset into train and test set
    train, test = train_test_split(data,test_size = 0.1)
    # Removing neutral sentiments
    train = train[train.sentiment != "Neutral"]


    train_pos = train[ train['sentiment'] == 'pos']
    train_pos = train_pos['text']
    train_neg = train[ train['sentiment'] == 'neg']
    train_neg = train_neg['text']

    def wordcloud_draw(data, color = 'black'):
        words = ' '.join(data)
        cleaned_word = " ".join([word for word in words.split()
                                if 'http' not in word
                                    and not word.startswith('@')
                                    and not word.startswith('#')
                                    and word != 'RT'
                                ])
        wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color=color,
                          width=2500,
                          height=2000
                         ).generate(cleaned_word)
        plt.figure(1,figsize=(13, 13))
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()
        
    # print("Positive words")
    wordcloud_draw(train_pos,'white')

