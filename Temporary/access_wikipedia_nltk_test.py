import nltk, matplotlib, numpy, pylab, string, codecs

import matplotlib.pyplot as plt 
import Graphics as artist

"from nltk.stem.porter import *"
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop = stopwords.words('english')
filename = '../data.txt'
READ = 'rb'
WRITE = 'wb'
lemma = nltk.WordNetLemmatizer()
punkt = set(string.punctuation)
data = [word.lower() for word in word_tokenize(open(filename,READ).read()) if word not in punkt]
data = [lemma.lemmatize(word) for word in data]
data = [word for word in data if word not in stop]
with open('sanitizted',WRITE) as outfile:
    for word in data:
        print>>outfile,word
      
filename2 = "../Harrison's/NSTEMI.pdf"
data2 = [word.lower() for word in word_tokenize(codecs.open(filename2,READ,'latin-1').read()) if word not in punkt]
data2 = [lemma.lemmatize(word) for word in data2]
data2 = [word for word in data2 if word not in stop]
with codecs.open('sanitized2',WRITE, 'utf-8') as outfile:
    for word in data2:
        print>>outfile,word

distri1 = nltk.FreqDist(open('sanitizted',READ).read().splitlines())
distri2 = nltk.FreqDist(open('sanitized2',READ).read().splitlines())

common = distri1.most_common(30)
common2= distri2.most_common(30)
words,freqs = zip(*common)
words2,freqs2 = zip(*common2)


with codecs.open("listedData.txt",WRITE,'utf-8') as outfile:
    for x,y in common:
        print>>outfile, "%s %s" % (y, x)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.semilogy(freqs,'k--',linewidth=3)
artist.adjust_spines(ax)

ax.set_xticks(xrange(len(words)))
ax.set_xticklabels([r'\textbf{\textsc{%s}'%word for word in words],rotation='vertical')
ax.set_ylabel(artist.format("Word Count"))

plt.tight_layout()
plt.show()
plt.savefig("wikipedia-word-frequencies.png", bbox_inches="tight")
