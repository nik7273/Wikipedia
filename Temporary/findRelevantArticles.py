# -*- coding: utf-8 -*-
#Search Wikipedia for Heart Attack
import wikipedia, codecs, itertools
from awesome_print import ap 
from pprint import pprint

relevant_categories = {'medical','emergencies','disease'}


def findRelevantArticles(term):
    articles,suggestion = wikipedia.search(term, suggestion = True)
    relList = []
    with codecs.open("HeartText.txt", 'wb', 'utf-8') as outfile:
        for article in articles:
            try: 
                article = wikipedia.page(article)
                category_keywords = set(list(itertools.chain.from_iterable([category.lower().split() for category in article.categories])))
                if category_keywords & relevant_categories:
                    print>>outfile,article.content
                    relList += article
            except wikipedia.exceptions.PageError as e:
                pprint(e)
            except wikipedia.exceptions.DisambiguationError as e:
                for article in e.options:
                    article = wikipedia.page(article)
                    if any([relevant_category in article.categories for relevant_category in relevant_categories]):
                        print>>outfile,article.content
                        relList += article
    return relList

findRelevantArticles("Heart Attack")