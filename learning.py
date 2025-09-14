import nltk
import numpy
from nltk.classify.scikitlearn import SklearnClassifier
from statistics import mode
import random
from nltk.corpus import movie_reviews,stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn import preprocessing
#looks like ClassifierI is iported just fine what is the issue then?
from nltk.classify import ClassifierI
from statistics import mode

class voteClassifier (ClassifierI):
    def __init__(self,*Classifier):
       self._classifiers=Classifier 

       def classify(self,training):
        votes=[]
        for c in self._classifiers:
            v=c.self.classify(training)
            votes.append(v)
        return mode(votes)

    def confidence(self,features):
        votes=[]
        for c in self._classifiers :
            v=c.nltk.classify(features)
            votes.append()
        choiceVotes=votes.count(mode(votes))
        conf=choiceVotes/len(votes)
        return conf
#movie reviews to get example posiitive and negative 
# get a better list next time
# maybe replace this with the opinion lexicon
documents=[]
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids():
        documents.append((list(movie_reviews.words(fileid)), category))

#shuffling to reduce bias
random.shuffle(documents)
#unprocessed comments from mkbhd channel on a product
# sampleComments=['Holy cow that intro was smooth', 'Funny how now phones are recognised by their back not front', 'I always love his entrance. It’s like the highest quality and best intros in YouTube.', 
                # 'The voice of this guy man... so relaxing', "Holy shit the production value of your videos are crazy. Half the time I'm not interested in anything but the  cinematography, even as more of a photo guy. Really damn impressive what you and your team manage to do", 'Pretty much every MKBHD intro: how did he do that?', 
                # 'Out of context Marques quotes: “I- I could kill it in a day, if I’m hammering it all day…” 8:32', "So glad I found you! Simplified and didn't feel like an idiot when done with the video. Very helpful!", 
                # "I just picked up the Samsung S21+ on Thursday, my provider was having a really really good deal. It's my first Samsung in about seven years, and wow Samsung really has really upped their game since my last one. I'm really loving this phone so far.", 
                # 'I really like your reviews because they’re more informational than opinion based', "After seeing that intro I'm literally gonna just delete my whole YouTube channel.", 
                # 'Thank you for such a concise review. You checked the perfect amount of both objective and subjective boxes for my viewing appeal! Now, I can make an informed decision. 👏🏽', 
                # 'Thanks so much for you reviews Marcus,  your so thorough and honest,  you always help me make the best decision . I got the s21 to save money , the battery life blows me away .', 
                # "And to think if it weren't for that Youtube Rewind mention by Will Smith I would have never learn you existed. Great vid. I just bought this.", 
                # "I remember the days when after a couple of years you could upgrade to the new model and it would be so different and exciting. Now it's meh. Innovation has packed up and gone home. \nAt the end of my contract I'm just going to hang on to my S10 and get a sim card and save a fortune.", 
                # 'Marques: "Now they could\'ve used a snapdragon 700 series processor"\nMe: Don\'t give them ideas Marques', 'I really love your review, your approach goes right at the central issues, very clear, very clever, also your speach has a very good speed, not too quickly, not too slow.', "I swear there is something in his voice  that makes me watch his videos does'nt matter how long they are",
                # "If this is the standard for review videos in the future.....I'm excited. Fresh, informative, beautiful, and and easy listen. Covered all the bases. I'm buying my purple S21!", 'Just ordered the S21 Plus so would love to see a review of that model, especially compared to the others in the S21 line :)', 
                # "Congrats guys we're living now in an age where 6.2inches is considered small 🙃", 'Amazing review Marq. From the intro to just about erveything!', 
                # 'Camera movement around the 1:00 mark is phenomenal. Subtle and very much appreciated. Bravo.', 'your videos are so chill its such a huge difference between ltt I can feel my brain tingling', 
                # 'Watched Many Times Still....\nInsanely Awesome Intro! \nBOOM!!!! Mind Blown! 🤯', "The intros just don't stop getting better!", 'Love the heavy technical explanations in your videos. Very esthetically pleasing too, well done!', 'I just love how samsung pulled itself out of China and launch this', 
                # 'I recently picked up this phone under a new plan. Just waiting on it to arrive.  I initially thought about going with the s20 fe but after watching this review it puts me so much at ease that i went with the S21 instead.  Thank you so much.', 
                # "Thanks for your video! It's the reason I went over to the dark side and brought my Samsung s21 with 256GB! A major upgrade from my iPhone 7 with 32GB 🤣", 
                # "The visuals are getting insanely great! Like how the colors blended and supported the phone's main colors. Keep up the good work!", "After a bunch of research, I got the S21 base model last weekend. I didn't need the silly zoom on the Ultra. The S21 has a really amazing camera!  I just used it to make pictures and videos in a factory. Shots ranged from tiny details in a dim mezzanine to broad areas with tall bright ceilings.  Everything about the camera is great. The 0.5 zoom gives a crazy wide shot. The pro modes give absolute control over ISO, aperture, color temp shift, focus, zoom, and more. I was able to balance every shot on the spot, dramatically reducing post processing effort. I'm really pleased with my purchase.",
                # "I still come back to watch this video, it is that good, one of the best reviews MKBHD's ever made", 
                # "I got the S21+ through Samsung's trade in program. I have to say I miss the MST since some of the vending machines at work don't have NFC, but eh, everything else does. Everything else is good. Upgrading from the S10e the screen is massive though, took me a little to get used to.", 'Ahhh this was pleasant to listen and see👌🏾👌🏾']

