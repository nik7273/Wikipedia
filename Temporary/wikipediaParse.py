# -*- coding: utf-8 -*-
#Search Wikipedia for Heart Attack
import wikipedia, codecs
from awesome_print import ap 
from pprint import pprint

articles,suggestion = wikipedia.search("Heart Attack", results = 10, suggestion = True)

relevant_categories = ['medical','emergencies','disease']
with codecs.open("HeartText.txt", 'wb', 'utf-8') as outfile:
    for article in articles:
        try: 
            article = wikipedia.page(article)
            if any([relevant_category in article.categories for relevant_category in relevant_categories]):
                print>>outfile,article.content
        except wikipedia.exceptions.PageError as e:
            pprint(e)
        except wikipedia.exceptions.DisambiguationError as e:
            for article in e.options:
                article = wikipedia.page(article)
                if any([relevant_category in article.categories for relevant_category in relevant_categories]):
                    print>>outfile,article.content
