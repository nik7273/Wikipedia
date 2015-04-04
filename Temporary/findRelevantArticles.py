# -*- coding: utf-8 -*-
#Search Wikipedia for Heart Attack
import wikipedia, codecs, itertools, os, time
from awesome_print import ap 
from pprint import pprint

relevant_categories = {'medical','emergencies','disease'}

def findRelevantArticles(term):
    articles = wikipedia.search(term) #Setting suggestion = False (default value); No clear use for it now
    filename = '%s.txt'%term
    if os.path.isfile(filename):
        filename += time.strftime("%Y%m%d-%H%M%S")

    with codecs.open(filename, 'a+', 'utf-8') as outfile:
        for article in articles:
            try: 
                article = wikipedia.page(article)
                category_keywords = set(list(itertools.chain.from_iterable([category.lower().split() for category in article.categories])))
                if len(category_keywords & relevant_categories) > 0:
                    print>>outfile,article.content
            except wikipedia.exceptions.PageError as e:
                #pprint(e)
                pass #Why print errors I do nothing with?
            except wikipedia.exceptions.DisambiguationError as e:
                for article in e.options:
                    article = wikipedia.page(article)
                    category_keywords = set(list(itertools.chain.from_iterable([category.lower().split() for category in article.categories])))
                    if len(category_keywords & relevant_categories) > 0:
                        print>>outfile,article.content

findRelevantArticles("Heart Attack")