# -*- coding: utf-8 -*-

from plotSave import plot_and_save
from listFreqs import fromPDFtoText, getAndListFreqs

plot_and_save(getAndListFreqs(fromPDFtoText("../Harrison's/NSTEMI.pdf","NSTEMITxtFromPDF.txt"), 'NSTEMI_words', 'listedNSTEMIData.txt')["freqs"], getAndListFreqs(fromPDFtoText("../Harrison's/NSTEMI.pdf","NSTEMITxtFromPDF.txt"), 'NSTEMI_words', 'listedNSTEMIData.txt')["words"], "Word Count", "Harrisons-NSTEMI-word-frequencies.png")

