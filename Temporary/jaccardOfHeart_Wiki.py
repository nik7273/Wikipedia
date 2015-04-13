# -*- coding: utf-8 -*-

#GET JACCARD SIMILARITY OF ALL HEART RELATED ARTICLES ON WIKIPEDIA (BETWEEN THEMSELVES)

from jaccard import jaccard
import wikipedia, codecs, nltk
from findRelevantArticles import findRelevantArticles
from pprint import pprint
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import subprocess as sub #Running BASH script within python???
import matplotlib.pyplot as plt
import numpy as np

lemma = nltk.WordNetLemmatizer()
relArticles = findRelevantArticles("Heart Attack")
articlefilelist = []

for article in relArticles:
    articlefilename = "content_"+str(article)+".txt"
    with codecs.open(articlefilename,'wb', 'utf-8') as outfile:
        content = wikipedia.page(article).content
        content = [lemma.lemmatize(word) for word in content]
        content = list(set(content))
        for word in content:
            print>>outfile,word
    articlefilelist.append(articlefilename)
    
jaccardVal = []
filenamelistx= []
filenamelisty= []
#GETTING JACCARD AND SAVING TO LISTS DONE IN THE SLOWER WAY
wordslist = ['STEMI_words','NSTEMI_words','WIKI_words']
for articlefilename in articlefilelist:
    filenamelistx.append(articlefilename)
    filenamelisty.append(articlefilename)
    inCompare = [jaccard(articlefilename, otherarticle) for otherarticle in articlefilelist]
    for val in inCompare:
        jaccardVal.append(val)
    jaccardVal.append(jaccard(articlefilename, "STEMI_words"))
    jaccardVal.append(jaccard(articlefilename, "NSTEMI_words"))
    jaccardVal.append(jaccard(articlefilename, "WIKI_words"))

for words in wordslist:
    filenamelistx.append(words)
    filenamelisty.append(words)
    compare = [jaccard(words,otherwords) for otherwords in wordslist]
    for wordval in compare:
       jaccardVal.append(wordval)
       
#PLOTTING INTO HEATMAP USING MATPLOTLIB
fig, ax = plt.subplots()
heatmap = ax.pcolor(jaccardVal, cmap=plt.cm.Blues)
# put the major ticks at the middle of each cell
ax.set_xticks(jaccardVal, minor=False)
ax.set_yticks(jaccardVal, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(filenamelistx, minor=False)
ax.set_yticklabels(filenamelisty, minor=False)
plt.show()