#processing the comments
stopWords=set(stopwords.words('english'))
wordPro=[]
b=[]
#for testing i am using the corpus right now 
#we need wordPro for making the feature set
# for i in sampleComments:
    # if i.lower() not in stopWords:
        # b=word_tokenize(i.lower())
        # wordPro=wordPro+b
# wordPro=[word.lower() for word in wordPro if word.isalpha()]
# fd=nltk.FreqDist(wordPro)

for w in movie_reviews.words():
    wordPro.append(w.lower())

#saved as a dictionary with the most number of words
wordPro= nltk.FreqDist(wordPro)

#this is going to be used to maek the feature sets
word_features = list(wordPro.keys())[:3000]

#feature set making
#this is making a feature set for the movie corpus in nltk
def findFeatures(documents):
    words=set(documents)
    features={}
    for w in word_features:
        features[w]=(w in words)
    return features

#list of dictionay of true or false
#dicitonary with review and positive or negative category
featureSets=[(findFeatures(rev),category) for (rev,category) in documents ]
training=featureSets[:1900]
# scaler = preprocessing.StandardScaler().fit(training)
testing=featureSets[1900:]

#thisis for training the set and getting classifier
# classifier= nltk.NaiveBayesClassifier.train(training)

#saved classifier already as pickle
nbcClassifier=open('/home/abhishek/Yt-Comment-Sentiment-Analysis/NaiveBayesClassifier','rb')
classifier=pickle.load(nbcClassifier)
nbcClassifier.close()

print('accuracy:',(nltk.classify.accuracy(classifier,testing)))
classifier.show_most_informative_features(15)

#code on how to save classifier as pickle
# saveClassifier=open("NaiveBayesClassifier","wb")
# pickle.dump(classifier,saveClassifier)
# saveClassifier.close()

MultinomialNBClassifier=SklearnClassifier(MultinomialNB())
MultinomialNBClassifier.train(training)
print('accuracy:',(nltk.classify.accuracy(MultinomialNBClassifier,testing)))
# MultinomialNBClassifier.show_most_informative_features(15)

BernoulliNBClassifier=SklearnClassifier(BernoulliNB())
BernoulliNBClassifier.train(training)
print('accuracy:',(nltk.classify.accuracy(BernoulliNBClassifier,testing)))

#these hings dont work for some reason to do with numpy array figure out later
# GaussianNBClassifier=SklearnClassifier(GaussianNB())
# numpyTraining=numpy.array(training)
# GaussianNBClassifier.train(numpyTraining.todense())
# print('accuracy:',(nltk.classify.accuracy(GaussianNBClassifier,testing)))
# GaussianNBClassifier.show_most_informative_features(15)

# LogisticRegressionClassifier=SklearnClassifier(LogisticRegression())
# LogisticRegressionClassifier.train(scaler)
# print('accuracy:',(nltk.classify.accuracy(LogisticRegressionClassifier,testing)))

svcClassifier=SklearnClassifier(SVC())
svcClassifier.train(training)
print('svc accuracy:',(nltk.classify.accuracy(svcClassifier,testing)))

linearsvcClassifier=SklearnClassifier(LinearSVC())
linearsvcClassifier.train(training)
print('linear accuracy:',(nltk.classify.accuracy(linearsvcClassifier,testing)))

#very low accuracy no sense in keeping it in
# nusvcClassifier=SklearnClassifier(NuSVC())
# nusvcClassifier.train(training)
# print('nusvc accuracy:',(nltk.classify.accuracy(nusvcClassifier,testing)))

sgdcClassifier=SklearnClassifier(SGDClassifier())
sgdcClassifier.train(training)
print('sgdc accuracy:',(nltk.classify.accuracy(sgdcClassifier,testing)))

votedClassifier=voteClassifier(nbcClassifier)
                               # MultinomialNBClassifier,
                               # BernoulliNBClassifier,
                               # svcClassifier,linearsvcClassifier,
                               # sgdcClassifier)
print("voted classification accuracy percent",
      (nltk.classify.accuracy(votedClassifier, testing[0][0]))*100)

