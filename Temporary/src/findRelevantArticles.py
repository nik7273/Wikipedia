# -*- coding: utf-8 -*-
#Search Wikipedia for Heart Attack
import wikipedia, codecs, itertools, os, time
from pprint import pprint

relevant_categories = {'medical','emergencies','disease'}

def findRelevantArticles(term):
    articleList = []
    articles = wikipedia.search(term) #Setting suggestion = False (default value); No clear use for it now
    filename = '%s.txt'%term
    if os.path.isfile(filename):
        filename = '%s.txt' % str(term+time.strftime("%Y%m%d-%H%M%S"))

    with codecs.open(filename, 'a+', 'utf-8') as outfile:
        for article in articles:
            try: 
                article = wikipedia.page(article)
                category_keywords = set(list(itertools.chain.from_iterable([category.lower().split() for category in article.categories])))
                if len(category_keywords & relevant_categories) > 0:
                    articlefilename = "content_"+str(article)+".txt"
                    with codecs.open(articlefilename,'wb', 'utf-8') as outfile:
                        content = wikipedia.page(article).content
                        print>>outfile,content
                    articleList.append(str(article.title))
            except wikipedia.exceptions.PageError as e:
                #pprint(e)
                pass #Why print errors I do nothing with?
            except wikipedia.exceptions.DisambiguationError as e:
                for article in e.options:
                    try:
                        article = wikipedia.page(article)
                        category_keywords = set(list(itertools.chain.from_iterable([category.lower().split() for category in article.categories])))
                        if len(category_keywords & relevant_categories) > 0:
                            print>>outfile,article.content
                            articleList.append(str(article.title))
                    except wikipedia.exceptions.DisambiguationError as f:
                        pass
        
    return list(set(articleList))