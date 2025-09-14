from comment import getComment
from sentiment import sentimentAnalysis
from abhayWordcloud import cloud


def backend(a):
    # a=input("Input YouTube video link here for sentiment analysis:")

    # get array q
    comments = getComment(a)
    result = []
    # print(comments)
    # the sentimentAnalysis works fro only one string at a time so be careful to
    for i in comments:
        print(i)
        # result will save a tuple inside an list with(neg,0.7) for example
        result.append(sentimentAnalysis(i))
        print('Sentiment Analysis:', sentimentAnalysis(i))
    cloud(result, comments)
    # cloud(comments)
