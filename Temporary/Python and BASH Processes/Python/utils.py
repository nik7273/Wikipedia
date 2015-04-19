# -*- coding: utf-8 -*-
#UTILITIES

def jaccard(file1, file2):
    lst1 = set(open(file1,'rb').read().splitlines())
    lst2 = set(open(file2,'rb').read().splitlines())
    return float(len(lst1 & lst2))/len(lst1 | lst2)


