# -*- coding: utf-8 -*-
from plotSave import plot_and_save
from listFreqs import fromPDFtoText, getAndListFreqs

plot_and_save(getAndListFreqs(fromPDFtoText("../Harrison's/STEMI.pdf","STEMITxtFromPDF.txt"), 'STEMI_words', 'listedSTEMIData.txt')["freqs"], getAndListFreqs(fromPDFtoText("../Harrison's/STEMI.pdf","STEMITxtFromPDF.txt"), 'STEMI_words', 'listedSTEMIData.txt')["words"], "Word Count", "Harrisons-STEMI-word-frequencies.png")

