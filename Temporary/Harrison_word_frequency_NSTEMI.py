# -*- coding: utf-8 -*-

import nltk, matplotlib, numpy, pylab, string, codecs

import matplotlib.pyplot as plt 
import Graphics as artist
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
"from nltk.stem.porter import *"
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


stop = stopwords.words('english')
READ = 'rb'
WRITE = 'wb'
lemma = nltk.WordNetLemmatizer()
punkt = set(string.punctuation)
filename2 = "../Harrison's/NSTEMI.pdf"
HarrTxt = "HarrisonTxtFromPDF.txt"
HarrTxt2 = "HarrisonTxtFromPDF2.txt"

#the pypdf method didnt work, so i used this instead  : http://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text


def pdfparser(data):

    fp = file(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'latin-1'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue() 
    print>>outfile,data
    
with codecs.open(HarrTxt,WRITE,'utf-8') as outfile:
    pdfparser(filename2)
d={}
with open("abbreviation_reference.txt",READ) as f:
    d = dict(x.split(' ') for x in f)

measures = ['cm', 'in', 'mg', 'lb', 'kg', 'mm', 'ft']
data2 = [word.lower() for word in word_tokenize(codecs.open(HarrTxt,READ,'utf-8').read()) if word not in punkt]
for item in data2:
    if item in d.keys():
        data2[data2.index(item)] = d[item]
        item.replace("_"," ")
        word_tokenize(item)
data2 = [lemma.lemmatize(word) for word in data2]
data2 = [word for word in data2 if word not in stop]
data2 = [word for word in data2 if word not in measures]
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
plt.savefig("Harrisons-NSTEMI-word-frequencies.png", bbox_inches="tight")

