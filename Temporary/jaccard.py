# -*- coding: utf-8 -*-
import nltk
from nltk.collocations import *
def bigramFinder(FileA):
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    bigString = ""
    with open(FileA,'rb') as infile:
        for line in infile:
            nltk.word_tokenize(line)
            bigString += (line + " ")
    finder = BigramCollocationFinder.from_words(bigString)  
    bigrams = finder.nbest(bigram_measures.pmi, 20)
    print bigrams

bigramFinder("sanitizted")
bigramFinder("sanitized2")
bigramFinder("sanitized3")

def jaccard(file1, file2):
    jaccardset1 = []
    with open(file1,'rb') as infile:
        for word in infile.read().splitlines():
            jaccardset1 += word
    jaccardset2 = []
    with open(file2, 'rb') as infile:
        for word in infile.read().splitlines():
            jaccardset2 += word
    print float(len(set(jaccardset1)&set(jaccardset2))/len(set(jaccardset1)|set(jaccardset2)))
    
jaccard('sanitizted', 'sanitized2')
jaccard('sanitizted', 'sanitized3')
jaccard('sanitized2', 'sanitized3')

