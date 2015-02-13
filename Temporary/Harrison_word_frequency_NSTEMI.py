# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 20:10:46 2015

@author: Nik
"""
import nltk, matplotlib, numpy, pylab, string, codecs, pyPdf

import matplotlib.pyplot as plt 
import Graphics as artist

"from nltk.stem.porter import *"
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop = stopwords.words('english')
READ = 'rb'
WRITE = 'wb'
lemma = nltk.WordNetLemmatizer()
punkt = set(string.punctuation)
filename2 = "../Harrison's/NSTEMI.pdf"
pdf = pyPdf.PdfFileReader(codecs.open(filename2,READ,'latin-1'))
HarrTxt = "HarrisonTxtFromPDF.txt"
with codecs.open(HarrTxt,WRITE,'utf-8') as outfile:
    for page in pdf.pages:
        print>>outfile,page.extractText()
data2 = [word.lower() for word in word_tokenize(codecs.open(HarrTxt,READ,'utf-8').read()) if word not in punkt]
data2 = [lemma.lemmatize(word) for word in data2]
data2 = [word for word in data2 if word not in stop]
with codecs.open('sanitized2',WRITE,'utf-8') as outfile:
    for word in data2:
        print>>outfile,word
        
distri2 = nltk.FreqDist(codecs.open('sanitized2',READ).read().splitlines())

common2 = distri2.most_common(30)
words2,freqs2 = zip(*common2)
with codecs.open("listedData2.txt",WRITE,'utf-8') as outfile:
    for x,y in common2:
        print>>outfile, "%s %s" % (y, x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.semilogy(freqs2,'k--',linewidth=3)
artist.adjust_spines(ax)

ax.set_xticks(xrange(len(words2)))
ax.set_xticklabels([r'\textbf{\textsc{%s}'%word for word in words2],rotation='vertical')
ax.set_ylabel(artist.format("Word Count"))

plt.tight_layout()
plt.show()
plt.savefig("Harrison's-NSTEMI-word-frequencies.png", bbox_inches="tight")

