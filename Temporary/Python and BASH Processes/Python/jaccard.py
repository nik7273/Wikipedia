# -*- coding: utf-8 -*-
import nltk
from nltk.collocations import *
def bigramFinder(FileA):
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    with open(FileA,'rb') as infile:
        finder = BigramCollocationFinder.from_words(nltk.word_tokenize(infile.read()))  
    bigrams = finder.nbest(bigram_measures.pmi, 20)
    return bigrams

print bigramFinder("WIKI_words")
print bigramFinder("NSTEMI_words")
print bigramFinder("STEMI_words")

def jaccard(file1, file2):
    lst1 = set(open(file1,'rb').read().splitlines())
    lst2 = set(open(file2,'rb').read().splitlines())
    return float(len(lst1 & lst2))/len(lst1 | lst2)

jaccard('WIKI_words', 'NSTEMI_words')
jaccard('WIKI_words', 'STEMI_words')
jaccard('NSTEMI_words', 'STEMI_words')

