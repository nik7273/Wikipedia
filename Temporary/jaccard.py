# -*- coding: utf-8 -*-
import nltk
from nltk.collocations import *
def bigramFinder(FileA):
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    with open(FileA,'rb') as infile:
        finder = BigramCollocationFinder.from_words(nltk.word_tokenize(infile.read()))  
    bigrams = finder.nbest(bigram_measures.pmi, 20)
    print bigrams

bigramFinder("sanitizted")
bigramFinder("sanitized2")
bigramFinder("sanitized3")

def jaccard(file1, file2):
    jaccardset1 = ""
    with open(file1,'rb') as infile:
        for word in infile:
            jaccardset1 += (word + " ")
    jaccardset2 = ""
    with open(file2, 'rb') as infile:
        for word in infile:
            jaccardset2 += (word + " ")
    set1 = set(jaccardset1.split())
    set2 = set(jaccardset2.split())
    print float(len(set1 & set2))/len(set1 | set2)
    
jaccard('sanitizted', 'sanitized2')
jaccard('sanitizted', 'sanitized3')
jaccard('sanitized2', 'sanitized3')

