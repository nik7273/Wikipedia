# -*- coding: utf-8 -*-

from plotSave import plot_and_save
from listFreqs import fromPDFtoText, getAndListFreqs
NSTEMItext = fromPDFtoText("../Harrison's/NSTEMI.pdf","HarrisonTxtFromPDF.txt")
wordss,freqss = getAndListFreqs(NSTEMItext, 'NSTEMI_words', 'listedData2.txt')
plot_and_save(freqss, wordss, "Word Count", "Harrisons-NSTEMI-word-frequencies.png")

