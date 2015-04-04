# -*- coding: utf-8 -*-

#GET JACCARD SIMILARITY OF ALL HEART RELATED ARTICLES ON WIKIPEDIA (BETWEEN THEMSELVES)

from jaccard import jaccard
import wikipedia, codecs
from findRelevantArticles import findRelevantArticles
from pprint import pprint

relArticles = findRelevantArticles()
articlefilelist = []
for article in relArticles:
    articlefilename = "content_"+str(article)+".txt"
    with open(articlefilename,'wb') as outfile:
        print>>outfile,article.content
    articlefilelist += articlefilename
jaccard(article, #INSERT SECOND ARTICLE HERE, TO BE TAKEN FROM FILELIST FROM FOR LOOP)

#WILL UPDATE TOMORROW WITH COMPLETED CODE




#######NOTES##########
#Lines in findRelevantArticles that save content to file ARE NOT accounted for here, this file is slower than should be because of this. It resaves everything to new files. 
#hence, an improvement would be going through the file that all article content is saved to, and just using that content to implement jaccard. However, this would then involve rewriting Jaccard
#since it uses files as parameters


#PLAN
#use for loop to go through articles in list
#jaccard them
#Then compare to NSTEMI and STEMI 