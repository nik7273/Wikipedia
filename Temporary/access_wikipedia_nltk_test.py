# -*- coding: utf-8 -*-
from plotSave import plot_and_save
from listFreqs import fromPDFtoText, getAndListFreqs
WIKItext = fromPDFtoText("../data.txt","anything.txt")
wordss,freqss = getAndListFreqs(WIKItext, 'WIKI_words', 'listedData.txt')
plot_and_save(freqss, wordss, "Word Count", "wikipedia-word-frequencies.png")

