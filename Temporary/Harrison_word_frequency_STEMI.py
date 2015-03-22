# -*- coding: utf-8 -*-
from plotSave import plot_and_save
from listFreqs import fromPDFtoText, getAndListFreqs
STEMItext = fromPDFtoText("../Harrison's/STEMI.pdf","HarrisonTxtFromPDF2.txt")
wordss,freqss = getAndListFreqs(STEMItext, 'STEMI_words', 'listedData3.txt')
plot_and_save(freqss, wordss, "Word Count", "Harrisons-STEMI-word-frequencies.png")

