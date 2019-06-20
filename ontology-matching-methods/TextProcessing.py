# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:06:04 2019

@author: Sorina
"""


# =============================================================================
# Basic text processing methods in Python
# =============================================================================

# =============================================================================
#  Traditional NLP pipeline could also help us to improve results of string-based methods. 
#  Before calculating basic string similarity between two elements process
#  them with this methods:
# 
# 1.Tokenization
#   a.Splitting into tokens
#   b.Stopwords removal
# 2.Lemmatization
#  a.Morphological analysis
#  b.Part-of-speech tagging
# 
# NLTK  is a great Python library that could do this job for us.
# =============================================================================

# -*- coding: utf-8 -*-
import re
import nltk
nltk.download('punkt')
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
nltk.download('stopwords')
import wordcloud


#Load the data -- test purpose only, first!!!
textReview = " location1 location2 in  the loccations..!!"


#Number of words
print ("no of words:", len(str(textReview).split(" "))) 

#Stopwords 
stopReplace = stopwords.words('english')
#print (stopwords.words()[620:680])

#print ("stopwords: ", len([x for x in textReview.split() if x in stopReplace])) 
#print("digits: ", len([x for x in textReview.split() if x.isdigit()])) 
#print("upper: ", len([x for x in textReview.split() if x.isupper()])) 

#Clean data
#remove punctuation 
textR = re.sub(r'[^\w\s]', '', textReview)
print("without punctuation:", textR)

#Remove Numbers 
textR =  re.sub(r'[\d]', '', textR)
print("without digits: ", textR)

#lower case 
textR = " ".join(x.lower() for x in textR.split())
print("lower-case: ", textR)
#print(len(textR))

#remove stop-words 
textR = " ".join(x for x in textR.split() if x not in stopReplace)
print("without stopwords: ", textR)

#tokenization - divide the text into a sequence of words or sentences
tokensR = nltk.word_tokenize(textR)
print("tokens: ", tokensR)


#Stemming or Lemmatization
#Stemming - the removal of suffices, like “ing”, “ly”, “s”, etc. 
porter = nltk.PorterStemmer()
stemsR = [porter.stem(t) for t in tokensR]
print("stems: ", stemsR)

#Lemmatization - it converts the word into its root word. It makes use of the vocabulary and does a
#morphological analysis to obtain the root word. 
nltk.download('wordnet')
wnl = nltk.WordNetLemmatizer()
lemR = [wnl.lemmatize(t) for t in tokensR]
print("lemmas: ", lemR)

# =============================================================================
# #frequent words
# fw = nltk.FreqDist(lemR)
# fw.plot(20)
# 
# #Generate word cloud
# wordCloudR2 = wordcloud.WordCloud().generate_from_frequencies(fw)
# plt.imshow(wordCloudR2)
# # Turn off the axis
# plt.axis("off")
# # Show the word cloud
# plt.show()
# =============================================================================
