import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import twitter_samples, names
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize

sampleComments = ['Atleast we are getting closer to a more usable phone. I bet by the 5th gen, I would probably buy it',
                  ' MB nails it, his gripes are exactly why I returned my fold3 and went back to my Note20U',
                  ' I think I would be extremely excited about the fold series if it was the same size as my Note while folded.',
                  'golove the intro behind the scenes... makes you appreciate how much work goes into something like this ']
# sentence tokenized and word tokenized
sentPro = []
wordPro = []
a = []
b = []
for i in sampleComments:
    a = sent_tokenize(i)
    b = word_tokenize(i)
    for j in a:
        sentPro = sentPro + a
    wordPro = wordPro + b
# str.isalpha() to include only the words that are made up of letters
# words = [w for w in nltk.corpus.movie_reviews.words() if w.isalpha()]
# words = [w.lower() for w in words ]
# stopwords = nltk.corpus.stopwords.words("english")
# words = [w for w in words if w.lower() not in stopwords]
sia = SentimentIntensityAnalyzer()
scores = [
    sia.polarity_scores(sentence)["compound"]
    for sentence in sentPro
]
print(scores)
unwanted = nltk.corpus.stopwords.words("english")
unwanted.extend([w.lower() for w in nltk.corpus.names.words()])

# positive_bigram_finder = nltk.collocations.BigramCollocationFinder.from_words([
# w for w in wordPro# (categories=["pos"])
# if w.isalpha() and w not in unwanted
# ]
# print(positive_bigram_finder)
# fd = nltk.FreqDist(words)
