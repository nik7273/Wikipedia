# -*- coding: utf-8 -*-

#Search Wikipedia for Heart Attack

import wikipedia, codecs
#Generates list of search suggestions
articleList = wikipedia.search("Heart Attack", results = 10, suggestion = True)
#Declares list for "page" objects (with 'content' property)
objectList = []
for suggestion in articleList[0]:
    #Gets rid of suggestion element with disambiguation in name (No proper content label for this page), adds page object to the list
    articleList[0].pop(articleList[0].index(suggestion)) if "disambiguation" in suggestion else objectList.append(wikipedia.page(title = str(suggestion), auto_suggest = True, redirect = True, preload = False))
#Prints text of each of the articles in articleList to the file "HeartText.txt"
with codecs.open("HeartText.txt", 'wb', 'utf-8') as outfile:
    for article in objectList:
        print>>outfile,article.content
        
        
#List of relevant articles pertaining to the subject
#Adds relevant articles to list based on their matching ontology (categories)
relevant = []
for article in objectList:
    categories = article.categories
    for category in categories:
        for stdcategory in wikipedia.page(title = "Heart", auto_suggest = True, redirect = True, preload = False).categories:
            if category == stdcategory:
                if article not in relevant:
                    relevant.append(article)





