# -*- coding: utf-8 -*-
"""-------------------OLD CODE----------------------------------"""

import json, requests, sys, codecs, nltk

from HTMLParser import HTMLParser

#function to strip html tags: taken from http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# Checks title for spacing so that the space can be replaced with an underscore in the parameters for the URL. sys.argv[1] 
# is used so PATH variable isn't put into parameters for URL
title = sys.argv[1]

x = title.replace(" ", "_") if " " in title else title
    
#Parameters to be passed into the url
parameters = {'format' : 'json', 'action' : 'query', 'titles' : x, 'prop' : 'extracts', 'rvprop' : 'content', 'continue' : '', "exsectionformat" : "plain", "redirects" : ""}

#getting the content of the url
r = requests.get('http://en.wikipedia.org/w/api.php', params=parameters)

#turning that content into json and loading it
data = r.json()
#writing json content to file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

#writing plaintext to file
with codecs.open('data.txt', 'w', 'utf-8') as file2:
    ids = data['query']['pages'].keys()
    text = ' '.join([data['query']['pages'][idx]['extract'] for idx in ids])
    text = strip_tags(text)
    file2.write(text) 
"""------------------OLD CODE-------------------------"""

"""----------------------NEW TEST CODE-------------------------"""

plain = open('data.txt', 'r')
#over here I read about tokenizing with nltk.tokenize.word_tokenize(), but I kept getting other errors with packages
distri1 = nltk.FreqDist()
for sentence in nltk.tokenize.sent_tokenize(plain):
    for word in nltk.tokenize.word_tokenize(sentence):
        distri1.inc(word)
common = distri1.most_common(50)
plain.close()
print common

"""------------------------NEW TEST CODE--------------------------"""