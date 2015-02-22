# -*- coding: utf-8 -*-

jaccardset1 = []
with open('../Temporary/raw-text-files/sanitizted','rb') as infile1:
    for word in infile1.read():
        jaccardset1 += word
jaccardset2 = []
with open('../Temporary/raw-text-files/sanitized2','rb') as infile1:
    for word in infile1.read():
        jaccardset2 += word
jaccardset3 = []
with open('../Temporary/raw-text-files/sanitized3','rb') as infile1:
    for word in infile1.read():
        jaccardset3 += word



jaccard = float(len(set(jaccardset1)&set(jaccardset2))/len(set(jaccardset1)|set(jaccardset2)))
jaccard2 = float(len(set(jaccardset2)&set(jaccardset3))/len(set(jaccardset2)|set(jaccardset3)))
jaccard3 = float(len(set(jaccardset1)&set(jaccardset3))/len(set(jaccardset1)|set(jaccardset3)))

print jaccard
print jaccard2
print jaccard3