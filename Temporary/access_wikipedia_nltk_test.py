import nltk, matplotlib, numpy, pylab
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

stop = stopwords.words('english')
filename = '../data.txt'
READ = 'rb'
WRITE = 'wb'
stemmer = PorterStemmer()
punkt = set(string.punctuation)
data = [word.lower() for word in word_tokenize(open(filename,READ).read()) if word not in punkt]
data = [stemmer.stem(word) for word in data]
data = [word for word in data if word not in stop]   
with open('sanitizted',WRITE) as outfile:
    for word in data:
        print>>outfile,word
     
'''
    plain = open('data.txt', 'r')  
    This command opens a filestream. It doesn't assign to plain the content of DATA.TXT
'''

'''
   #over here I read about tokenizing with nltk.tokenize.word_tokenize(), but I kept getting other errors with packages
   There are many ways to tokenize a string into components. Line 5 uses a very simple 
   method, assuming that spaces are the only thing that separates tokens and that spaces
   are only used to separate tokens. 

   word_tokenize uses regular expressions to account for cases when characters or groups
   of characters whitespace separate tokens. 

   sent_tokenize does the same thing for sentences. The analogous method to 'split()' 
   would be 'split('.')'. A space is the most common character separating words. A 
   period is the most common character separating sentences. Variants of sent_tokenize
   can be useful when analyzing text from social media. Users of social media rarely
   follow grammar conventions. 

'''


distri1 = nltk.FreqDist(open('sanitizted',READ).read().splitlines())
'''
    
     The constructor for FreqDist prefers an enumerable. If you instantiate FreqDist
     without an enumerable, then you must update the instantiation with an enumerable
     before calling any of that instance's methods.   
 
     It is more efficient and makes for more concise and cogent code if you instantiate
     FreqDist with an enumerable. There is no need for a nested for-loop.

for sentence in nltk.tokenize.sent_tokenize(plain):
    for word in nltk.tokenize.word_tokenize(sentence):
        distri1.inc(word)


    --> Given what I wrote above, modify the instantiation of FreqDist so that the 
    following call works.
'''
common = distri1.most_common(50)
words,freqs = zip(*common)
print freqs
xrange(len(words))
'''
     # Remember our discussion of the 'with' idiom in Python
'''
print common

"The next portion doesn't work because of error: could not convert string to float: '(most frequent word) ' "
color1 = (0/255., 0/255., 0/255.)
pylab.plot(freqs, color=color1, lw=3, ls="--")
pylab.title("Top Frequencies of Words in the Wikipedia Article on Heart Attack", fontsize="16", family='eurostile', color=color1, style='oblique')
pylab.ylim(10,150)
pylab.xlabel('Words', family='eurostile',fontsize="14", color=color1)
pylab.ylabel('Word Count', family='eurostile',fontsize="14", rotation=45, color=color1)
axis = pylab.subplot(111)
axis.spines["right"].set_visible(False)
axis.spines["top"].set_visible(False)
axis.spines["left"].set_visible(True)
axis.spines["bottom"].set_visible(True)
axis.set_yscale('log', nonposy='clip')
pylab.xticks(xrange(len(words)), words, rotation = 90, fontsize="12", family='eurostile', color=color1)
pylab.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="on", right="off", labelleft="on")
pylab.tight_layout()
pylab.show()
pylab.savefig("wikipedia-word-frequencies.png", bbox_inches="tight")  