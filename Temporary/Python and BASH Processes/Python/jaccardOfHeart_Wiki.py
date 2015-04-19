# -*- coding: utf-8 -*-

#GET JACCARD SIMILARITY OF ALL HEART RELATED ARTICLES ON WIKIPEDIA (BETWEEN THEMSELVES)

from utils import jaccard
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
wordslist = ['C:/Users/Nik/Documents/GitHub/Wikipedia/Temporary/Text and Content/STEMI_words','C:/Users/Nik/Documents/GitHub/Wikipedia/Temporary/Text and Content/NSTEMI_words','C:/Users/Nik/Documents/GitHub/Wikipedia/Temporary/Text and Content/WIKI_words']

for article in relArticles:
    articlefilename = "content_"+str(article)+".txt"
    with codecs.open(articlefilename,'wb', 'utf-8') as outfile:
        content = wikipedia.page(article).content
        content = [lemma.lemmatize(word) for word in content]
        content = list(set(content))
        for word in content:
            print>>outfile,word
    articlefilelist.append(articlefilename)

for piece in wordslist:
    articlefilelist.append(piece)

matrix = np.matrix([[jaccard(i,j) for i in articlefilelist] for j in articlefilelist])
print matrix
with open('jaccardVals', 'wb') as outfile:
    print>>outfile,matrix
    
articlefilelist += wordslist
column_labels = articlefilelist
row_labels = articlefilelist
fig, ax = plt.subplots()
heatmap = ax.pcolor(matrix, cmap=plt.cm.Blues)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(matrix.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(matrix.shape[1])+0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(column_labels, minor=False)
plt.show()