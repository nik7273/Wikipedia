# -*- coding: utf-8 -*-
from plotSave import plot_and_save
from listFreqs import fromPDFtoText, getAndListFreqs

plot_and_save(getAndListFreqs(fromPDFtoText("../data.txt","anything.txt"), 'WIKI_words', 'listedWikiData.txt')["freqs"], getAndListFreqs(fromPDFtoText("../data.txt","anything.txt"), 'WIKI_words', 'listedWikiData.txt')["words"], "Word Count", "wikipedia-word-frequencies.png")

